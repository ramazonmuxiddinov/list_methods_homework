def main(mevalar):
    """
    Mevalar ro'yxati berilgan. Barcha "olma" larning indekslarini ro'yxat ko'rinishida qaytaring (append()).
    Argumentlar:
        mevalar(list): mevalar
    Qaytaradi:
        list: natija ro'yxati
    """
    ls  = []
    i = 0 
    l = len(mevalar)
    while i<l:
        if mevalar[i]=='olma':
            ls.append(i)
        i +=1
    return ls

mevalar=["olma", "anor", "olma", "uzum", "olma"]
print(main(mevalar))