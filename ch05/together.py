import park

setlist = []

for height in input().split():
    setlist.append(set(park.allowedrides(int(height))))

for ride in set.intersection(*setlist):
    print(ride)
