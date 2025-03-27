def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

print(lengthOfLastWord("   fly me   to   the moon  "))