# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
my_list = [1, 3, 3, 5, 1, 6 ,9, 9, 9]
def double_list(array: list[int]):
    res = set()
    for el in array:
        counter = array.count(el)
        if counter > 1:
            res.add(el)
    return list(res)


print(double_list(my_list))