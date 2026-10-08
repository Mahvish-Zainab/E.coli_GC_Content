F=open("sequence.fasta","r")
x=F.read()
a=x.count("A")
t=x.count("T")
g=x.count("G")
c=x.count("C")
total= a+t+g+c
gc_content= (g+c)*100 / total
print(gc_content)
F.close()
