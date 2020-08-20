import random 
import string

# Satunnaisuus
print(random.randint(1, 10))

# Nopan heittäminen
print("Silmäluku: ", random.randint(1,6))

# Kolikon heitto
a = ["Kruna","Klaava"]
print("Tulos: " + random.choice(a))

#Salasanan arpoja
salasana = ""
merkkienmaara = 0

#Lisää uuden kirjaimen salasanaan kunnes kirjaimia on 8
while(merkkienmaara<8):
   salasana += random.choice(string.ascii_lowercase)
   merkkienmaara +=1

print("Salasanasi on: " + salasana)

#Sekoittaja



def sekoitaLista(luvut):

    random.shuffle(luvut)


def tulostaLista(luvut):

    print(luvut)

luvut = [1, 2, 3, 4, 5, 6, 7, 8]
sekoitaLista(luvut)
tulostaLista(luvut)

#Vihollisten sijainnit



def sijainnit():

    listanKoko = 0
    vihollistenSijainnit = ""

    while(listanKoko<1):

        listanKoko +=1
        xSijainti = random.randint(1,100)
        ySijainti = random.randint(1,100)
        lokaatio = str(xSijainti) + "," + str(ySijainti)
        vihollistenSijainnit += lokaatio

    return vihollistenSijainnit

print(sijainnit())

#Listan järjestäminen

#Listat
lista = [1, 3, 5, 4, 7, 8, 11, 91919, -1000, 1122]
aakkosJärjestys = ["a","b","ai","r","os","öd","ofk"]

#Listojen järjestäminen
lista.sort()
aakkosJärjestys.sort()

#Järjestettyjen listojen printtaus
print(lista) 
print(aakkosJärjestys)

#Pistelista
loppu = 0
while(loppu < 1):
  Nimi = input("Pelaajan nimi: ")
  Pisteet = input("Pisteiden määrä: ")
  Lopeta = input("Haluatko että tämä on käyttäjäsi?: ")
  if Lopeta == "kyllä":
     print("Pelaajan nimi: " + Nimi)
     print("Pelaajan pisteet: " + Pisteet)
     loppu = 1








