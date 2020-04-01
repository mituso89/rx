import flight.suppliers.index as flight
import flight.utils.dbconnection as db
import sys

name = 'flight'

def flightctl(param):

    suppliername = 'ClarityTTS'
    param['cabin_class'] = 'Economy'
    result = db.getdata(
        'SELECT id, `code`, source_id, name, username, passwd, url,default_currency FROM Flight.supplier where `code` = "ClarityTTS"')
    return flight[suppliername][name](result[0], param)
