def count(text,char):
    count=0
    for c in text:
        if c==char:
            count+=1
        return count
with open("abc.txt") as f:
    text=f.read()
count(text,"am")

#What is the result of this code?
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))


text=input()
c=text.split()


    

           


        

