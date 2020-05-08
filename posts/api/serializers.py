from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from posts.models import Post, Categoria


# model listings
class CategoriaListingField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.name}"

    def to_internal_value(self, value):
        obj = Categoria.objects.filter(name=value)
        if obj and (len(obj)) == 1:
            return obj.get().id
        else:
            raise ValidationError(f"Categoria with name {value} does not exist")


class AuthorListingField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.username.capitalize()}"

    def to_internal_value(self, value):
        return value


# model serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("name",)


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post-detail", lookup_field="slug"
    )
    author = AuthorListingField(queryset=User.objects.all())
    published_date = serializers.DateTimeField(format="%a, %d %b  %I:%M %p")

    class Meta:
        model = Post
        fields = ("url", "title", "published_date", "author")


class PostDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post-detail", lookup_field="slug"
    )
    author = AuthorListingField(queryset=User.objects.all())
    categoria = CategoriaListingField(queryset=Categoria.objects.all(), many=True)
    published_date = serializers.DateTimeField(format="%a, %d %b  %I:%M %p")

    class Meta:
        model = Post
        fields = (
            "url",
            "title",
            "categoria",
            "content",
            "published_date",
            "author",
            "status",
        )


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="post-detail", lookup_field="slug"
    )
    author = serializers.HiddenField(default=CurrentUserDefault())
    categoria = CategoriaListingField(queryset=Categoria.objects.all(), many=True)
    published_date = serializers.DateTimeField(
        format="%a, %d %b  %I:%M %p", read_only=True
    )

    class Meta:
        model = Post
        fields = (
            "url",
            "title",
            "categoria",
            "content",
            "published_date",
            "author",
            "status",
        )

    def create(self, validated_data):
        title = validated_data.get("title", "")
        validated_data["slug"] = slugify(title)
        # pops out the list of categorias
        categorias = validated_data.pop("categoria")
        # and saves the rest of the data
        post = Post.objects.create(**validated_data)
        # add categorias separately
        for categoria in categorias:
            post.categoria.add(categoria)
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.slug = slugify(instance.title)

        categorias = validated_data.get("categoria")
        # deassociate existing categories from instance
        instance.categoria.clear()
        for categoria in categorias:
            instance.categoria.add(categoria)

        instance.author = self.context.get("request").user
        instance.content = validated_data.get("content", instance.content)
        instance.save()
        return instance
