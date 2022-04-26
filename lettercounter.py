#lettercounter.py
#This program reports the number of times a certain letter appears in a sentence.
#By Ashley Cook

def main():

    print("This program reports the number of times a chosen letter appears in a sentence.\n")
    #Prompt for sentence and letter
    sentence = input("Enter input sentence:" )
    chosen = input("Enter input letter:" )

 

    upper = sentence.lower().count(chosen)
    lower = sentence.upper().count(chosen)
    total = (upper + lower)
  
   

    print("Number occurrences of the letter", chosen , ":" , total)

main()
