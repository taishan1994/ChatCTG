# coding=utf-8
# openai==0.27.2
import openai
import urllib.request
import os

os.environ["http_proxy"] = "http://127.0.0.1:1080"
os.environ["https_proxy"] = "http://127.0.0.1:1080"
print(urllib.request.getproxies())

openai.api_key = "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"


def chat(mess):
    # 根据自己服务器的vpn情况设置proxy
    responde = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mess
    )

    res = responde['choices'][0]['message']['content']
    return res


if __name__ == '__main__':
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    text = chat(mess)
    print(text)
