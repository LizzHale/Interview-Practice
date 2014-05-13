def merge(l1, l2):
    output_list = []
    while l1 and l2:
        if l1[0] < l2[0]:
            num = l1.pop(0)
        else:
            num = l2.pop(0)
        output_list.append(num)
    output_list = output_list + l1 + l2
    return output_list


def mergesort(some_list):
    
    if len(some_list) <= 1:
        return some_list
    half = len(some_list)/2
    l1 = some_list[:half]
    l2 = some_list[half:]
    l1 = mergesort(l1)
    l2 = mergesort(l2)
    return merge(l1, l2)