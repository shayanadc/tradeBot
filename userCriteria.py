import pymongo
import setting
myclient = pymongo.MongoClient(setting.MONGOPORT)
mydb = myclient["users"]


def getColBy(symbol):
    symbol = str(symbol).upper()
    mycol = mydb[symbol]

    return mycol

def userExist(name,symbol):
    mycol = getColBy(symbol)
    myquery = {"name": name}
    return mycol.find_one(myquery)

def storeUser(name, symbol, low, high):
    if userExist(name,symbol): deleteKey(symbol,name)

    mycol = getColBy(symbol)


    user = {'name': name, 'symbol': str(symbol).upper(), 'low': low, 'high': high}

    mycol.insert_one(user)


def getAll(symbol):

    mycol = getColBy(symbol)


    myquery = {"symbol": str(symbol).upper()}
    mydoc = mycol.find(myquery)
    new = []
    for i in mydoc:
        new.append(i)
    return new

def deleteKey(symbol,name):

    mycol = getColBy(symbol)


    myquery = {"name": name}

    mycol.delete_many(myquery)

def dropCol(symbol = None):
    if symbol is None:
        allC = mydb.list_collection_names()
        for item in allC:
            dropCol(item)
    mycol = getColBy(symbol)
    mycol.drop()