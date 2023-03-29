from common import chat


def get_result(res):
    out = []
    res = res.split("\n")
    for r in res:
        ind = r.index(".")
        r = r[ind + 1:].strip()
        out.append(r)
    return out


def product_description_generate(chatbot, inputs):
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    keywords = inputs["keywords"]
    num = inputs["num"]
    out = []
    try:
        sig = "请根据我输入的关键词：'{}'生成{}条商品文案，文案中请尽量包含给的关键词。".format(
            keywords,
            num
        )
        mess.append({"role": "user", "content": sig})
        res = chatbot(mess)
        out = get_result(res)
        return out, mess
    except Exception as e:
        print(e)
        return ['error:' + str(e)], mess


inputs = {
    "keywords": "上衣 牛仔布 白色 简约 刺绣 外套 破洞",
    "num": 10,
}
print(product_description_generate(chat, inputs))
