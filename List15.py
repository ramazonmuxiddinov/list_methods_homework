def main(ballar):
    """
    Allamurodning test ballari ro'yxati berilgan. Eng past ballni bir marta o'chiring (remove(), min()) va qolgan ballarning o'rtachasini 1 xona aniqlikda yaxlitlab qaytaring.
    Argumentlar:
        ballar(list): ballar
    Qaytaradi:
        float: o'rtacha ball
    """
    x=min(ballar)
    ballar.remove(x)
    urtacha=sum(ballar)/len(ballar)
    return round(urtacha,1)
print(main([87, 92, 78, 95]))
print(main([60, 60, 90]))
