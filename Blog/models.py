from django.db import models

# Create your models here.
class PostModel (models.Model):

    PostImage=models.ImageField(upload_to= "postimage/",null=True)
    PostTitle=models.CharField(max_length=70)
    PostDescrption=models.CharField(max_length=400)
    def __str__(self):
        return self.PostTitle


class SingelPostModel (models.Model):
    Post = models.ForeignKey(PostModel , on_delete=models.CASCADE)
    def __str__(self):
        return self.PostTitle