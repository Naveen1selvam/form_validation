from django import forms
def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('data is not valid')
def check_for_age(value):
    if value<18:
        raise forms.ValidationError('data is not valid')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a])
    age=forms.IntegerField(validators=[check_for_age])
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('invalid')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('invalid')
