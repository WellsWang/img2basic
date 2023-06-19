# -*- coding: utf-8 -*-

import sys
import numpy as np
from PIL import Image

def image2array(img):

    arr = np.array(Image.open(img), dtype='uint8')
    return arr

def output_array(arr):
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            print("▓" if arr[row][col] else " ",end="")
        print("")

def array2data(arr, expand=False):
    data = []

    if len(arr):
        bits = 4 if expand else 8
        data.append(len(arr[0])*2 if expand else len(arr[0]))
        data.append(len(arr))

        for row in range(len(arr)):
            for col in range(len(arr[row])):
                b = col % bits
                if b == 0:
                    byte = 0
                if expand:
                    byte += arr[row][col] * (pow(2,7-2*b) + pow(2,6-2*b))
                else:
                    byte += arr[row][col] * pow(2,7-b)
                if b == bits - 1 or col == len(arr[row])-1 :
                    data.append(byte)
        if (len(data) % 2 ==1 ):
            data.append(0)
    return data

if __name__ == '__main__':
    if len(sys.argv)>1:
        #try:
        arr = image2array(sys.argv[1])
        output_array(arr)
        data = array2data(arr)
        print(data)
        print(len(data))
        data = array2data(arr, True)
        print(data)
        print(len(data),int(len(data)/2+1))
        #except:
        #    print("Error on open image file, please check the image file.")
    else:
        print("-= Image to Array =- \n Usage:\n img2arr.py <filename>")
