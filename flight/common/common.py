from flask import (jsonify)
import flight.utils.dbconnection as db


def generatejson(result):
    return jsonify(result)


def FetchAccount(email):
    query = """
    SELECT * FROM Flight.user_x_supplier  uxs 
    inner join Flight.user  us on uxs.user_id = us.id 
    inner join supplier s on uxs.supplier_id = s.id  
    where email = '{0}'
    """
    User = db.getdata(
        query.format(email))
    return User
