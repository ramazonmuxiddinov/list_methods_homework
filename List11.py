def main(numbers1, numbers2):
    """
    Ikkita ro'yxat numbers1 va numbers2 berilgan. numbers1 ning oxirgi elementini o'chirib (pop()), uni numbers2 ning boshiga qo'shing (insert()). So'ng numbers1 ning qolgan elementlarini numbers2 ning oxiriga qo'shib (extend()), numbers2 ni qaytaring.
    Argumentlar:
        numbers1(list): 1-ro'yxat
        numbers2(list): 2-ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    oxirgi=numbers1.pop()
    numbers2.insert(0,oxirgi)
    numbers2.extend(numbers1)
    return numbers2
print(main([1,2,3],[4,5]))
print(main([26],[178,74]))
