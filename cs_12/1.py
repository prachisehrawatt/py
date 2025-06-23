'''1.⁠ ⁠Read data.txt and display all letters that start with the letter 'A'.
2.⁠ ⁠Check if the word 'significant' exists. If yes, print “Found”
3.⁠ ⁠Display the last line from the file summary.txt
4⁠. ⁠Read all lines from data.txt into a list and print that list.'''

#program1
f=open('data.txt','r')
data=f.read()
word=data.split()
for i in word:
    if i[0]=='T':
        print('Words starting with letter T :',i)

#program2
if 'significant' in data:
    print("Word significant found !")
f.close()

#program3
f=open('data.txt','r')
lines = f.readlines()
if lines:
    print(lines[-1])
f.close()

#program4
f=open('data.txt','r')
data=f.read()
lst=data.split()
print(lst)
f.close()
