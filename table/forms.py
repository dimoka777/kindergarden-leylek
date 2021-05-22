from django import forms
from .models import Queue, Group


class QueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ['child_name', 'child_gender',
                  'child_birthday', 'birth_certificate', 'custom_given_certificate',
                  'certificate_given_date', 'child_address', 'parent_name', 'parent_phone']


class GroupChangeForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ['choice_group']


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'group_year_from', 'group_year_to', 'about_text',
                  'group_reg', 'group_teachers', 'group_img', ]
