# Given a list of positive integers and a target integer, 
# write a function that returns all of the 
# unique pairs of integers in the list that sum to the target.

# O(n^2) solution:
def target_sum(some_list, n):
    out = []
    for i in range(len(some_list)-1):
        for j in range(i + 1, len(some_list)):
            if (some_list[i] + some_list[j]) == n:
                if not (some_list[i], some_list[j]) in out:
                    out.append((some_list[i], some_list[j]))
    return out


# O(n) solution:
def sum_of_two(some_list, n):
    d = {}
    out = []
    for i in some_list:
        target = n - i
        if d.get(target, 0) > 0:
            out.append((i, target))
            d[target] -= 1

        else:
            d[i] = d.get(i, 0) + 1
    return out

# What if we wanted three numbers that added up to 0:
def sum_three(l, n):
    out = []
    new_l = list(l)
    for each in l:
        # remove the first item from the copy list
        new_l.pop(0)
        complementary = n - each
        new_tuples = [(each, ) + result for result in sum_of_two(new_l, complementary)]
        out = out + new_tuples

    return out

l = [1, 2, 2, 4, 6, 8, 3, 5, 5]
t = 10

# should return [(2,8), (4, 6), (5, 5)]
# returns the correct pairs but since the function
# looks back at the previous list items 
# the pairs are backward 
print sum_of_two(l, t)

# should return [(1, 3, 6), (1, 5, 4), (2, 6, 2), (2, 5, 3)]
# still returning duplicate (2, 5, 3)
print sum_three(l, t)