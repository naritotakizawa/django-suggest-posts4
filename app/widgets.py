from django import forms


class SuggestWidget(forms.TextInput):
    template_name = 'app/widgets/suggest.html'

    class Media:
        js = ['app/js/suggest.js']
        css = {
            'all': ['app/css/suggest.css']
        }

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if 'class' in self.attrs:
            self.attrs['class'] += ' suggest'
        else:
            self.attrs['class'] = 'suggest'
