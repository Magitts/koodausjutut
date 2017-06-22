#!/usr/bin/python
# coding=utf-8
# YLEISET MUUTTUJAT JOITA EI MUUTELLA MYÖHEMMIN#
# + ALUSTUKSET								  #
###############################################
# BUGIT -Jos tekstitiedostoon laitetaan edge, jonka arvot on väärissä kohdissa, eli se alkaa vaikka endillä         #
# niin se aiheuttaa kummallista käytöstä myöhemmin -> paikkatiedoissa kyseiseen edgeen viittaava kohta siirtää      #
# listaa vasemmalle, niin että siitä näkyy vain reitin pituus ja  'nodes:'. Virhe on luultavasti                    #
# jossain ylempänä listan käsittelyssä.                                                                             #
#####################################################################################################################

import re
import math

dbfile = "tietokanta_tiedot.txt"

# TIETOKANNAN TIETOJEN KÄSITTELY KÄYTETTÄVÄÄN MUOTOON#
#####################################################

# ladataan tiedot tiedostosta arvoihin
# poistetaan ylimääräinen roska
kaikki = []
nodelist = []

import cgi, cgitb

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
varid = {"red": 25, "blue": 15, "green": 5, "Green": 5}
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
    #paikka = valinta
    #turha = "start:" + valinta
    varit = ["green","blue","red","Green"]
    #korvaa varit reg ex haulla, joka etsii näitä sanoja, riippumatta niiden kirjainkoosta.
    varitt = "color:"
    endp = "end:"
    if any(isinstance(i, list) for i in paikkatiedot) is True:
        for lista in paikkatiedot:
            kohta = 0
            while kohta <= len(lista)-1:

                if lista[kohta] == valinta:
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
# lopuksi funktio siistii ulos työnnettävän arvon -> alku piste poistetaan koska se tiedetään jo kun funktiota kutsutaan
# päätepisteestä otetaan vain nimi ja matkan pituus kerrotaan minuutteina.

# for i in range(len(nodelist)):
#     print(":",i)
#     print(nodelist[i])
#     print(haepaikkatiedot(nodelist[i]))

# nyt reittitiedot saadaan ulos jokaisesta nodesta. Seuraavaksi pitää

# perimmäinen tavoite on tehdä kartta, josta näkyy kaikki sijainnit ja reitit niiden välillä.

#nyt voi olla tarpeen alkaa tekemään verkkosivua, johon koodi laittaa tietoja.
#toinen on tehdä funktio, joka käy läpi kaikki nodet ja lisää niiden tiedot dictionaryyn.
#jos koodia halutaan optimoida, voidaan kaikki tähänastinen häslääminen ohittaa laittamalla tietoja dictionaryyn jo
#lukuvaiheessa reg expressionin avulla.

#kartan visuaalinen ulkoasu: pisteet laitetaan koordinaatistoon suhteessa toisiinsa. koska etäisyydet
# on kuvattu vain minuutteina, voidaan kukin hubi kuvata pisteenä, josta lähtee 1-n viivaa muihin pisteisiin
# ne hubit jotka jakavat päätepisteen ovat lähellä toisiaan ja ne jotka eivät, ovat n hubin päässä.
#jotta kaikki hubit eivät päädy toistensa päälle, kunkin hubin päätepisteelle tulee määrittää joku kulma mistä
#  se lähtee pois hubista. 1. jaa 360 niin monella, kuin hubilla on päätepisteitä 2. ennalta määrätyt kulmat,
#  jos endejä on 3 tai alle, lähtökulmat ovat 90, 6 tai alle: 45.
# hubin tulee ottaa huomioon "saapumisviiva" eli mistä kulmasta edellinen hubi liittyy siihen ja huolehtia että uusia
# hubeja ei tehdä tähän kulmaan tai lähelle sitä.
#on otettava huomioon myös ne joista ei lähde muualle -> ovat umpikujia


# ei ole pakko olla _verkkosivu_


#

def nayta():
    cgitb.enable()
    first_name = "baba"
    last_name = "yaga"
    print("Content-type:text/html\r\n\r\n")

    print("<html>")

    print("<head>")

    print("<title>Hello - Second CGI Program</title>")

    print("</head>")

    print("<body>")

    print("<h2>Hello %s %s</h2>" % (first_name, last_name))

    print("</body>")

    print("</html>")
nayta()













################
# KOODIN LOPETUS#
################
# Rimpsut jotka suoritetaan kun koodi saa kaiken tehtyä
