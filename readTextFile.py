#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
テキストファイル読み込み

[使い方]
readTextFile.py list.txt

"""

def main():

    # コマンドライン引数
    argvs = sys.argv
    for path in argvs[1:]:

        # 全文字一括読み込み
        result = readAll(path)
        print result

        # 行単位でリストとして読み込み
        result = readLines(path)
        print result

# 全文字一括読み込み
def readAll(path):
    with open(path) as f:
        text = f.read()
    return text

# 行単位でリストとして読み込み
def readLines(path):
    lines = []
    with open(path) as f:
        for line in f.readlines():
            line = line.rstrip()
            lines.append(line)
    return lines


######################################

if __name__ == '__main__':
    main()

