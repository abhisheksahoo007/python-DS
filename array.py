# mylist1 =   ['January','February','March','April','May']
# mylist2 =   [2200,2350,2600,2130,2190]



# for i in range(len(mylist1)):
#     if mylist1[i]   ==  'February':
#         for j in range(len(mylist1)):
#             if mylist1[j]   ==  'January':
#                 print("Expense difference between February and January is")
#                 print(mylist2[i]-mylist2[j])

# x   =   0
# for i in range(3):
#     x+=mylist2[i]
   
# print("Quarterly Expense")
# print(x)


# for i in mylist2:
#     if i == 2000:
#         print(mylist1[i])
#         break
#     else:
#         print("No month found")
#         break
# mylist1.append('June')
# mylist2.append(1980)
# print(mylist1)
# print(mylist2)            

def findPair():
    s   =   int(input("Enter the array Size:"))
    print("Enter the elements:")
    a   =   []
    for x in range(s):
        a.insert(x,int(input()))
    q= int(input("Enter the maximum value:"))
    print(a)
    # for x in a:
    #     n   = q-x
    #     a.remove(x)
    #     if n in a:
    #         print("pair is",n,x)
    for i in range(0,s):
        for j in range(1,s):
            if a[i]+a[j] == q:
                print("Pair is",a[i],a[j])


findPair()                
