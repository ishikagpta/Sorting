from sort import *
from random import randint
import timeit
import sys


# Main driver to test sorting methods and accept user input to test sort.py sorting
# code ensuring each input parameter works
def main():
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        raise ValueError("Number of parameters is not valid!")

    types_of_sort_list = ["BubbleSort", "InsertionSort", "MergeSort", "IterativeMergeSort", "QuickSort", "ShellSort"]

    if sys.argv[1] not in types_of_sort_list:
        raise ValueError("Please choose sort type: BubbleSort,InsertionSort,MergeSort, _"
                         "IterativeMergeSort,QuickSort,ShellSort")

    try:
        int(sys.argv[2])
    except:
        raise TypeError("Please enter a positive number only!")
    if len(sys.argv) > 3:
        if sys.argv[3] != "PRINT":
            raise ValueError("Please write PRINT properly.")

    random_list = []
    for i in range(int(sys.argv[2])):
        random_list.append(randint(0, 5000))
        printing = False
    if len(sys.argv) > 3:
        printing = sys.argv[3] == "PRINT"
    if printing:
        print(random_list)
    types_of_sort = {"BubbleSort": bubble_sort(random_list),
                     "InsertionSort": insertion_sort(random_list),
                     "MergeSort": merge_sort(random_list),
                     "IterativeMergeSort": iterative_merge_sort(random_list),
                     "QuickSort": quick_sort(random_list),
                     "ShellSort": shell_sort(random_list)
                     }

    sort_type = sys.argv[1]

    if sort_type in types_of_sort and printing:
        types_of_sort[sort_type]
        print(random_list)
    elif sort_type in types_of_sort:
        types_of_sort[sort_type]
        print("Finished Sorting")
    else:
        print("Not Found")


if __name__ == "__main__":
    main()


# Below code is to generate data for performance graphs for various sort algorithms and various
# input sizes using timeit
setup_code = '''
import sort
import random
random_list = []
for i in range(50000):
    random_list.append(random.randint(0,100000))'''

num_of_reps = 1


def bubble_sort_timing():
    time_list = timeit.repeat(setup=setup_code, stmt="sort.bubble_sort(random_list)", repeat=num_of_reps, number=10)
    print(f'bubble_sort_timing: {time_list}')


def insertion_sort_timing():
    time_list = timeit.repeat(setup=setup_code, stmt="sort.insertion_sort(random_list)", repeat=num_of_reps, number=10)

    print(f'insertion_sort_timing: {time_list}')


def merge_sort_timing():
    time_list = timeit.repeat(setup=setup_code, stmt="sort.merge_sort(random_list)", repeat=num_of_reps, number=10)

    print(f'merge_sort_timing: {time_list}')


def iterative_merge_sort_timing():
    time_list = timeit.repeat(setup=setup_code, stmt="sort.iterative_merge_sort(random_list)", repeat=num_of_reps,
                              number=10)

    print(f'iterative_merge_sort_timing: {time_list}')


def quick_sort_timing():
    time_list = timeit.repeat(setup=setup_code, stmt="sort.quick_sort(random_list)", repeat=num_of_reps, number=10)

    print(f'quick_sort_timing: {time_list}')


def shell_sort_timing():
    time_list = timeit.repeat(setup=setup_code, stmt="sort.shell_sort(random_list)", repeat=num_of_reps, number=10)

    print(f'shell_sort_timing: {time_list}')

# bubble_sort_timing()
# insertion_sort_timing()
# merge_sort_timing()
# iterative_merge_sort_timing()
# quick_sort_timing()
# shell_sort_timing()
