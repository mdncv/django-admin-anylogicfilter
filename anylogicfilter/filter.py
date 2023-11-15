from django.contrib import admin
from django import forms


class AnyLogicFilter(admin.FieldListFilter):
    template = 'anylogicfilter/filter.html'
    field_names = []

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwargs = field_path
        super().__init__(field, request, params, model, model_admin, field_path)
        self.form = self.prepare_form(request)

    def expected_parameters(self):
        return self.field_names

    def _prepare_form_fields(self):
        return (
            (name, forms.CharField(max_length=100, required=False, initial=''))
            for name in self.field_names
        )

    def _prepare_form_class(self):
        fields = self._prepare_form_fields()
        form_class = type(str('AnyLogicFilter'), (forms.Form,), dict(fields))
        return form_class

    def prepare_form(self, _request):
        form_class = self._prepare_form_class()
        return form_class(self.used_parameters or None)

    # no predefined choices
    def choices(self, cl):
        return []

    def queryset(self, request, queryset):
        """
        Make your own queryset function or fear the consequences!
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
        raise NotImplementedError(
            'Told ya!'
        )
