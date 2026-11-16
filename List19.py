def main(royxat):
    """
    Ro'yxat berilgan. Takrorlanuvchi elementlarni olib tashlab, birinchi uchragan tartibni saqlagan holda yangi ro'yxat qaytaring (append()).
    Argumentlar:
        royxat(list): ro'yxat
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    i=0
    while i<len(royxat):
        mahsulot=royxat[i]
        if ls.count(mahsulot)==0:
            ls.append(mahsulot)
        i+=1    
    return ls
print(main(["olma", "anor", "olma", "uzum", "olma"]))
