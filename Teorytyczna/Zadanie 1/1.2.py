# ZADANIE 1.2. (0–6) 
# Napisz algorytm (w postaci listy kroków, w pseudokodzie lub w wybranym języku programowania), 
# który znajdzie sumę wszystkich liczb mniejszych niż milion, które są palindromiczne jednocześnie 
# w systemie dziesiętnym i dwójkowym. Uwaga: Przy ocenie będzie brana pod uwagę złożoność obliczeniowa algorytmu.
#
# Specyfikacja:
# Dane:
# n – liczba całkowita mniejsza od miliona
# Wynik:
# suma – liczba całkowita będąca sumą liczb palindromicznych jednocześnie w systemie dziesiętnym i dwójkowym
#
# KOMENTARZ
#
# Palindromy są dość rzadkie, więc zamiast przejść przez milion liczb i sprawdzić je, możemy po
# prostu wygenerować wszystkie palindromy w jednej bazie i sprawdzić, czy są one palindromem
# w drugiej bazie. 
# 
# Zasadniczo dla każdej liczby od 1 do 1000 możemy dodać jej odwrotność z duplikacją 
# lub bez (np. 146 może stać się palindromami 14641 i 146641). Ponieważ liczby palindromiczne w systemie 
# binarnym muszą mieć najbardziej i najmniej znaczący bit ustawiony na
# 1, możemy sprawdzać tylko liczby nieparzyste. Dodatkowo sprawdzenie palindromu w systemie
# binarnym wykonuje przy użyciu operacji bitowych.
# 
# Komentarz zaczerpnięty z: https://arkusze.pl/maturalne/informatyka-2020-operon-probna-rozszerzona-odpowiedzi.pdf
# 
suma = 0

#Generowanie nowych palindromów
def new_palindrome(number: int, without_duplication: bool) -> int:
   #W przypadku bez duplikacji
   if without_duplication: 
      new = number #Bierzemy i zapisujemy początek palindroma np. 146
      cut = int((number - number%10)/10) #Ucinamy końcówkę np. 14/6 -> 14
      reversedCut = str(cut)[::-1] #Odwracamy końcówkę mp. 14 -> 41
      result = str(new) + str(reversedCut) # Doklejamy np. 146 + 41 -> 14641
      return int(result) #Zwracamy rezultat jako numer
   #W przypadku z duplikacją
   else: 
      new = number #Bierzemy i zapisujemy początek palindroma np. 146
      reversedNum = str(number)[::-1] #Odwracamy końcówkę mp. 146 -> 641
      result = str(new) + str(reversedNum) # Doklejamy np. 146 + 641 -> 146641
      return int(result) #Zwracamy rezultat jako numer
#Funkcja sprawdza, czy po przekształcaniu na sys. binarny nadal jest palindromem
def is_palindrome_in_binary(dec_palindrome: int) -> bool:
   #Przekształcenie na palindrom bez pierwszych 2 znaków, które zawsze będą "0b".
   bin_palindrome = bin(dec_palindrome)[2:]

   #Porównanie przekształconego palindroma z jego odwrotnością.
   return bin_palindrome == bin_palindrome[-1::-1] #Zwracamy Boolean (True/False) czy jest palindromem, czy nie

#Dla wszystkich liczb od 1 do 999
for i in range(1, 1000):
   #Sprawdzamy dla palindroma bez duplikacji
   if is_palindrome_in_binary(new_palindrome(i, True)):
      suma += new_palindrome(i, True)
   #Sprawdzamy dla palindroma z duplikacją
   if is_palindrome_in_binary(new_palindrome(i, False)):
      suma += new_palindrome(i, False)

print(suma) #Zwracamy wynik
      
   
