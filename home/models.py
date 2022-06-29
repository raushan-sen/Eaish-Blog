from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Categery(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(null=True,unique=True,default=None,blank=True)
    

    class Meta:
        ordering = ['-pk']


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})

class Blog(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=True,unique=True,default=None,blank=True)
    thumbnail=models.ImageField(upload_to='static/images', null=True, blank=True,default='/static/images/default.jpg')
    categery=models.ManyToManyField(Categery)
    content=models.TextField()
    meta_decs=models.TextField(null=True,default=None,blank=True)
    keywords=models.TextField(null=True,default=None,blank=True)
    added_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    view=models.IntegerField(default=0)
    
    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return '#'

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:blog", kwargs={"pk": self.slug})

class Page(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(null=True,unique=True,default=None,blank=True)
    thumbnail=models.ImageField(upload_to='static/images', null=True, blank=True, default='/static/images/default.jpg')

    content=models.TextField()
    meta_decs=models.TextField(null=True,default=None,blank=True)
    keywords=models.TextField(null=True,default=None,blank=True)
    added_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    view=models.IntegerField(default=0)

    
    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return '#'

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("app:page", kwargs={"pk": self.page})
    
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.s = slugify(self.title)

        super(Page, self).save(*args, **kwargs)

class Comment(models.Model):
    slug=models.SlugField(null=True,default=None,blank=True)
    name=models.CharField(max_length=100)
    comment=models.TextField()
    date=models.DateField()


    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f"{self.name} : {self.date}" 

class Seo_Setup(models.Model):
    SiteName=models.CharField(max_length=50,default='Hello World')
    SiteDecs=models.TextField(default=None)
    SiteMetaDecs=models.TextField(default=None)
    Favicon=models.ImageField(upload_to='static/favicon',default='/static/favicon/default.jpg')
    SiteKeywords=models.TextField(default=None)
    MainMenu=models.ManyToManyField(Categery)


    def __str__(self):
        return self.SiteName

class Images(models.Model):
    image=models.ImageField(upload_to='static/uploads')

    def __str__(self):
        return self.image

