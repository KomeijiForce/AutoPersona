# AutoPersona

这是一个基于[萌娘百科](https://zh.moegirl.org.cn/%E8%90%8C%E5%A8%98)的原始文本从[GPT-4o](https://openai.com/index/hello-gpt-4o/)中蒸馏下来的自动从未预处理的脏数据中总结角色人设的中文[llama-3模型](https://huggingface.co/KomeijiForce/Meta-Llama-3-8B-AutoPersona-Chinese)，使用该模型可以免费地从大量未经预处理的脏文本中迅速地抽取有用的人设信息，可以帮助构建大规模的人设数据。

## 使用

本工具非常容易使用，功能被完全封装在```auto_persona(character, passage)```这个function之中，以下是一个使用例：

```python
from autopersona import AutoPersona

model = AutoPersona("KomeijiForce/Meta-Llama-3-8B-AutoPersona-Chinese")

character = "古明地恋"

passage = '''{| style="text-align:left"
| """能力""" || 操纵无意识程度的能力
|-
| """危险度""" || 不明
|-
| """人类友好度""" || 完全没有
|-
| """主要活动场所""" || 不明
|}
跟姐姐觉一样的妖怪，觉。只不过她是一个把自己的内心关闭了，没办法读出他人的内心的觉。'''

print(auto_persona(character, passage))
```

你将会看到如下的输出
```
古明地恋是一位拥有操纵无意识程度能力的妖怪，跟姐姐觉一样的觉。然而，她的内心已被关闭，无法读出他人的内心。她的危险度不明，人类友好度为完全没有，主要活动场所不明。
```

当模型认为```passage```无法被转化为人设信息时，会固定输出“无用信息。”

```python
character = "古明地恋"

passage = '''== 经历 =='''

print(model.auto_persona(character, passage))
```

你将会看到“无用信息。”作为输出

## 应用

你可以在这个萌娘百科的原始文本[milashkaarshif/MoeGirlPedia_wikitext_raw_archive](https://huggingface.co/datasets/milashkaarshif/MoeGirlPedia_wikitext_raw_archive)上使用AutoPersona，但是我在使用load_dataset的时候遇到了问题，所以你可以看使用我从该repo中的.gz文件中得到的2024年5月的萌娘百科的原始文本[(KomeijiForce/moe_girl_wiki)](KomeijiForce/moe_girl_wiki)上使用。
