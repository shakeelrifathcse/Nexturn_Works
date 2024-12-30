import requests

# Base URL for the API
BASE = 'https://jsonplaceholder.typicode.com/'

# Get all posts from the API


def get_posts():
    response = requests.get(BASE + 'posts')
    if response.status_code == 200:
        return response.json()
    else:
        print(f'failed to retrieve posts: {response.status_code}')
        return None

# Create a new post:


def create_post():
    response = requests.post(BASE + 'posts', {
    'userId': 1,
    'title': 'Hello World',
    'body': 'This is a new post'
    })

    if response.status_code == 201:
        print(response.status_code)
        return response.json()
    else:
        print(f'failed to create post: {response.status_code}')
        return None


# result = get_posts()
# print(result)

result = create_post()
print(result)

