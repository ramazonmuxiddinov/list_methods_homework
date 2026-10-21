# Ro'yxat metodlari

## List01

Allamurodning bozorlik ro'yxati va meva x berilgan. x ni ro'yxat oxiriga qo'shib qaytaring (`append()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "nok", "uzum"], x="anor"
Chiqarish: ["olma", "nok", "uzum", "anor"]
```

---

## List02

Allamurodning bozorlik ro'yxati, indeks i va meva x berilgan. x ni i-o'ringa qo'shib qaytaring (`insert()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "nok", "uzum"], i=1, x="anor"
Chiqarish: ["olma", "anor", "nok", "uzum"]
```

---

## List03

Ikkita mevalar ro'yxati berilgan. Ikkinchisini birinchisiga qo'shib, birinchi ro'yxatni qaytaring (`extend()`).

**Misol 1:**

```Python
Kirish: mevalar1=["olma", "nok", "uzum"], mevalar2=["anor", "shaftoli"]
Chiqarish: ["olma", "nok", "uzum", "anor", "shaftoli"]
```

---

## List04

Allamurodning oylik daromadlari ro'yxati va indeks i berilgan. i-indeksdagi elementni o'chirib, ro'yxatni qaytaring (`pop()`).

**Misol 1:**

```Python
Kirish: royxat=[6500000, 7200000, 6800000], i=1
Chiqarish: [6500000, 6800000]
```

---

## List05

Mevalar ro'yxati berilgan. Unda nechta "olma" borligini qaytaring (`count()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "anor", "olma", "uzum", "olma"]
Chiqarish: 3
```

**Misol 2:**

```Python
Kirish: mevalar=["olma", "nok", "uzum"]
Chiqarish: 1
```

---

## List06

Allamurodning haftalik sport jadvali berilgan (1 — bordi, 0 — bormadi). Necha kun sportga bormaganini qaytaring (`count()`).

**Misol 1:**

```Python
Kirish: royxat=[1, 0, 1, 1, 0, 0, 1]
Chiqarish: 3
```

---

## List07

Mevalar ro'yxati berilgan (unda albatta "uzum" bor). "uzum" ning indeksini qaytaring (`index()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "nok", "uzum"]
Chiqarish: 2
```

**Misol 2:**

```Python
Kirish: mevalar=["olma", "anor", "olma", "uzum", "olma"]
Chiqarish: 3
```

---

## List08

Allamurodning fanlardan olgan ballari ro'yxati berilgan. Ro'yxatni o'sish tartibida saralab qaytaring (`sort()`).

**Misol 1:**

```Python
Kirish: ballar=[87, 92, 78, 95]
Chiqarish: [78, 87, 92, 95]
```

---

## List09

Ro'yxat berilgan. Uni teskari tartibga keltirib qaytaring (`reverse()`).

**Misol 1:**

```Python
Kirish: royxat=["olma", "nok", "uzum"]
Chiqarish: ["uzum", "nok", "olma"]
```

---

## List10

Mevalar ro'yxati berilgan (unda albatta "olma" bor). Birinchi uchragan "olma" ni o'chirib, ro'yxatni qaytaring (`remove()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "anor", "olma", "uzum", "olma"]
Chiqarish: ["anor", "olma", "uzum", "olma"]
```

---

## List11

Ikkita ro'yxat numbers1 va numbers2 berilgan. numbers1 ning oxirgi elementini o'chirib (`pop()`), uni numbers2 ning boshiga qo'shing (`insert()`). So'ng numbers1 ning qolgan elementlarini numbers2 ning oxiriga qo'shib (`extend()`), numbers2 ni qaytaring.

**Misol 1:**

```Python
Kirish: numbers1=[1, 2, 3], numbers2=[4, 5]
Chiqarish: [3, 4, 5, 1, 2]
```

**Misol 2:**

```Python
Kirish: numbers1=[26], numbers2=[178, 74]
Chiqarish: [26, 178, 74]
```

---

## List12

Mevalar ro'yxati berilgan. Undagi barcha "olma" larni o'chirib, ro'yxatni qaytaring (`count()` va `remove()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "anor", "olma", "uzum", "olma"]
Chiqarish: ["anor", "uzum"]
```

**Misol 2:**

```Python
Kirish: mevalar=["olma", "nok", "uzum"]
Chiqarish: ["nok", "uzum"]
```

---

## List13

Mevalar ro'yxati berilgan. Barcha "olma" larning indekslarini ro'yxat ko'rinishida qaytaring (`append()`).

**Misol 1:**

```Python
Kirish: mevalar=["olma", "anor", "olma", "uzum", "olma"]
Chiqarish: [0, 2, 4]
```

**Misol 2:**

```Python
Kirish: mevalar=["nok"]
Chiqarish: []
```

---

## List14

Allamurodning haftalik sport jadvali berilgan (1 — bordi, 0 — bormadi). `[birlar soni, nollar soni]` ro'yxatini qaytaring (`count()`).

**Misol 1:**

```Python
Kirish: royxat=[1, 0, 1, 1, 0, 0, 1]
Chiqarish: [4, 3]
```

---

## List15

Allamurodning test ballari ro'yxati berilgan. Eng past ballni bir marta o'chiring (`remove()`, `min()`) va qolgan ballarning o'rtachasini 1 xona aniqlikda yaxlitlab qaytaring.

**Misol 1:**

```Python
Kirish: ballar=[87, 92, 78, 95]
Chiqarish: 91.3
```

**Misol 2:**

```Python
Kirish: ballar=[60, 60, 90]
Chiqarish: 75.0
```

---

## List16

Allamurodning test ballari ro'yxati berilgan. Ballarni kamayish tartibida saralang (`sort(reverse=True)`) va eng yuqori 3 ta ballni qaytaring.

**Misol 1:**

```Python
Kirish: ballar=[87, 92, 78, 95, 81]
Chiqarish: [95, 92, 87]
```

---

## List17

Allamurodning bozorlik ro'yxati va mahsulot nomi berilgan. Agar mahsulot ro'yxatda bo'lsa, u sotib olindi — o'chiring (`remove()`). Aks holda ro'yxat oxiriga qo'shing (`append()`). Ro'yxatni qaytaring.

**Misol 1:**

```Python
Kirish: royxat=["olma", "nok", "uzum"], mahsulot="nok"
Chiqarish: ["olma", "uzum"]
```

**Misol 2:**

```Python
Kirish: royxat=["olma", "nok", "uzum"], mahsulot="non"
Chiqarish: ["olma", "nok", "uzum", "non"]
```

---

## List18

Allamurod va akasining bozorlik ro'yxatlari berilgan. Ikkala ro'yxatda ham bor mahsulotlarni birinchi ro'yxatdagi tartibda yangi ro'yxatga yig'ib qaytaring (`append()`).

**Misol 1:**

```Python
Kirish: royxat1=["olma", "nok", "uzum", "non"], royxat2=["non", "sut", "olma"]
Chiqarish: ["olma", "non"]
```

---

## List19

Ro'yxat berilgan. Takrorlanuvchi elementlarni olib tashlab, birinchi uchragan tartibni saqlagan holda yangi ro'yxat qaytaring (`append()`).

**Misol 1:**

```Python
Kirish: royxat=["olma", "anor", "olma", "uzum", "olma"]
Chiqarish: ["olma", "anor", "uzum"]
```

**Misol 2:**

```Python
Kirish: royxat=[2, 0, 0, 2, 6]
Chiqarish: [2, 0, 6]
```

---

## List20

Bankdagi navbat ro'yxati va amallar ro'yxati berilgan. "+Ism" amali shu ismni navbat oxiriga qo'shadi (`append()`). "-" amali navbatdagi birinchi odamni chiqaradi (`pop(0)`). Navbat bo'sh bo'lsa, "-" hech narsa qilmaydi. Barcha amallardan keyingi navbatni qaytaring.

**Misol 1:**

```Python
Kirish: navbat=["Akmal", "Dilshod"], amallar=["+Allamurod", "-", "+Sardor"]
Chiqarish: ["Dilshod", "Allamurod", "Sardor"]
```

**Misol 2:**

```Python
Kirish: navbat=[], amallar=["-", "+Allamurod"]
Chiqarish: ["Allamurod"]
```

