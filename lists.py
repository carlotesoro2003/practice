letters = []
letters_range = int(input("Enter array size: "))

#add to list
for i in range(letters_range):
    input_list = input("Enter letter to add: ")
    letters.append(input_list)
    print(letters)


#remove to list of all occurences  
remove = input("Enter letter to remove in array: ")
letters = [letter for letter in letters if letter != remove]  
print("Final list: ", letters)


#find index
find = input("Enter letter to find its index: ")
indices = [index for index, letter in enumerate(letters) if letter == find]
if indices:
    print(find, "is found at indices:", indices)
    print("Occurrences of", find, ":", len(indices))
else:
    print(find, "is not found in the list.")


#max min
high = max(letters)
low = min(letters)

print("Highest letter: ", high)
print("Lowest letter: ", low)
