from pymongo import MongoClient

## client 연결 및 생성
client = MongoClient('localhost', 27017)

## database 생성
# db = client['clien']

## collection 생성
# collection = db['tesla']

## documents 삽입
def insert_item_one(mongo, data, db_name=None, collection_name=None):
  result = mongo[db_name][collection_name].insert_one(data).inserted_id
  return result

# def insert_item_many(mongo, datas, db_name=None, collection_name=None):
#   result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
#   return result

def insert_item_many(datas, db_name=None, collection_name=None):
  result = client[db_name][collection_name].insert_many(datas).inserted_ids
  return result

