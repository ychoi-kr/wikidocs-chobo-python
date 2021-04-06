import glob

outfile = open("out.txt", "wt")

for x in glob.glob("korean_national_anthem_?.txt"):
    infile = open(x, "rt")
    #infile = open(x, "rt", encoding="utf-8-sig") # https://stackoverflow.com/a/44573867
    
    outfile.write(x + '\n')
    outfile.write('-' * len(x) + '\n')
    outfile.write(infile.read() + "\n\n")

outfile.close()
