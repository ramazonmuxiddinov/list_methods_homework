def main(mevalar):
    """
    Mevalar ro'yxati berilgan (unda albatta "uzum" bor). "uzum" ning indeksini qaytaring (index()).
    Argumentlar:
        mevalar(list): mevalar
    Qaytaradi:
        int: natija
    """
    x=mevalar.index("uzum")
    return x
print(main(["olma", "nok", "uzum"]))
print(main(["olma", "anor", "olma", "uzum", "olma"]))
