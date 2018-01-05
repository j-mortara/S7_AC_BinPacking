#! /usr/bin/env python3

from _heapq import *
from sys import argv


# def next_fit_no_list(inputs):
#     nb_bins = 1
#     remaining_space_in_bin = inputs[0]
#     for item_value in inputs[1]:
#         if item_value > remaining_space_in_bin:
#             nb_bins += 1
#             remaining_space_in_bin = inputs[0]
#         remaining_space_in_bin -= item_value
#     return nb_bins


# If the item fits in the same bin as the previous item, put it there. Otherwise, open a new bin and put it in there.
# Complexity : We never go back in the bins list => O(n)
def next_fit(inputs):
    # For n values to store, the maximum number of bins is n,
    # so we directly create a list of n bins to avoid appending items
    bins = [0] * len(inputs[1])  # Array of maximum size: number of items
    index = 0  # iterator
    for item in inputs[1]:  # for each item
        if item + bins[index] > inputs[0]:  # if the capacity for the current bin is not enough for this item
            index += 1  # get a new bin
        bins[index] += item  # add the new item
    # We keep the bins containing items by filtering the bins list, then we return the length of this filtered list.
    opened_bins = list(filter(lambda x: x > 0, bins))  # used to remove all unused (=empty) bins
    print(len(opened_bins))
    return opened_bins


def first_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    
    for item in inputs[1]:  # for each items to pack
        j = index
        while item + bins[j] > inputs[0] :
            j += 1
        bins[j] += item
       
    opened_bins = list(filter(lambda x: x > 0, bins))
    return opened_bins

# Put each item as you come to it into the oldest (earliest opened) bin into which it fits.
# Complexity : Worst case -> when the item to place is lighter than the previous one, we are starting to iterate
# from index 0 => O(n^2)
# Complexity : Best case -> when the item to place is weighter (or equal) than the previous one, we are starting
# to iterate from the previous index 0 => O(???)
def first_fit_enhanced(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    # For the first iteration we are considering the previous item as an infinite weighted item.
    previousItem = float('inf')
    previousIndex = -1
    for item in inputs[1]:
        # If the next item is lighter than the previous one, iterate from 0
        if item < previousItem:
            iterator = 0
        # Else we are starting to iterate from the last bin used (the bins before are too full to be used).
        else:
            iterator = previousIndex
        # We are iterating to a bin used
        while item + bins[iterator] > inputs[0]:
            iterator += 1
        # Store the item, save its weight and the bin index used.
        bins[iterator] += item
        previousItem = item
        previousIndex = iterator

    opened_bins = list(filter(lambda x: x > 0, bins))
    return opened_bins

# 1. Put each item into the emptiest bin among those with something in them.
# Only start a new bin if the item doesn't fit into any bin that's already been started.
# 2. If there are two or more bins already started which are tied for emptiest, use the bin
# opened earliest from among those tied.
# Complexity : For each value, we iterate over the bins to find the emptiest one => O(n^2)
def worst_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        j = index
        min_index = j
        min_val = inputs[0]
        # we browse the opened bins to find the emptiest one
        while j >= 0:
            # the possible equality with min_val guarantees that the earliest opened bin will be picked in case of tie,
            # as we browse the bins from the latest opened one to the earliest opened one
            if bins[j] <= min_val:
                min_val = bins[j]
                min_index = j
            j -= 1
        # if the emptiest bin cannot contain the item, we create one
        if item + bins[min_index] > inputs[0]:
            index += 1
            bins[index] += item
        # if the emptiest bin can contain the item, we add it in the bin
        else:
            bins[min_index] += item
    opened_bins = list(filter(lambda x: x > 0, bins))
    return opened_bins


# Same as worst fit, but we put the item in the second-emptiest bin
# Complexity : For each value, we iterate over the bins to find the second-emptiest one => O(n^2)
def almost_worst_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        j = index
        min_index = j
        min_val = inputs[0]
        second_min_index = None
        first_loop = True
        # we browse the opened bins to find the emptiest one
        while j >= 0:
            # the possible equality with min_val guarantees that the earliest opened bin will be picked in case of tie,
            # as we browse the bins from the latest opened one to the earliest opened one
            if bins[j] <= min_val:
                # if the current bin is the first valid one encountered, we don't set the second emptiest bin index
                if first_loop:
                    first_loop = False
                else:
                    second_min_index = min_index
                min_index = j
                min_val = bins[j]
            j -= 1
        # we set the emptiest bin index to the second emptiest bin index if it exists
        # What if the second-emptiest one exists but cannot contain item ?

        # Case : create another
        # Here, the next if condition will check if the second_min_index can contain the item.
        # Supposing it cannot, another bin will be opened.
        # if second_min_index is not None:
        #     min_index = second_min_index

        # Case : check if the second emptiest one can contain the item, and take this one if it is the case.
        # Otherwise, keep the emptiest one.
        if second_min_index is not None and item + bins[second_min_index] < inputs[0]:
            min_index = second_min_index

        # if the bin cannot contain the item, we create one
        if item + bins[min_index] > inputs[0]:
            index += 1
            bins[index] += item
        # if the bin can contain the item, we add it in the bin
        else:
            bins[min_index] += item
    opened_bins = list(filter(lambda x: x > 0, bins))
    return opened_bins


# Array of two elements arrays [valBin, numBin]
# We put each item in the emptiest opened bin.
# If the emptiest bin cannot contain the item, we open a new one.
# If the two emptiest bins have the same value, priority is given to the last opened.
# We use a heap to represent this problem, as we have O(1) access to the lowest value.
# Insertion in the heap is done in O(log n) for each item, therefore the complexity is O(n log n).
def _worst_fit_log(inputs):
    # bins = [[0, 0] for _ in range(len(inputs[1]))]
    heap = []
    for item in inputs[1]:
        if len(heap) == 0 or heap[0][0] + item > inputs[0]:
            heappush(heap, [item, len(heap)])  # O(log n)
        else:
            heapreplace(heap, [heap[0][0] + item, heap[0][1]])  # O(1) for access, O(log n) for insert
    return heap


def worst_fit_log(inputs):
    # bins = [[0, 0] for _ in range(len(inputs[1]))]
    return [i[0] for i in _worst_fit_log(inputs)]


# Place each item in the fullest one capable of containing the item.
# Complexity : Worst case -> for each value, the adequate bin is at the beginning of the array => O(n^2)
def best_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        j = index
        max_index = j
        max_val = 0
        # we browse the opened bins to find the adequate bin
        while j >= 0:
            # if the bin is fullest than the previous valid one but can still contain the item,
            # it becomes the new valid one
            if max_val < bins[j] <= inputs[0] - item:
                max_val = bins[j]
                max_index = j
            j -= 1
        # If we enter this condition, this means that the bin at index max_index cannot contain the item.
        # In order to enter this condition, max_index must be equal to 0.
        # Indeed, having max_index != 0 implies that we entered the precedent if condition at least once,
        # meaning that the bin at index max_index can contain the item.
        # Therefore, we know by entering this condition that no bin can contain the item, so we open a new one.
        if item + bins[max_index] > inputs[0]:
            index += 1
            bins[index] += item
        else:
            # we add the item in the bin
            bins[max_index] += item
    opened_bins = list(filter(lambda x: x > 0, bins))
    return opened_bins


# Returns the input in a tuple
# 0 : capacity of the bins
# 1 : the values to store in the bins
def get_inputs(file_path):
    f = open(file_path, "r")
    f.readline()
    bin_size = int(f.readline())
    f.readline()
    objects = list(map(int, f.readline().replace(".", "").split(", ")))
    return bin_size, objects


if __name__ == '__main__':
    values = get_inputs(argv[1])
    print("next fit :")
    nf = next_fit(values)
    print(nf)
    print(len(nf))
    print("first fit :")
    ff = first_fit(values)
    print(ff)
    print(len(ff))
    print("worst fit :")
    wf = worst_fit(values)
    print(wf)
    print(len(wf))
    print("worst fit nlogn :")
    wf_log = worst_fit_log(values)
    print(wf_log)
    print(len(wf_log))
    print("almost worst fit :")
    awf = almost_worst_fit(values)
    print(awf)
    print(len(awf))
    print("best fit :")
    bf = best_fit(values)
    print(bf)
    print(len(bf))
