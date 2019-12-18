#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Snowball stemmer.
"""

import re
import unittest

global_match = []

class Stemmer:
    # Helper regex strings.
    _vowel = "[аәоөұүыіеиуёэюя]"
    _non_vowel = "[^аәоөұүыіеиуёэюя]"

    # Word regions.
    _re_rv = re.compile(_vowel)
    _re_r1 = re.compile(_vowel + _non_vowel)

    # Endings.

    _re_all = re.compile(
        r"(шалық|шелік|даған|деген|таған|теген|лаған|леген|"
	r"дайын|дейін|тайын|тейін|"
        r"ңдар|ңдер|дікі|тікі|нікі|атын|етін|йтын|йтін|"
	r"гелі|қалы|келі|ғалы|шама|шеме|"
	r"мын|мін|бын|бін|пын|пін|мыз|міз|быз|біз|пыз|піз|сың|сің|"
	r"сыз|сіз|ңыз|ңіз|дан|ден|тан|тен|нан|нен|нда|нде|дың|дің|тың|"
	r"тің|ның|нің|дар|дер|тар|тер|лар|лер|бен|пен|мен|"
	r"дай|дей|тай|тей|дық|дік|тық|тік|лық|лік|паз|"
	r"ғыш|гіш|қыш|кіш|шек|шақ|шыл|шіл|нші|ншы|дап|деп|"
	r"тап|теп|лап|леп|даc|деc|таc|теc|лаc|леc|ғар|гер|қар|кер|дыр|"
	r"дір|тыр|тір|ғыз|гіз|қыз|кіз|ған|ген|қан|кен|"
	r"ушы|уші|лай|лей|сын|сін|бақ|бек|пақ|пек|мақ|мек|йын|йін|йық|йік|"
	r"сы|сі|да|де|та|те|ға|ге|қа|ке|на|не|"
	r"ді|ты|ті|ны|ні|ды|ба|бе|па|пе|ма|ме|"
	r"лы|лі|ғы|гі|қы|кі|ау|еу|ла|ле|ар|ер|"
	r"ып|іп|ша|ше|са|се|"
        r"лақ|лық|"
	r"н|р|п|й|ы|і)$"
    )

    def stem(self, word):

        """
        Gets the stem.
        """

        rv_pos, r2_pos = self._find_rv(word), self._find_r2(word)

        word1 = self._step_1(word, r2_pos)

        while word1 != word:
            word = word1
            word1 = self._step_1(word, r2_pos)

        return word1

    def _find_rv(self, word):

        """
        Searches for the RV region.
        """

        rv_match = self._re_rv.search(word)

        if not rv_match:
            return len(word)
        return rv_match.end()



    def _find_r2(self, word):

        """
        Searches for the R2 region.
        """

        r1_match = self._re_r1.search(word)
        if not r1_match:
            return len(word)
        r2_match = self._re_r1.search(word, r1_match.end())
        if not r2_match:
            return len(word)
        return r2_match.end()

    def _cut(self, word, ending, pos):

        """
        Tries to cut the specified ending after the specified position.
        """
        global global_match
        match = ending.search(word, pos)
        for_match = str(match)
        global_match.append(for_match)
        if match:
            try:
                ignore = match.group("ignore") or ""
            except IndexError:
                # No ignored characters in pattern.
                return True, word[:match.start()]
            else:
                # Do not cut ignored part.
                return True, word[:match.start() + len(ignore)]
        else:
            return False, word
    
    def _step_1(self, word, r_pos):

        _, word = self._cut(word, self._re_all, r_pos)
        return word


class TestStemmer(unittest.TestCase):
    global global_match

    """
    Tests the stemmer.
    """

    _stemmer = Stemmer()
    
    def test_stem(self):


        with open("diffs-kazak.txt", "rt", encoding="utf-8") as diffs_file:
            diffs = diffs_file.readlines()
        for i, line in enumerate(diffs):
            word, stem = line.split()
            self.assertEqual(
                stem,
                self._stemmer.stem(word),
                "Diff in word: %s (%d/%d)" % (word, i + 1, len(diffs)),
            )


if __name__ == "__main__":



    """"
    unittest.main()
    """

    stemmer = Stemmer()



    array_word = []
    array_word_match = []

    open_file = open('Final/FinalKZ.txt',"r")
    lines_open_file = open_file.readlines()

    for x in lines_open_file:
        word = x
        word = stemmer.stem(word)
        match_word = ''
        for i in global_match:
            if i == 'None':
                global_match.remove(i)

        if len(global_match) == 0:
            match_word = 'NONE'
            print(x.rstrip() + '\t' + match_word + '\t' + word.rstrip())
            array_word.append(word.rstrip())
            array_word_match.append(match_word)
        else:

            for i in range(len(global_match)):
                result = re.findall(r"match='(\w+)",global_match[i])
                global_match[i] = ''.join(result)

            global_match.reverse()

            for i in global_match:
                if i == '':
                    global_match.remove(i)

            for i in global_match:
                match_word = match_word + '-'+''.join(i)
            print(x.rstrip() + '\t' + word+match_word+'\t'+word)
            array_word.append(word)
            array_word_match.append(word+match_word)

        print('-'*50)
        global_match.clear()
    print(len(array_word))
    print(len(array_word_match))

    file_array_word = open('Final/Array_word.txt','w+')
    file_array_word_match = open('Final/Array_word_match.txt','w+')
    for i in array_word:
        file_array_word.writelines(i+'\n')
    for i in array_word_match:
        file_array_word_match.writelines(i+'\n')
    file_array_word.close()
    file_array_word_match.close()



    
