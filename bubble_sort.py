alist1 = [10,2,3,1,5,8,6]

print("Original list: ", alist1)
Flags = False
for i in range(len(alist1)-1):
    for j in range(len(alist1)-1-i):
        print("1:\t",j, alist1[j],alist1[j+1],sep="\t")

        if alist1[j] > alist1[j+1]:
            temp = alist1[j]
            alist1[j] = alist1[j+1]
            #print("2:\t",j, alist1[j],alist1[j+1],sep="\t")
            alist1[j+1] = temp
            #print("3:\t", j,  alist1[j + 1], temp,sep="\t")
            Flags = True


if Flags == True:

    print("bubble sorted is ",alist1)
else:
    print("Already sorted!")
