class Comment:
    def __init__(self, p_username, p_text=0, p_likes=0 ):
        self.username = p_username
        self.text = p_text
        self.like = p_likes

comment1 = Comment(input("Имя пользователя: "))
print(comment1.username, comment1.text, comment1.like)
