#!/usr/bin/env python
#Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些
#ABBA，ABA，A，123321，但是他们有时会在开始或结束时加入一些无关的字符以防止别国
#破解。比如进行下列变化ABBA->12ABBA,ABA->ABAKK,123321->51233214　。因为截获的串
#太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），Cathcer
#的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？


# recursive is_pal to help identify the palindrome
def is_palindrome(s):
    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            answer = (s[0]) == s[-1] and is_pal(s[1:-1])
            return answer

    return is_pal(s)


def validPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right-1
            return True


# O(n^2)) runtime, O(1) space
#  def expand_pal_center(s, left, right):
def xcenter(s, left, right):
    while (left >= 0 and right < len(s)) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_pal(s):
    """figure out the longest palindrome in a string
    """
    start, end = 0, 0
    for i in range(len(s)):
        #  len1 = expand_pal_center(s, i, i)
        #  len2 = expand_pal_center(s, i, i + 1)
        len1 = xcenter(s, i, i)
        len2 = xcenter(s, i, i + 1)
        len_max = max(len1, len2)
        if len_max > end - start:
            start = i - (len_max - 1) // 2
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
    print(s)
    #  print('-'*len(s))
    print(longest_pal(s))
