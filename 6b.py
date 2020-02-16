import os
count =0
file=open("somu.txt")
for line in file:
 for l in range(0,len(line)):
    count+=1
print("no of characters:",count)
filename,file_extension=os.path.splitext("somu.txt")
print("file_extension==",file_extension)
if(file_extension=='.py'):
 print("its python program file")
elif(file_extension==".txt"):
 print("its a txt file")
elif(file_==extension==".c"):
 print("its a c program file")