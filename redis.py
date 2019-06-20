import redis

# create connection
client = redis.StrictRedis(host="localhost", port=6379)

# String operation
restaurant = "Extreme Pizza"
client.set(restaurant, "300 broadway,newe youk,NY")
client.append(restaurant, "10011")
address = client.get(restaurant)
print("address for " + restaurant + " is : " + address)

# list operations
listKey = "favorate_restaurants"
client.lpush(listKey, "PF chang's", "Olive Garden")
client.rpush(listKey, "outrback steakhouse", "red lobster")
favoriteRestaurants = client.lrange(listKey, 0, -1)
print("favorate:", favoriteRestaurants)
