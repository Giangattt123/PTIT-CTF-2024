from typing import List
dword_403040 : List[int] = [34, 49, 63, 49, 49, 39, 35, 9, 33, 70, 11, 85, 7, 58, 0, 48, 24, 58, 65, 11, 86, 45, 85, 0, 85, 15]
Str : str = "reverse"
flag : str = ""

for i in range(26):
    flag += chr(dword_403040[i] ^ ord(Str[i % len(Str)]))
print(flag)