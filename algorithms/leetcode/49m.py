# https://leetcode.com/problems/group-anagrams/

# leetcode 49
# medium

from collections import Counter, defaultdict


def solution(strs):
    anagrams = defaultdict(list)
    for word in strs:
        cnt = Counter(word)
        key = tuple([(k, cnt[k]) for k in sorted(cnt.items())])
        anagrams[key].append(word)
    return list(anagrams.values())


def simple(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = sorted(word)
        anagrams[key].append(word)
    return list(anagrams.values())