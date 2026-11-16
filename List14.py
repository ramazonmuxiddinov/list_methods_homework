def main(royxat):
    """
    Allamurodning haftalik sport jadvali berilgan (1 — bordi, 0 — bormadi). [birlar soni, nollar soni] ro'yxatini qaytaring (count()).
    Argumentlar:
        royxat(list): 0 va 1 lar
    Qaytaradi:
        list: natija ro'yxati
    """
    bir=royxat.count(1)
    nol=royxat.count(0)
    return [bir,nol]
print(main([1, 0, 1, 1, 0, 0, 1]))
