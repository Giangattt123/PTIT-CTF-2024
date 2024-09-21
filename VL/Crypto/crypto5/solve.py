from Crypto.Util.number import *
from hashlib import *

def binary_to_string(binary_str):
    binary_str = binary_str.strip()
    if len(binary_str) % 8 != 0:
        raise ValueError("Binary string length is not a multiple of 8")
    
    binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values if all(c in '01' for c in bv)]
    return ''.join(ascii_characters)


with open('bin', 'r') as f:
    _k, n , _sum, sm = [int(binary_to_string(line).strip(), 16) for line in f.readlines()]

e = 65537
p = GCD(pow(_sum, e, n) - _k, n)
# pow(_sum, e, n) số mũ của chữ ký bị lỗi
q = n // p
print('flag{' + md5(str(p).encode()).hexdigest() + '}')
print('flag{' + md5(str(q).encode()).hexdigest() + '}')
"""
flag{32cf4ba1ab6c2724b7397dc9352c36e6}
flag{c345231b78deaf1f30944d8a7c6808b7}
"""