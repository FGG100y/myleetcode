#!/usr/bin/env python
#  对字符串中的所有单词进行倒排。
#
#  说明：
#
#  1、每个单词是以26个大写或小写英文字母构成；
#
#  2、非构成单词的字符均视为单词间隔符；
#
#  3、要求倒排后的单词间隔符以一个空格表示；
#     如果原字符串中相邻单词间有多个间隔符时，倒排转换后也只允许出现一个空格间隔符；
#
#  4、每个单词最长20个字母；

def reverse_words(s):
    """
    """
    def reverse(s, begin, end):
        for i in range((end - begin) // 2):
            s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

    s = list(s)
    reverse(s, 0, len(s))
    print(s)
    i = 0
    #  for j in range(len(s) + 1):
    for j in range(len(s)):
        if j == len(s) or not s[j].isalpha():
            reverse(s, i, j)
            i = j + 1
        while not s[j].isalpha() and s[j] != " ":
            s[j] = " "
            j += 1
    s = clean_spaces(s)
    print(s)
    return s


def clean_spaces(s):
    n = len(s)
    i, j = 0, 0
    while j < n:
        while j < n and s[j] == ' ':
            j += 1
        while j < n and s[j] != ' ':
            s[i] = s[j]
            i += 1
            j += 1
        while j < n and s[j] == ' ':
            j += 1
        if j < n:
            s[i] = ' '
            i += 1
    return ''.join(s[:i])

if __name__ == "__main__":
    s = 'wyZksmG XY ReXA Pedt mabjlFdGmJUseHz GzciYPmv OFKis SQzQAeQexsgy ZVrsqqSbHdQF AKPJECiP vOgIXvbuJTDnpPcCD GWlPWTGQSWyaZtxHd ydpT pHSeYKetXH RdBcHmggvESwIEWlBtYq H VdkLHvSGupDEFOfH BcWxbNOQOOYYhBNEz MAFjrzTFKWZOCGGZazCn Ef owSLRoGJXMWAR pLdQQWx ZSRXXCUOSetMNfSOnRk jDhskr WHBmEifhgEEBoT CJNtdFFM n UAbfJKuoVfoqAvbEcv MnDWh'
    print(reverse_words(s))


#  // trim leading, trailing and multiple spaces
#  String cleanSpaces(char[] a, int n) {
#      int i = 0, j = 0;
#
#      while (j < n) {
#          while (j < n && a[j] == ' ') j++;             // skip spaces
#          while (j < n && a[j] != ' ') a[i++] = a[j++]; // keep non spaces
#          while (j < n && a[j] == ' ') j++;             // skip spaces
#          if (j < n) a[i++] = ' ';                      // keep only one space
#      }
#
#      return new String(a).substring(0, i);
#  }
