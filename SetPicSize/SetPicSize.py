#!/usr/bin/python
# coding=utf-8
import os
import sys
import subprocess
from PIL import Image
import cv2
import numpy as np
'''
用于修改当前脚本目录下（只检索文件，不检索文件夹）所有图片的大小
通过CMD指令传入要修改的大小
第一个参数是当前模块名称
第二个参数是图片宽度，单位像素
第三个参数是图片高度，单位像素

'''
#递归遍历文件夹，筛选符合要求的文件，并执行替换重命名
def convert_pic(root_path,w,h):
    print (root_path)
    try:
        for root,dir,files in os.walk(root_path):
                for file in files:
                    mPath, ext = os.path.splitext(file)
                    # 判断是否为图片格式
                    if ext!=".png" and ext!= ".jpg" and ext!= ".bmp":
                        continue
                    img = Image.open(root_path+"/"+str(file))
                    print(root_path+"\\"+str(file))
                    # print(int(w)+int(h))
                    # 想调整的大小，第一个参数为宽度，第二个参数为高度
                    newImg = img.resize((int(w), int(h)), Image.BILINEAR) 
                    converted_path=root_path+"/converted"
                    folder = os.path.exists(converted_path)
                    if not folder:
                        os.mkdir(converted_path)   
                    newImg.save(converted_path+'/'+str(file))  
        print("转换成功!")            
    except Exception as e :
        print (e)
        print("转换失败!")
         
 
#定义主函数，接收命令行参数
# 宽度，像素
# 高度，像素 
def main(argv):
    print (argv[0])
    
    length=len(argv)
    #subprocess.call("pause",shell=True)#按任意键退出 
    n=1 #从第二个参数开始，第一个参数是当前脚本文件名
    print ("宽度"+argv[n])
    print ("高度"+argv[n+1])
    #subprocess.call("pause",shell=True)#按任意键退出 
    # convert_pic(os.getcwd(),argv[n],argv[n+1])
    convert_pic(".",argv[n],argv[n+1])
    subprocess.call("pause",shell=True)#按任意键退出   
   
    # convert_pic(".",96,96)
    
    
    
        
if __name__ == '__main__':
    main(sys.argv)
    