name = "Python"
first_letter = name[0] # 'P' <--- Indexing
slice = name[1:4]      # 'yth' <--- slicing

# print(first_letter)
# print(slice)

address = "Diliman, Quezon City 1101"
# print(len(address))
# slice = address[len]

#practice
len_of_add = len(address)
len_of_zip_code = len(address) - 4
slice = address[len_of_zip_code:len_of_add]

# Efficient
slice = address[-4:]
print(slice)