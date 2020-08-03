import csv


def uloz_obec(data_1):
    with open("obec.csv", "w", newline="") as csv_s:
        zahlavi = ["code", "location"]
        writer = csv.DictWriter(csv_s, fieldnames=zahlavi)
        writer.writeheader()

        for obec, _ in enumerate(data_1):
            writer.writerow(
                {
                    "code": data_1[obec]["cislo"],
                    "location": data_1[obec]["jmeno"],

                }
            )

def uloz_reg(data_2):
    with open("obec.csv", "a", newline="") as csv_s:
        zahlavi = ["registered", "envelopes", "valid"]
        writer = csv.DictWriter(csv_s, fieldnames=zahlavi)
        writer.writeheader()

        for index, _ in enumerate(data_2):
            writer.writerow(
                {
                    "registered": data_2[index]["registered"],
                    "envelopes": data_2[index]["envelopes"],
                    "valid": data_2[index]["valid"],

                }
            )

def uloz_hlasy(data_3):
    with open("obec.csv", "a", newline="") as csv_s:
        zahlavi = ["Občanská demokratická strana", "Řád národa - Vlastenecká unie", "CESTA ODPOVĚDNÉ SPOLEČNOSTI", "Česká str.sociálně demokrat.", "Radostné Česko", "STAROSTOVÉ A NEZÁVISLÍ", "Komunistická str.Čech a Moravy", "Strana zelených", "ROZUMNÍ-stop migraci,diktát.EU", "Strana svobodných občanů", "Blok proti islam.-Obran.domova", "Občanská demokratická aliance", "Česká pirátská strana", "Referendum o Evropské unii", "TOP 09", "ANO 2011", "Dobrá volba 2016", "SPR-Republ.str.Čsl. M.Sládka", "Křesť.demokr.unie-Čs.str.lid.", "REALISTÉ", "SPORTOVCI", "Dělnic.str.sociální spravedl.", "Svob.a př.dem.-T.Okamura (SPD)", "Strana Práv Občanů"]
        writer = csv.DictWriter(csv_s, fieldnames=zahlavi)
        writer.writeheader()


        for index, _ in enumerate(data_3):
            writer.writerow(
                {
                    "Občanská demokratická strana": data_3[index]["Občanská demokratická strana"],
                    "Řád národa - Vlastenecká unie": data_3[index]["Řád národa - Vlastenecká unie"],
                    "CESTA ODPOVĚDNÉ SPOLEČNOSTI": data_3[index]["CESTA ODPOVĚDNÉ SPOLEČNOSTI"],
                    "Česká str.sociálně demokrat.": data_3[index]["Česká str.sociálně demokrat."],
                    "Radostné Česko": data_3[index]["Radostné Česko"],
                    "STAROSTOVÉ A NEZÁVISLÍ": data_3[index]["STAROSTOVÉ A NEZÁVISLÍ"],
                    "Komunistická str.Čech a Moravy": data_3[index]["Komunistická str.Čech a Moravy"],
                    "Strana zelených": data_3[index]["Strana zelených"],
                    "ROZUMNÍ-stop migraci,diktát.EU": data_3[index]["ROZUMNÍ-stop migraci,diktát.EU"],
                    "Strana svobodných občanů": data_3[index]["Strana svobodných občanů"],
                    "Blok proti islam.-Obran.domova": data_3[index]["Blok proti islam.-Obran.domova"],
                    "Občanská demokratická aliance": data_3[index]["Občanská demokratická aliance"],
                    "Česká pirátská strana": data_3[index]["Česká pirátská strana"],
                    "Referendum o Evropské unii": data_3[index]["Referendum o Evropské unii"],
                    "TOP 09": data_3[index]["TOP 09"],
                    "ANO 2011": data_3[index]["ANO 2011"],
                    "Dobrá volba 2016": data_3[index]["Dobrá volba 2016"],
                    "SPR-Republ.str.Čsl. M.Sládka": data_3[index]["SPR-Republ.str.Čsl. M.Sládka"],
                    "Křesť.demokr.unie-Čs.str.lid.": data_3[index]["Křesť.demokr.unie-Čs.str.lid."],
                    "REALISTÉ": data_3[index]["REALISTÉ"],
                    "SPORTOVCI": data_3[index]["SPORTOVCI"],
                    "Dělnic.str.sociální spravedl.": data_3[index]["Dělnic.str.sociální spravedl."],
                    "Svob.a př.dem.-T.Okamura (SPD)": data_3[index]["Svob.a př.dem.-T.Okamura (SPD)"],
                    "Strana Práv Občanů": data_3[index]["Strana Práv Občanů"],


                }
            )
