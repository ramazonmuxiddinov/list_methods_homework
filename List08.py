def main(ballar):
    """
    Allamurodning fanlardan olgan ballari ro'yxati berilgan. Ro'yxatni o'sish tartibida saralab qaytaring (sort()).
    Argumentlar:
        ballar(list): ballar
    Qaytaradi:
        list: natija ro'yxati
    """
    ballar.sort()
    return ballar
print(main([87, 92, 78, 95]))
