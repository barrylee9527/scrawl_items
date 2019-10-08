import os
import numpy as np
from os import path
from PIL import Image
import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import chardet
import matplotlib.pyplot as plt
# 获取当前文件路径
d = path.dirname(__file__) if '__file__' in locals() else os.getcwd()
# 打开文档
f = open(path.join(d, '上海堡垒.txt'), 'r', encoding='utf-8').read()
# 检测编码读取结果
# 设置背景图片
stopwords_file = open(os.path.join(d, 'stopwords.txt'), 'r',encoding='utf-8')
stopwords = [words.strip() for words in stopwords_file.readlines()]
alice_coloring = np.array(Image.open(path.join(d, 'F:/ima.jpg')))
stopwords = set(stopwords)
# jieba切分
Is = jieba.cut(f)
txt = "".join(Is)
# 初始化
w = WordCloud(font_path="C:/Windows/Fonts/SIMYOU.TTF",  # 字体 # 图片尺寸
              background_color="white",  # 背景颜色
              max_words=500,  # 最多词数量
              scale=2,
              mask=alice_coloring,
              stopwords=stopwords,
              random_state=42
              )
w.generate(txt)
image_colors = ImageColorGenerator(alice_coloring)

w.to_file("grwordcloud.png")
plt.imshow(w, interpolation='bilinear')
plt.axis('off')
# plt.imshow(w.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis('off')
# plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.show()
