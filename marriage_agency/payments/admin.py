from django.contrib import admin
from .models import TariffPlan, UserSubscription, UserAdditionalService, AdditionalService, Payment

admin.site.register(TariffPlan)
admin.site.register(UserAdditionalService)
admin.site.register(UserSubscription)
admin.site.register(Payment)
admin.site.register(AdditionalService)