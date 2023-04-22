# core/user/serializers.py

# DRF modules
from rest_framework import serializers

# Locals
from core.user.models import User  

# Model: UserSerializer
class UserSerializer(serializers,ModelSerializer):
	id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
	created = serializers.DateTimeField(read_only=True)
	updated = serializers.DateTimeField(read_only=True)

	class Meta:
		model = User
		fields = [
			'id', 'username', 'first_name', 
			'last_name', 'bio', 'avatar', 'email',
			'is_active', 'created', 'updated'
		]
		read_only_field = ['is_active']

"""
The UserSerializer class inherits from the serializers.ModelSerialzer class. It’s a class 
inheriting from the serializers.Serializer class but has deep integrations for supporting 
a model. It’ll automatically match the field of the model to have the correct validations for each one.
For example, we’ve stated that the email is unique. Then, every time someone registers and enters an 
email address that already exists in the database, they will receive an error message concerning this.
The fields attribute contains all the fields that can be read or written. Then, we also have the 
read_only fields. These fields are only readable. This means that they can’t be modified and 
it’s definitely better like that. Why give the external user the possibility to modify the created, 
updated, or id fields?
"""