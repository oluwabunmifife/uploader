from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# def user_directory_path(instance, filename):
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


# Create your models here.
class Images(models.Model):
    # height = models.PositiveIntegerField()
    # width=models.PositiveIntegerField()

    file=models.ImageField()#From stackoverflow
    #height_field='height', width_field = 'width
    # file = models.ImageField(#upload_to=user_directory_path,
    # width_field=100, height_field=100, blank=True, null=True)
    name = models.CharField(max_length=30)
    description = models.TextField(help_text="Give a short description of the image", max_length=100)


    def __str__(self):
        return self.name

    @property #for returning images....
    def get_img_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
        else:
            return ''