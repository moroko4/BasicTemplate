#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

"""
コマンドライン引数を取得

[使い方]
getArgs.py *.txt

"""

def main():

    # コマンドライン引数を取得
    argvs = sys.argv
    for path in argvs[1:]:
        print path


######################################

if __name__ == '__main__':
    main()

