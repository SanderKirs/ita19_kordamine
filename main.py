#impordin teistest failidest kõik vajaliku
from plaat import *
from laulud import *
from esitaja import *

#küsin kas kasutaja soovib lisada albumit
b = input("Kas soovid lisada vinüülplaatide nimekirja albumit? jah/ei ")

#tsükkel, mis küsib lisatava albumi esitajat, albumit, aastat ja laulu
#ning lisab selle albumite faili
if b == "jah":
    seis = "aktiivne"
    grupp = esitaja(input("Sisestage esitaja nimi: "))
    album = plaat(input("Sisestage albumi nimi: "))
    aasta = input("Sisestage aasta: ")
    while seis == "aktiivne":

        laul = laulud(input("Sisestage laulu pealkiri:"))
        laulupealkiri = grupp.esitajaNimi.title() + "\t" + album.plaadiNimi.title() + "\t" + aasta + "\t" + laul.lauluNimi.title()
        fail = open("albumid.txt", "a", encoding="UTF-8")
        fail.write("\n" + laulupealkiri)
        #küsin kas soovitakse veel laule lisada
        b = input("Kas soovite veel laule lisada? jah/ei")
        if b == "jah":
            seis = "aktiivne"
        else:
            seis = "inaktiivne"
            fail.close()

else:
    pass
#küsin kas kasutaja soovib albumite nimekirja näha
y = input("Kas soovid näha vinüülplaatide nimekirja? jah/ei ")


fail = open("albumid.txt", encoding="UTF-8")
albumid = []

#funktsioon, mis poolitab read, lisab esineja, aasta, laulu ja albumi loendisse,
#ning teeb kriipsud, iga albumi tagant kriipsud koos esineja, aasta, albumi ja lauluga
def albumiteKriipsud():
    for rida in fail:
        elemendid = rida.split("\t")
        esineja = esitaja(elemendid[0])
        album = plaat(elemendid[1])
        albumid.append(elemendid[1])
        aasta = elemendid[2]
        laul = laulud(elemendid[3])
        if len(albumid) > 1:
            if albumid[-2] != albumid[-1]:
                print()
                print("--------------------------------------------")
                print()
        print(esineja.esitajaNimi, album.plaadiNimi, aasta, laul.lauluNimi)

if y == "jah":
    albumiteKriipsud()

#küsitakse kas kasutaja soovib otsida laulu
else:
    w = input("Kas soovid otsida laulu? jah/ei ")

#positiivse vastuse korral küsitakse artisti või albumi nime, mida otsitakse.
#negatiivse vastuse korral lõpetatakse tegevus ning pannakse fail kinni.
    if w == "jah":

        for rida in fail:
            albumid.append(rida)

        nimi = input("Sisesta albumi või artisti nimi: ")
        x = nimi.title()

        for str in albumid:
            if x in str:
                print(str)

    else:
        print("Ei soovinud midagi!")


fail.close()