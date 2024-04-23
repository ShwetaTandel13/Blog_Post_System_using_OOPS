class post:
    def __init__(self,title,content,author,date):
        self.title=title 
        self.content=content
        self.author=author 
        self.date=date 
class blog:
    def __init__(self):
        self.posts=[]
    def addpost(self,post):
        self.posts.append(post)

    def displaypost(self):
        for post in self.posts:
            print('Author:',post.author)
            print('Date:',post.date)
            print('content:',post.content)
            print('Title:',post.title)
            print()


p=post('Python','operators','Pooja','12-2-2000')

b=blog()
b.addpost(p)
b.displaypost()
