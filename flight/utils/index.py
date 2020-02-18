import flight.utils.dbconnection
import sys

sys.modules[__name__] = {'redis': flight.utils.dbconnection.redisConnect, 'getdata': {
    flight.utils.dbconnection.getdata}}
