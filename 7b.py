k=open('somu.txt','r')
char,wc,lc=0,0,0
for i in k:
 for k in range(len(i)):
    char +=1
    if(i[k]==' '):
        wc+=1
    if(i[k]=='\n'):
        lc=wc+1
print("The no.of chars is ",char,"\n The no.of words is ",wc+lc,"\n The no.of lines is ",lc)