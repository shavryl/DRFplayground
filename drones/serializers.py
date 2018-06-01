from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
import drones.views


class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):

    drones = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='drone-detail')

    class Meta:
        model = DroneCategory
        fields = ('url', 'pk', 'name', 'drones')


class DroneSerializer(serializers.HyperlinkedModelSerializer):

    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(),
        slug_field='name')

    class Meta:
        model = Drone
        fields = ('url', 'name', 'drone_category', 'manufacturing_date',
                  'has_it_competed', 'inserted_timestamp')
