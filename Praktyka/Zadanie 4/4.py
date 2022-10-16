#KROK 1 wygenerowanie wszystkich liczb szczęśliwych

counter = 0                      # licznik indeksu liczby, która jest aktualnie najnowszą szczęśliwą
luckyTab = []                    # lista przechowująca szczęśliwe liczby
luckyTabCurrent = []             # lista do której w danej iteracji bądą wpisywane liczby poza wykluczonymi

#Liczby szczęśliwe są nieparzyste
for i in range(1, 10001):        # pętla dzięki której na początku uzyskamy w LuckyTab same liczby nieparzyste
    if (i % 2 != 0):
            luckyTab.append(i)
counter += 1
newLuckier = luckyTab[counter]  # przypisanie do zmiennej newLuckier najnowszej szczęśliwej liczby

while newLuckier < len(luckyTab):                   # cała pętla będzie się wykonywała dopóki najnowsza szczęśliwa liczba będzie mniejsza od długości listy
    for i in range(0, len(luckyTab)):               # tworzymy pętle równą długości listy
        if (i + 1) % newLuckier != 0:               # wyrzucamy indeksy o wielokrotności ostatniej szczęśliwej liczby(zgodnie z założeniem zadania)
            luckyTabCurrent.append(luckyTab[i])

    luckyTab = luckyTabCurrent.copy()               # przypisuję tablicy luckyTab wartości zaaktualizowane
    luckyTabCurrent.clear()                         # czyszczę tablicę pomocniczą, żeby była gotowa na kolejny obrót pętli ;)
    counter += 1                                    # za każdym obrotem pętli zwiększam licznik o 1
    newLuckier = luckyTab[counter]

#algorytm do sprawdzania czy liczba jest pierwsza
def is_number_prime(n: int): 
    if n == 2: #Sprawdzamy, czy to nie jest numer 2 - jedyna parzysta liczba pierwsza
        return True
    if n % 2 == 0 or n <= 1: #Odrzycamy wszystkie parzyste i mniejsze równe 1
        return False

    root = int(n**0.5) + 1
    for divider in range(3, root, 2): #sprawdzamy wszystkie dzielniki od 3 do sqrt(n)+1, skacząc co dwa
        if n % divider == 0:
            return False
    return True

file = open("dane.txt", "r")

records = file.read().splitlines()

allFortuneNumbers = 0
allFortunePrimeNumbers = 0
inARow = 0
firstinArow = 0
maxInARow = 0
maxFirstInARow = 0

#Sprawdzamy ile liczb z pliku jest szczęśliwych
for record in records: 
   if int(record) in luckyTab:
      if inARow == 0: # Za każdym razem kiedy ciąg jest zerowany zapisz pierwszy wyraz
         firstinArow = int(record)

      if is_number_prime(int(record)):
         allFortunePrimeNumbers+=1
      allFortuneNumbers+=1
      inARow+=1
   else:
      if inARow > maxInARow: #Jeśli pojawi się dłuższy ciąg zmień maksymalną długość oraz pierwszy element ciągu
         maxInARow=inARow
         maxFirstInARow = firstinArow
      inARow = 0
      firstinArow = 0

print("4.1: " + str(allFortuneNumbers))
print("4.2: " + str(maxInARow) + " " + str(maxFirstInARow))
print("4.3: " + str(allFortunePrimeNumbers))

file.close()