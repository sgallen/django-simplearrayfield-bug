import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from django.contrib.admin.sites import AdminSite

from bug_app.admin import ArrayFieldModelAdmin
from bug_app.models import ArrayFieldModel


class MockRequest():
    pass


class MockSuperUser():
    def has_perm(self, perm):
        return True


request = MockRequest()
request.user = MockSuperUser()

admin_site = AdminSite()
bug_app_admin = ArrayFieldModelAdmin(ArrayFieldModel, admin_site)
bug_app_form = bug_app_admin.get_form(request)

# original_array_field_model = ArrayFieldModel.objects.first()
posted_data = {
    'arrays': '1',
}

# test_form = bug_app_form(posted_data, instance=original_array_field_model)
test_form = bug_app_form(posted_data)

print(test_form.errors)
