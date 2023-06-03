import json
import openai
import re
import os

# 从 setup.json 文件中读取 API 密钥
with open('setup.json', 'r') as file:
    data = json.load(file)
    api_key = data['apikey']

# 设置 OpenAI API 密钥
openai.api_key = api_key

# 初始化对话历史
conversation_history = []

# 调用ChatGPT
def chat_with_gpt(user_input):
    # 将用户输入添加到对话历史中
    conversation_history.append(user_input)
    
    # 将对话历史连接为单个字符串，并生成对话的提示
    prompt = "\n".join(conversation_history)
    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.3,
        top_p=0.5,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    # 获取回复中的文本
    reply = response.choices[0].text.strip()
    
    # 将AI的回复添加到对话历史中
    conversation_history.append(reply)
    
    return reply

#"接下来你只需要按照我的需求输出cmd代码，代码必须以“:c”开头，以“:c”结尾，让我们开始吧！"
# 用户提供初始的提示语
user_prompt = "接下来你只需要按照我的需求输出cmd代码，代码必须以“:c”开头，以“:c”结尾，让我们开始吧！"
conversation_history.append(f"用户: {user_prompt}")

# 与ChatGPT进行对话
while True:
    user_input = input("用户：")
    
    if user_input.lower() == 'exit':
        break
    
    # 调用ChatGPT并获取回复
    ai_response = chat_with_gpt(user_input)
    
    # 打印AI的回复
    print("AI：", ai_response)

    # 提取中间字符串
    def extract_string(input_str):
        pattern = r":c\s*(.+?):c$"
        match = re.search(pattern, input_str)
        if match:
            return match.group(1).rstrip()
        else:
            return None

    # 用户输入
    user_input =  ai_response

    # 提取中间字符串
    extracted_string = extract_string(user_input)

    if extracted_string:
        # 输出提取的字符串
        print("提取的字符串：", extracted_string)

        # 用户同意执行
        confirmation = input("是否要执行提取的字符串？(y/n): ")

        if confirmation.lower() == "y":
            # 使用os.system执行提取的字符串作为命令
            os.system(extracted_string)
        else:
            print("操作已取消。")
    else:
        print("未找到符合的字符串。")