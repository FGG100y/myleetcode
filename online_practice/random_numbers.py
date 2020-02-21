import sys


def sort_random_nums():
    arr_length = sys.stdin.readline().strip()
    arrs = [int(sys.stdin.readline().strip()) for n in range(int(arr_length))]
    # drop the duplicates first
    for n in sorted(set(arrs)):
        print(n)


if __name__ == "__main__":
    # ＇样例输入解释：样例有两组测试＇和它头顶上那一句, "注：balala.测试用例不止一组＇，
    # 这两句话也就让我多折腾到夜里两点左右吧 --! 因为不确定到底测试用的case到底有多少组，
    # 所以我用(while 1)循环，但却忘记用（try...except）来捕捉异常（也就是处理case读完之后的情况）
    # 当然是通不过了．再加上心烦气噪，极易丧失理智．
    # 我昨晚不知道，现在才发现，所谓的 “注” 这一句，纯粹就是扰乱视听；
    # 再加上，”点击对比用例标准输入与你的输入“ 弹窗那两栏的“极其毫无歧义”的标题，我真的跪了：
    # 左边的“标准输出”可以理解为stdout的翻译，也就是我们写的程序输出的内容（打印到屏幕）；
    # 右边的“你的输出”...嗯，写前端的这位，建议语文要加强一下，应该是表达“你应该输出”，
    # 或者，其实，这两个标题跑位了，这就不是语文问题，而是前端代码问题了，而对我们使用者来说，就是大问题了。

    # 当然了，人家也有话要说，＇是你自己审题不仔细嘛＇．这让我感到旧日被高考支配的恐惧．
    try:
        while 1:
            sort_random_nums()
    except Exception:
        pass
