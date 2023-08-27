from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, RedirectView

from .models import SignupRedirect


class ActiveRedirects(ListView):
    queryset = SignupRedirect.objects.active()

    context_object_name = "redirects"
    template_name = "signup_redirects/active.html"


class FollowRedirect(RedirectView):
    permanent = False

    def get_redirect_url(self, origin: str) -> str | None:
        try:
            redirect = SignupRedirect.objects.active().get(origin=origin)

            return redirect.target

        except SignupRedirect.DoesNotExist:
            messages.warning(
                self.request,
                f"Na adrese {self.request.build_absolute_uri()}"
                f" práve neprebieha žiadne prihlasovanie",
            )

            return reverse("redirects:active")
