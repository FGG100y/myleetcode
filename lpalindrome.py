#!/usr/bin/env python

#  # recursive is_pal to help identify the palindrome
#  def is_palindrome(s):
#      def is_pal(s):
#          if len(s) <= 1:
#              return True
#          else:
#              answer = (s[0]) == s[-1] and is_pal(s[1:-1])
#              return answer
#
#      return is_pal(s)
#
#
#  def validPalindrome(s, left, right):
#      while left < right:
#          if s[left] != s[right]:
#              return False
#          left, right = left+1, right-1
#      return True


# O(n^2)) runtime, O(1) space
#  def expand_pal_center(s, left, right):
def xcenter(s, left, right):
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def longest_pal(s):
    """counts the length of the longest palindrome in a string
    """
    start, end = 0, 0
    for i in range(len(s)):
        # len(s) is odd
        len1 = xcenter(s, i, i)
        # len(s) is even
        len2 = xcenter(s, i, i + 1)
        len_max = max(len1, len2)
        if len_max > end - start:
            # 'distance' between start and center
            start = i - (len_max - 1) // 2
            # 'distance' between end and center
            end = i + len_max // 2

    return len(s[start:end+1])


if __name__ == "__main__":
    #  s = '1234321kka'
    #  print(s)
    #  print('-'*len(s))
    # ###################
    #  import sys
    #  print(longest_pal(sys.argv[1]))
    # ###################
    s = 'dsuehgfqxzrnkmtmiwytshrerjfybxirufrsobkjeghiunftxyqqcyoreevvktxgvjjqzvcujsynsrlgllebyukyxgugrvkesovfhzdznstvtbblmjcngwsdrmfczsihiblqhkfvhzylwopepfmnixeesvugyifdxvpcknpqunolpgjehoxgylnzoggqpbdkhrngchidhfdktblrifjvppttemmplzrsbjhltvwprhkigkvfkxcxfsgyiyuuziqurgcmddqshenindtrfzlrqpfpekfosmugpwjgydtbwexcwrvdedposftffjrfeojsqpxtoguroojsgrwpyiyhurprcfsgnnykjtrjjzdswfqfwuohpcssgjzyikruvomeggqzyslmfurgnmhyvnksktvdcidvutrrxzixbxiypbvozgnmopfjiljggqrronwkfqvlpdwhtzfpsokfbvftyxdinknsrjlxbzyfmsinegprbnuezqlikgsbbixfdjtsjxojqwxdrvwfflrwjsnpcxqvfpmbidyvvlcnvvvvbglhhmkpuzhosfitgzclicpzsvozsbtvtlmjffqieosliqysgyxmceytmezfbtkcprfomftlkyortyfmykslfdmxzfeetmzxbuvoorpwmkerujcjcuuyvmpqidrrksrtmxhqoqdyvjgvcftbhywmbdfoixecfgorpxoxbqlhbnynwflbodsdqvwwoizdfyczefvonoczocvtbixehcvpmimyxgzddvomklofuthtytqougojqwmxvhzpmvtfsjwrgmxuoeizmnfptssolqbmnrhfjitoqxizflyoddgjlxknumclfmpmrzpomrqqogvmwgclpquhuqbkriyjkwcusetkyxozomcrsuyfmsddwubkiyyjoeqlzjsfnwkhdpgxkeicbivlwbdvcbvdqbyxuwdolmtxzgpogtzctlcjemoxdrbrmmtkuuidtiebckmqluiszgichpmgbsxdiurxdgkvvufyihcjejgwwepswxmjducltnxngtylgiqcvxldeebykysdgwokcupxmjnbiqlzovnocuesodotqivceqhimuhtromxxullejgzhzevzvtdhbfhcwbdivgslkfmudzofbmeeqixuprbsyrelcgvvkbtkgckezrrisnnkwwchcfwlqdoucccqinjplgwlqcylqojstlvdjmcjyqjsqwrvxjmujcuzirinocnnwszxjnyszncytltbusmcsxustpxeuxgmwlixnjnigsxnollfbpqrwohbshbohhnpsvenvgreqfwqypkkibenvgjcwmumwcgehehiyediindvppefciihjkcnzvelorusllpbexivekbflpyqpefpjlumctorwejnefenhrlfugnkywvwuvrdrxsxjksgowxholmpjfyjcksmhwpcpjcodwzmolzgkcjxmiqxdpewlyjilcbbwyxmxhqvsxkepiwdvmfxdceiswscupzpmhvmyciyosxuwnmjxnkdhhnquxsmekmcwgcklxzhhqxkebqcvxpsqzuoxikverbskrwvewomemysgcmrdnzgufysnoxuerrqcufevwwumrvbowvvkjuediygphwgwgdrpbgreytkmgcmzonbyxwkolywjcigvyqqhwsjmtkvvhbtuhctcigvfnkkffvsjrjiumlowlwvsbuopmsfcqrxlpprtmswlkdmkoxewhtfkzzoohdbutqccmzsscjdozeeecdqmugcrqqfjingovwfmvnltdfcmrofcftnoozquguyyzdxqqgwbdpotbquhokorykpurvwbvcwdnmzgimuzjipikdtvhstsgeykmunxvbszjmbgwhiymumfmlhennthtjwspxvqrelkhwqxjrzbkqbobfetlejvdhzpmwreqfhnupgovixdemmngzorgfooiruhjbjmvwgmzrvjgrwouxugmysbrdtdujjeffomribgqkhjohitgonqevcweedmleexqjgtywpwbwmoltxbdkiyvgrykhbesgckhvecyvcjryqbhstwrcloqmoivrmkkimzwbywumxfrzyterxmwpqcullcvebkflwmbbexqifohjrrgsnbsqhlxkwkuhwocmjfrhyfkqpqlbvxokbvbufqffclzlnlszcimzucrsrohldxeohdiktubdrvkzvgvhnrkeenmhcvujlxlpcyhohumnuxmswwfwyhuyqhurvcrvmnkgsyygunrvpbvdmpetuixhwtnswhmgtuunzybkyosezpzttrzcdukbtmxxeschlkjgqgrnhvixqbcusimvwdceedhhbbbrxefvztdcfdtzglhmzfthlmc'
    print(longest_pal(s))
