class Solution(object):

    def get_tuple_from_word(self, word):
        l_ = list(set(word))
        l_.sort()
        return tuple(l_)

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = 0
        map_ = {}
        for word in words:
            tuple_of_word = self.get_tuple_from_word(word)
            if tuple_of_word in map_:
                if map_[tuple_of_word] < len(word):
                    map_[tuple_of_word] = len(word)
            else:
                map_[tuple_of_word] = len(word)

        tuple_of_map = tuple(map_.items())

        for i in range(len(tuple_of_map) - 1):
            for j in range(i + 1, len(tuple_of_map)):
                if not set(tuple_of_map[i][0]) & set(tuple_of_map[j][0]):
                    temp_result = tuple_of_map[i][1] * tuple_of_map[j][1]
                    if temp_result > result:
                        result = temp_result

        return result


test_arr = ["fedacddc", "ccbccfacbcdeadfacad", "fbeaeeebcfbcbaa", "ceefecebb", "afefda", "fafa", "bedafffcbfcaf", "eff", "fdbeaaecaefca", "bbcbffcfafcadddbea", "bdcffdca", "eacddaed", "afccbbcdbbdfecedcbbcc", "fdafe", "fdeedcbdcfcafadd", "ccbfddcfacedf", "aecadbffb", "cbbafbaccfedc", "baf", "bfdfddaadfeebaccfc", "acebcbebdbbdfeafcf", "dfa", "dabefeebde", "feecfbcedfa", "dfffaefcbaccf", "acebeaae", "ce", "eaadbafeed", "ecffabcfdbcbbbdddeacd", "acefffbbbecff", "fdbeeebbf", "afecacacade", "eaedcabdeafecef", "cdacacfd", "cdcbdadbaaeafcfcb", "fffdbeaeabd", "ecfebbccfcdedb", "bfcbee", "becdefcdcbeefadaecaf", "edbafdcacdfefa", "fedbbadbbdfbfd", "dcbbfbaeafabccdde", "fffaefea", "bcb", "aee", "afbcfbacbcfdddadebb", "febcefcdaac", "bfafdccefcf", "ddcfcaeaabdcaeafccbd", "caaead", "bbccedfcaa", "aeebcfabdcf", "bbcfaeaefcdecf", "bffbacbaabcfaea", "eaaddeca", "feeeecdecbcbfedcb", "ddcdbbebcbdd", "acbceedddcadaf", "acffbfaecbbebceb", "ecaedabfdbbcdfd", "ccbdca", "ffdfeececebafcdedfb", "edcebfcffdbfdacbeeb", "afcbcdfdffecfefcedade", "efedacdbcbcafddf", "bf", "fedddbabdb", "bbdbfdcdfcecaaba", "eefaafe", "cfef", "edcddececdd", "dbcfddddfbfacacfdcec", "ccdaaafebfddd", "ec", "fecbecaebfadacc", "ecfcacebdfcbcba", "dbefbdbfdb", "cedbaffeabaccbdacf", "fcffaeeefdecebfabbcf", "daa", "ebeccdcecf", "afcdbcdcd", "efefbafcfeadbf", "bdbea", "eaeadcebabccaeeafbedf", "ddbbdfbdc", "fdefe", "fcfafabccfdcfeffdfbd", "abfdbfadeafcac", "bbbfcffeebdeddbccab", "fecfcbcdecc", "afadebcbeebaddacfae", "cefba", "abeddeacda", "baefaaaad", "bbbaedafdae", "acfabbdbfdacacebded", "aacfacec", "fbcaaccdbcfea", "de", "fcddffaefbbd", "ebfffdc", "aaefeacbce", "effaefddefcefeccfcafa", "edfccdaae", "cc", "bce", "fbbccaebb", "cba", "caca", "aedcdead", "ceddbccdfcd", "fefceacf", "fccffeffdbeeafe",
            "aebbfacbbbcffddfd", "ebab", "aea", "bfcbfabbbbfb", "baadbeedbbdaacacdced", "dea", "abbabbeaaeedcdb", "dbcfc", "dfefeeebdcbd", "adc", "efefbbfafba", "feaacadfeb", "aeacabeaea", "dedcb", "acceeceefbafa", "bc", "bfeffdfddff", "ddd", "afcdfbeeeabdfacccefef", "eadffdedbfdda", "eecebabefebefbca", "ebefccb", "addcabaad", "deeecefeaabfdfaadeee", "cffddffbeecaccbbbcbec", "eaeefbbdfdcd", "bcdedecfdfecfb", "edfafdba", "deba", "bedcbfd", "bafbdefaddcbfcdbcde", "eb", "aaabfacafae", "bc", "cdefcfbdda", "aadddeaa", "fdd", "dcedf", "eddfcfbeedadffbeed", "ecadceebba", "bfdffaeaebaaccbeead", "bedcdbe", "acdcfdbc", "fdebbefbf", "abebdebfccbbbecceabfb", "eeefecadc", "aebdfdfffefbfecf", "edd", "fdedb", "aaddaefdbaa", "abdbd", "eeabcfbcfafbfedfa", "ebabdadabcfdaacada", "adcdce", "aebd", "fdcbfafca", "abaaacdfe", "cfdcb", "dcabbb", "ebec", "acdccafebdaedadcee", "afebaeffeacb", "dcbfddbc", "bbbeba", "efbbefddceeacd", "faeefaefebccddc", "bdeefbbbb", "bfdebfaeaedeacbaf", "fbfdbdefdfe", "ae", "fbefdcaedad", "ddeadebafd", "cdceafbbacfdeab", "aff", "eaaeecddeafbeafafeebe", "aafaacdeaaf", "cafdcecfadfbf", "fddaccadcedbbf", "dabf", "caecfdfaee", "fbf", "acebaabaabfabbefee", "addcdfdd", "dfdeebdeeaebdbca", "ffc", "ebe", "dadcafadbafedff", "edccffcdbcbaefdaab", "bdccfcfcfaadcddcaca", "bee", "bccfcffedadd", "fceafafdcbf", "dfdeeff", "dabeebadaabf", "bcddbbac", "bd", "ddbaabcdfffbaffdcbdad", "efbebbe", "dfcaddeeea", "baa", "bbebafe", "bdcefcdfcacdb", "dc", "cda", "fdafcfbd", "fcbfbefcdacab", "eafbbacaaebcbaca", "fdadfbffefacbdfce", "accbdebbdffcafbccfb", "baeddeed", "ddee", "bcbafbcbedbeaaecfc", "fcdbcffbfdfaccee", "febfadfeccfabcea", "ebeadeceffabb", "fcebefceaaedceb", "aadafadffdbacabeff", "fdbacb", "fdfbdcaddddcfdcfd", "cebcdfdeaeeaebfcbabf", "fcfccfcdebfcafffba", "efbdeed", "efebbdbfc"]

test_arr2 = ["abcw","baz","foo","bar","xtfn","abcdef"]
s = Solution()
print(s.maxProduct(test_arr))
