## Writeup

Đoạn code thực hiện như sau:

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+20h] [rbp-60h]
  int v5; // [rsp+28h] [rbp-58h]
  int v6; // [rsp+30h] [rbp-50h]
  int v7; // [rsp+38h] [rbp-48h]
  int v8; // [rsp+40h] [rbp-40h]
  int v9; // [rsp+48h] [rbp-38h]
  char Buffer[112]; // [rsp+50h] [rbp-30h] BYREF
  int v11[102]; // [rsp+C0h] [rbp+40h] BYREF
  int j; // [rsp+258h] [rbp+1D8h]
  int v13; // [rsp+25Ch] [rbp+1DCh]
  int v14; // [rsp+260h] [rbp+1E0h]
  int v15; // [rsp+264h] [rbp+1E4h]
  int v16; // [rsp+268h] [rbp+1E8h]
  int v17; // [rsp+26Ch] [rbp+1ECh]
  int v18; // [rsp+270h] [rbp+1F0h]
  unsigned int v19; // [rsp+274h] [rbp+1F4h]
  unsigned int v20; // [rsp+278h] [rbp+1F8h]
  unsigned int i; // [rsp+27Ch] [rbp+1FCh]

  _main();
  logo();
  puts("Your input");
  for ( i = 0; (int)i <= 99; ++i )
  {
    printf("x[%d] = ", i);
    scanf("%d", &v11[i]);
  }
  if ( (unsigned __int8)check_equations(v11) )
  {
    puts("Correct.");
    v20 = 0;
    v19 = 0;
    v18 = 0;
    v17 = 0;
    v16 = 0;
    v15 = 0;
    v14 = 0;
    v13 = 0;
    for ( j = 0; j <= 99; ++j )
    {
      if ( (v11[j] & 1) == 0 )
        v20 += v11[j];
      if ( !(v11[j] % 3) )
        v19 += v11[j];
      if ( (v11[j] & 3) == 0 )
        v18 += v11[j];
      if ( !(v11[j] % 5) )
        v17 += v11[j];
      if ( !(v11[j] % 6) )
        v16 += v11[j];
      if ( !(v11[j] % 7) )
        v15 += v11[j];
      if ( (v11[j] & 7) == 0 )
        v14 += v11[j];
      if ( !(v11[j] % 9) )
        v13 += v11[j];
    }
    v9 = v13;
    v8 = v14;
    v7 = v15;
    v6 = v16;
    v5 = v17;
    v4 = v18;
    sprintf(Buffer, "PTITCTF{%x%x%x%x%x%x%x%x}", v20, v19, v4, v5, v6, v7, v8, v9);
    puts(Buffer);
  }
  else
  {
    puts("Wrong");
  }
  return 0;
}
```

- Đề bài cho phép nhập 100 phần tử của mảng `v5` và kiểm tra một loạt các phương trình thỏa mãn ở hàm `check_equation` nếu đúng sẽ lấy được `flag`

- Xem nội dung hàm `check_equation`

```
_BOOL8 __fastcall check_equations(int *a1)
{
  return *a1 + a1[1] == 4
      && a1[1] + a1[2] == 6
      && a1[2] + a1[3] == 8
      && a1[3] + a1[4] == 10
      && a1[4] + a1[5] == 12
      && a1[5] + a1[6] == 14
      && a1[6] + a1[7] == 16
      && a1[7] + a1[8] == 18
      && a1[8] + a1[9] == 20
      && a1[9] + a1[10] == 22
      && a1[10] + a1[11] == 24
      && a1[11] + a1[12] == 26
      && a1[12] + a1[13] == 28
      && a1[13] + a1[14] == 30
      && a1[14] + a1[15] == 32
      && a1[15] + a1[16] == 34
      && a1[16] + a1[17] == 36
      && a1[17] + a1[18] == 38
      && a1[18] + a1[19] == 40
      && a1[19] + a1[20] == 42
      && a1[20] + a1[21] == 44
      && a1[21] + a1[22] == 46
      && a1[22] + a1[23] == 48
      && a1[23] + a1[24] == 50
      && a1[24] + a1[25] == 52
      && a1[25] + a1[26] == 54
      && a1[26] + a1[27] == 56
      && a1[27] + a1[28] == 58
      && a1[28] + a1[29] == 60
      && a1[29] + a1[30] == 62
      && a1[30] + a1[31] == 64
      && a1[31] + a1[32] == 66
      && a1[32] + a1[33] == 68
      && a1[33] + a1[34] == 70
      && a1[34] + a1[35] == 72
      && a1[35] + a1[36] == 74
      && a1[36] + a1[37] == 76
      && a1[37] + a1[38] == 78
      && a1[38] + a1[39] == 80
      && a1[39] + a1[40] == 82
      && a1[40] + a1[41] == 84
      && a1[41] + a1[42] == 86
      && a1[42] + a1[43] == 88
      && a1[43] + a1[44] == 90
      && a1[44] + a1[45] == 92
      && a1[45] + a1[46] == 94
      && a1[46] + a1[47] == 96
      && a1[47] + a1[48] == 98
      && a1[48] + a1[49] == 100
      && a1[49] + a1[50] == 102
      && a1[50] - a1[51] == 104
      && a1[51] + a1[52] == 106
      && a1[52] + a1[53] == 108
      && a1[53] + a1[54] == 110
      && a1[54] + a1[55] == 112
      && a1[55] + a1[56] == 114
      && a1[56] + a1[57] == 116
      && a1[57] + a1[58] == 118
      && a1[58] + a1[59] == 120
      && a1[59] + a1[60] == 122
      && a1[60] + a1[61] == 124
      && a1[61] + a1[62] == 126
      && a1[62] + a1[63] == 128
      && a1[63] + a1[64] == 130
      && a1[64] + a1[65] == 132
      && a1[65] + a1[66] == 134
      && a1[66] + a1[67] == 136
      && a1[67] + a1[68] == 138
      && a1[68] + a1[69] == 140
      && a1[69] + a1[70] == 142
      && a1[70] + a1[71] == 144
      && a1[71] + a1[72] == 146
      && a1[72] + a1[73] == 148
      && a1[73] + a1[74] == 150
      && a1[74] + a1[75] == 152
      && a1[75] + a1[76] == 154
      && a1[76] + a1[77] == 156
      && a1[77] + a1[78] == 158
      && a1[78] + a1[79] == 160
      && a1[79] + a1[80] == 162
      && a1[80] + a1[81] == 164
      && a1[81] + a1[82] == 166
      && a1[82] + a1[83] == 168
      && a1[83] + a1[84] == 170
      && a1[84] + a1[85] == 172
      && a1[85] + a1[86] == 174
      && a1[86] + a1[87] == 176
      && a1[87] + a1[88] == 178
      && a1[88] + a1[89] == 180
      && a1[89] + a1[90] == 182
      && a1[90] + a1[91] == 184
      && a1[91] + a1[92] == 186
      && a1[92] + a1[93] == 188
      && a1[93] + a1[94] == 190
      && a1[94] + a1[95] == 192
      && a1[95] + a1[96] == 194
      && a1[96] + a1[97] == 196
      && a1[97] + a1[98] == 198
      && a1[98] + a1[99] == 200
      && a1[99] + *a1 == 202;
}
```

- Script để giải các phương trình đồng thời trên , ở đây tôi sử dụng thư viện [Z3Solver](https://pypi.org/project/z3-solver/) của `python`:

```
from z3 import *
solver = Solver()
x = [Int(f'x{i}') for i in range(100)]
solver.add(x[0] + x[1] == 4)
solver.add(x[1] + x[2] == 6)
solver.add(x[2] + x[3] == 8)
solver.add(x[3] + x[4] == 10)
solver.add(x[4] + x[5] == 12)
solver.add(x[5] + x[6] == 14)
solver.add(x[6] + x[7] == 16)
solver.add(x[7] + x[8] == 18)
solver.add(x[8] + x[9] == 20)
solver.add(x[9] + x[10] == 22)
solver.add(x[10] + x[11] == 24)
solver.add(x[11] + x[12] == 26)
solver.add(x[12] + x[13] == 28)
solver.add(x[13] + x[14] == 30)
solver.add(x[14] + x[15] == 32)
solver.add(x[15] + x[16] == 34)
solver.add(x[16] + x[17] == 36)
solver.add(x[17] + x[18] == 38)
solver.add(x[18] + x[19] == 40)
solver.add(x[19] + x[20] == 42)
solver.add(x[20] + x[21] == 44)
solver.add(x[21] + x[22] == 46)
solver.add(x[22] + x[23] == 48)
solver.add(x[23] + x[24] == 50)
solver.add(x[24] + x[25] == 52)
solver.add(x[25] + x[26] == 54)
solver.add(x[26] + x[27] == 56)
solver.add(x[27] + x[28] == 58)
solver.add(x[28] + x[29] == 60)
solver.add(x[29] + x[30] == 62)
solver.add(x[30] + x[31] == 64)
solver.add(x[31] + x[32] == 66)
solver.add(x[32] + x[33] == 68)
solver.add(x[33] + x[34] == 70)
solver.add(x[34] + x[35] == 72)
solver.add(x[35] + x[36] == 74)
solver.add(x[36] + x[37] == 76)
solver.add(x[37] + x[38] == 78)
solver.add(x[38] + x[39] == 80)
solver.add(x[39] + x[40] == 82)
solver.add(x[40] + x[41] == 84)
solver.add(x[41] + x[42] == 86)
solver.add(x[42] + x[43] == 88)
solver.add(x[43] + x[44] == 90)
solver.add(x[44] + x[45] == 92)
solver.add(x[45] + x[46] == 94)
solver.add(x[46] + x[47] == 96)
solver.add(x[47] + x[48] == 98)
solver.add(x[48] + x[49] == 100)
solver.add(x[49] + x[50] == 102)
solver.add(x[50] - x[51] == 104)
solver.add(x[51] + x[52] == 106)
solver.add(x[52] + x[53] == 108)
solver.add(x[53] + x[54] == 110)
solver.add(x[54] + x[55] == 112)
solver.add(x[55] + x[56] == 114)
solver.add(x[56] + x[57] == 116)
solver.add(x[57] + x[58] == 118)
solver.add(x[58] + x[59] == 120)
solver.add(x[59] + x[60] == 122)
solver.add(x[60] + x[61] == 124)
solver.add(x[61] + x[62] == 126)
solver.add(x[62] + x[63] == 128)
solver.add(x[63] + x[64] == 130)
solver.add(x[64] + x[65] == 132)
solver.add(x[65] + x[66] == 134)
solver.add(x[66] + x[67] == 136)
solver.add(x[67] + x[68] == 138)
solver.add(x[68] + x[69] == 140)
solver.add(x[69] + x[70] == 142)
solver.add(x[70] + x[71] == 144)
solver.add(x[71] + x[72] == 146)
solver.add(x[72] + x[73] == 148)
solver.add(x[73] + x[74] == 150)
solver.add(x[74] + x[75] == 152)
solver.add(x[75] + x[76] == 154)
solver.add(x[76] + x[77] == 156)
solver.add(x[77] + x[78] == 158)
solver.add(x[78] + x[79] == 160)
solver.add(x[79] + x[80] == 162)
solver.add(x[80] + x[81] == 164)
solver.add(x[81] + x[82] == 166)
solver.add(x[82] + x[83] == 168)
solver.add(x[83] + x[84] == 170)
solver.add(x[84] + x[85] == 172)
solver.add(x[85] + x[86] == 174)
solver.add(x[86] + x[87] == 176)
solver.add(x[87] + x[88] == 178)
solver.add(x[88] + x[89] == 180)
solver.add(x[89] + x[90] == 182)
solver.add(x[90] + x[91] == 184)
solver.add(x[91] + x[92] == 186)
solver.add(x[92] + x[93] == 188)
solver.add(x[93] + x[94] == 190)
solver.add(x[94] + x[95] == 192)
solver.add(x[95] + x[96] == 194)
solver.add(x[96] + x[97] == 196)
solver.add(x[97] + x[98] == 198)
solver.add(x[98] + x[99] == 200)
solver.add(x[99] + x[0] == 202)


if solver.check() == sat:
    model = solver.model()
    solution = [model[x[i]].as_long() for i in range(100)]
    a = b = c = d = e = f = g = h = 0
    for i in range(100):
        value = model[x[i]].as_long()
        if value % 2 == 0: a += value
        if value % 3 == 0: b += value
        if value % 4 == 0: c += value
        if value % 5 == 0: d += value
        if value % 6 == 0: e += value
        if value % 7 == 0: f += value
        if value % 8 == 0: g += value
        if value % 9 == 0: h += value
    flag = "PTITCTF{{{:x}{:x}{:x}{:x}{:x}{:x}{:x}{:x}}}".format(a, b, c, d, e, f, g, h)
    print(flag)
```

> Flag: PTITCTF{14506909c43e869034854821c}
