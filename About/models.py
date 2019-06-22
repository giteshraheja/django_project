from django.db import models


from django.contrib.auth import models as auth_
models

class Banner(models.Model):
    Title = models.CharField(max_length= 150)
    Created = models.DateTimeField(auto_now_add=True)
    Image = models.ImageField(default='default.png', upload_to='Banner_image')

    def __str__(self):
        return self.Title + '--' + self.Created.strftime('%d-%m-%y')

class aboutus(models.Model):
    heading = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.heading + '--' + self.create.strftime("%d-%m-%y")

class questions(models.Model):
    question = models.CharField(max_length=200)
    Create = models.DateTimeField(auto_now_add=True)
    answer = models.TextField()

    def __str__(self):
        return self.question + '--' + self.Create.strftime("%d-%m-%y")



