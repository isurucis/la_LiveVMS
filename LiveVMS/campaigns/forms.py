from django import forms
from .models import Campaign
from unfold.contrib.forms.widgets import WysiwygWidget

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'
        widgets = {
            'background': WysiwygWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set default value for 'background' if it's not provided
        if not self.instance.pk:  # Check if it's a new instance
            self.fields['background'].initial = "<b>BACKGROUND</b><ul><li>point one</li></ul> <b>EXPECTED KPIs</b><ul><li>point one</li></ul> <b>SEGMENTATION</b><ul><li>point one</li></ul> <b>MESSAGES</b><ul><li>point one</li></ul> <b>LOOK & FEEL</b><ul><li>point one</li></ul>"