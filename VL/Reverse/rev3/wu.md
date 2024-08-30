## Writeup

- Nhìn vào file được cung cấp có thể thấy ngay đây là file `exe` được biên dịch ra từ file `python`

![img16](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-16.png?raw=true)

- Sử dụng [pyinstxtractor](https://github.com/extremecoders-re/pyinstxtractor) để `extract` ra các file `.pyc`

![img17](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-17.png?raw=true)

- Đi vào folder vừa được `extract` tôi tìm thấy 1 file có thể là nơi để tìm ra flag là `chall.pyc`

![img18](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-18.png?raw=true)

- Để decomple file .pyc tôi sử dụng tool [pycdc](https://github.com/zrax/pycdc)(do tool này dùng `lệnh`) , nếu không muốn dùng `lệnh` có thể sử dụng `tool online` [pylingual](https://pylingual.io/)

![img19](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-19.png?raw=true)

- Tôi ra được 2 mảng `a` và `b` như bên dưới

```
    a = [
        201,
        109,
        176,
        225,
        31,
        132,
        131,
        32,
        183,
        80,
        161,
        50,
        159,
        19,
        105,
        46,
        166,
        227,
        151,
        123,
        56,
        143,
        47,
        50,
        223,
        162,
        216,
        94,
        25,
        170,
        78,
        169,
        34,
        96,
        22,
        68,
        69,
        48,
        57,
        154,
        155,
        64]
    b = [
        153,
        57,
        249,
        181,
        92,
        208,
        197,
        91,
        199,
        41,
        144,
        92,
        236,
        103,
        93,
        66,
        202,
        208,
        229,
        36,
        95,
        191,
        112,
        85,
        239,
        253,
        186,
        44,
        113,
        194,
        38,
        193,
        20,
        87,
        32,
        34,
        36,
        5,
        92,
        175,
        253,
        61]
```

- Tiến hành xor các giá trị của 2 mảng lại để lấy được `flag`

```
def xor_decrypt(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result

a = [
    201, 109, 176, 225, 31, 132, 131, 32, 183, 80, 161, 50, 159, 19,
    105, 46, 166, 227, 151, 123, 56, 143, 47, 50, 223, 162, 216, 94,
    25, 170, 78, 169, 34, 96, 22, 68, 69, 48, 57, 154, 155, 64
]

b = [
    153, 57, 249, 181, 92, 208, 197, 91, 199, 41, 144, 92, 236, 103,
    93, 66, 202, 208, 229, 36, 95, 191, 112, 85, 239, 253, 186, 44,
    113, 194, 38, 193, 20, 87, 32, 34, 36, 5, 92, 175, 253, 61
]

decrypted = xor_decrypt(a, b)
print(''.join(chr(c) for c in decrypted))
```

> Flag: PTITCTF{py1nst4ll3r_g0_g0_brhhhh676fa5e5f}
