def main(navbat, amallar):
    """
    Bankdagi navbat ro'yxati va amallar ro'yxati berilgan. "+Ism" amali shu ismni navbat oxiriga qo'shadi (append()). "-" amali navbatdagi birinchi odamni chiqaradi (pop(0)). Navbat bo'sh bo'lsa, "-" hech narsa qilmaydi. Barcha amallardan keyingi navbatni qaytaring.
    Argumentlar:
        navbat(list): navbat
        amallar(list): amallar
    Qaytaradi:
        list: natija ro'yxati
    """
    l = len(amallar)
    i = 0
    while i < l:
        if amallar[i][0]=='+':
            navbat.append(amallar[i][1::])
        else:
            navbat.pop(0)
        i+=1
    return navbat

navbat=["Akmal", "Dilshod"]
amallar=["+Allamurod", "-", "+Sardor"]
print(main(navbat, amallar))