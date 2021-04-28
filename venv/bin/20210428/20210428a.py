# sys.pathでモジュール検索パスを確認

import sys
import pprint

pprint.pprint(sys.path)

print("============\n")

################################################################

import os

# モジュール検索パスに
# ディレクトリを追加
sys.path.append(os.path.join(os.path.dirname(__file__),'../../include'))

pprint.pprint(sys.path)

################################################################

import argparse

parser = argparse.ArgumentParser(description='使い方')

# 受け取る引数を追加する
parser.add_argument("commit",help="1:commit/0:rollback")

args = parser.parse_args()
