# -*- coding:utf-8 -*-
#  plt 用于显示图片
import matplotlib.pyplot as plt
from color_based import *
# mpimg 用于读取图片
import matplotlib.image as mpimg
import os
import numpy as np
import imageio


def init_centre(img,k):
    (x, y) = img.shape[0:2]
    r = 1
    while r * r <= k:
        r = r + 1
    r = r - 1
    c = k // r
    r_space = x // r
    c_space = y // c
    print(x, y, r, c, r_space, c_space)
    ret = np.zeros((k,3),dtype=int)
    print(type(ret.item(0,0)))
    for i in range(0, r):
        for j in range(0, c):
            t = j*r+i
            if(t<k):
                ret.itemset((t, 0), img.item((r_space // 2 + i * r_space, c_space // 2 + j * c_space, 0)))
                ret.itemset((t, 1), img.item((r_space // 2 + i * r_space, c_space // 2 + j * c_space, 1)))
                ret.itemset((t, 2), img.item((r_space // 2 + i * r_space, c_space // 2 + j * c_space, 2)))
    return ret

dir = '.\\data'
lst = os.listdir(dir)
# img = mpimg.imread('.\\data\osho.bmp')
# ans = kmeans_color(init_centre(img,9),img,9)
# imageio.imwrite('.\\output\\osho.bmp',ans)
for i in range(0,len(lst)):
    path = os.path.join(dir,lst[i])
    if(path[-4:] == '.jpg'):
        sp = lst[i].split('.')
        img = mpimg.imread('./data/' + lst[i])
        ans = kmeans_color(init_centre(img, 9), img, 9)
        imageio.imwrite('.\\output\\' + sp[0] + '_9.jpg', ans)
        ans = kmeans_color(init_centre(img, 4), img, 4)
        imageio.imwrite('.\\output\\' + sp[0] + '_4.jpg', ans)

# plt.imshow(ans)
# plt.axis('off')
# plt.show()
