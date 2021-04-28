import sys
import os

# モジュール検索パスに
# ディレクトリを追加
sys.path.append(os.path.join(os.path.dirname(__file__),'../../include'))
from a20210428.Arg20210428 import Arg20210428

print("__name__["+ __name__ +"]\n")

#print("__doc__ ["+ __doc__  +"]\n")

argObj = Arg20210428()
argObj.analyze(sys.argv[1:])
#argObj.hi()


