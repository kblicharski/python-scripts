list = ['a', 'a', 'b', 'b', 'b']
dict = {'a': 1, 'b': 2, 'c': 3}
output_list = []

for i in range(len(list)):
    if list[i] in dict.keys():
        output_list.append(dict[list[i]])
print(output_list)


output_list = [dict[list[i]] for i in range(len(list))
               if list[i] in dict.keys()]
print(output_list)

