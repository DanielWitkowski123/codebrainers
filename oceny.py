try:
	wynik = int(input("Podaj ile masz punktow z egzaminu: "))
except ValueError:
	print("Czy ty sie smierci nie boisz czlowieku? Prawie doszlo do eksplozji. Nie podawaj wiecej takich danych")

if wynik > 100:
	print("Wyszedles poza ramy. To sie nazywa innowacja")
elif wynik >= 91:
	print("Jestes bardzo uproszczona wersja Boga, otrzymujesz ocene Bardzo Dobra")
elif wynik >= 81:
	print("Super wynik. Otrzymujesz ocene Ponad Dobra")
elif wynik >= 71:
	print("Otrzymujesz ocene Dobra. Jeszcze troche i bedziesz mistrzem")
elif wynik >= 61:
	print("Ocena Ponad Dostateczna. To jeszcze nie grzech ale wstyd. Stac Cie na wiecej")
elif wynik >= 50:
	print("Ocena Dostateczna. Jeszcze sporo nauki przed Toba")
elif wynik >= 0:
	print("Bardzo mi przykro ale bedzie wrzesien")
elif wynik <= -1:
	print("Mniej niz zerooo")
else:
	print("Wychodzisz calkiem poza ramy. Kogo ty chcesz oszukac")