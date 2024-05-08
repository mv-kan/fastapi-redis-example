import redis 

r = redis.Redis(host='localhost', port=16379, db=0)

mykey = "mykey"
r.set(mykey, "VALUE_OF_MY_KEY")

status = r.get(mykey)
print(f"mykey: {status.decode()}")  # 'active'

tmpq = "tmpq"
myq = "myq"
while True:
    l = r.blpop([myq])
    value = l[1].decode()
    r.lpush(tmpq, value)

    # do some work
    print(value)

    # remove from tmp queue
    r.lrem(tmpq, 1, value)

    
