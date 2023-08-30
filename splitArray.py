# this list to split
array = [
    [1,2,3,4,5,6,7,8,9,0],
    [0,9,8,7,6,5,4,3,2,1],
    [2,3,4,5,6,7,8,9,0,1],
    [9,8,7,6,5,4,3,2,1,0],
    [3,4,5,6,7,8,9,0,1,2],
    [8,7,6,5,4,3,2,1,0,9],
    [4,5,6,7,8,9,0,1,2,3],
    [7,6,5,4,3,2,1,0,9,8]
]

# the number of splits
# this should result in 4 arrays 
num_splits = 4

# create a new list to add the sub lists to
new_list = []

split = len(array) // num_splits
print(f'Splitting array of len({len(array)}) into {num_splits} arrays of size {split}')

for i in range(0, len(array)):
    sub_split = i % split
    new_sub_list = []
    
    # print(f'array[{i}]: {i} % {split} = {sub_split}')
    if sub_split == 0:
       for j in range(i, i + split):
           new_sub_list.append(array[j])

    if len(new_sub_list) > 0:
        new_list.append(new_sub_list)

print(new_list)
