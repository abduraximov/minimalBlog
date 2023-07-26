from django.db import models
from apps.common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(BaseModel):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(BaseModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(BaseModel):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Video(BaseModel):
    name = models.CharField(max_length=32)
    video = models.FileField(upload_to="post_videos/", null=True, blank=True)

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.CharField(max_length=256)
    photo = models.ImageField(upload_to="post_images/", blank=True, null=True)
    content = RichTextField(null=True, blank=True)
    author = models.ForeignKey("post.Author",
                               on_delete=models.CASCADE,
                               related_name="posts",
                               verbose_name=_("Author"))
    category = models.ForeignKey("post.Category",
                                 on_delete=models.CASCADE,
                                 related_name="posts",
                                 verbose_name=_("Category"))
    tags = models.ManyToManyField("post.Tag",
                                  related_name="posts",
                                  verbose_name=_("Tags")
                                  )
    video = models.ForeignKey("post.Video",
                              on_delete=models.CASCADE,
                              related_name="post",
                              verbose_name=_("Video"),
                              null=True,
                              blank=True)
    is_popular = models.BooleanField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class ViewPost(BaseModel):
    post = models.ForeignKey("post.Post",
                             on_delete=models.CASCADE,
                             related_name="viewpost",
                             verbose_name=_("Post"))
    device = models.CharField(max_length=255)

    def __str__(self):
        return self.post

    class Meta:
        unique_together = ("post", "device")


class Comment(BaseModel):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="comment",
                             verbose_name=_("Comment"),
                             null=True,
                             blank=True
                             )
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.CharField(max_length=1024)
