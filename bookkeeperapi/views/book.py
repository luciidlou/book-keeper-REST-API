import base64
import uuid
from django.core.files.base import ContentFile
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from bookkeeperapi.models import Book, Genre


class GetBookSerializer(serializers.ModelSerializer):
    """JSON serializer for Books"""
    model = "Book"
    # fields = ('title', 'author', 'publication_date',
    #           'synopsis', 'genre', 'page_length',
    #           'goodreads_link', 'image', 'average_rating')
    fields = ('__all__', 'average_rating')


class CreateBookSerializer(serializers.ModelSerializer):
    """JSON serializer for Books"""
    model = "Book"
    fields = ('title', 'author', 'publication_date',
              'synopsis', 'genre', 'page_length',
              'goodreads_link', 'image', 'average_rating')


class BookView(ViewSet):
    """Contains all the views for Books"""

    def create(self, request):
        """Handles a POST request on a Book object"""

        #! ----------------------------------------------------------------
        #! Need to look into this more
        img_format, img_str = request.data["game_image"].split(';base64,')
        ext = img_format.split('/')[-1]
        random_filename = ContentFile(base64.b64decode(
            img_str), name=f'{request.data["title"]}-{uuid.uuid4()}.{ext}')
        #! ----------------------------------------------------------------

        serializer = CreateBookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(image=random_filename)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles a PUT request on a Book object"""
        # Get the book we need to update
        book = Book.objects.get(pk=pk)
        genre = Genre.objects.get(pk=request.data['genre'])

        # Update properties on the book
        book.title = request.data['title']
        book.author = request.data['author']
        book.publication_date = request.data['publication_date']
        book.synopsis = request.data['synopsis']
        book.genre = genre
        book.page_length = request.data['page_length']
        book.goodreads_link = request.data['goodreads_link']
        book.image = request.data['image']

        # use the .save() request to save the book
        book.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        """Handles a GET request on many Books"""
        books = Book.objects.all()
        serializer = GetBookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handles a GET request on a Book object"""
        book = Book.objects.get(pk=pk)
        serializer = GetBookSerializer(book)
        return Response(serializer.data)

    def destroy(self, request, pk):
        """Handles a DELETE request on a book object"""
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
