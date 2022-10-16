suma = 0

def new_palindrome(number: int, symmetry: bool) -> int:
   if symmetry: 
      new = number
      cut = int((number - number%10)/10)
      reversedCut = str(cut)[::-1]
      result = str(new) + str(reversedCut)
      return int(result)
   else: 
      new = number
      reversedNum = str(number)[::-1]
      result = str(new) + str(reversedNum)
      return int(result)

def if_is_palindrome_in_binary(dec_palindrome: int) -> bool:
   bin_palindrome = bin(dec_palindrome)[2:]

   return bin_palindrome == bin_palindrome[-1::-1]


for i in range(1, 1000):
   if if_is_palindrome_in_binary(new_palindrome(i, True)):
      suma += new_palindrome(i, True)
   if if_is_palindrome_in_binary(new_palindrome(i, False)):
      suma += new_palindrome(i, False)

print(suma)
      
   
