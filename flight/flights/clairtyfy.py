import flight.utils.index as db
import json

def search():
        print('____________')
        redis = db['redis']()
        my_json = json.loads(redis.get('flight-api:lucky:supplier:user:35'))
        return 'Wellcome to {0}'.format(my_json[0]['name'])