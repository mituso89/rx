import flight.suppliers.index as flight
import sys

name = 'flight'

def flightctl(suppliername):

    return flight[suppliername][name]()
