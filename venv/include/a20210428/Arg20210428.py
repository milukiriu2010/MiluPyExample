import getopt

class Arg20210428:
    def analyze(self,argv):
        try:
            opts, args = getopt.getopt(
                argv,
                "",
                ["commit=","v="]
            )

            for opt in opts:
                print("opt="+str(opt))
        except getopt.GetoptError as err:
            print("===ERROR==========")
            print(str(err))

    def hi(self):
        msg = '''
        あいうえお
        かきくけこ 
        '''
        print(msg)
