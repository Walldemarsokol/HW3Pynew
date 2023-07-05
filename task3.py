# Создайте словарь со списком вещей для похода
# в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

stuff = {'map': 1, 'cup': 2, 'tent': 10, 'ration': 5, 'spare shoes': 3}

def backpack_capacity(capacity: int, stuff: dict):
    packaging_option = []
    for key, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(backpack_capacity(10, stuff))