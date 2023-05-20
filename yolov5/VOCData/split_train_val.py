import os
import random
import argparse

parser = argparse.ArgumentParser()
# xml 文件的地址，根据自己的数据进行修改 xml一般存放在labels下
# parser.add_argument("echo", help="display all files and dics in this path")
# parser.add_argument("square", help="operation square", type=int)
# 读取xml文件，接着写入txt文件


# parser.add_argument("xml_path", default="annotations", type=str, help="input xml label path")
# parser.add_argument("txt_path", default="txt_file", type=str, help="output txt label path")
# arg = parser.parse_args()

# xml_path = os.xml_path
xml_path = "annotations"
txt_path = "txt_file"
total_xml = os.listdir(xml_path)
if not os.path.exists(txt_path):
    os.mkdir(txt_path)  # 创建一个文件夹dic

num = len(total_xml)  # images里面一共多少文件

file_train = open(txt_path + '/train.txt', 'w')
for i in range(num):
    name = total_xml[i][:-4] + '\n'
    file_train.write(name)
file_train.close()
