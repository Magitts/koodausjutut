#!/usr/bin/python
# coding=utf-8
# YLEISET MUUTTUJAT JOITA EI MUUTELLA MYÖHEMMIN#
# + ALUSTUKSET								  #
###############################################

import re

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
            continue
    if nodelist[0] == "nodes:":
        del nodelist[0]
    # määritellään nodelist. Kirjoitetaan listaan kunnes tullaan edges kohtaan.

    edgelist = kaikki
    for x in nodelist:
        try:
            edgelist.remove(x)
        except ValueError:
            pass
    del edgelist[0]

    if select is "nodes":
        return nodelist
    elif select is "edges":
        return edgelist


edges = init("edges")
nodes = init("nodes")


# määritellään edgelist. Poistetaan edgelistasta, joka sisältää aluksi kaikki listan, nodelist.
# poistetaan turhat edges: ja nodes: kohdat

def edgemuokkaus():
    mlr = edges
    ls = 0
    pakattulista = []
    rangestart = 0
    rangeend = 3
    while ls <= len(mlr) and rangeend <= len(mlr):

        templist = []

        for i in range(rangestart, rangeend, 1):
            # List cleanup



            # Append
            templist.append(mlr[i])

        rangestart = rangestart + 3
        rangeend = rangeend + 3
        pakattulista.append(templist)
        ls = ls + 3

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

    return pakattulista


pakattulista = edgemuokkaus()


def haepaikkatiedot(valinta):
    valittu = []
    valinta = "start:" + valinta

    # nyt haluamme pakatusta listasta juuri sen kohdan, johon valinta viittaa.
    # print(pakattulista[0][0]) pakatunlistan lista 0 kohta 0

    # halutaan käydä läpi pakattulista. Jokaisesta käydystä listasta käydään läpi vain listan ensimmäinen kohta, tai vaihtoehtoisesti
    # kohta joka alkaa "start:". Menossa olevasta listasta pidetään lukua, ja kun listan kohdassa, josta search löytää sekä
    # start: että valinta stringin, se lista valitaan pakatustalistasta, ja asetetaan valittu arvoon.




    k2 = 0
    for k in range(len(pakattulista)):  # käydään läpi pakatunlistan listat
        for k2 in range(0, len(pakattulista[k][k2]), 1):
            if pakattulista[k][k2] == valinta:
                valittu = pakattulista[k]
            else:
                print("ARGH")

                # if bool(re.search(valinta, pakattulista[k][k2])) is True:

    return valittu


print(haepaikkatiedot(nodes[0]))

# nodet : paikat, edges : reitit. halutaan reittien pituudet paikasta toiseen. 1. fuktio joka listaa paikat ja mihin
# niistä pääsee.
# 2. funktio joka katsoo paikkojen välisten reittien pituudet tähän voipi tarvita classia:
# class jossa on funktiot jotka katsoo minne mistäkin pääsee ja miten pitkä matka on.
# funktio joka ottaa nodelistista nimen ja sanoo minne nodesta pääsee ja miten pitkä matka on.
# esim) funktio jotakin(Outokumpu){tekee juttuja}
# return: Outokummusta pääsee Polvijärvelle, matka 5min ja Viinijärvelle, matka 5min

# tai sitten pelkästään funktio joka tekee tuon.













################
# KOODIN LOPETUS#
################
# Rimpsut jotka suoritetaan kun koodi saa kaiken tehtyä
