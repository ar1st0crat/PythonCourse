# -*- coding: utf8 -*-

def binary_search(a, elem):
    ''' Binary Search iterative implementation.

    Parameters
    ----------
    a : array of items
    elem : item to find
    Returns
    ---------- 
    position or -1
    '''
    l = 0
    r = len(a) - 1

    while l <= r:
        mid = (l + r) // 2

        if a[mid] == elem:
            return mid
        elif a[mid] > elem:
            r = mid - 1
        else:    
            l = mid + 1

    return -1


def interpolation_search(a, elem):
    ''' Interpolation Search iterative implementation.

    The worst case complexity of interpolation search is O(N), 
    e.g., searching for 1000 in 1,2,...,999,1000,10^9 will take 1000 accesses.
    However, its average case complexity, under the assumption that the keys 
    are uniformly distributed, is O(log log N) '''
    l = 0
    r = len(a) - 1

    while l <= r and a[l] != a[r]:
        mid = l + (elem - a[l]) * (r - l) // (a[r] - a[l])

        if mid > r or mid < l:
            return -1

        if a[mid] == elem:
            return mid
        elif a[mid] > elem:
            r = mid - 1
        else:    
            l = mid + 1

    return -1 


def exponential_search(a, elem):
    ''' Exponential Search implementation '''
    l = 1;
    r = len(a) - 1

    while l < r and a[l] < elem:
        l *= 2

    start = l // 2
    end = min(l, r)
    return start + binary_search(a[start:end], elem)


def __test_speed():
    ''' Routine for comparing performance of search algorithms '''

    pos = binary_search(nums, x)
    print('Element {} found in position {}'.format(x, pos))

    pos = interpolation_search(nums, x)
    print('Element {} found in position {}'.format(x, pos))

    pos = exponential_search(nums, x)
    print('Element {} found in position {}'.format(x, pos))


    t = timeit.timeit('pos = binary_search(nums, x)', 
                setup="from __main__ import binary_search, nums, x",  
                number=100)
    print('Binary search: {} sec'.format(t))

    t = timeit.timeit('pos = interpolation_search(nums, x)', 
                setup="from __main__ import interpolation_search, nums, x",
                number=100)
    print('Interpolation search: {} sec'.format(t))

    t = timeit.timeit('pos = exponential_search(nums, x)', 
                setup="from __main__ import exponential_search, nums, x",
                number=100)
    print('Exponential search: {} sec'.format(t))


if __name__ == '__main__':
    import random
    import timeit

    N = 10000
    BIG_OUTLIER = 100000000
    nums = list(range(N))
    nums.append(BIG_OUTLIER)
    x = random.randint(0, N)

    __test_speed()