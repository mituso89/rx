import requests
import asyncio
import json

methodMap = {
    'availability': 'AirShopping',
    'confirm_tax': 'AirOfferPrice',
    'generate_pnr': 'AirOrderCreate',
    'eticket': 'AirOrderPayment',
    'retrieve': 'AirOrderRetreive',
    'cancel': 'AirOrderCancel'
}


async def looprequest(datas, acc):

    headers = generateheaders(acc)
    loop = asyncio.get_event_loop()
    response = [loop.run_in_executor(None, makerequest, acc['url'] + '/' +
                                     methodMap[data['method']],
                                     data['body'],
                                     headers) for data in datas]
    result = await asyncio.gather(*response)
    return result


def makerequest(url, data, headers):
    response = requests.request("POST", url, data=json.dumps(data),
                                headers=headers)
    return response


def generateheaders(acc):
    header = {
        'Authorization': acc['passwd'],
        'Content-Type': 'application/json'
    }
    return header


def sentrequest(acc, data, method):
    headers = {
        'Authorization': acc['passwd'],
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", acc['url']+'/' + methodMap[method],
                                headers=headers, data=json.dumps(data))
    return response


def buildPassenger(**kwargs):
    passengerlist = []
    for i in range(0, kwargs['adults']):
        passengerlist.append({
            'PassengerID': 'ADT{0}'.format(i),
            'PTC': 'ADT'
        })
    for i in range(0, kwargs['children']):
        passengerlist.append({
            'PassengerID': 'ADT{0}'.format(i),
            'PTC': 'ADT'
        })
    for i in range(0, kwargs['infants']):
        passengerlist.append({
            'PassengerID': 'ADT{0}'.format(i),
            'PTC': 'ADT'
        })
    return passengerlist
