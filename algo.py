from _heapq import *


def next_fit_no_list(inputs):
    nb_bins = 1
    remaining_space_in_bin = inputs[0]
    for item_value in inputs[1]:
        if item_value > remaining_space_in_bin:
            nb_bins += 1
            remaining_space_in_bin = inputs[0]
        remaining_space_in_bin -= item_value
    return nb_bins


# If the item fits in the same bin as the previous item, put it there. Otherwise, open a new bin and put it in there.
# Complexity : We never go back in the bins list => O(n)
def next_fit(inputs):
    # For n values to store, the maximum number of bins is n,
    # so we directly create a list of n bins to avoid appending items
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        if item + bins[index] > inputs[0]:
            index += 1
        bins[index] += item
    print(bins)
    # We keep the bins containing items by filtering the bins list, then we return the length of this filtered list.
    return len(list(filter(lambda x: x > 0, bins)))


# Put each item as you come to it into the oldest (earliest opened) bin into which it fits.
# Complexity : Worst case -> for each value, the first empty enough bin is at the beginning of the array => O(n^2)
def first_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        # if the bin cannot contain the item
        if item + bins[index] > inputs[0]:
            j = index
            # we browse the bins until we find one that can contain the item
            while item + bins[j] > inputs[0] and j > 0:
                j -= 1
            # if, arrived at index 0, no bin can contain the item, we add one
            if j == 0 and item + bins[j] > inputs[0]:
                index += 1
                j = index
            bins[j] += item
        # if the bin can contain the item, we add it in the bin
        else:
            bins[index] += item
    print(bins)
    return len(list(filter(lambda x: x > 0, bins)))


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
    print(bins)
    return len(list(filter(lambda x: x > 0, bins)))


# Array of two elements arrays [valBin, numBin]
# We put each item in the emptiest opened bin.
# If the emptiest bin cannot contain the item, we open a new one.
# If the two emptiest bins have the same value, priority is given to the last opened.
# We use a heap to represent this problem, as we have O(1) access to the lowest value.
# Insertion in the heap is done in O(log n) for each item, therefore the complexity is O(n log n).
def worst_fit_log(inputs):
    # bins = [[0, 0] for _ in range(len(inputs[1]))]
    heap = []
    for item in inputs[1]:
        if len(heap) == 0 or heap[0][0] + item > inputs[0]:
            heappush(heap, [item, len(heap)])  # O(log n)
        else:
            heapreplace(heap, [heap[0][0] + item, heap[0][1]])  # O(1) for access, O(log n) for insert
    print(heap)
    return len(heap)


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
    print(bins)
    return len(list(filter(lambda x: x > 0, bins)))


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
    values = get_inputs("test_files/exemple100.txt")
    print("next fit :")
    print(next_fit(values))
    print("first fit :")
    print(first_fit(values))
    print("worst fit :")
    print(worst_fit(values))
    print("worst fit nlogn :")
    print(worst_fit_log(values))
    print("best fit :")
    print(best_fit(values))
