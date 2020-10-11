from rest_framework.throttling import AnonRateThrottle


class AnonymousPerMinThrottle(AnonRateThrottle):
    scope = 'max_per_min'


class AnonymousPerDayThrottle(AnonRateThrottle):
    scope = 'max_per_day'