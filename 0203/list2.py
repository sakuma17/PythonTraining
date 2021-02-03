import pprint
W=10
H=10
data=[None]*H
for i in range(H):
    data[i]=[0]*W
pprint.pprint(data)

"""
Javaでの書き方
int[] numList=new int[10][10];
for(int i=0;i<numList.length;i++){
    for(int j=0;j<numList[i].length;j++){
        numList[i][j]=0;
    }
}
"""
