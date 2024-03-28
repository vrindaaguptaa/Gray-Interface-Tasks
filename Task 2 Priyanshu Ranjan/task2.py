# 1. Read content from one file and write it into another file
fr = open('file1.txt', 'r')
fw = open('file2.txt', 'w')
fw.write(fr.read())
fr.close()
fw.close()

# 2. Write a dictionary to a file in Python
f = open('file3.txt', 'w')
dict = {
    "Name" : "Priyanshu" ,
    "Branch" : "CSE",
    "Batch" : "2027"    
}
for key, value in dict.items():
    f.write("%s:%s\n" % (key,value))
f.close()

# 3. How to check file size in Python?
import os
size = os.path.getsize('file1.txt')
print("File Size = " + str(size) + " bytes")

# 4. Find the most repeated word in a text file
f = open('file1.txt', 'r')
c = 0
w = ""
h = 0
a = []       
for line in f:  
    string = line.lower().replace(',','').replace('.','').split(" ") 
    for s in string:  
        a.append(s)
 
for i in range(0, len(a)):  
    c = 1 
    for j in range(i+1, len(a)):  
        if a[i] == a[j]:  
            c = c+1
    if c>h:  
        h = c 
        w = a[i]        
print("Most repeated word = " + w)   
f.close()

# 5. How to read specific lines from a File in Python?
f = open('file1.txt', 'r')
s = f.readlines()
print(s[2], end="")
f.close()