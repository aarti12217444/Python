# wap to print each line of a file in reverse order(you should present file in ur file which u will provide name of file)
i = input("Enter the file name: ")
fin=open(i,'r')
for i in range(7):
    a=fin.readline()
    print(a.strip()[::-1])
fin.close()

# copy content of one file to another(here i have outputdata3.txt file soo i use this file)
file=input("Enter file name: ")
fin=open(file,'r')
fout=open("outputdata3.txt",'w')
fin.close()
fout.close()
fin2=open("outputdata3.txt",'r')
print(fin.read())
fin2.close()

