from rest_framework import serializers
from games.models import Game, GameCategory, Player, PlayerScore
from django.contrib.auth.models import User
import games.views


class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'games'
        )


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='game-detail'
    )

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games'
        )


class GameSerializer(serializers.HyperlinkedModelSerializer):
    # display the owner username (read-only)
    owner = serializers.ReadOnlyField(source='owner.username')
    # display the game's category instead of the id
    game_category = serializers.SlugRelatedField(
        queryset=GameCategory.objects.all(), slug_field='name')

    class Meta:
        model = Game
        fields = (
            'url',
            'owner',
            'game_category',
            'name',
            'release_date',
            'played'
        )

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('played', instance.played)
        instance.save()
        return instance


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'game',
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICE)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
        )


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game',
        )
