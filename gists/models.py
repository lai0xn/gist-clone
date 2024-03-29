from django.db import models
from users.models import User

class Gist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users_gists')
    file = models.FileField(upload_to="gists")
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    stargazers = models.ManyToManyField(User)
    is_private = models.BooleanField(default=False)
class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    cotent = models.TextField()
    gist = models.ForeignKey(Gist,on_delete=models.CASCADE)


# Create your models here.
