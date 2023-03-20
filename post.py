class Post:
    def __init__(self, user_id, post_id, title, body):
        self.userId = user_id
        self.post_id = post_id
        self.title = title
        self.body = body

    def test_func(self):
        return f"{self.userId} {self.post_id} {self.title} {self.body}"
