rom_num = input()

print(rom_num, 'in arabic numbers')

alloc = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

k = len(rom_num)
arb_num = 0
pst_curr = 0
while k > 0:
    curr = alloc[rom_num[k-1]]
    if curr < pst_curr:
        curr = - curr
    arb_num = arb_num+curr
    k = k-1
    pst_curr = curr; del curr

del k; del pst_curr

print('equals to', arb_num, '.')
