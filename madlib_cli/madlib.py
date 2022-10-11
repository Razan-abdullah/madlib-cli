print ("Welcome to madlib game")

x=input("Are you ready to start A game ?(Y/N)")
x=x.upper()
if (x=="Y"):
    print ("let's play :)")
    a1=input ("Enter an Ajective")
    a2=input ("Enter an Ajective")
    a3=input ("Enter A first name")
    a4=input ("Enter A Past Tense Verb")
    a5=input ("Enter A first name")
    a6=input ("Enter an Ajective")
    a7=input ("Enter an Ajective")
    a8=input ("Enter a  Plural Noun")
    a9=input ("Enter a Large Animal")
    a10=input ("Enter a Small Animal")
    a11=input ("Enter A Girl's Name")
    a12=input ("Enter an Adjective")
    a13=input ("Enter a  Plural Noun")
    a14=input ("Enter an Adjective")
    a15=input ("Enter a  Plural Noun")
    a16=input ("Enter a Number 1-50")
    a17=input ("Enter A first name")
    a18=input ("Enter a Number")
    a19=input ("Enter a  Plural Noun")
    a20=input ("Enter a Number")
    a21=input ("Enter a  Plural Noun")
file=open("./f1.txt")
# print(file)
b=file.read()
# print (b)

print()
print(b.format(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21))

    



    



    

print(x)