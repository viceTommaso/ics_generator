# -*- coding: utf-8 -*-
# !/usr/bin/env python3

__author__ = "Vicentini Tommaso"
__version__ = "01.01"


import time


def dt_generator(data, ora):
    """
    Genera data ed orario per il formato ics
    :data: data
    :ora: ora
    :return: ev_dt
    """
    v_data = data.split("-")
    v_ora = ora.split(":")
    ev_dt = v_data[2] + v_data[1] + v_data[0] + "T" + v_ora[0] + v_ora[1] + "00Z"
    return ev_dt


def main():
    """
    main
    :return: 0
    """
    start_ics = f"""BEGIN:VCALENDAR\nPRODID:ics_generator\nVERSION:2.0\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH"""
    end_ics = f"""END:VCALENDAR"""

    nome_file_evento = input("Nome file:   ")
    if nome_file_evento == "":
        nome_file_evento = "evento"

    with open(f"""{nome_file_evento}.ics""", "w", encoding="utf-8") as f_out:
        f_out.write(start_ics + "\n")

        n_event = input("Numero di eventi(int):   ")
        if n_event == "":
            n_event = 1
        
        for i in range(int(n_event)):
            evento = 1
            allday = 0

            summary = input("Titolo:   ")
            if summary == "":
                if (int(n_event)) == 1:
                    summary = "Evento personale"
                else:
                    summary = "Evento personale " + str(evento)

            uid = input("UID:   ")
            if uid == "":
                uid = f"""uid_{time.strftime("%Y")}{time.strftime("%m")}{time.strftime("%d")}{time.strftime("%H")}{time.strftime("%M")}{time.strftime("%S")}"""

            data_inizio = input("Data inizio (dd-mm-yyyy):   ")
            while len(data_inizio) != 10:
                if data_inizio == "":
                    data_inizio = f"""{time.strftime("%d")}-{time.strftime("%m")}-{time.strftime("%Y")}"""
                    break
                print("formato non valido (premere invio per la data attuale)")
                data_inizio = input("Data inizio (dd-mm-yyyy):   ")

            ora_inizio = input("Ora inizio (hh:mm):   ")
            while len(ora_inizio) != 5:
                if ora_inizio == "":
                    allday = 1
                    ora_inizio = f"""{time.strftime("%H")}:00"""
                    break
                print("formato non valido (premere invio per l'ora attuale)")
                ora_inizio = input("Ora inizio (dd-mm-yyyy):   ")

            data_fine = input("Data fine (dd-mm-yyyy):   ")
            while len(data_fine) != 10:
                if data_fine == "":
                    data_fine = data_inizio
                    break
                print("formato non valido (premere invio per la stessa data di inizio)")
                data_inizio = input("Data fine (dd-mm-yyyy):   ")

            ora_fine = f"""{int(ora_inizio.split(":")[0]) + 1}:00"""
            if allday == 0:
                ora_fine = input("Ora fine (hh:mm):   ")
                if ora_fine == "":
                    ora_fine = f"""{int(ora_inizio.split(":")[0]) + 1}:00"""

            descrizione = input(repr("Descrizione (usare (\n) per mandare a capo:   ").strip("'"))

            luogo = input("Luogo:   ")

            f_out.write("BEGIN:VEVENT" + "\n")
            f_out.write(f"""TRANSP:OPAQUE\n""")
            f_out.write(f"""SUMMARY:{summary}\n""")
            f_out.write(f"""UID:{uid}\n""")
            if allday == 1:
                f_out.write(f"""DTSTART;VALUE=DATE:{dt_generator(data_inizio, ora_inizio)}\n""")
                f_out.write(f"""DTEND;VALUE=DATE:{dt_generator(data_fine, ora_fine)}\n""")
            else:
                f_out.write(f"""DTSTART;VALUE=DATE-TIME:{dt_generator(data_inizio, ora_inizio)}\n""")
                f_out.write(f"""DTEND;VALUE=DATE-TIME:{dt_generator(data_fine, ora_fine)}\n""")
            f_out.write(f"""DTSTAMP:{time.strftime("%Y")}{time.strftime("%m")}{time.strftime("%d")}T{time.strftime("%H")}{time.strftime("%M")}{time.strftime("%S")}Z\n""")
            if descrizione != "":
                f_out.write(f"""DESCRIPTION:{descrizione}\n""")
            if luogo != "":
                f_out.write(f"""LOCATION:{luogo}\n""")
            """
            BEGIN:VALARM
            TRIGGER:-PT10M
            ACTION:DISPLAY
            DESCRIPTION:Alarm
            END:VALARM"""
            f_out.write("END:VEVENT" + "\n")
        f_out.write(end_ics)
        f_out.close()

        evento = evento + 1
    return 0


if __name__ == "__main__":
    main()
