def main(mevalar):
    """
    Mevalar ro'yxati berilgan. Undagi barcha "olma" larni o'chirib, ro'yxatni qaytaring (count() va remove()).
    Argumentlar:
        mevalar(list): mevalar
    Qaytaradi:
        list: natija ro'yxati
    """
    olma=mevalar.count("olma")
    i=0
    while i<olma:
        mevalar.remove("olma")
        i+=1
    return mevalar
print(main(["olma", "anor", "olma", "uzum", "olma"]))
print(main(["olma", "nok", "uzum"]))