from django.db import models
from django.contrib.auth.models import Permission, User

class Post(models.Model):
    RATING = (
        ('L', 'Lame'),
        ('G', 'Good'),
        ('A', 'Awesome'),
    )
    pub_date    =   models.DateField()
    post_title  =   models.CharField(max_length=300)
    post_image  =   models.FileField()
    post_rating =   models.CharField(max_length=1,choices=RATING)

    def __str__(self):
        return self.post_title
