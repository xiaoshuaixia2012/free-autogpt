# free-autogpt（免费autogpt）
用gpt3.5生成cmd命令并经过用户同意运行
- 需要安装python（最好是3.11）
- 需要openai三方库

cmd输入
```
pip install openai
```
- 中国用户需要"魔法"
- 然后在setup.json里的apikey填上你的apikey
- 接着cmd里直接输入run
- 最后直接输入需求，chatgpt就会为你生成cmd代码（有时候chatgpt不会按照格式输出代码，会显示“未找到符合的字符串。”，重新运行就行）
输出代码记得检查一下，然后输入y就可以执行代码了
