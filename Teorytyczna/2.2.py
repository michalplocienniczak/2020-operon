s: str = input()
f1: int = int(input())
f2: int = int(input())

d = len(s)

szyfr = ""

for i in range(0,d):
   if ord(s[i])>=ord('A') and ord(s[i])<=ord('Z'):
      szyfr += chr(int(ord('A')+((ord(s[i])-ord('A'))+f1)%26))
      f=(f1+f2)%26
      f1=f2
      f2=f


# xdrlib 2
# for i in range(9,80):
#    print(i)
print(szyfr)
