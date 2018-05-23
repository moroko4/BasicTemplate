#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
リスト作成

[使い方]
getArgs.py 5 10

"""

def main():

    # コマンドライン引数
    argvs = sys.argv
    args = len(argvs)

    if args != 3:
        print "error !"
        exit()
    else:
        min = int(argvs[1])
        max = int(argvs[2]) + 1
        list = range(min, max)
        print list


######################################

if __name__ == '__main__':
    main()

