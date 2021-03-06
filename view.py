from wordcloud import WordCloud
import cv2
import jieba
import matplotlib.pyplot as plt

def showcloud():
    # 文本路径
    text_path = './utils/danmu.txt'
    if text_path:
        with open(text_path, 'r', encoding='utf-8') as f:
            text = f.read()
        cut_text = " ".join(jieba.cut(text))
        color_mask = cv2.imread('./view/show.jpg')
        cloud = WordCloud(
            # 设定字体，不指定字体会乱码
            font_path='./view/FZSTK.TTF',
            # 设置背景色
            background_color='white',
            # 词云形状
            mask=color_mask,
            # 允许最大词汇
            max_words=2000,
            # 最大号字体
            max_font_size=40
        )
        wCloud = cloud.generate(cut_text)
        wCloud.to_file('./view/danmu.png')

        plt.imshow(wCloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    showcloud()