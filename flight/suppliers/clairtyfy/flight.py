import flight.utils.index as db
import flight.utils.dbconnection as data
import json
import asyncio
import flight.suppliers.clairtyfy.helper as helper
from flight.config import Config

fareClassMap = {
    'Economy': 'ECONOMY',
    'Premium Economy': 'PREMECONOMY',
    'Business': 'BUSINESS',
    'First': 'FIRSTCLASS'
}


def makerequest(acc, req):
    AirShoppingRQ = {
        'AirShoppingRQ': {
            'Document': {
                'Name': 'Demo Agency',
                'ReferenceVersion': '1.0'
            },
            'Party': {
                'Sender': {
                    'TravelAgencySender': {
                        'Name': 'Demo Agency',
                        'IATA_Number': None,
                        'AgencyID': None,
                        'Contacts': {
                            'Contact': [
                                {
                                    'EmailContact': 'r.subba@claritytts.com'
                                }
                            ]
                        }
                    }
                }
            },
            'CoreQuery': {
                'OriginDestinations': {
                    'OriginDestination': [
                        {
                            'Departure': {
                                'AirportCode': req['departure_airport_code'],
                                'Date': req['departure_date']
                            },
                            'Arrival': {
                                'AirportCode': req['arrival_airport_code']
                            }
                        },
                        {
                            'Departure': {
                                'AirportCode': req['arrival_airport_code'],
                                'Date': req['return_date']
                            },
                            'Arrival': {
                                'AirportCode': req['departure_airport_code']
                            }
                        }
                    ] if req['is_round_trip'] else [
                        {
                            'Departure': {
                                'AirportCode': req['departure_airport_code'],
                                'Date': req['departure_date']
                            },
                            'Arrival': {
                                'AirportCode': req['arrival_airport_code']
                            }
                        }
                    ]

                }
            }, 'DataLists': {
                'PassengerList': {
                    'Passenger': helper.buildPassenger(
                        adults=int(req['adults']),
                        children=int(req['children']),
                        infants=int(req['infants'])
                    )
                }
            },

            'Preference': {
                'TripType':   'Return' if req['is_round_trip'] else 'Oneway',
                'FareType': 'BOTH',
                'Cabin': fareClassMap[req['cabin_class']],
                'AlternateDays': 0,
                'DirectFlight': '',
                'Refundable': '',
                'NearByAirports': '',
                'FreeBaggage': ''
            },
            'MetaData': {
                'Currency': acc['default_currency'],
                'FareGrouping': 'Deal'
            }
        }
    }

    return AirShoppingRQ


def clean(result):
    return 'tuan'


def search(acc, req):
    print(acc)

    request = makerequest(acc, req)
    result = helper.sentrequest(acc, request, 'availability')
    data.insert_mongo({'request': request, 'response':result.json() }, Config.mongo_db, 'logs')


    # redis = db['redis']()
    # my_json = json.loads(redis.get('flight-api:lucky:supplier:user:35'))
    return clean(result)
