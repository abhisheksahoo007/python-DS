
def is_part_of_series(lst):
    for element in lst:
        vals = [0]
        counter = 1
        while counter <= (element/2)+1:
            vals.insert(0,(vals[0]*2+1))
            if element in vals:
                print(element)
                break
            counter += 1
    




x = int(input("Enter the number of elements in list :"))
a = []
print('Please enter the elements....\n')
for i in range(x):
    a.insert(i,int(input()))
print("Values satisfying recurrance relation are")
is_part_of_series(a)
