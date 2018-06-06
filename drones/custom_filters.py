from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter


class CompetitionFilter(filters.FilterSet):

    from_achievement_date = DateTimeFilter(
        name='distance_achievement_date', lookup_expr='gte')
    to_achievement_date = DateTimeFilter(
        name='distance_achievement_date', lookup_expr='lte')
