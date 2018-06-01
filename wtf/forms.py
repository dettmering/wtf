from django import forms

class AddWTFForm(forms.Form):
    wtf_content = forms.CharField(widget=forms.Textarea, label='WTF?', max_length=500)
