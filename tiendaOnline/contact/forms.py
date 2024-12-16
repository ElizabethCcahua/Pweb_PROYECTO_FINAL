from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='',required=True, widget=forms.TextInput(
        attrs = {
            'placeholder' : 'Your name',
            'id' : 'name',
        }
    ))
    email = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs = {
            'placeholder' : 'Your email',
            'id' : 'email',
        }
    ))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs = {
            'placeholder' : 'Your message',
            'id' : 'message',
            'class' : 'col-lg-12',
        }
    ))
    