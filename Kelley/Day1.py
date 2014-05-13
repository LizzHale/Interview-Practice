# Given a list of positive integers and a target integer, 
# write a function that returns all of the 
# unique pairs of integers in the list that sum to the target.

def target_sum(some_list, target):
    out = []
    for first_index in range(len(some_list)-1):
        for second_index in range(first_index + 1, len(some_list)):
            if (some_list[first_index] + some_list[second_index]) == 10:
                if not (some_list[first_index], some_list[second_index]) in out:
                    out.append((some_list[first_index], some_list[second_index]))
    return out


l = [1, 2, 2, 4, 6, 8, 3, 5, 5]
t = 10
# should return [(2,8), (4, 6), (5, 5)]
print target_sum(l, t)