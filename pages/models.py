from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
LAYOUT_CHOICES =(
    ("standard", "Standard"),
    ("stacked", "Stacked"),
    ("classic", "Classic")
)


def layout_validator(value):
    if value[0] != "#":
        raise ValidationError("must start wth #")
    if len(value) == 4 or len(value) == 7:
        return value
    raise ValidationError("Incorrect length ")


class Page(models.Model):
    title                     = models.CharField(max_length=300)
    small_heading             = models.CharField(max_length=300,blank=True, null=True,help_text="h2 in the manin page ")
    head_description          = models.TextField(blank=True, null=True, help_text="flexple to add html code or just text ")
    head_bttn                 = models.CharField(max_length=50, blank=True, null=True)
    head_bttn_url             = models.URLField(blank=True, null=True)
    page_content              = models.TextField(blank=True, null=True, help_text="flexple to add html code or just text ")
    show_nav                  = models.BooleanField(default=True)
    nav_color                 = models.CharField(max_length=7, default='transparent',blank=True, null=True, validators=[layout_validator])
    layout                    = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default='standard')
    video_embed               = models.TextField(null=True, blank=True, help_text="add the embaed code ")
    image_bg                  = models.URLField(null=True, blank=True, help_text="uplade back grond to the first part of the page ")
    slug                      =models.SlugField(default="page-slug", blank=True)
    featured                  =models.BooleanField(default=False)
    active                    =models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if self.featured:
            qs = Page.objects.filter(featured=True).exclude(pk=self.pk)
            if qs.exists():
                qs.update(featured=False)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


def prw_save_receiver_page_model(sender,instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == '':
        instance.slug = unique_slug_generator(instance)
pre_save.connect(prw_save_receiver_page_model, sender=Page)