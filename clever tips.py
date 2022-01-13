# """Tip 1-many inputs in a single line"""
# name, location, id, phone = input("Enter your details:name,location, id, phone: \n").split(',')
# print("My name is", name, 'from', location, '\nMy id number is', int(id) * 2, 'and telephone number is', phone)
# """Tip 2-conditions in a list"""''
# a, b, c = 1200, 1500, 2344
# condition = [a > 200,
#              b == 1500,
#              c > 1299]
# if any(condition):
#     print("True")
# else:
#     print("False")
#
# if all(condition):
#     print('Truee')
# else:
#     print("Falsee")
# """Tip 3-find if its a palindrome"""
# a = 12121
# aa = str(a)
# rev = aa.find(aa[::-1])
# print(rev)
# name = ['madam', 'sus', 'house', 'dad']
# for i in name:
#     rev = i.find(i[::-1])
#     print(rev)
# """Find the max and min value in a list"""
# list_name = [11, 11, 11, 11, 2, 22, 22, 2, 1]
# # print(list(set(list_name)))
# most = max(set(list_name), key=list_name.count)
# print(most)
# not_most = min(set(list_name), key=list_name.count)
# print(not_most)
