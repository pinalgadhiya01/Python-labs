import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self, post_id=None):
        if post_id:
            url = f"{self.BASE_URL}/posts/{post_id}"
        else:
            url = f"{self.BASE_URL}/posts"
        response = requests.get(url)
        return response.json()

    def create_post(self, title, body, user_id):
        url = f"{self.BASE_URL}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=payload)
        return response.json()


# -------- USING THE CLASS ----------
client = JSONPlaceholderClient()

print("All Posts:")
print(client.get_posts())

print("\nPost 1:")
print(client.get_posts(1))

print("\nCreating New Post:")
print(client.create_post("Hello", "This is a new post", 5))
