from __future__ import print_function, division

import anagram_sets

def metathesis_pairs(d):
    """通过交换两个字母，打印出所有不同的单词对。
       D:从单词映射到字谜列表
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)

def word_distance(word1, word2):
    """计算两个单词之间的差异数。
       Word1, word2:字符串
       返回:整数
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count

if __name__ == '__main__':
    sets = anagram_sets.all_anagrams('words.txt')
    metathesis_pairs(sets)
