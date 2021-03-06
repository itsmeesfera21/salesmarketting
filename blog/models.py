from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your models here.

class Category(models.Model):
	name= models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    category = models.ForeignKey('blog.Category' ,on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def save(self):
        super(Post, self).save()
        #date = datetime.date.today()
        self.slug = '%s'%(slugify(self.title))
        super(Post, self).save()

