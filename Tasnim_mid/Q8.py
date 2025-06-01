list1 = [1,2,3,4,5]
list2 = [4,5,3,6,7,8,9]
print(f'list1 {list1} \nlist2 {list2}')
union = list()
for i in list1:
    union.append(i)

for i in list2:
    if i not in list1:
        union.append(i)
print(f'union {union}')

inter = list()

for i in list2:
    if i in list1:
        inter.append(i)

print(f'Intersection {inter}')
