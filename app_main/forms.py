import datetime
from datetime import timedelta
from django import forms

from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['amount', 'until', 'reason']
        labels = {
            'amount': '*Miqdor',
            'until': '*Qaysi sanagacha',
            'reason': 'Qarz olishdan sabab'
        }
        widgets = {
            'until': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'min': datetime.datetime.today().date(),
                'value': datetime.datetime.today().date() + timedelta(days=7)
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })
