import pprint
fuji_list=[[i*10-j for j in range(10)]for i in range(10,0,-1)]
pprint.pprint(fuji_list)

print()

row=col=5
saku_list=[[1 if (j==i or j==(col-1-i)) else 0 for j in range(col)] for i in range(row)]
pprint.pprint(saku_list)

print()

take_list=[[i-j for j in range(0,100,10)] for i in range(0,100,10)]
pprint.pprint(take_list)

print()

row=col=5
sato_list=[[1 if j==i else 0 if j>i else 2 for j in range(col)]for i in range(row)]
pprint.pprint(sato_list)

print()

kano_list=[[i*j for j in range(1,10)]for i in range(3,10,2)]
pprint.pprint(kano_list)

print()

col=row=3
hana_list=[[3 if (i==1 and j==1) else 7 for j in range(col)]for i in range(row)]
pprint.pprint(hana_list)
