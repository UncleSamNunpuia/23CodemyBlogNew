from django.db import models

# Create your models here.
from django.utils.text import capfirst
# added to import user as a foregn key
from django.contrib.auth.models import User
# to validate integer fields these are req
from django.core.validators import MinValueValidator, MaxValueValidator


class InkhawmInchhiarnaBlogNew(models.Model):
    inkhawm_ni = models.DateField()
    mat_grp_cmt = models.IntegerField(null=False, blank=False,
                                      default=0, validators=[MinValueValidator(0), MaxValueValidator(25)])
    mat_members = models.IntegerField(null=False, blank=False,
                                      default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    marka_grp_cmt = models.IntegerField(null=False, blank=False,
                                        default=0, validators=[MinValueValidator(0), MaxValueValidator(25)])
    marka_members = models.IntegerField(null=False, blank=False,
                                        default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    luka_grp_cmt = models.IntegerField(null=False, blank=False,
                                       default=0, validators=[MinValueValidator(0), MaxValueValidator(25)])
    luka_members = models.IntegerField(null=False, blank=False,
                                       default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    johan_grp_cmt = models.IntegerField(null=False, blank=False,
                                        default=0, validators=[MinValueValidator(0), MaxValueValidator(25)])
    johan_members = models.IntegerField(null=False, blank=False,
                                        default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    leader_secy = models.IntegerField(null=False, blank=False,
                                      default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    chhimtu1 = models.CharField(null=True, blank=True, max_length=25)
    chhimtu1_no = models.IntegerField(null=True, blank=True,
                                      default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    chhimtu2 = models.CharField(null=True, blank=True, max_length=25)
    chhimtu2_no = models.IntegerField(null=True, blank=True,
                                      default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    chhimtu3 = models.CharField(null=True, blank=True, max_length=25)
    chhimtu3_no = models.IntegerField(null=True, blank=True,
                                      default=0, validators=[MinValueValidator(0), MaxValueValidator(50)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True, default=0)

    def save(self, *args, **kwargs):
        self.total = self.mat_grp_cmt + self.mat_grp_cmt + self.marka_grp_cmt + self.marka_members + \
            self.luka_grp_cmt + self.luka_members + self.johan_grp_cmt + \
            self.johan_members + self.chhimtu1_no + self.chhimtu2_no + self.chhimtu3_no
        super().save(*args, **kwargs)

    # added function to capitaise each name first letter
    # then saved the date before it is pushed to db

    def save(self, *args, **kwargs):
        self.chhimtu1 = capfirst(self.chhimtu1)
        self.chhimtu2 = capfirst(self.chhimtu2)
        self.chhimtu3 = capfirst(self.chhimtu3)
        super().save(*args, **kwargs)

    # this is added to prevent django prefixing the table name with the app name in db
    class Meta:
        db_table = "InkhawmInchhiarnaBlogNew"

    # this is what will appear in admin area of django as well as
    # the html pages (if we do not specify what to appear)
    def __str__(self):
        return "Inkhawm Ni: "+str(self.inkhawm_ni)+" | Inkhawm zawng zawng belhkhawm: "+str(self.total)+" | update hnuhnung ber: "+str(self.updated_at)
