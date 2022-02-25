from django import forms


class ContactForm(forms.Form):
    """
    Class for the form used on Contact Us page
    """
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs['rows'] = 4
