from django import forms
from django.contrib import admin
from fundraising.models import *
import csv


class AllDataAdmin(admin.ModelAdmin):
    fields = ('donorName','donorWebsite','donorType','donorCountry','recipientName','recipientWebsite','recipientType',
        'recipientCountry','transactionDate','amount','currency','aidType','transactionType','description','source',
        'links','dateType','date','sector','targetGeography','vdc')
    list_display = ('donorName','donorWebsite','donorType','donorCountry','transactionDate','amount')
    search_fields = ['donorCountry','donorType','donorName','transactionDate']

class AidsDataAdmin(admin.ModelAdmin):
    fields = ('donorName','donorWebsite','donorType','donorCountry','recipientName','recipientWebsite','recipientType',
        'recipientCountry','transactionDate','amount','currency','aidType','transactionType','description','source',
        'links','dateType','date','sector','targetGeography','vdc')
    list_display = ('donorName','donorWebsite','donorType','donorCountry','recipientName','recipientWebsite','recipientType',
        'recipientCountry','transactionDate','amount','currency','aidType','transactionType','description','source',
        'links','dateType','date','sector','targetGeography','vdc')
    search_fields = ['donorCountry','donorType','donorName','transactionDate']




class FundraiserAdmin(admin.ModelAdmin):
    list_display = ('fundraiser', 'url', 'raised')
    search_fields = ['fundraiser', 'url', 'raised']


class GoFundMeAdmin(admin.ModelAdmin):
    list_display = ('url', 'campaign', 'location', 'goal', 'total', 
        'donors_number', 'created_by', 'date_created', 'date_closed')
    list_display_links = ('url', 'campaign', 'location', 'goal', 'total', 
        'donors_number', 'created_by', 'date_created', 'date_closed')
    search_fields = ['url', 'campaign', 'location', 'goal', 'total', 
        'donors_number', 'created_by', 'date_created', 'date_closed']


class TableAdmin(admin.ModelAdmin):
    list_display = ('table', 'description', 'name', 'url', 'aid_amount', 
        'extra_field_1', 'extra_field_2', 'extra_field_3', 'extra_field_4', 
        'extra_field_5', 'extra_field_6', 'extra_field_7', 'last_updated_activate')


class TableDataAdmin(admin.ModelAdmin):
    fields = ('table', 'name', 'url', 'aid_amount', 'extra_field_1',
        'extra_field_2', 'extra_field_3', 'extra_field_4', 'extra_field_5', 
        'extra_field_6', 'extra_field_7')
    list_display = ('table', 'name', 'url', 'aid_amount', 'extra_field_1',
        'extra_field_2', 'extra_field_3', 'extra_field_4', 'extra_field_5', 
        'extra_field_6', 'extra_field_7')
    list_display_links = ('table', 'name', 'url', 'aid_amount', 'extra_field_1',
        'extra_field_2', 'extra_field_3', 'extra_field_4', 'extra_field_5', 
        'extra_field_6', 'extra_field_7')
    list_filter = ('table',)
    search_fields = ['table__table', 'name', 'url', 'aid_amount', 'extra_field_1',
        'extra_field_2', 'extra_field_3', 'extra_field_4', 'extra_field_5', 
        'extra_field_6', 'extra_field_7']


class SurveyAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'organization_name', 
        'email')
    search_fields = ['first_name', 'last_name', 'organization_name', 
        'email']
    # list_display = ('first_name', 'last_name', 'organization_name', 
    #     'email', 'phone', 'description', 'crowdfunding', 'goal', 
    #     'campaign_time', 'goal_reached', 'raised', 'used_ngo', 'ngo', 
    #     'ngo_fee', 'ngo_cost', 'used_ingo', 'ingo', 'ingo_fee', 
    #     'ingo_cost', 'visited', 'visited_area', 'worked_with_team', 
    #     'distributed_materials', 'type_of_work', 'time_on_site', 
    #     'staying_location',  'visit_expense', 'how_support')
    # search_fields = ['first_name', 'last_name', 'organization_name', 
    #     'email', 'phone', 'description', 'crowdfunding', 'goal', 
    #     'campaign_time', 'goal_reached', 'raised', 'used_ngo', 'ngo', 
    #     'ngo_fee', 'ngo_cost', 'used_ingo', 'ingo', 'ingo_fee', 
    #     'ingo_cost', 'visited', 'visited_area', 'worked_with_team', 
    #     'distributed_materials', 'type_of_work', 'time_on_site', 
    #     'staying_location',  'visit_expense', 'how_support']


class SurveyExtraQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'type_of_input', 'order')
    list_display_links = ('question', 'type_of_input', 'order')


class SurveyExtraAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'survey',)


class MultipleChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice', 'question',)
    list_display_links = ('choice', 'question',)


admin.site.register(AllData, AllDataAdmin)
admin.site.register(AidsData, AidsDataAdmin)
admin.site.register(Fundraiser, FundraiserAdmin)
admin.site.register(GoFundMe, GoFundMeAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(TableData, TableDataAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyExtraQuestion, SurveyExtraQuestionAdmin)
admin.site.register(SurveyExtraAnswer, SurveyExtraAnswerAdmin)
admin.site.register(MultipleChoice, MultipleChoiceAdmin)