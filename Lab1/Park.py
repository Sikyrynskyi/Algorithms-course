class Park:
    def __init__(self, adress, bikelanes_length, price):
        self.adress = adress
        self.bikelanes_length = bikelanes_length
        self.price = price

    def __str__(self):
        return "Adress: " + self.adress + "| " + "Bikelanes length: " + str(self.bikelanes_length) + "| " + \
               "price: " + str(self.price)


    #insertion sort by the bikelanes length by recurrence
    @staticmethod
    def insertion_sort(parks):
        compares = 0
        swaps = 0
        for i in range(1, len(parks)):
            j = parks[i]
            position = i
            while position > 0 and j.bikelanes_length > parks[position - 1].bikelanes_length:
                compares += 1
                swaps += 1
                parks[position] = parks[position - 1]
                position -= 1
            parks[position] = j
        print("Compares: " + str(compares))
        print("Swaps: " + str(swaps))

#merge sort by the ticket price on growth
#split list into two
def merge_sort(parks):
    if len(parks)>1:
        mid = len(parks)//2
        left_list = parks[:mid]
        right_list = parks[mid:]

        sorted_left_list = merge_sort(left_list)
        sorted_right_list = merge_sort(right_list)

        return merge(sorted_left_list, sorted_right_list)
    else:
        return parks

def merge(left_list, right_list):
    merged_list = []
    i = 0
    j = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i].price < right_list[j].price:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1
    merged_list.extend(left_list[i:])
    merged_list.extend(right_list[j:])
    return merged_list



