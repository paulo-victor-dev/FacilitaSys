from django import forms
from django_flatpickr.widgets import DatePickerInput


class DatePeriodForm(forms.Form):
    start_date = forms.DateField(
        widget=DatePickerInput(
            attrs={"class": "start_date"}),
            input_formats=["%Y-%m-%d"]
    )

    end_date = forms.DateField(
        widget=DatePickerInput(
            attrs={"class": "end_date"}, range_from="start_date"),
            input_formats=["%Y-%m-%d"]
    )

