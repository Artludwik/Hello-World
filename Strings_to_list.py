# Try This:
with open('data.txt','w') as f:
    lis=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
    for x in zip(*lis):
        f.write("{0}\t{1}\t{2}\n".format(*x))
        print(lis)
