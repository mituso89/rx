import flight.suppliers.clairtyfy.flight
import flight.suppliers.clairtyfy.tax
import sys

sys.modules[__name__] = {'flight': flight.suppliers.clairtyfy.flight.search
                         }


