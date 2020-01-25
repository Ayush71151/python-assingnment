outfile=open("pholosopher.txt",'w')
outfile.write("560\n")
outfile.write("400\n")
outfile.write("l30\n")
outfile.write("20\n")
outfile.write('10\n')
outfile.close()
outfile=open("pholosopher.txt",'r')
print (outfile.read())
outfile.close()

def main():
    infile=open('pholosopher.txt','r')
    line=infile.readline()
    while line !="":
        amount=float(line)
        line=infile.readline()
        print(amount)
main()