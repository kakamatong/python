
from ToolUtils import ToolUtils
import GetImage
def main():
    print("main")
    def printInfo():
        #print("this is test for timer forever")
        GetImage.getBYImage()
    ToolUtils.timerForever(1, printInfo)

    # def printInfo2():
    #     print("this is test for timer2")
    # ToolUtils.timer(5, printInfo2)
    pass

if __name__ == "__main__":
    main()
    pass