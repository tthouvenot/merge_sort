# Le principe est:
# On prend une liste on la divise en deux:
#  - puis chaques sous-liste on divise en deux jusqu'à ce qu'il ne reste plus qu'un élément
#  - puis on compare les sous-liste entre elle pour au final les ordonnées

my_list = [21, 125, 18, 99, 42, 78, 3, 0, 6, 33]

def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        middle = len(list) // 2
        left = merge_sort(list[:middle])
        right = merge_sort(list[middle:])
        return merge(left, right)

def merge(list1, list2):
    merged_list = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    return merged_list + list1 + list2

print(merge_sort(my_list))