from django import forms
from my_app.models import InfoModel


class InfoForm(forms.Form):
    fname = forms.CharField(max_length=50, required=False)
    salary = forms.IntegerField(min_value=1000, required=False)

    def clean_fname(self, *args, **kwargs):
        fname = self.cleaned_data['fname']
        if not fname:
            raise forms.ValidationError("Please Enter your Name!")
        else:
            return fname

    def clean_salary(self, *args, **kwargs):
        salary = self.cleaned_data['salary']
        if not salary:
            raise forms.ValidationError("Please Enter Your Salary!")
        else:
            return salary

    # class Meta:
    #     model = InfoModel
    #     fields = ['fname', 'salary']
