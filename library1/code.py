#!/usr/bin/python
# coding=utf-8
# YLEISET MUUTTUJAT JOITA EI MUUTELLA MYÖHEMMIN#
# + ALUSTUKSET								  #
###############################################

import re
import math

dbfile = "tietokanta_tiedot.txt"

# TIETOKANNAN TIETOJEN KÄSITTELY KÄYTETTÄVÄÄN MUOTOON#
#####################################################

# ladataan tiedot tiedostosta arvoihin
# poistetaan ylimääräinen roska
kaikki = []
nodelist = []


def init(select):
    with open(dbfile) as file:
        for line in file:
            kaikki.append(re.sub(r'[\[|\]|\n|\'|\t|\{|\}|","|\s]', "", line))
    while '' in kaikki:
        kaikki.remove('')

    for index in range(len(kaikki)):
        if bool(re.search("edges", kaikki[index])):  # '"edges": [\n':    kaikki[index]

            break
        else:
            nodelist.append(kaikki[index])
            #continue
    if nodelist[0] == "nodes:":
        del nodelist[0]
    # määritellään nodelist. Kirjoitetaan listaan kunnes tullaan edges kohtaan.

    edgelist = kaikki
    #print(kaikki)
    for x in nodelist:
        try:
            edgelist.remove(x)
            #print("removing: ",x)
        except ValueError:
            print("error")
            pass
    del edgelist[0]

    #print(len(edgelist))




    #print(len(edgelist))
    #print(edgelist)
    if select is "nodes":
        return nodelist
    elif select is "edges":
        return edgelist


edges = init("edges")
nodes = init("nodes")




# määritellään edgelist. Poistetaan edgelistasta, joka sisältää aluksi kaikki listan, nodelist.
# poistetaan turhat edges: ja nodes: kohdat
varid = {"red": 25, "blue": 15, "green": 5}
def edgemuokkaus():
    mlr = edges

    ls = 0
    pakattulista_work = []
    rangestart = 0
    rangeend = 3
    templist = []

    for i in range(round(len(mlr)/2)):
        while bool(re.match("start:", mlr[i])) is True:
            templist.append(mlr[i])

            templist.append(mlr[i+1])

            templist.append(mlr[i+2])

            pakattulista_work.append(templist)
            break
        templist = []



    # while ls <= len(mlr) and rangeend <= len(mlr):
    #
    #     templist = []
    #
    #     for i in range(rangestart, rangeend, 1):
    #
    #
    #
    #
    #         # Append
    #         templist.append(mlr[i])
    #
    #     rangestart = rangestart + 3
    #     rangeend = rangeend + 3
    #     pakattulista_work.append(templist)
    #     ls = ls + 3

        # Tässä while loopissa laitetaan edgelistan yksittäiset kohdat omiin listoihinsa suuremman listan sisälle.
        # Listan koostumus: start,end,color

    # edgelistassa kunkin paikan tiedot on 3 ryppäissä.
    # jaetaan edgelista siis pienemmiksi listoiksi, joissa kussakin on vain kyseisen paikan tiedot
    #
    # käydään läpi nodelista for loopilla. Kun tullaan start: kohdalle otetaan menossa olevan kohdan lisäksi 2 seuraavaa,
    # eli end ja color ja laitetaan ne listaan, nimellä [paikka]_tiedot, jossa [paikka] korvataan nodes listasta
    # menossa olevalla nimellä.
    # lopuksi kaikki listat pakataan tupleen, jotta ne voidaan asettaa funktion ulkopuolella sopiviin arvoihin.
    # tuplea voidaan myös käyttää niin, että siitä vaan otetaan haluttu arvo valitsemalla joku paikka siitä käyttämällä
    # nodelistan numeroita, mutta sille voi tehdä oman funktion sitten.

    return pakattulista_work


pakattulista = edgemuokkaus()


def haepaikkatiedot(valinta):
    valittu = []
    valinta = "start:" + valinta

    temp_valittu = []
    hae = True
    # nyt haluamme pakatusta listasta juuri sen kohdan, johon valinta viittaa.
    # print(pakattulista[0][0]) pakatunlistan lista 0 kohta 0

    # halutaan käydä läpi pakattulista. Jokaisesta käydystä listasta käydään läpi vain listan ensimmäinen kohta, tai vaihtoehtoisesti
    # kohta joka alkaa "start:". Menossa olevasta listasta pidetään lukua, ja kun listan kohdassa, josta search löytää sekä
    # start: että valinta stringin, se lista valitaan pakatustalistasta, ja asetetaan valittu arvoon.

    # HUOM. pakatussa listassa on useita kohtia jotka alkavat jollain paikkakunnalla. Tämän funktion tarkoitus
    # on hakea paikkatiedot, eli kerätä ne listaan (tai tässä tapauksessa tupleen, josta taas haetaan reittitiedot)

        # yhdestä paikasta voi lähteä x tietä. Haluamme siis ensin kaikki listat joissa start: sisältää etsityn paikan.
    while hae is True:
        # print("WHile looppi alkaa")
        for i in range(len(pakattulista)): #käy läpi koko listan
            # print("ulompi forlooppi alkaa")
            # print("menossa oleva lista: ",pakattulista[i])
            for i2 in range(len(pakattulista[i])):  #käy läpi listasta valitun listan
                if pakattulista[i][i2] == valinta: #jos listassa on kohta joka on sama kuin valinta
                    valittu.append(pakattulista[i]) #kyseinen lista lisätään valittuun.
        break

    paikkatiedot = valittu
    paikka = valinta
    turha = "start:" + paikka
    varit = ["green","blue","red"]
    varitt = "color:"
    endp = "end:"
    if any(isinstance(i, list) for i in paikkatiedot) is True:
        for lista in paikkatiedot:
            kohta = 0
            while kohta <= len(lista)-1:

                if lista[kohta] == turha:
                    del lista[kohta]
                kohta += 1
            kohta = 0
            while kohta < len(lista):

                # print(endp + paikka, " ", lista[kohta])
                if "end:" in lista[kohta]:
                    teksti = lista[kohta].split("end:")[1]
                    lista[kohta] = teksti

                elif lista[kohta] == varitt + varit[0] or varit[1] or varit[2]:
                    for i in varit:
                        if lista[kohta] == varitt + i:
                            lista[kohta] = varid[i]
                    # hieno looppi jossa listan kohta korvataan värillä.
                    #
                kohta += 1
    else:
        kohta = 0
        while kohta <= len(paikkatiedot) - 1:

            if paikkatiedot[kohta] == turha:
                del paikkatiedot[kohta]
            kohta += 1
            while kohta < len(paikkatiedot):

                # print(endp + paikka, " ", lista[kohta])
                if "end:" in paikkatiedot[kohta]:
                    teksti = paikkatiedot[kohta].split("end:")[1]
                    paikkatiedot[kohta] = teksti

                elif paikkatiedot[kohta] == varitt + varit[0] or varit[1] or varit[2]:
                    for i in varit:
                        if paikkatiedot[kohta] == varitt + i:
                            paikkatiedot[kohta] = varid[i]
                    # hieno looppi jossa listan kohta korvataan värillä.
                    #
                kohta += 1

    valittu2 = paikkatiedot


    return valittu2
print(haepaikkatiedot(nodelist[0]))
#print(haepaikkatiedot(nodelist[0]))


#määritellään reittien värien pituudet




def reittitiedot(paikka):
    paikkatiedot = haepaikkatiedot(paikka)
    turha = "start:" + paikka
    varit = ["green","blue","red"]
    varitt = "color:"
    endp = "end:"
    if any(isinstance(i, list) for i in paikkatiedot) is True:
        for lista in paikkatiedot:
            kohta = 0
            while kohta <= len(lista)-1:

                if lista[kohta] == turha:
                    del lista[kohta]
                kohta += 1
            kohta = 0
            while kohta < len(lista):

                # print(endp + paikka, " ", lista[kohta])
                if "end:" in lista[kohta]:
                    teksti = lista[kohta].split("end:")[1]
                    lista[kohta] = teksti

                elif lista[kohta] == varitt + varit[0] or varit[1] or varit[2]:
                    for i in varit:
                        if lista[kohta] == varitt + i:
                            lista[kohta] = varid[i]
                    # hieno looppi jossa listan kohta korvataan värillä.
                    #
                kohta += 1
    else:
        kohta = 0
        while kohta <= len(paikkatiedot) - 1:

            if paikkatiedot[kohta] == turha:
                del paikkatiedot[kohta]
            kohta += 1
            while kohta < len(paikkatiedot):

                # print(endp + paikka, " ", lista[kohta])
                if "end:" in paikkatiedot[kohta]:
                    teksti = paikkatiedot[kohta].split("end:")[1]
                    paikkatiedot[kohta] = teksti

                elif paikkatiedot[kohta] == varitt + varit[0] or varit[1] or varit[2]:
                    for i in varit:
                        if paikkatiedot[kohta] == varitt + i:
                            paikkatiedot[kohta] = varid[i]
                    # hieno looppi jossa listan kohta korvataan värillä.
                    #
                kohta += 1





        # funktion pitää tietää onko paikkatiedot listassa 1 vai useampi lista. jos on vain yksi, eli on vain yksi reitti
        # niin lista ei sisällä muita listoja
        # any(isinstance(i, list) for i in a) tällä voi katsoa onko lista nested vai ei





# palautettavan tiedon pitää sisältää minne valitusta paikasta pääsee ja miten pitkiä reitit niihin on.
        # 0 paikan tulos: reitti polvijärvelle, 5min; reitti viinijärvelle, 5min
        #
    return paikkatiedot

#print(reittitiedot(nodelist[0]))

# reittitiedot funktiossa määritellään paikasta menevien reittien tiedot.
# se antaa tulokseksi paikat jonne valitusta paikasta pääsee ja miten mitkä matka niihin on minuuteissa.

#

#print(haepaikkatiedot(nodes[20]))

# nodet : paikat, edges : reitit. halutaan reittien pituudet paikasta toiseen. 1. fuktio joka listaa paikat ja mihin
# niistä pääsee.
# 2. funktio joka katsoo paikkojen välisten reittien pituudet tähän voipi tarvita classia:
# class jossa on funktiot jotka katsoo minne mistäkin pääsee ja miten pitkä matka on.
# funktio joka ottaa nodelistista nimen ja sanoo minne nodesta pääsee ja miten pitkä matka on.
# esim) funktio jotakin(Outokumpu){tekee juttuja}
# return: Outokummusta pääsee Polvijärvelle, matka 5min ja Viinijärvelle, matka 5min

# tai sitten pelkästään funktio joka tekee tuon.


# test










################
# KOODIN LOPETUS#
################
# Rimpsut jotka suoritetaan kun koodi saa kaiken tehtyä
