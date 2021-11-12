#!/usr/bin/python
# coding=utf-8
import os
import sys
import subprocess
'''
用于修改当前目录下所有文件的文件名
通过CMD指令传入要参数
第一个参数是模块名称
第二个参数如果是以下
-fup：将所有文件名大写
-flow：将所有文件名小写
如果第二个参数不是以上参数
直接传入要修改的指定内容
第二个参数是要修改的内容
第三个参数是替换的内容

'''
SWITCHCHAR=1
PYFILENAME="formatRourcename.py"
ORFUP="-fup"
ORLOW="-flow"
 
#递归遍历文件夹，筛选符合要求的文件，并执行替换重命名
def listfiles(root,arg,rep):
    global SWITCHCHAR #设定全局变量标志
    global PYFILENAME
    for dir in os.listdir(root):
        filepath=root+"/"+dir
        if os.path.isdir(filepath):
            listfiles(filepath,arg)
        else:
            # file name (with extension)
            src_apk_file_name = os.path.basename(dir)
            if PYFILENAME==src_apk_file_name:#不修改本脚本文件
                continue
            #检查文件名称格式
            isIn=arg in dir
            if isIn==True:
                dir=dir.replace(arg,rep)
            
            if SWITCHCHAR==1:
                if isIn==True:
                    os.rename(filepath,root+"/"+dir)
                    print (filepath+"-->"+dir)
                continue
 
            if SWITCHCHAR==2:
                dir=dir.upper() 
            if SWITCHCHAR==3:
                dir=dir.lower()
            os.rename(filepath,root+"/"+dir)
            print (filepath+"-->"+dir)
 
#定义主函数，接收命令行参数
# -fup 替换所有小写字符
# -flow 替换所有大写字符
def main(argv):
    global SWITCHCHAR
    global PYFILENAME
    
    length=len(argv)
    if length>3 :
        print ("错误：参数个数不对！")
        return
    n=1 #从第二个参数开始，第一个参数是当前脚本文件名
    if argv[n]==ORFUP:
        SWITCHCHAR=2
        if length==2:
            listfiles(".","","")#只执行字符变大命令
    elif argv[n]==ORLOW:
            SWITCHCHAR=3
            if length==2:
                listfiles(".","","")#只执行字符变小命令
    else:
        listfiles(".",argv[n],argv[n+1])
    # listfiles(".","副本","1")   
      
    
    
    
        
if __name__ == '__main__':
    main(sys.argv)
    