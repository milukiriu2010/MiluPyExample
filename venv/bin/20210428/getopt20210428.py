# https://qiita.com/watyanabe164/items/4de7821b3b38790aaf12
# python3 getopt20210428.py -t 127.0.0.1 -p 8888 --message hello --hogehoge

import sys
import getopt

def main():
    if not len(sys.argv[1:]):
        print("argument is nothing")
        sys.exit()

    text = sys.argv[1:]

    try:
        opts,args = getopt.getopt(
            text,
            "t:p:m:h",
            ["target=", "port=", "message=", "hogehoge"]
            )
        print("Options:", opts)
        print("Arguments:", args)
    except getopt.GetoptError as err:
        print(str(err))

main()
print("finished")
