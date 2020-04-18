
outfile = open("numdirs.txt","w")

for i in range(0,99999):
	post = "{:05d}".format(i)
	outfile.write(str(post)+"\n")
	
outfile.close()