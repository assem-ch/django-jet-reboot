from django.contrib import admin
from django.contrib.sites.models import Site

from jet.tests.models import TestModel, RelatedToTestModel


class TestModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')


class RelatedToTestModelAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Site)
admin.site.register(TestModel, TestModelAdmin)
admin.site.register(RelatedToTestModel, RelatedToTestModelAdmin)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_per_page = 10