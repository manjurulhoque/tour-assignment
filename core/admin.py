from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User, Permission
from django.utils.translation import gettext, gettext_lazy as _

admin.site.unregister(Group)
admin.site.unregister(User)


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)
        # labels = {
        #     'is_staff': 'Is Assistant'
        # }


class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserCreateForm
    prepopulated_fields = {'username': ('first_name', 'last_name',)}
    list_filter = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'password1', 'password2',),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        # ('Permissions', {
        #     'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        # }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super(CustomUserAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['is_superuser'].label = 'Admin status'
        form.base_fields['is_staff'].label = 'Is Assistant'
        # del form.base_fields['groups']
        return form

    def queryset(self, request):
        qs = super(CustomUserAdmin, self).queryset(request)
        # return qs.filter(is_staff=True)
        return qs


admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
