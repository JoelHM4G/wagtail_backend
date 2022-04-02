from django.shortcuts import render

from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter
from wagtail.api.v2.views import BaseAPIViewSet

from subscribers.models import Subscribers

class SubscribersAPIViewSet(BaseAPIViewSet):
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter]
    body_fields = BaseAPIViewSet.body_fields + ['email']
    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['email', 'full_name']
    nested_default_fields = BaseAPIViewSet.nested_default_fields + ['email', 'full_name']
    name = 'subscribers'
    model = Subscribers
