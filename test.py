#!usr/bin/python
# -*- coding:utf-8 -*-

import subprocess
import re
import os.path
import time
import argparse

class Result(object):
	SUCCESS  = 0 # 成功
	FAILURE  = 1 # 結果エラー
	TIME_ERR = 2 # 実行時間エラー
	ERROR    = 3 # 実行失敗
	
	TIMELIMIT_SEC = 2.0

def main():
	argparser = argparse.ArgumentParser(description="Check if the code is valid and measure the time.")
	argparser.add_argument("-e", "--exefile", action="store", required=True, help="A file checking a test case.")
	argparser.add_argument("-i", "--input", action="store", help="Test case.")
	argparser.add_argument("-if", "--infile", action="store", help="Input a test file.")
	argparser.add_argument("-a", "--answer", action="store", help="Specify the answer.")
	argparser.add_argument("-af", "--ansfile", action="store", help="Answer in the file.")
	args = argparser.parse_args()
		
	# 実行pythonファイル存在チェック
	if os.path.exists(args.exefile) == False:
		print args.exefile, ": Invalid python file"
		return Result.ERROR
		
	# テスト
	test = args.input
	if args.input == None:
		if args.infile == None:
			print  "error : Not set a test"
			return Result.ERROR
			
		elif os.path.exists(args.infile) == False:
			print args.infile, ": Invalid check file"
			return Result.ERROR
			
		else:
			with open(args.infile, "r") as f:
				test = f.read()

	# 答え
	answer = args.answer
	if args.answer == None:
		if args.ansfile == None:
			print  "error : Not set a answer"
			return Result.ERROR
			
		elif os.path.exists(args.ansfile) == False:
			print args.ansfile, ": Invalid check file"
			return Result.ERROR
			
		else:
			with open(args.ansfile, "r") as f:
				answer = f.read()
			
	# 入力の最後は改行で終わってないといけないので答えに改行を足す
	if answer[-1] != "\n":
		answer += "\n"
	
	# 実行コマンド
	cmd = "python " + args.exefile
	process = subprocess.Popen(cmd.split(" "), stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	
	start = time.time()
	result = process.communicate(test)[0]
	exeTime = time.time() - start
	
	# 実行結果エラー
	if result != answer:
		print "result error :"
		print "[input]"
		print test
		print "[expected]"
		print "\"" + answer + "\""
		print "[result]"
		print "\"" + result + "\""
		print "[time]"
		print "%fs (limit:%f)" % (exeTime, Result.TIMELIMIT_SEC)
		return Result.FAILURE
		
	# 実行時間エラー
	elif Result.TIMELIMIT_SEC < exeTime:
		print "time limit error :"
		print "[time]"
		print "%fs (limit:%f)" % (exeTime, Result.TIMELIMIT_SEC)
		return Result.TIME_ERR
		
	return Result.SUCCESS

if __name__ == "__main__":
	exit(main())

