t1 = (1,'a')
t2 = (4,'c')
t3 = (3,'c')
t4 = (2,'b')

list_ = list()

list_.append(t1)
list_.append(t2)
list_.append(t3)
list_.append(t4)

print(list_)

dict_ = dict(list_)
print(dict_)


# Sorting the dictionary by value
sorted_dict = dict(sorted(dict_.items(), key=lambda item: item[1]))
print(sorted_dict)