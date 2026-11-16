def main(royxat, i):
    """
    Allamurodning oylik daromadlari ro'yxati va indeks i berilgan. i-indeksdagi elementni o'chirib, ro'yxatni qaytaring (pop()).
    Argumentlar:
        royxat(list): daromadlar
        i(int): indeks
    Qaytaradi:
        list: natija ro'yxati
    """
    royxat.pop(i)
    return royxat
print(main([6500000, 7200000, 6800000],1))
