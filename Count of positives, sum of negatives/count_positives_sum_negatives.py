putin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
putin2 = [0,0]
putin3 = []


def count_positives_sum_negatives(arr):
    cum = []
    count = []
    result = []
    if not arr:
        return result
    
    else:
        for i in arr: 
            if i < 0:cum.append(i)
            if i > 0:count.append(i)
    result.append(len(count))
    result.append(sum(cum))
    return result

print(count_positives_sum_negatives(putin))
print(count_positives_sum_negatives(putin2))
print(count_positives_sum_negatives(putin3))