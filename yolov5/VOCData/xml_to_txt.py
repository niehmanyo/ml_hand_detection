import xml.etree.ElementTree as ET
import os
from os import getcwd
'''
'''

def convert_annotation(image_id):
    input_file = open('annotations/%s.xml' % image_id, encoding='UTF-8')
    output_file = open('txt_file/%s.txt' % image_id, 'w')
    tree = ET.parse(input_file)  # !!!理解xml文件的格式必须!!!
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text


print(os.getcwd())  # 获取当前路径
pwd = os.getcwd()
labels = "annotations"
