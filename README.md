# paginator
Little project for comfortable pagination



# Instalation:
1. Download pagination.py
2. go to foleder with installed python 
3. go to \Lib
4. paste file here



# Using:
```python
from pagination import Pagination

paginator = Pagination(data=[1, 2, 3, 4, 5, 6, 7, 8, 9], PAGINATION_RATE=2)
page = paginator.get_page(1)
print(page.data) # -> [1, 2]
print(page.has_next_page) # -> True
print(page.has_previous_page) # -> False
```
Also you can set start page:
```python
paginator = Pagination(data=[1, 2, 3, 4, 5, 6, 7, 8, 9], PAGINATION_RATE=2, start_page=2)
page = paginator.get_page(2)
print(page.data) # -> [1, 2]
```
As default start_page = 1
