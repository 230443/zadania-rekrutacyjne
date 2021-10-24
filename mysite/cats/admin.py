from django.contrib import admin

from .models import Cat, Hunting, Prey, PreyType


# Register your models here.


class PreyInline(admin.StackedInline):
    model = Prey
    extra = 1


class HuntingAdmin(admin.ModelAdmin):
    model = Hunting
    inlines = [PreyInline]


class CatAdmin(admin.ModelAdmin):
    readonly_fields = ['is_male']
    list_display = ('name', 'user', 'is_male', 'color')
    search_fields = ['name']


admin.site.register(Hunting, HuntingAdmin)
admin.site.register(Cat, CatAdmin)
admin.site.register(PreyType)
