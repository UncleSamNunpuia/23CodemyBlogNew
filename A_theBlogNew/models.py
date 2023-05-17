from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import capfirst
from django.db import models
# added
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # post_content = RichTextField(blank=True, null=True')
    # config_name tih hian settings.py ah CKEDIROT bik kan customise na name a kawk
    post_content = RichTextField(
        blank=True, null=True, config_name='sam_custom')
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    # added below for up of image
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    # this is what will appear in admin area of django
    def __str__(self):
        return "Title: "+self.post_title+" | Author: "+str(self.author)

    # This is the redirection on submission of post button
    def get_absolute_url(self):
        # this directs it to the just added blog post content
        # return reverse('blog_article', args=(str(self.id)))
        # this redirects it to blog home page
        return reverse('blog_homePage')

# for image ul and fetech
# class MyModel(models.Model):
#     my_file = models.FileField(upload_to='uploads/')
#     my_image = models.ImageField(upload_to='uploads/')


# Create your models here.
# added to import user as a foregn key
# to validate integer fields these are req


# class InkhawmInchhiarnaBlogNew(models.Model):
#     inkhawm_ni = models.DateField()
#     mat_grp_cmt = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
#     mat_grp_cmt = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
#     marka_grp_cmt = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
#     marka_members = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
#     luka_grp_cmt = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
#     luka_members = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
#     johan_grp_cmt = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(24)])
#     johan_members = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
#     leader_secy = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
#     chhimtu1 = models.CharField(null=True, blank=True, max_length=25)
#     chhimtu1_no = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
#     chhimtu2 = models.CharField(null=True, blank=True, max_length=25)
#     chhimtu2_no = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
#     chhimtu3 = models.CharField(null=True, blank=True, max_length=25)
#     chhimtu3_no = models.IntegerField(
#         default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

#     total = models.IntegerField(default=0)

#     def save(self, *args, **kwargs):
#         self.total = self.mat_grp_cmt + self.mat_grp_cmt + self.marka_grp_cmt + self.marka_members + \
#             self.luka_grp_cmt + self.luka_members + self.johan_grp_cmt + \
#             self.johan_members + self.chhimtu1_no + self.chhimtu2_no + self.chhimtu3_no
#         super().save(*args, **kwargs)

#     # added function to capitaise each name first letter
#     # then saved the date before it is pushed to db

#     def save(self, *args, **kwargs):
#         self.chhimtu1 = capfirst(self.chhimtu1)
#         self.chhimtu2 = capfirst(self.chhimtu2)
#         self.chhimtu3 = capfirst(self.chhimtu3)
#         super().save(*args, **kwargs)

#     # this is added to prevent django prefixing the table name with the app name in db
#     class Meta:
#         db_table = "InkhawmInchhiarnaBlogNew"

#     # this is what will appear in admin area of django as well as
#     # the html pages (if we do not specify what to appear)
#     def __str__(self):
#         return "Inkhawm Ni: "+self.inkhawm_ni+" | Inkhawm zawng zawng belhkhawm: "+str(self.total)+" | update hnuhnung ber: "+str(self.updated_at)
