import time
from Park import Park
from Park import merge_sort
from Park import print_global_vars

# read from file and create list
def read_file():
    parks = []
    file = open('Parks.txt')
    adress = 0
    bikelanes_length = 1
    price = 2
    for line in file:
        value = line.split(', ')
        park = Park(value[adress], int(value[bikelanes_length]), int(value[price]))
        parks.append(park)
    return parks

#pretty self-explanatory
def print_list(parks):
    for i in parks:
         print(i)

if __name__ == "__main__":
    parks_list = read_file()

    print("Insertion:")
    start_time = time.clock()
    Park.insertion_sort(parks_list)
    elapsed_time = time.clock() - start_time
    print_list(parks_list)
    print("Timing: " + str(elapsed_time))

    print("\n\nMerge Sort:")
    start_time = time.clock()
    #had to do that because otherwise it wouldnt be showed
    temp = merge_sort(parks_list)
    elapsed_time = time.clock() - start_time
    print_list(temp)
    print("Timing: " + str(elapsed_time))
    print_global_vars()