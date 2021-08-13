def count(text,char):
    count=0
    for c in text:
        if c==char:
            count+=1
        return count
with open("abc.txt") as f:
    text=f.read()
count(text,"am")


        

