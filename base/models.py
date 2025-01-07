from django.db import models

class Image(models.Model):
    IMAGE_TYPES = [
        ('bar', 'Bar'),
        ('cone', 'Cone'),
        ('sundae', 'Sundae'),
        ('cake', 'Cake'),
    ]

    image_url = models.CharField(max_length=255)
    image_type = models.CharField(max_length=10, choices=IMAGE_TYPES, default='bar')
    list = models.BooleanField(default=False)

    def __str__(self):
        return f'Image {self.id}'

