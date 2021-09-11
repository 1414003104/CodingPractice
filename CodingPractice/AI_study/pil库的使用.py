'''
PIL库是一个具有强大图像处理能力的第三方库。

图像的组成：由RGB三原色组成,RGB图像中，一种彩色由R、G、B三原色按照比例混合而成。0-255区分不同亮度的颜色。

图像的数组表示：图像是一个由像素组成的矩阵，每个元素是一个RGB值
'''
from PIL import Image
import matplotlib.pyplot as plt

img=Image.open('F:/各学科文档/蓝桥杯竞赛/CodingPractice/AI_study/image_pil/dark.jpg')

plt.imshow(img)
plt.show()

width,height=img.size
#输出图片
print(width,height)
print(img.mode)

#旋转图片
img1=img.rotate(45)
plt.imshow(img1)
plt.show()

#图片剪切
#剪切 crop()四个参数分别是：
# (左上角点的x坐标，左上角点的y坐标，右下角点的x坐标，右下角点的y坐标)
img_crop_result = img.crop((200,0,1500,1200))
#保存图片
img_crop_result.save('F:/各学科文档/蓝桥杯竞赛/CodingPractice/AI_study/image_pil/dark_crop.jpg')
plt.imshow(img_crop_result)
plt.show()

#图片缩放
img_resize_result = img.resize((int(width*0.6),int(height*0.6)),Image.ANTIALIAS)#抗锯齿
print(img_resize_result.size)
img_resize_result.save('F:/各学科文档/蓝桥杯竞赛/CodingPractice/AI_study/image_pil/dark_resize.jpg')
plt.imshow(img_resize_result)
plt.show()

#镜像效果：左右旋转、上下旋转
img_lr=img.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(img_lr)
plt.show()
img_tb=img.transpose(Image.FLIP_TOP_BOTTOM)
plt.imshow(img_tb)
plt.show()



