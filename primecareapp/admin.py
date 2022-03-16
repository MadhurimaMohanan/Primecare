from django.contrib import admin

# Register your models here.
from .models import P_user
from .models import P_Photo
from .models import P_Work_permit_certificate
from .models import P_Address
from .models import P_Sssc
from .models import P_Pvg
from .models import P_Experience
from .models import P_Contact
from .models import user_temp
from .models import P_caretaker
from .models import P_CV
from .models import P_admin
from .models import P_previous_employer
# from .models import P_details


admin.site.register(P_user)
admin.site.register(P_Photo)
admin.site.register(P_Work_permit_certificate)
admin.site.register( P_Address)
admin.site.register(P_Sssc)
admin.site.register(P_Pvg)
admin.site.register(P_Experience)
admin.site.register(P_Contact)
admin.site.register(user_temp)
admin.site.register(P_caretaker)
admin.site.register(P_CV)
admin.site.register(P_admin)
admin.site.register(P_previous_employer)

# admin.site.register(P_details)
