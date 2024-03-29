# Task 2 (i) Reading and Writing from a file
# to read from file1
file1=open("File1.txt","r")
data=file1.read()
# to write in file2

file2=open("File2.txt","w")
file2.write(data)
# closing the file objects
file1.close()
file2.close()


# Task 2 (ii)  To write a dictionary in a file 
dict={
    "name":"Sanjeet Raj",
    "roll":2306009,
    "language":"python"
}

# using pickle 
import pickle
file3=open("File3.txt","wb")

pickle.dump(dict,file3)
file3.close()

# normally
file3=open("File3.txt","w")
file3.write("{")
for i in dict:
    text=str(i)+":"+str(dict[i])+","
    file3.write(text)
file3.write("}")
file3.close()


# Task 2 (iii) Finding the size of a file
import os
f=os.path.getsize("./File1.txt")
print("Size of the given file:",f)


# Task 2 (iv) Most repeated word

file1=open("File1.txt","r")
str1=""
data=file1.read()
file1.close()
for i in range(len(data)):
    if(not(data[i].isalnum())):
        str1=str1+" "
    else:
        str1+=data[i]
array=str1.split(None)

wordDict={}
for i in array :
    if i in wordDict:
        wordDict[i]+=1
    else:
        wordDict[i]=1
max=0
lWord=""
for i in wordDict:
    if wordDict[i]>max:
        max=wordDict[i]
        lWord=i

print("Most repeated word in file:",lWord,"\t\t freq:",max,"times")


# Task 2 (v) Read Specific Lines from a file
file1=open("File1.txt","r")
data=file1.readlines()
file1.close()
index=int(input("Enter the line number to read:"))
print(f"line at line number {index} is ")
print(data[index-1])

