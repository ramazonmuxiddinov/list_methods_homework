def main(royxat1, royxat2):
    """
    Allamurod va akasining bozorlik ro'yxatlari berilgan. Ikkala ro'yxatda ham bor mahsulotlarni birinchi ro'yxatdagi tartibda yangi ro'yxatga yig'ib qaytaring (append()).
    Argumentlar:
        royxat1(list): Allamurodning ro'yxati
        royxat2(list): akasining ro'yxati
    Qaytaradi:
        list: natija ro'yxati
    """
    ls=[]
    i=0
    while i<len(royxat1):
        mahsulot=royxat1[i]
        if mahsulot in royxat2:
            ls.append(mahsulot)
        i+=1    
    return ls
print(main(["olma", "nok", "uzum", "non"],["non", "sut", "olma"]))

