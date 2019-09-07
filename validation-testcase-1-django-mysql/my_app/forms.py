from django import forms
from my_app.models import InfoModel


class InfoForm(forms.Form):
    fname = forms.CharField(max_length=50, required=False)
    salary = forms.IntegerField(min_value=1000, required=False)

    # def clean_fname(self):
    #     data = self.cleaned_data['fname']
    #
    #     if data != 'hello':
    #         raise forms.ValidationError("Please enter this fucking field!")

    # class Meta:
    #     model = InfoModel
    #     fields = ['f_name', 'salary']
