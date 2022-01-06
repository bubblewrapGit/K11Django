from django.db import models
import os
from django.conf import settings


class Board(models.Model):
    names = models.CharField(max_length=10)
    emails = models.EmailField(max_length=30)
    passwords = models.CharField(max_length=12)
    postdates = models.DateTimeField(auto_now_add=True)
    visitcounts = models.PositiveIntegerField(default = 0)
    titles = models.CharField(max_length=12)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.titles
    
    def delete(self, *args, **kargs):
        if self.mainphoto:
            print("이미지 삭제")
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
        super(Board, self).delete(*args, **kargs)

    