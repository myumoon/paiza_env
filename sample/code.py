#! usr/bin/python
# -*- coding: utf-8 -*-
# 
# �����Ŏw�肳�ꂽ�C�ӂ̐��̐�����S�đ������킹�����ʂ��o�͂���B
# 
# ��1)
# $python code.py 1 2 3 4
# > 10
# 
# ��2)
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
