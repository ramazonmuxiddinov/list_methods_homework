def main(royxat, mahsulot):
    """
    Allamurodning bozorlik ro'yxati va mahsulot nomi berilgan. Agar mahsulot ro'yxatda bo'lsa, u sotib olindi — o'chiring (remove()). Aks holda ro'yxat oxiriga qo'shing (append()). Ro'yxatni qaytaring.
    Argumentlar:
        royxat(list): bozorlik ro'yxati
        mahsulot(str): mahsulot
    Qaytaradi:
        list: natija ro'yxati
    """
    if mahsulot in royxat:
       royxat.remove(mahsulot)
    else:
       royxat.append(mahsulot)
    return royxat
print(main(["olma", "nok", "uzum"],"nok"))
print(main(["olma", "nok", "uzum"],"non"))