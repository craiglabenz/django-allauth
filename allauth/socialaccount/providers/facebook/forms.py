from django import forms


class FacebookConnectForm(forms.Form):
    access_token = forms.CharField(required=True)
    expires_at = forms.DateTimeField(required=False)
