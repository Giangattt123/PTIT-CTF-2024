## Writeup

- Đề bài cho 1 file `beginner_reverse.exe` , cho vào `ida` và tôi thấy một chuỗi **"This is your flag"** có thể là nơi chứa `flag`

![img13](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-13.png?raw=true)

- Đọc nội dung của nó xem hàm này hoạt động như thế nào

![img14](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-14.png?raw=true)

- Có thể thấy nó lấy các giá trị của mảng `dword_403040` đem đi `xor` với giá trị của `Str[i % v1]` để ra từng ký tự của flag

- Kiểm tra các giá trị của `dword_403040` và chuỗi `Str`

![img15](https://github.com/Giangattt123/PTIT-CTF-2024/blob/master/VL/images/image-15.png?raw=true)

> Mảng `dword_403040` sau khi convert về hệ 10:

```
dword_403040 = [34, 49, 63, 49, 49, 39, 35, 9, 33, 70, 11, 85, 7, 58, 0, 48, 24, 58, 65, 11, 86, 45, 85, 0, 85, 15]
```

> Chuỗi Str: `reverse`

- Từ đó ta viết đoạn code để tìm ra `flag` như sau:

```
from typing import List
dword_403040 : List[int] = [34, 49, 63, 49, 49, 39, 35, 9, 33, 70, 11, 85, 7, 58, 0, 48, 24, 58, 65, 11, 86, 45, 85, 0, 85, 15]
Str : str = "reverse"
flag : str = ""

for i in range(26):
    flag += chr(dword_403040[i] ^ ord(Str[i % len(Str)]))
print(flag)
```

> Flag: PTITCTF{D0n't_rUn_3x3_0v0}
