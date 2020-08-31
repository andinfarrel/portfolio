from django import forms

from .models import SkillItem, SkillsCategory, Experience

# class SkillForm(forms.Form):
#     skill = forms.CharField(label='skill', max_length=10)


class SkillForm(forms.ModelForm):
    category = forms.CharField(max_length=15)

    def save(self, commit=True):
        category_name = self.cleaned_data['category']
        category = SkillsCategory.objects.get_or_create(category=category_name)[0]
        self.instance.category = category

        return super(SkillForm, self).save(commit)

    class Meta:
        model = SkillItem
        fields = ('item_text',)


class ExperienceForm(forms.ModelForm):
    role = forms.CharField(max_length=50, required=True)
    company = forms.CharField(max_length=50, required=True)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)

    class Meta:
        model = Experience
        fields = ('role', 'company', 'start_date', 'end_date',)