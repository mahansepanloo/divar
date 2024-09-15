from rest_framework import serializers


class UserRelationalField(serializers.RelatedField):
	def to_representation(self, value):
		return f'{value.username}'

