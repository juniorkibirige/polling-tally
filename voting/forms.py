from django import forms


class PollingStationDataUploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select Polling Station File to Upload'
            }))


class PollingCandidateDataUploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Select Candidates File to Upload'
            }))
