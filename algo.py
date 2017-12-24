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


# We never go back in the bins list => O(n)
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


# Worst case : for each value, the first empty enough bin is at the beginning of the array => O(n^2)
def first_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        if item + bins[index] > inputs[0]:
            j = index
            while item + bins[j] > inputs[0] and j > 0:
                j -= 1
            if j == 0 and item + bins[j] > inputs[0]:
                index += 1
                j = index
            bins[j] += item
        else:
            bins[index] += item
    print(bins)
    return len(list(filter(lambda x: x > 0, bins)))


# For each value, we iterate over the bins to find the emptiest one => O(n^2)
def worst_fit(inputs):
    bins = [0] * len(inputs[1])
    index = 0
    for item in inputs[1]:
        j = index
        min_index = j
        min_val = inputs[0]
        while j >= 0:
            if bins[j] < min_val:
                min_val = bins[j]
                min_index = j
            j -= 1
        if item + bins[min_index] > inputs[0]:
            index += 1
            bins[index] += item
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
