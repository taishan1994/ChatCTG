from fm_utils import SketchExtractor

from common import chat


def get_result(res):
    out = []
    res = res.split("\n")
    for r in res:
        ind = r.index(".")
        r = r[ind + 1:].strip()
        out.append(r)
    return out


def fill_mask(chatbot, inputs):
    mess = [{"role": "system", "content": "You are a helpful assistant."}, ]  # chatgpt对话历史
    sen = inputs["sen"]
    keywords = inputs["keywords"]
    if len(keywords) == 0:
        sketchExtractor = SketchExtractor(model="jieba")
        _, kws = sketchExtractor.get_kws(sen)
        keywords = sketchExtractor.get_sketch_from_kws(sen, kws, template=4, mask='[MASK]', sep='')
    num = inputs["num"]
    out = []
    try:
        sig = "请将句子中'[MASK]'掉的文本进行补全。\n句子：'{}'。\n生成{}条文本，生成的句子中请保留不是[MASK]的部分，请输出完整的句子。".format(
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
    "sen": "白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常抢眼。",
    "keywords": "",
    "num": 10,
}
print(fill_mask(chat, inputs))
