immutable_var = [1, 2, 3, "cake", True]
print(immutable_var)
#immutable_var[0] = 200
#кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3, 5]
mutable_list.remove(5)
mutable_list.append(4)
mutable_list.extend(["birds", 5])
print(mutable_list)

