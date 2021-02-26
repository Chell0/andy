from django.db import models
# from django.urls import reverse

# class Article(models.Model):
# pass


class Art(models.Model):
    """
    model representing an art piece
    """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = ('id', 'slug'),

    def __str__(self):
        return self.name

 #   def get_absolute_url(self):
 #       return reverse('main.art_detail', args=[self.id, self.slug])
