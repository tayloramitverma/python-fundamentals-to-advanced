import requests

# req = requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random")
# print(req.json())

def fetchUser():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res = requests.get(url)
    data = res.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data!")


def main():
    try:
        fetchUser()
    except Exception as e:
        print(str(e))
    
if __name__ == "__main__":
    main()