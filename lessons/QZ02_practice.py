"""Quiz practice function writing. ;(."""


def odd_and_even(nums: list[int]) -> list[int]:
    i: int = 0
    result: list[int] = list()
    while i < len(nums):
        if i % 2 == 0:
            if nums[i] % 2 != 0:
                result.append(nums[i])
        i += 1
    
    return result


def vowels_and_threes(a: str) -> str:
    i: int = 0
    result: str = ""
    is_vowel: bool = False
    j: int = 0
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    while i < len(a):
        is_vowel = False
        j = 0
        while j < len(vowels):
            if vowels[j] == a[i]:
                is_vowel = True
            j += 1
        if i % 3 == 0 and is_vowel:
            result += ""
        elif i % 3 == 0:
            result += a[i]
        elif is_vowel:
            result += a[i]
        i += 1
    return result
            
