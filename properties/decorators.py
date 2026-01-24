from django.shortcuts import redirect
from django.contrib import messages


def landlord_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request.user, 'userprofile'):
            if request.user.userprofile.user_type == 'landlord':
                return view_func(request, *args, **kwargs)

        messages.error(request, "Only landlords can add properties.")
        return redirect('home')

    return _wrapped_view
