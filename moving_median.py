from indexed_pq import median_ipqa

def moving_median(A):
    my_median_ipqa = median_ipqa()
    out = []
    for i, val in enumerate(A):
        my_median_ipqa.insert(i, val)
        out.append(my_median_ipqa.get_median())
    return out

def moving_windowed_median(A, w):
    # A the array of values,
    # w the width of the moving window
    my_median_ipqa = median_ipqa()
    out = []
    for i, exp in enumerate(A):
        if i+1 > w:
            my_median_ipqa.pop_by_index(i - w)
        
        my_median_ipqa.insert(i, exp)
        out.append(my_median_ipqa.get_median())
    return out

if __name__ == "__main__":
    print(moving_median([1,2,3,4,5]))
    print(moving_windowed_median([1,2,3,4,5], 3))