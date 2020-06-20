from django.db import models
from django.urls import reverse

class Case(models.Model):
	case_number = models.CharField(u'案號',max_length=100)
	country = models.CharField(max_length=100,blank=True,null=True)
	township = models.CharField(u'鄉鎮區',max_length=100,blank=True,null=True)
	big_section = models.CharField(u'段號',max_length=100,blank=True,null=True)
	small_section = models.CharField(u'小段',max_length=100,blank=True,null=True)
	other_address = models.CharField(u'住址',max_length=100,blank=True,null=True)

	def __str__(self):
		return self.case_number

	def get_absolute_url(self):
		return reverse("case_detail",args={str(self.id)})