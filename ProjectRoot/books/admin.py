from django.contrib import admin
from books.models import Author, Book, Publisher

# 관리자모드에 테이블이 보이도록 등록.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
