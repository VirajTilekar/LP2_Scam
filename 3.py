def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = []
n = 'Y'

while n!='N':
    m=int(input("Enter Number : "))
    data.append(m)
    print("do you want add number : Y/N")
    n = input()

size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)