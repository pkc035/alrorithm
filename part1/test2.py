import time

def logging_time(origin_fn):
    def wrapper_fn(*args, **kwargs):
        start_time = time.time()
        result = origin_fn(*args, **kwargs)
        end_time = time.time()

        print("Working time [{}] : {} sec".format(origin_fn.__name__, end_time-start_time))
        return result
    return wrapper_fn

#팰린드롬
#앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장

#1.1 리스트로 변환
@logging_time
def vaildPalindrome(s: str) -> bool:
    strs = []

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True

#1.2 데크 자료형을 이용한 최적화
import collections

@logging_time
def vaildPalindrome2(s: str) -> bool:
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

#1.3 슬라이싱 사용
import re

@logging_time
def vaildPalindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

#문자열 뒤집기

@logging_time
def reverseString(s: list[str]) -> None:
    print(s.reverse())

@logging_time
def reverseString2(s: list[str]) -> None:
    print(s[::-1])

#로그 파일 재정렬

@logging_time
def reorderLogFiles(logs: list[str]) -> list[str]:
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    
    return letters + digits

#가장 흔한 단어
#금지된 단어를 제외한 가장 흔하게 등장하는 단어 출력

@logging_time
def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                if word not in banned]

    counts = collections.Counter(words)

    print(counts.most_common(1))

    return counts.most_common(1)[0][0]


#그룹 애너그램
#문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    return list(anagrams.values())

#가장 긴 팰린드롬 부분 문자열
#1. 중앙을 중심으로 확장하는 풀이

def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]
    
    if len(s) < 2 or s ==s[::-1]:
        return s
    
    result = ''

    for i in range(len(s) - 1):
        result = max(result,
                    expand(i, i+1),
                    expand(i, i+2),
                    key=len)
    
    return result

if __name__ == "__main__":
    test = "A man, a plan, a canal: Panama"
    test2 = "race a car"
    print("result : ",vaildPalindrome(test))
    print("result : ",vaildPalindrome(test2))

    print("result : ",vaildPalindrome2(test))
    print("result : ",vaildPalindrome2(test2))

    print("result : ",vaildPalindrome3(test))
    print("result : ",vaildPalindrome3(test2))

    print("result : ",reverseString(list(test)))
    print("result : ",reverseString2(list(test2)))

    test3 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print("result : ",reorderLogFiles(list(test3)))
    
    test4 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print("result : ",mostCommonWord(test4, banned))

    test5 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("result : ",groupAnagrams(test5))

    test6 = "babad"
    print("result : ",longestPalindrome(test6))