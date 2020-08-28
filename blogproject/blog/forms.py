from django import forms


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=20)
    sender = forms.EmailField()
    to = forms.EmailField()
    message = forms.CharField(required=False, widget=forms.Textarea)
