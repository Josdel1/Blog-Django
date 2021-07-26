from django import forms

class RegisterForm(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput())
    username = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput())
    
    class Meta:
        fields = ('username', 'email', 'password', 'password2' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})