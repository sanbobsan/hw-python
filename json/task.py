import json
import random


def input_user() -> dict:
    """# No validation 0_0"""
    print("---User-creating---")
    user = {}
    for value in ["username", "name", "surname", "age", "phone"]:
        user[value] = input(f"Enter {value}\n>> ")
    print("-------------------")
    return user


def create_random_users(num_of_users: int) -> list:
    users = []
    for _ in range(num_of_users):
        user = {}
        user["username"] = random.choice(["joker", "creeper", "validator", "class", "python", "chatgpt", "assasin", "restapi", "graphql", "sql"])
        user["name"] = random.choice(["bob", "mike", "max", "jake", "alex", "ivan", "andrew", "john", "liza", "polina", "vadim", "makar"])
        user["surname"] = random.choice(["ivanov", "smith", "jason", "nikulin", "vasilyev", "lilith", "apple", "stoner", "guchi", "lampochkin"])
        user["age"] = random.randint(18, 52)
        user["phone"] = f"+79{random.randint(10**6, 10**7 - 1)}"
        users.append(user)
    return users


def dumps_json_to_file(data, file_name: str = "data.json") -> None:
    with open(file_name, "w") as f:
        f.write(json.dumps(data, indent=4))


def loads_json_from_file(file_name: str = "data.json") -> list[dict]:
    with open(file_name, "r") as f:
        return json.loads(f.read())


def main():
    users = create_random_users(10)
    users.append(input_user())
    dumps_json_to_file(users)
    data = loads_json_from_file()
    print(*[key.ljust(10) for key in (data[1]).keys()])
    print(*[" ".join([str(value).ljust(10) for value in user.values()]) for user in data], sep="\n")


if __name__ == "__main__":
    main()