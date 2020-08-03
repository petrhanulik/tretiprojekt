import sys

import requests
from bs4 import BeautifulSoup
from odkaz_Hradec_Kralove import ziskej_odpoved
from vytvor_csv import uloz_obec
from vytvor_csv import uloz_reg
from vytvor_csv import uloz_hlasy


def hlavni() -> None:
    if STRANKA == "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201":
        odpoved = ziskej_odpoved()
        naparsovane = parsuj(odpoved)
        tabulka_obce = ziskej_tabulku(naparsovane)
        radky = vypis_radky(tabulka_obce)
        udajeo = [udaje(radek) for radek in radky]
        odkazy_na_obce = odkaz(naparsovane)
        ba =(odkazy_na_obce[0]["href"])
        newurl = "https://volby.cz/pls/ps2017nss/" + ba
        cele_odkazy = [vytvor_odkaz(odkaz) for odkaz in odkazy_na_obce]

        udaje_obce = [udaje_obec(rad) for rad in cele_odkazy]
        parsovani_obce = [parsuj(rad) for rad in udaje_obce]
        rozhodl = [rozhodni1(rad) for rad in parsovani_obce]
        upravene_registered = uprav_reg(rozhodl)
        hlasy = [rozhodni2(rad) for rad in parsovani_obce]
        upravene_hlasy = uprav_hla(hlasy)

        uloz_obec(udajeo)
        uloz_reg(upravene_registered)
        uloz_hlasy(upravene_hlasy)

    else:
        print("Spatne zadany odkaz")


def rozhodni1(obec):
    radek = obec.find_all("tr")[0]
    nadpis = radek.find_all("th")[0].text
    par = obec.find("div", {"id": "inner"})
    registered = []

    if nadpis == "Okrsky":
        radek2 = obec.find_all("tr")[2]
        vysledky_voleb = najdi_cisla(radek2)
        registered.append(vysledky_voleb)

    elif nadpis == "Okrsek":
        obec = obec.find("table", {"class": "table"})
        radek2 = obec.find_all("tr")[1]
        odkaz = radek2.find_all("td")
        odkazy_na_obce = odkaz_okr(obec)
        seznam_odk = [vytvor_odkaz(radek) for radek in odkazy_na_obce]
        stazeni_okrsku = [udaje_obec(od) for od in seznam_odk]
        parsovani_okr = [parsuj(od) for od in stazeni_okrsku]
        upravene_okrsky1 = [uprav_okr(ok) for ok in parsovani_okr]
        upravene_okrsky2 = uprav_ukr2(upravene_okrsky1)
        registered.append(upravene_okrsky2)

    return registered


def rozhodni2(obec):
    radek = obec.find_all("tr")[0]
    nadpis = radek.find_all("th")[0].text
    par = obec.find("div", {"id": "inner"})
    kandidujici_strany =[]

    if nadpis == "Okrsky":
        vysledky2 = uprav_stranu(par)
        kandidujici_strany.append(vysledky2)


    elif nadpis == "Okrsek":
        obec = obec.find("table", {"class": "table"})
        radek2 = obec.find_all("tr")[1]
        odkaz = radek2.find_all("td")
        odkazy_na_obce = odkaz_okr(obec)
        seznam_odk = [vytvor_odkaz(radek) for radek in odkazy_na_obce]
        stazeni_okrsku = [udaje_obec(od) for od in seznam_odk]
        parsovani_okr = [parsuj(od) for od in stazeni_okrsku]
        upravene_hlasy = [uprav_hlasy(radek) for radek in parsovani_okr]
        upravene_hlasy2 = uprav_strany(upravene_hlasy)
        kandidujici_strany.append(upravene_hlasy2)

    return kandidujici_strany


def uprav_reg(reg):
    upravene_reg = []
    for prvek in reg:
        upravene_reg.append(prvek[0][0])
    return upravene_reg

def uprav_hla(hls):
    upravene_hlasy = []
    for prvek in hls:
        upravene_hlasy.append(prvek[0])
    return upravene_hlasy


def parsuj(odp):
    return BeautifulSoup(odp.text, "html.parser")

def ziskej_tabulku(pars):
    return pars.find("div", {"id":"inner"})

def vypis_radky(tabl):
    return tabl.find_all("tr")[2:37] + tabl.find_all("tr")[39:74] + tabl.find_all("tr")[76:110]

def udaje(rad):
    try:
        cislo = rad.find_all("td")[0].text
        jmeno = rad.find_all("td")[1].text
        return {
        "cislo": cislo,
        "jmeno": jmeno,
        }
    except AttributeError:
        print("indexy nejsou v poradku")


def odkaz(tabl):
    return tabl.find_all("a")[::2][3:-1]

def vytvor_odkaz(odk):
    odkazy = odk["href"]
    return "https://volby.cz/pls/ps2017nss/" + odkazy


def udaje_obec(odk):
    return requests.get(odk)

def odkaz_okr(tabl):
    return tabl.find_all("a")

def najdi_cisla_okr(rad):
    registered = int((rad.find_all("td")[0].text).replace("\xa0", ""))
    envelopes = int((rad.find_all("td")[1].text).replace("\xa0", ""))
    valid = int((rad.find_all("td")[4].text).replace("\xa0", ""))
    return registered, envelopes, valid


def uprav_hlasy(hl):
    return najdi_strany(hl)

def uprav_okr(okr):
    return najdi_cisla_okr(okr)

def uprav_ukr2(dict):
    sum_reg = 0
    sum_env = 0
    sum_val = 0
    for index in (dict):
        sum_reg += (index[0])
        sum_env += index[1]
        sum_val += index[2]
    return [{
    "registered": sum_reg,
    "envelopes": sum_env,
    "valid": sum_val,
    }]



def najdi_cisla(rad):
    try:
        registered = rad.find_all("td")[3].text
        envelopes = rad.find_all("td")[4].text
        valid = rad.find_all("td")[7].text
        return [{
        "registered": registered,
        "envelopes": envelopes,
        "valid": valid,
        }]
    except AttributeError:
        print("indexy nejsou v poradku")



def uprav_stranu(rad):
    key = []
    value = []
    najdi = rad.find_all("td")
    for strana in najdi[1::5]:
        key.append(strana.text)
    for hlasy in najdi[2::5]:
        value.append(int(hlasy.text))
    (slov_stran := {key: value
          for (key, value) in zip(key, value)})
    return slov_stran


def najdi_strany(rad):
    stra = []
    najdi = rad.find_all("td")
    for strana, hlasy in zip(najdi[7::5], najdi[8::5]):
        stra.append(strana.text)
        stra.append(int(hlasy.text))
    return(stra)

def uprav_strany(dict):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    s9 = 0
    s10 = 0
    s11 = 0
    s12 = 0
    s13 = 0
    s14 = 0
    s15 = 0
    s16 = 0
    s17 = 0
    s18 = 0
    s19 = 0
    s20 = 0
    s21 = 0
    s22 = 0
    s23 = 0
    s24 = 0
    for prvek in dict:
        s1 += prvek[1]
        s2 += prvek[3]
        s3 += prvek[5]
        s4 += prvek[7]
        s5 += prvek[9]
        s6 += prvek[11]
        s7 += prvek[13]
        s8 += prvek[15]
        s9 += prvek[17]
        s10 += prvek[19]
        s11 += prvek[21]
        s12 += prvek[23]
        s13 += prvek[25]
        s14 += prvek[27]
        s15 += prvek[29]
        s16 += prvek[31]
        s17 += prvek[33]
        s18 += prvek[35]
        s19 += prvek[37]
        s20 += prvek[39]
        s21 += prvek[41]
        s22 += prvek[43]
        s23 += prvek[45]
        s24 += prvek[47]
    return {
        "Občanská demokratická strana": s1,
        "Řád národa - Vlastenecká unie": s2,
        "CESTA ODPOVĚDNÉ SPOLEČNOSTI": s3,
        "Česká str.sociálně demokrat.": s4,
        "Radostné Česko": s5,
        "STAROSTOVÉ A NEZÁVISLÍ": s6,
        "Komunistická str.Čech a Moravy": s7,
        "Strana zelených": s8,
        "ROZUMNÍ-stop migraci,diktát.EU": s9,
        "Strana svobodných občanů": s10,
        "Blok proti islam.-Obran.domova": s11,
        "Občanská demokratická aliance": s12,
        "Česká pirátská strana": s13,
        "Referendum o Evropské unii": s14,
        "TOP 09": s15,
        "ANO 2011": s16,
        "Dobrá volba 2016": s17,
        "SPR-Republ.str.Čsl. M.Sládka": s18,
        "Křesť.demokr.unie-Čs.str.lid.": s19,
        "REALISTÉ": s20,
        "SPORTOVCI": s21,
        "Dělnic.str.sociální spravedl.": s22,
        "Svob.a př.dem.-T.Okamura (SPD)": s23,
        "Strana Práv Občanů": s24,
    }


if __name__ == "__main__":
    STRANKA = sys.argv[1]
    SOUBOR = sys.argv[2]
    hlavni()




