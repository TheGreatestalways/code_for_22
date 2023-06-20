

# def str_counter(my_string):
#     my_set = set(my_string)
#     print(my_set)
#     for i in my_set:
#         count = 0
#         for j in my_string:
#             if i == j:
#                 count += 1
#         print(i, count)

def str_counter(my_string):
    my_dict = {}
    for i in my_string:
        my_dict[i] = my_dict.get('a', 0) + 1
    print(my_dict)








# str_counter('abc')
str_counter('aaaaaaaaaaaabbbbbbb454c')