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


# PUT request to update a post


def update_post(post_id):# https://jsonplaceholder.typicode.com/posts/1, Post Object
    response = requests.put(BASE + 'posts/' + str(post_id), {
    'title': 'Hello World',
    'body': 'This is an updated post'
    })
    if response.status_code == 200:
        print(response.status_code)
        return response.json()
    else:
        print(f'failed to update post: {response.status_code}')
        return None

# DELETE Request to delete a post


def delete_post(post_id):
    response = requests.delete(BASE + 'posts/' + str(post_id))
    if response.status_code == 200:
        print(response.status_code)
        return response.json()
    else:
        print(f'failed to delete post: {response.status_code}')
        return None


# Generate a menu driven program to test the above functions until the user decides to quit
user_input = 0
while user_input != 5:
    print('1. Get all posts')
    print('2. Create a new post')
    print('3. Update a post')

    print('4. Delete a post')
    print('5. Quit')
user_input = int(input('Enter your choice: '))
if user_input == 1:
    print(get_posts())
elif user_input == 2:
    print(create_post())
elif user_input == 3:
    post_id = int(input('Enter the post id to update: '))
    print(update_post(post_id))
elif user_input == 4:
    post_id = int(input('Enter the post id to delete: '))
    print(delete_post(post_id))
elif user_input == 5:
    print('Quitting the program')
else:
    print('Invalid choice. Please try again')


