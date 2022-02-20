from rest_framework import serializers
from api.models import ToDoList
from datetime import date
from .models import ToDoList

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id','title','description','due_date','tags','status','created_at','user_id']
        #--------Time Stamp non Editable--------
        read_only_fields = ['created_at']
    def validate(self,data):
        #--------Due Date Check--------
        due = data.get('due_date')
        if due is None:
            pass
        elif due < date.today():
            raise serializers.ValidationError('Date Cannot be Before Today date')
        return data
    def create(self, validated_data):
        #--------Tags Duplicate Remover--------
        tags = validated_data.get('tags')
        tags = list(set(tags.split()))
        str1 = " "
        tags = str1.join(tags)
        validated_data['tags'] = tags
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)

        


