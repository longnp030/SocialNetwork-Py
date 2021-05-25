import datetime as dt
from tomo.settings import USER_LASTSEEN_TIMEOUT
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin

class OnlineUserMiddleware(MiddlewareMixin):
    '''def __init__(self, get_response):
        self.get_response = get_response'''

    def process_request(self, request):
        current_user = request.user
        if request.user.is_authenticated:
            now = dt.datetime.now()
            cache.set('seen_%s' % (current_user.username), now, USER_LASTSEEN_TIMEOUT)