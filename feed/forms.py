from django import forms


class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Title")

class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput)
    Email = forms.EmailField(required=True)
    Age = forms.DateTimeField(label='Date of Birth')
    Nationality = forms.CharField()
    Comments = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass