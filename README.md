# django-admin-anylogicfilter
Django app that adds admin filter with any functionality you need.
## Requirements
App tested with
* Python 3.11
* Django 4
## Installation
```Bash
pip install django-admin-anylogicfilter
```
## Quick start
1. Add anylogicfilter to INSTALLED_APPS:
```Python
INSTALLED_APPS = [
    ...
    'anylogicfilter',
    ...
]
```
2. Declare your filter class by inheriting from ```AnyLogicFilter``` class:
```Python
from django import forms
from anylogicfilter.filter import AnyLogicFilter


class MyFilter(AnyLogicFilter):
    filter_title = 'Abracadabra'
    
    filter_fields = [
        ('field_name', forms.CharField(max_length=100, required=True, initial='')),
        ('other_field_name', forms.BooleanField(label='Not default by-name label', required=False, initial='')),
    ]

    def queryset(self, request, queryset):
        if self.form.is_valid():
            filter_params = {
                p: self.form.cleaned_data.get(p)
                for p in self.expected_parameters()
                if self.form.cleaned_data.get(p) is not None
            }
            # some query, using subquery with 2+ parameters or anything else you need
            return queryset.filter(...filter_params['field_name']...filter_params['other_field_name']...)
        else:
            return queryset
```
3. Add it to ```admin.py```:
```Python
@admin.register(YourModel)
class YourModelAdmin(admin.ModelAdmin):
    list_filter = [
        ...
        ('name_of_any_field_from_or_related_to_your_model', MyFilter),
        ...
    ]
```
4. Enjoy!
## Maintainers
* [Maxim Medentsev](https://github.com/mdncv)
* [Ivan Golyshev](https://github.com/Nomer77)
## Contributing
Bug reports and/or pull requests are welcome :)
## License
[MIT License](LICENSE)