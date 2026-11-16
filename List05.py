def main(mevalar):
    """
    Mevalar ro'yxati berilgan. Unda nechta "olma" borligini qaytaring (count()).
    Argumentlar:
        mevalar(list): mevalar
    Qaytaradi:
        int: natija
    """
    x=mevalar.count("olma")
    return x
print(main(["olma", "anor", "olma", "uzum", "olma"]))
print(main(["olma","nok","uzum"]))