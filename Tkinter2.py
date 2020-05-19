import random
uniq = [1,2,3,4,5]
fifa = ['a','b','c','d','e']
uniq_and_fifa = dict(zip(uniq, fifa))
a = {'Родное 15':['Пашем 17', 'Бороним 119'],'ytРодное 18':['ytПашем 7', 'ytБороним 9'], 'RytРодное 10':['RytПашем 7', 'RytБороним 9']}

for key in a:
    print(int(key[-2:]))
print(a['Родное 15'][0][-3:])
print(a['Родное 15'][1][-3:])
print(a['Родное 15'])
# b = a.values()
# b = list(b)
# c = []
# d=''
# jтобразить список задач без квадратных скобок
# for i in range(len(b)):
#     for k in range(len(b[i])):
#         d += ' ' + b[i][k]+','
#     c.append(d)
#     d = ''
#
# print(c)