def main(mevalar, i, x):
    """
    Allamurodning bozorlik ro'yxati, indeks i va meva x berilgan. x ni i-o'ringa qo'shib qaytaring (insert()).
    Argumentlar:
        mevalar(list): mevalar
        i(int): indeks
        x(str): meva
    Qaytaradi:
        list: natija ro'yxati
    """
    mevalar.insert(i,x)
    return mevalar
print(main(["olma", "nok", "uzum"],1,"anor"))
