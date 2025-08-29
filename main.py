TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
uzivatele = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

#jmeno = input("Zadej uživatelské jméno: ")
#heslo = input("Zadej heslo: ")

#if jmeno in uzivatele and uzivatele[jmeno] == heslo:
#    print(f"Ahoj {jmeno}! Pusťme se do práce.")
#else:
#    print("Kombinace jména a hesla je nesprávná. Ukončuji program.")
#    quit()

seznam_textu = dict(enumerate(TEXTS,1))

cislo_textu = input("Vyber si číslo textu od 1 do 3.")

if not cislo_textu.isdigit():
    print("Neplatný znak. Ukončuji program.")
    quit()
elif int(cislo_textu) not in range(1,4):
    print("Zvolené číslo neodpovídá zadanému rozsahu. Ukončuji program.")
    quit()

zvoleny_text = seznam_textu[int(cislo_textu)]

zvoleny_text = zvoleny_text.split()

pocet_slov = len(zvoleny_text)
print(pocet_slov)

pocet_title_slov = 0

for title_slovo in zvoleny_text:
    if title_slovo[0].isupper():
        pocet_title_slov += 1

print(pocet_title_slov)

pocet_velkych_slov = 0

for velke_slovo in zvoleny_text:
    if velke_slovo.isupper():
        pocet_velkych_slov += 1

print(pocet_velkych_slov)

pocet_malych_slov = 0

for male_slovo in zvoleny_text:
    if male_slovo.islower():
        pocet_malych_slov += 1

print (pocet_malych_slov)

pocet_cisel = 0
soucet_cisel = 0

for cislo in zvoleny_text:
    if cislo.isdigit():
        pocet_cisel += 1
        soucet_cisel += int(cislo)

print(pocet_cisel)
print(soucet_cisel)

cetnost = {}

for slovo in zvoleny_text:
    delka = len(slovo)
    if delka in cetnost:
        cetnost[delka] += 1
    else:
        cetnost[delka] = 1

print(sorted(cetnost.items()))