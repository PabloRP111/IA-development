list2 = [6, 3, 9, 2, 10, 31, 15, 7]
list1 = [6]
if (len(list1) > 2):
    max = list1[int((len(list1)/2) + 1)]
else:
    max = list1[0]
for i in range(0, int((len(list1)/2) + 1)):
    if (max < list1[i]):
        max = list1[i]
    if (max < list1[int(-(i + 1))]):
        max = list1[int(-(i + 1))]
print(f"El número mas grande es {max} y lo encontre en {i} iteraciones")