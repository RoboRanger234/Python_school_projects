a = input(("Enter the first word: "))
b = input(("Enter the second word: "))
c = int(input("Number of repitions for first word:"))
d = input("What operation do you want me to do on these words: ")
def RepeatWord(a,b,c):
    print(a**c)
def AddWords(a,b):
    print("the two words added together are:",a+b)
def Operations(a,b,c,d):
    if(d == "repeat"):
        print(a*c)
    if(d == "add the words" or d == "add"):
        print("the concatenation of the two words is:",'\t',a+b)
Operations(a,b,c,d)
