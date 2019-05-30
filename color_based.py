# -*- coding:utf-8 -*-

import numpy as np

def distance(f1,f2):
    ret = (f1[0]-f2[0])*(f1[0]-f2[0])+(f1[1]-f2[1])*(f1[1]-f2[1])+(f1[2]-f2[2])*(f1[2]-f2[2])
    return ret**0.5


def kmeans_color(centre,img,k):
    d = np.zeros((300000,30),float)
    means = np.zeros(300000,dtype=np.int)
    (x,y) = img.shape[0:2]
    n = x * y
    cnt = 0
    while cnt < 10:
        print(cnt, "is going on")
        centre_cnt = np.zeros(k,dtype=int)
        for i in range(0,x):
            for j in range (0,y):
                p = i*y + j
                for t in range(0,k):
                    d[p, t] = distance(img[i,j],centre[t])
                w = np.argmin(d[p, 0:k])
                means[p] = w
                centre_cnt[w] += 1
        centre = np.zeros((k,3))
        for i in range(0,n):
            nx = i//y
            ny = i%y
            (r, g, b) = img[nx, ny]
            centre[means[i], 0] += r
            centre[means[i], 1] += g
            centre[means[i], 2] += b
        for i in range(0, k):
            if centre_cnt[i]!=0:
                centre[i, 0] //= centre_cnt[i]
                centre[i, 1] //= centre_cnt[i]
                centre[i, 2] //= centre_cnt[i]
            else:
                centre[i, 0] = 0
                centre[i, 1] = 0
                centre[i, 2] = 0
        print(cnt, "is finished")
        cnt += 1
    ret = np.zeros((x,y,3),dtype=np.uint8)
    print(ret.shape)
    for i in range(0,n):
        nx = i // y
        ny = i % y
        #print(nx, ny)
        ret.itemset((nx, ny, 0), int(centre.item(means[i], 0)))
        ret.itemset((nx, ny, 1), int(centre.item(means[i], 1)))
        ret.itemset((nx, ny, 2), int(centre.item(means[i], 2)))

    return ret
