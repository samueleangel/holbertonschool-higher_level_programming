#!/usr/bin/python3
"""
Script that fetches posts from JSONPlaceholder API.
It prints the titles of the posts and also saves them into a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print their titles.
    Also prints the HTTP response status code.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder and save selected fields
    (id, title, body) to a CSV file named 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data_to_write = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]
        with open('posts.csv', mode='w', newline='', encoding='utf-8')
        as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_write)
    else:
        print("Failed to fetch posts.")


# Only execute the following when the script is run directly
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
