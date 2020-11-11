from django.db import models
# Create your models here.
class Cert(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	thumbnail = models.ImageField(null=True, blank=True, upload_to="images")

	def __str__(self):
		return self.headline
