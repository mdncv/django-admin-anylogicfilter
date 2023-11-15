from django.contrib import admin
from django import forms


class AnyLogicFilter(admin.FieldListFilter):
    template = 'anylogicfilter/filter.html'

    # Populate form_fields list in the inherited class with field_name-field tuples.
    # (Like this: [(field_name, forms.AnyTypeOfField(**some_form_params)), ...])
    form_fields = []

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.form = self.prepare_form(request)

    def expected_parameters(self):
        return [field[0] for field in self.form_fields]

    def _prepare_form_class(self):
        return type(str('AnyLogicFilter'), (forms.Form,), dict(self.form_fields))

    def prepare_form(self, _):
        return self._prepare_form_class()(self.used_parameters or None)

    def choices(self, _):
        # no predefined choices
        return []

    def queryset(self, request, queryset):
        """
        Implement your own queryset function or suffer the consequences!
        (Don't forget to set form_fields)!
        This might help you:

        if self.form.is_valid():
            filter_params = {
                p: self.form.cleaned_data.get(p)
                for p in self.expected_parameters()
                if self.form.cleaned_data.get(p) is not None
            }
            return queryset.filter(**filter_params)
        else:
            return queryset
        """
        raise NotImplementedError('Told ya!')
