from django.db import models

STATUS = [
    ('draft','draft'),
    ('published','published'),
    ('deleted','deleted'),
]
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="")
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to="page",
        null=True,
    )
    status = models.CharField(
        default="draft",
        choices=STATUS,
        max_length=11,
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class carousel(models.Model):
      title =models.CharField(max_length=200 ,
                        blank=True,
                        null=True
                        )
      cover_image =models.ImageField(
    upload_to="carousel",
    null=True,
    blank=True
)
      status = models.CharField(
    default="draft",
    choices=STATUS,
    max_length=11,
)
created_at = models.DateTimeField(auto_now=True)
updated_at = models.DateTimeField(auto_now=True)


