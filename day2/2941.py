a = str(input())

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_list:
    a = a.replace(i, '*')

print(len(a))
