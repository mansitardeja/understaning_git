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


def swap_cases(s):
    c= s.swapcase()
    print(c)
swap_cases("Hola lol Plal")


a="hey there  how are you "
b=a.split()
print(b) 
b="#".join(b)
print(b)


hashtags="goodvibes iphonegraphy naturelove"
a=hashtags.split()
a="# ".join(a)
print(a)


def print_full_name(first, last):
    print("Hello",first,last,"You just delved into python")
    


first_name = input()
last_name = input()
print_full_name(first_name, last_name)



def mutate_string(string, position, character):
    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

string="abc"
a=string.replace("a","b")
print(a)

s="abrakadabra"

for i in range(0,len(s)):
    print(s[i])


    

           


        

