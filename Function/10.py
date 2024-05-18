def cek_anagram(kata1, kata2):
    return sorted(kata1) == sorted(kata2)

print(cek_anagram("listen", "silent"))
