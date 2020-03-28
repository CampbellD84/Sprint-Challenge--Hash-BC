#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Length of List of weights is less than 2,
    #  return None
    if length < 2:
        return None

    # Iterate through weights list
    for idx in range(length):
        load = weights[idx]
        # insert weights into hashtable
        hash_table_insert(ht, load, idx)

    for idx in range(length):
        load = weights[idx]
        # Create key
        load_key = limit - load
        # Check for key in hashtable
        load_check = hash_table_retrieve(ht, load_key)

        # Check which of 2 indices is largest
        # then return tuple with largest 1st, smallest 2nd
        # ex. (lrg_val, sml_val)
        if load_check is not None:
            if idx < load_check:
                sml_load = idx
                lrg_load = load_check
            else:
                sml_load = load_check
                lrg_load = idx
            return (lrg_load, sml_load)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
