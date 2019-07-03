import random
print("Witamy w pytho-lotku. Zgadnij jaka liczbe od 1 do 100 mam na mysli. Mozesz strzelac 7 razy")
liczba = random.randint(0,101)
proba = 1

while proba < 8:
    try:
        zgadywana = int(input("Podaj liczbe: "))
    except ValueError:
	    print("Czy ty sie smierci nie boisz czlowieku? Nie podawaj wiecej takich danych")
    proba =+ proba + 1
    if zgadywana == liczba:
        print("Gratulacje!!! Udalo ci sie wygrac za ", proba, "razem. Jako nagrode zyskujesz wycieczke do Krakowa. Transport i wyzywienie we wlasnym zakresie")
        break
    elif proba == 8:
        print("O nie! Moze za kolejnym razem pojdzie Ci lepiej!")
    elif zgadywana < liczba:
        print("Troche wyzej, troche wyzej")
    elif zgadywana > liczba:
        print("Troche nizej, troche nizej")