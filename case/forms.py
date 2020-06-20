from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import *

COUNTRY_LIST= [
	('新北市', '新北市'),
	('台北市', '台北市'),
	('台中市', '台中市'),
	('台南市', '台南市'),
	('高雄市', '高雄市'),
	('屏東縣', '屏東縣')
]

class CaseForm(forms.ModelForm):
	country = forms.ChoiceField(label='縣市',choices=COUNTRY_LIST)
	class Meta:
		model= Case
		fields='__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'case_number',
			Row(
				Column('country', css_class='form-group col-md-2 mb-0'),
				Column('township', css_class='form-group col-md-2 mb-0'),
				Column('big_section', css_class='form-group col-md-2 mb-0'),
				Column('small_section', css_class='form-group col-md-2 mb-0'),
				Column('other_address', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Submit('submit', '新增', css_class='form-group col-md-2 mb-0')
		)