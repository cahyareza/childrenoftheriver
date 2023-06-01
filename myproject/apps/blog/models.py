from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from myproject.apps.core.mixins import CreationModificationDateBase, UrlBase
from django.utils.text import slugify

class Category(CreationModificationDateBase, UrlBase):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=200, blank=True, help_text="Generate otomatis jika dikosongkan")

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Post(CreationModificationDateBase, UrlBase):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    category = models.ForeignKey(Category, related_name = 'post', on_delete = models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, blank=False, null=False, default='admin', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, blank=True, help_text="Generate otomatis jika dikosongkan")
    body = RichTextUploadingField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image).convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

    # ========== SAVE FUNCTION ========== !
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)