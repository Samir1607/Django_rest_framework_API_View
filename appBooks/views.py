from rest_framework.views import APIView
from .models import Book
from .serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookCreate(APIView):
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Book1(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                "error": "Book Does Not Exist"
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book1 = self.get_book_by_pk(pk)
        serializer = BookSerializer(book1)
        return Response(serializer.data)

    def put(self, request, pk):
        book1 = self.get_book_by_pk(pk)
        serializer = BookSerializer(book1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book1 = self.get_book_by_pk(pk)
        book1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

