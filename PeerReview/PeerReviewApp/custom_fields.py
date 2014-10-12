from django.db import models
import json

class SeparatedValuesField(models.CharField):
	''' Serializer for python lists '''
	__metaclass__ = models.SubfieldBase
	
	def __init__(self, *args, **kwargs):
		self.token = kwargs.pop('token',',')
		super(SeparatedValuesField, self).__init__(*args, **kwargs)
	
	def to_python(self, value):
		if not value: return
		if isinstance(value, list):
			return value
		return value.split(self.token)
	
	def get_db_prep_value(self, value, *args, **kwargs):
		if not value: return
		assert(isinstance(value, list) or isinstance(value, tuple))
		return self.token.join([unicode(s) for s in value])
	
	def value_to_string(self, obj):
		value = self._get_val_from_obj(obj)
		return self.get_db_prep_value(value)