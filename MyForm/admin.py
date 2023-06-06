from django.contrib import admin
from .models import MyForm
from django.shortcuts import render

# Register your models here.
class MyFormAdmin(admin.ModelAdmin):
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('name', 'phone_number', 'email', 'photograph_preview')    # telling which fields to display

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = MyForm.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'pdfs.html', context)
    actions = [generatePDF]   # the function generatePDF will get called when we click on that action button

admin.site.register(MyForm, MyFormAdmin)