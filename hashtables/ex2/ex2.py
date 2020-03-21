#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Fill the Hashtable with ticket info (src, dest)
    for tkt in tickets:
        src = tkt.source
        dest = tkt.destination
        hash_table_insert(hashtable, src, dest)

    # Setting up flight itinerary
    itinerary = hash_table_retrieve(hashtable, "NONE")
    for i in range(length):
        route[i] = itinerary
        itinerary = hash_table_retrieve(hashtable, itinerary)

    return route[:-1]
