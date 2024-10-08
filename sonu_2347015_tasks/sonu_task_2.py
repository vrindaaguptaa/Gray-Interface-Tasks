#task1
a=open('text_file_1.txt','r')
c=a.read()
print(c)
a.close()
b=open('text_file_2.txt','w')
print(b.write(c))
b.close()

#task2
x=open('text_file_3.txt','w')
sonu={
    'sonu':'good',
    'nitp':'bad'
}
y=x.write(str(sonu))
print(y)
x.close()


#task3
import os
m=os.path.getsize('text_file_1.txt')
print(f"{m} bytes")


#task5
p=open('text_file_1.txt','r')
q=p.readlines()
print(f"printing lines of index 1 to 5:\n {q[2:6]}")
print(f"printing line of index 3:\n {q[3]}")
p.close()



#task4
a = open("text_file_4.txt", "r") 
diction = dict() 
for line in a: 
    words = line.split(" ") #splitting into words 
    for i in words: 
        if i in diction: 
            diction[i] = diction[i] + 1
        else: 
            diction[i] = 1
for w in list(diction.keys()): 
    print(f"{w} occurs {diction[w]} times")
a.close()    
