import pymongo
import certifi

client = pymongo.MongoClient("mongodb+srv://Logan:19941217@mycluster.g4ddrju.mongodb.net/?retryWrites=true&w=majority",
tlsCAFile=certifi.where())
db = client.login_data #選擇要操作的database
collecttion=db.member_data

result=collecttion.insert_one({
    'accountID':'test',
    'passwords':'test'
})

print('成功')