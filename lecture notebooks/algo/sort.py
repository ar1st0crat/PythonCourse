'''
Sort

The module provides a standard set of trivial sorting algorithms (O(N^2)):
    - Insertion Sort
    - Selection Sort
    - Bubble Sort
'''

def insertion_sort(a):
    ''' Insertion Sort implementation.

    Parameters
    ----------
    a : array of items

    Returns
    ---------- 
    array of sorted items
    '''
    for i in range(1, len(a)):
        j = i - 1 
        key = a[i]
        while a[j] > key and j >= 0:
           a[j + 1] = a[j]
           j -= 1
        a[j + 1] = key


def selection_sort(a):
    ''' Selection Sort implementation.

    Original:
    https://rosettacode.org/wiki/Sorting_algorithms/Selection_sort

    Parameters
    ----------
    a : array of items

    Returns
    ---------- 
    array of sorted items
    '''
    for i, e in enumerate(a):
        min_idx = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[min_idx] = a[min_idx], e


def bubble_sort(a):
    ''' Bubble Sort implementation.

    Parameters
    ----------
    a : array of items

    Returns
    ---------- 
    array of sorted items
    '''
    inversions = True
    while inversions:
        inversions = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                inversions = True