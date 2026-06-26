import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Send GET request
    response = requests.get(url)

    # Check status
    response.raise_for_status()

    # Convert JSON into Python object
    users = response.json()

    print("="*60)
    print("USER DETAILS")
    print("="*60)

    # Display all users
    for user in users:
        print(f"Name     : {user['name']}")
        print(f"Username : {user['username']}")
        print(f"Email    : {user['email']}")
        print(f"City     : {user['address']['city']}")
        print("-"*50)

    # Search Example
    search = input("\nEnter city name to search users: ")

    print("\nUsers Found:\n")

    found = False

    for user in users:
        if user['address']['city'].lower() == search.lower():
            print(f"{user['name']} ({user['email']})")
            found = True

    if not found:
        print("No users found.")

except requests.exceptions.HTTPError:
    print("HTTP Error occurred.")

except requests.exceptions.ConnectionError:
    print("Connection Error.")

except requests.exceptions.Timeout:
    print("Request Timed Out.")

except requests.exceptions.RequestException as e:
    print("Error:", e)
