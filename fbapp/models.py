from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse





# Create your models here.

class a(User):
    gender=models.CharField(max_length=1)
    birth=models.DateTimeField()




class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="pics",default="pics/defaultmale.jpg")




class PhotoPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="pics")
    caption=models.CharField(max_length=50,default="")

    @property
    def comments(self):
        a=Comment.objects.filter(post_connected=self)
        for i in range(len(a)):
           return Comment.objects.filter(post_connected=self)

    def get_absolute_url(self):
        return reverse("post-detail",kwargs={"pk":self.pk})

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300,null=True)
    post_connected = models.ForeignKey(PhotoPost,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.comment)











