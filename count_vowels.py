a=input("enter a line ")
b=a.strip().lower()
countvowel=0
countconsonant=0
for i in b:
   if i.isalpha():
     if i in ('a', 'e', 'i', 'o', 'u'):

           countvowel+=1
     else:
          countconsonant+=1
print("number of vowel is", countvowel)
print("number of consonat is ", countconsonant)
