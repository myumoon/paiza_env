#! usr/bin/python
# -*- coding: utf-8 -*-
# 
# 引数で指定された任意の数の整数を全て足し合わせた結果を出力する。
# 
# 例1)
# $python code.py 1 2 3 4
# > 10
# 
# 例2)
# $python code.py 1 -2
# > -1
# 

import sys

def main():
	sum = 0
	for arg in raw_input().split():
		sum += int(arg)
		
	print sum
	

if __name__ == '__main__':
	exit(main())
