from django.contrib import admin

from .models import Cat, Hunting, Prey, PreyType


# Register your models here.


class PreyInline(admin.StackedInline):
    model = Prey
    extra = 1


class HuntingAdmin(admin.ModelAdmin):
    model = Hunting
    inlines = [PreyInline]


admin.site.register(Hunting, HuntingAdmin)
admin.site.register(Cat)
admin.site.register(PreyType)
