# Zadanie 2.2. (0–4)
#
# Pan Kowalski zauważył, że w jego algorytmie występują dwa problemy.
# 1. Funkcja rekurencyjna bardzo spowalnia działanie algorytmu.
# 2. Za każdym uruchomieniem algorytm do szyfrowania używa tych samych wartości, 
# ponieważ ciąg liczb Fibonacciego jest stały i jego dwa początkowe elementy mają zawsze
# wartości 1 i 1.
# Pan Kowalski planuje wykorzystać swój pomysł z użyciem ciągu Fibonacciego. 
# Jednak chce zmienić algorytm tak, aby przed każdym szyfrowaniem możliwe było ustalenie 
# dwóch początkowych wartości oraz wyznaczenie każdej następnej jako sumy dwóch poprzednich 
# na bieżąco – iteracyjnie, w trakcie szyfrowania.
#
# Napisz algorytm (w postaci listy kroków, schematu blokowego, pseudokodu lub w wybranym
# języku programowania), który będzie szyfrował wiadomości zgodnie z wymogami pana Kowalskiego.
#
# Specyfikacja:
# Dane:
#  F1, F2 – dwie liczby naturalne określające początkowe wartości pseudociągu Fibonacciego
# F – kolejny wyraz pseudociągu Fibonacciego liczony w arytmetyce modularnej mod 26
# s[1..d] – tekst jawny składający się z dużych liter alfabetu o długości d znaków
# Wynik:
# szyfr[1..d] – tekst po zaszyfrowaniu składający się z dużych liter alfabetu o długości
# d znaków

#Pobieramy dane
s: str = input() #Hasło do zaszyfrowania
f1: int = int(input()) #Pierwszy element ciągu Fibonacciego
f2: int = int(input()) #Drugi element ciągu Fibonacciego

d = len(s) #Ustalamy długość wprowadzonego hasła

szyfr = ""

#Dla każdego znaku w haśle
for i in range(0,d):
   #Jeżeli jest znakiem od A do Z
   if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
      #Przesuń znak o F1 miejsc w alfabecie 
      szyfr += chr(int(ord('A')+((ord(s[i])-ord('A'))+f1)%26))
      #Iteracyjny algorytm do tworzenia pseudociągu Fibonacciego
      f=(f1+f2)%26
      f1=f2
      f2=f

#Zwracamy zaszyfrowane hasło
print(szyfr)
