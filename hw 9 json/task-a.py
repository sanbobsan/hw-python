import json
import random

users = []
for _ in range(5):
    user = {}
    data = random.choice([""])
    user["username"] = random.choice(["joker", "creeper", "validator", "class"])
    user["name"] = random.choice(["bob", "mike", "max", "jake", "alex", "ivan"])
    user["surname"] = random.choice(["ivanov", "smith", "jason", "nikulin", "vasilyev", "lilith"])
    user["age"] = random.randint(18, 36)
    user["phone"] = f"+79{random.randint(100000000, 999999999)}"
    users.append(user)

print(json.dumps(users))