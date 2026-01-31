# Delete Operation
## Command:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print("Book deleted")
all_books = Book.objects.all()
print(f"Total books: {all_books.count()}")
```