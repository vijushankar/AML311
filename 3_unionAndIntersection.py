def find_union(list1, list2):
    union_set = set(list1).union(set(list2))
    union_list = list(union_set)
    return union_list

def find_intersection(list1, list2):
    intersection_set = set(list1).intersection(set(list2))
    intersection_list = list(intersection_set)
    return intersection_list

# Test the functions with two sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

union_result = find_union(list1, list2)
intersection_result = find_intersection(list1, list2)

print("List 1:", list1)
print("List 2:", list2)

print("Union:", union_result)
print("Intersection:", intersection_result)
