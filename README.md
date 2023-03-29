# ChatCTG
基于ChatGPT的可控文本生成。这里主要是使用ChatGPT实现一些文本生成相关的项目。

你需要一个openai账号并生成api key，然后替换common.py里面的key。

| 文件   | 描述                                                         |
| ------ | ------------------------------------------------------------ |
| pdg.py | 商品文案生成。输入一段关键词，输出关键词对应的商品文案。     |
| fm.py  | 根据草稿生成完整的句子。参考[genius](https://github.com/beyondguo/genius)，可用来作数据增强使用。 |

#### 商品文案生成

```shell
inputs = {
    "keywords": "上衣 牛仔布 白色 简约 刺绣 外套 破洞",
    "num": 10,
}

'【简约白色牛仔布上衣】，简单随性却又不失优雅，细腻的刺绣点缀更显品质，优美俏丽，凸显出了浪漫气息。', 
'夏日必备【白色 牛仔布破洞外套】，清新自然的颜色搭配上几处小破洞，闪现原始的青春活力。', 
'【简约白色牛仔布外套】，利落清新的剪裁，让身材更加修长，外衣细节处加入的精细刺绣，让时尚感和品质都实现了大幅提升。', 
'家中一件【白色牛仔布上衣】相信是少不了的，但是这件还拥有独特的浪漫感觉，细腻的刺绣和浅色的色调都十分优雅，更加凸显出穿着者高贵的气质。', 
'【牛仔布刺绣上衣】，别具一格的刺绣设计，为简单的牛仔面料增添了华丽的元素，仿佛置身于艺术殿堂之中。', 
'【白色牛仔布破洞外套】，来一份凡尔赛玫瑰风，小破洞的设计更是营造了惬意闲散的感觉，同时穿着者的优雅感也得到了很好的提升。', 
'【简约牛仔布外套】，暗藏巧妙的设计和细节，搭在身上立刻增添时尚感，浅色的色调和清爽的面料，既清新又不失经典。', 
'【白色牛仔布刺绣上衣】，精致的花卉刺绣呼之欲出，让这件牛仔上衣的品质彻底提升，穿在身上也倍感舒适轻盈。', 
'【白色牛仔布破洞外套】，有着清新的颜色和简约的剪裁，破洞的设计也显得十分特别，简洁的线条使得这件外套呈现出了别样的做法感。', 
'【牛仔布刺绣上衣】，身上的一抹明亮点缀，仿佛春天的花儿在身上盛开。深度简约，浅色牛仔布的面料搭配精致刺绣的点缀，简单而不失华丽。'
```

#### 草稿文本补全

```shell
inputs = {
	"sen": "",
    "keywords": "白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足[MASK]抢眼[MASK]",
    "num": 10,
}

'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常抢眼。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，极其抢眼。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常引人注目。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，相当引 人瞩目。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常耀眼。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常出众。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常惹眼。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，格外抢眼。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，相当耀眼。', 
'白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，十分吸引人。'

inputs = {
    "sen": "白色的罗马高跟鞋，圆球吊饰耳饰单带，个性十足，非常抢眼。",
    "keywords": "",
    "num": 10,
}
如果是输入句子，会先生成草稿：
白色[MASK]罗马高跟鞋[MASK]圆球吊饰耳饰单带[MASK]个性十足[MASK]抢眼[MASK]

'白色丝绒罗马高跟鞋配圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色皮革罗马高跟鞋搭配圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色网眼罗马高跟鞋搭配圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色素面罗马高跟鞋伴随圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色绒面罗马高跟鞋伴随圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色雪纺罗马高跟鞋搭配圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色亮面罗马高跟鞋搭配圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色绸缎罗马高跟鞋伴随圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色真丝罗马高跟鞋搭配圆球吊饰耳饰单带，个性十足，抢眼。', 
'白色亚克力罗马高跟鞋伴随圆球吊饰耳饰单带，个性十足，抢眼。'
```

# 引用
```
@misc{ChatCTG,
  author = {Oubo Gong},
  title = {Sentiment analysis with chatGPT},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  url="https://github.com/taishan1994/ChatCTG",
}
```
