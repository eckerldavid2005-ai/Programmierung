#!/usr/bin/env python

def add(a, b):
    # die Summe von a und b berechnen
    # und dieses Summe als Rueckgabewert zurueckgeben
    return a + b
    pass


def two_return_args(a):
    # den Wert a und das Doppelte von a zurueckgeben
    # mehrere Werte koennen mit komme getrennt zurueckgegeben werden
    return a, a*2
    pass


def create_list():
    # Erstellen einer Liste (wird mit eckigen Klammern erzeugt)
    # die Liste soll die eintraege 1 2 3 und 4 beinhalten
    # diese Liste zurueckgeben
    return [1, 2, 3, 4]
    pass


def create_list2():
    # Erstellen einer Liste (wird mit eckigen Klammern erzeugt)
    # die Liste soll die eintraege 1 Hallo und 3.14 beinhalten
    # diese Liste zurueckgeben
    return [1, "Hallo", 3.14]
    pass


def create_dict():
    # ein Dictionary (assoziatives array) erzeugen (geschweifte Klammern!)
    # dieses soll den folgenden Staedten ihre Einwohnerzahl zuordnen:
    # Muenchen  1488202
    # Nuernberg 515543
    # Landshut 73065  
    return {"Muenchen": 1488202, "Nuernberg": 515543, "Landshut": 73065}
    pass


def while_loop():
    # eine Schleife erstellen die von 0 bis 100 zaehlt und den Wert ausgibt
    # zusaetzlich soll der letzte Schleifenindex zurueckgegeben werden 
    # die Ausgabe kann mit print(variablen_name) erfolgen
    i = 0
    while (i<=100):
        print(i)
        i += 1
    return i
    pass


def while_loop_list(input_list):
    # ermitteln und speichern der Laenge der uebergebenen Liste (len(input_liste))
    # eine zaehlvariable initialisieren
    # eine while-schleife, die alle werte der Liste nacheinander ausgibt
    laenge=len(input_list)
    i=0
    while(i<laenge):
        print(input_list[i])
        i+=1
    pass


def for_loop():
    # eine for-schleife, die von 0 bis 100 alle geraden Zahlen ausgibt (range-funktion!)
    for i in range(0, 100, 2):
        print(i)
    return i
    pass


def for_loop_list(my_list):
    # eine for-schleife, die die uebergebene Liste ausgibt und dabei den Listenindex mit ausgibt
    # Die Ausgabe koennte wie folgt aussehen: print(f"{zaehler} : {i}")
    laenge=len(my_list)
    for i in range(0, laenge):
        print(f"{i} : {my_list[i]}")
    pass


def for_loop_dict(my_dict):
    # eine for-schleife, die das uebergebene dictionary schluessel samt wert ausgibt
    # Ausgabe mit print(f"{name} : {my_dict[name]}")
    for i in my_dict:
        print(f"{i} : {my_dict[i]}")

    pass


def to_binary(in_val):
    # der uebergebenen Wert soll in die binaerdarstellung uebertragen werden
    # einen leeren ergebnis-string anlegen 
    # eine while-schleife, die laeuft, solang in_val > 0
    # in jeden Schleifendurchgang am ergebins-string vorne str(in_val%2) (Modulo!) anhaengen
    # in jedem Schleifendurchgang in_val ganzzahlig durch 2 teilen (ganzzahliges teilen: //2) 
    result = ""
    while (in_val > 0):
        result = str(in_val % 2) + result
        in_val //= 2
    return result

if __name__ == "__main__":
    print(add(1,2))
    print(two_return_args(2))
    create_list()
    create_list2()
    while_loop()
    while_loop_list([1, 2, 5])
    for_loop()
    for_loop_list(create_list2())
    for_loop_dict(create_dict())
    print(to_binary(0xaffe))