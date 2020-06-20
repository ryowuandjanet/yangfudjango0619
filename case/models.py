from django.db import models
from django.urls import reverse

class Country(models.Model):
	name = models.CharField(verbose_name="縣市", max_length=50)
	
	def __str__(self):
		return self.name

class Township(models.Model):
	name = models.CharField(verbose_name="鄉鎮區", max_length=50)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="縣市")
	
	def __str__(self):
		return self.name
		
class Case(models.Model):
	case_number = models.CharField(u'案號',max_length=100)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name="縣市")
	township = models.ForeignKey(Township, on_delete=models.SET_NULL, null=True, verbose_name="鄉鎮區")
	big_section = models.CharField(u'段號',max_length=100,blank=True,null=True)
	small_section = models.CharField(u'小段',max_length=100,blank=True,null=True)
	other_address = models.CharField(u'住址',max_length=100,blank=True,null=True)

	def __str__(self):
		return self.case_number

	def get_absolute_url(self):
		return reverse("case_detail",args={str(self.id)})