def main(mevalar):
    """
    Mevalar ro'yxati berilgan (unda albatta "olma" bor). Birinchi uchragan "olma" ni o'chirib, ro'yxatni qaytaring (remove()).
    Argumentlar:
        mevalar(list): mevalar
    Qaytaradi:
        list: natija ro'yxati
    """
    mevalar.remove("olma")
    return mevalar
print(main(["olma", "anor", "olma", "uzum", "olma"]))
