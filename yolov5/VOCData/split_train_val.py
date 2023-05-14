import os
import random
import argparse

parser = argparse.ArgumentParser()
# xml 文件的地址，根据自己的数据进行修改 xml一般存放在labels下
# parser.add_argument("echo", help="display all files and dics in this path")
# parser.add_argument("square", help="operation square", type=int)
parser.add_argument("a", help="a", type=int)
parser.add_argument("b", help="b", type=int)
args = parser.parse_args()

print(max(args.a,args.b))
print(1)
