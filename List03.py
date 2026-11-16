def main(mevalar1, mevalar2):
    """
    Ikkita mevalar ro'yxati berilgan. Ikkinchisini birinchisiga qo'shib, birinchi ro'yxatni qaytaring (extend()).
    Argumentlar:
        mevalar1(list): 1-ro'yxat
        mevalar2(list): 2-ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    mevalar1.extend(mevalar2)
    return mevalar1
print(main(["olma", "nok", "uzum"],["anor", "shaftoli"]))
