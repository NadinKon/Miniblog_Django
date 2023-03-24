from django.db import models

class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Text')
    author = models.CharField('Name', max_length=100)
    date = models.DateField('Date')
    img = models.ImageField('Img', upload_to='image/%Y')


    def __str__(self):
        return f'{self.title}, {self.author}'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=50)
    text_comments = models.TextField('Text', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'
