from rest_framework.throttling import SimpleRateThrottle


class CustomAnonRateThrottle(SimpleRateThrottle):

    scope = "custom_anon"

    def get_rate(self):

        settings_rate = getattr(self, "THROTTLE_RATES", {}).get(self.scope)
        return settings_rate or self.default_rate

    def get_cache_key(self, request, view):

        if request.user and request.user.is_authenticated:
            return None
        return self.cache_format % {
            "scope": self.scope,
            "ident": self.get_ident(request),
        }


class CustomUserRateThrottle(SimpleRateThrottle):

    scope = "custom_user"

    def get_rate(self):

        settings_rate = getattr(self, "THROTTLE_RATES", {}).get(self.scope)
        return settings_rate or self.default_rate

    def get_cache_key(self, request, view):
        if request.user and request.user.is_authenticated:
            ident = request.user.pk
        else:
            ident = self.get_ident(request)

        return self.cache_format % {"scope": self.scope, "ident": ident}


class UserAnonRateThrottle(CustomUserRateThrottle, CustomAnonRateThrottle): ...
