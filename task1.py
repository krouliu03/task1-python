mylist = []
for i in range(3):
    mylist.append(input())


def change(arr):
    for i in arr:
        for j in arr:
            for k in arr:
                if i != j and j != k and i != k:
                    print(i,j,k)

change(mylist)