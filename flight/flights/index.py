#from flight.flights.clairtyfy import search
import flight.flights.clairtyfy
import flight.flights.kiwi
import sys

sys.modules[__name__] = {'clairty': flight.flights.clairtyfy.search,
                         'kiwi': flight.flights.kiwi.search
                         }
