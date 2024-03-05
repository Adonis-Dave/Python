my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Appended elements: ", my_list)

my_list.insert(1, 15)
print("Inserted item: ", my_list)

list = [50, 60, 70]

my_list.extend(list)
print("Extended list: ", my_list)

del my_list[-1]
print("Deleted last item: ", my_list)

my_list.sort()
print("The list in ascending order: ", my_list)

index30 = my_list.index(30)
print("The index of value 30 in the list is ", index30)
