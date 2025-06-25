from django.contrib import admin

# Register your models here.
from .models import Company, IPO, Document,User,Application

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    search_fields = ('company_name',)

@admin.register(IPO)
class IPOAdmin(admin.ModelAdmin):
    list_display = ('company', 'status', 'open_date', 'close_date')
    list_filter = ('status', 'issue_type')
    search_fields = ('company__company_name',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('ipo',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'role')
    search_fields = ('email', 'name', 'role')
    list_filter = ('role',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'ipo', 'quantity', 'status')
    list_filter = ('status',)
    search_fields = ('user__email', 'ipo__company_name')
