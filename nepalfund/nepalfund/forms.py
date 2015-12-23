import csv
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import CharField, BooleanField
from fundraising.models import *

class UploadForm(forms.Form):
    table = [('gofundme', 'Go Fund Me')]
    # table = []

    t = Table.objects.all()
    for row in t:
        name = row.table
        value = name.replace(' ', '-').lower().strip()
        tup = (value, name)
        table.append(tup)

    tables = forms.ChoiceField(choices=table)
    file = forms.FileField()


class DownloadForm(forms.Form):
    # table = [('gofundme', 'Go Fund Me')]
    table = []

    t = Table.objects.all()
    for row in t:
        name = row.table
        value = name.replace(' ', '-').lower().strip()
        tup = (value, name)
        table.append(tup)

    tables = forms.ChoiceField(choices=table)


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['first_name', 'last_name', 'organization_name', 
            'email']
        # fields = ['first_name', 'last_name', 'organization_name', 
        #     'email', 'phone', 'description', 'crowdfunding', 'goal', 
        #     'campaign_time', 'goal_reached', 'raised', 'used_ngo', 'ngo', 
        #     'ngo_fee', 'ngo_cost', 'used_ingo', 'ingo', 'ingo_fee', 
        #     'ingo_cost', 'visited', 'visited_area', 'worked_with_team', 
        #     'distributed_materials', 'type_of_work', 'time_on_site', 
        #     'staying_location',  'visit_expense', 'how_support']

        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'name': _('Name of Organization'),
            'email': _('Contact Email Address'),
            # 'phone': _('Contact Telephone Number'),
            # 'description': _('Briefly describe your NGO'),

            # 'crowdfunding': _('What crowdfunding site did you use?'),

            # 'goal': _('What was your goal/target amount? ($USD)'),
            # 'campaign_time': _('How long did you run the campaign?'),
            # 'goal_reached': _('Did you reach this goal?'),
            # 'raised': _('If you did not reach goal how much did you raise?'),

            # 'used_ngo': _('Did you raise funds for a disaster relief using an NGO?'),
            # 'ngo': _('If yes, please state the NGO'),
            # 'ngo_fee': _('What percentage of fees was paid to NGO?'),
            # 'ngo_cost': _('What was the overhead cost of using NGO?'),

            # 'used_ingo': _('Did you raise funds for INGO?'),
            # 'ingo': _('If yes, Please state the INGO'),
            # 'ingo_fee': _('What percentage of fees was paid to INGO?'),
            # 'ingo_cost': _('What was the overhead cost to you for using INGO?'),

            # 'visited': _('Did you go visit the disaster site? e.g. Nepal'),
            # 'visited_area': _('Which part of disaster site did you visit?'),
            # 'worked_with_team': _('Did you work with local team?'),
            # 'distributed_materials': _('Did you distribute materials?'),
            # 'type_of_work': _('What other work did you do?'),
            # 'time_on_site': _('How long did you spend at the disaster site?'),
            # 'staying_location': _('Where did you live during this period?'),
            # 'visit_expense': _('What was your expense for the visit?'),
            # 'how_support': _('How did you support your visit?'),
        }

        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }

class SurveyExtraForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SurveyExtraForm, self).__init__(*args, **kwargs)
        questions = SurveyExtraQuestion.objects.order_by('order')

        for q in questions:
            question = q.question.replace(' ', '_').lower().strip()
            if q.type_of_input == 'check':
                choices = [('yes', 'Yes'), ('no', 'No'), ('na', 'N/A')]
                self.fields[question] = CharField(required=False, widget=forms.Select(choices=choices, attrs={'class': 'form-extra-field'}))

            elif q.type_of_input == 'multiple_choice':
                choice_list = MultipleChoice.objects.filter(question=q)
                choices = []
                for c in choice_list:
                    choice = c.choice
                    tup = (choice, choice)
                    choices.append(tup)
                self.fields[question] = CharField(required=False, widget=forms.Select(choices=choices, attrs={'class': 'form-extra-field'}))

            else:
                self.fields[question] = CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-extra-field'}))

# Notes
# name = forms.CharField(label="Name of Organization", widget=forms.TextInput(attrs={'class': 'form-field'}))
