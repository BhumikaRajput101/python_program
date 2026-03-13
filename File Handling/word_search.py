#search  a word in a file
def search(a):
    with open (r'd:\python_practice\1-data-analysis.ipynb\fileoperation.ipynb\example.txt','r') as file:
        content=file.read().split()
        count=0
        for w in content:
            if w==a:
             count+=1
        if count>0:
            print("Word is found ",count," times")
        else:
            print("The word is not found in the file")
a=(input("Enter the word:"))
search(a)
