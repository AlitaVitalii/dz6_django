from application.models import Logger, Person

from django.contrib import admin


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'date_time')

    fieldsets = [
        (None, {'fields': ['path', 'method']}),
        ('Query', {'fields': ['query']}),
        ('Body', {'fields': ['body']}),
    ]

    search_fields = ['path']
    list_filter = ['date_time']
    date_hierarchy = 'date_time'

    list_per_page = 10
