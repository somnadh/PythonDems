file=open('somu.txt','r')
for line in file:
 l=len(line)
 s=' '
while(l>=1):
 s=s+line[l-1]
 l=l-1
print(s)
file.close()