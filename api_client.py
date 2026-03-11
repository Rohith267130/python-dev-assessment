import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url)

        # Check HTTP status code
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None

        # Parse JSON response
        users = response.json()

        # Ensure the response is a list
        if not isinstance(users, list):
            print("Error: Unexpected JSON structure.")
            return None

        # Print the first num_users users
        for user in users[:num_users]:
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]

                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"City: {city}")
                print("-" * 30)

            except KeyError:
                print("Error: Missing expected data in user record.")
                return None

    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
        return None


# Example calls
fetch_and_display_users(3)
print("\nFetching more users:\n")
fetch_and_display_users(5)