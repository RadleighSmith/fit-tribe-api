from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the current user's details, extending the default
    UserDetailsSerializer provided by dj_rest_auth to include additional
    profile-related fields and admin status fields.

    This serializer adds the following fields:
    - profile_id: The ID of the user's profile.
    - profile_image: The URL of the user's profile image.
    - is_staff: Boolean indicating if the user is a staff member.
    - is_superuser: Boolean indicating if the user is a superuser.

    Attributes:
    - profile_id (ReadOnlyField): The ID of the user's profile, sourced from
                                  the related profile object.
    - profile_image (ReadOnlyField): The URL of the user's profile image,
                                     sourced from the related profile object.
    - is_staff (ReadOnlyField): Indicates if the user is a staff member.
    - is_superuser (ReadOnlyField): Indicates if the user is a superuser.

    Meta:
    - fields (tuple): The fields to be included in the serialized
                      representation of the user, combining the default
                      fields from UserDetailsSerializer with the added
                      profile_id, profile_image, is_staff,
                      and is_superuser fields.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(
        source='profile.profile_image.url'
    )
    is_staff = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'is_staff', 'is_superuser'
        )
