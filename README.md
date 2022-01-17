# Тестовое задание 
Создать Django-проект:

создать модель Product c полями:
  1. name - наименование
  2. description - описание продукта
  3. uuid - уникальный идентификатор
  4. created - дата создания
  5. updated - дата обновления
  6. logo - картинка
  7. rotate_duration - дробное
 
----------------------------------------------------------------------------

1. создать api-points(CRUD) для модели Product.
2. доступ к Product Details c использованием <uuid>. (пример /products/<uuid>/)
3. список продуктов должен содержать пагинацию на 10 элементов.
4. при загрузке файла logo, необходимо повернуть картинку на 180 градусов и
сохранить, так же необходимо сохранить длительность операции поворота в
эту же Модель Product (rotate_duration) в секундах.
5. Необходимо реализовать возможность изменения Продукта только один
раз(т.е. повторный запрос на изменение поля description, например, вернет
соответствующее сообщение об ошибке)
6. добавить фильтр на апи-поинт списка продуктов, чтобы посмотреть какие из
продуктов уже были модифицированы, а какие не были ( пример
/products/?modified=true)
  
  
-----------------------------------------------------------------------------
# API
```  
GET http://127.0.0.1:8000/products/api/list/ - to show a list of all products
```  
```  
POST http://127.0.0.1:8000/products/api/update/uuid/ - to update the selected product by uuid
  
fields modified, name, description, logo

Also you cannot edit an object if the modified = True. Every time after editing the object
if the modified = False, it takes the value True after request
```  
```  
DELETE http://127.0.0.1:8000/products/api/delete/uuid/ - to delete the selected product by uuid  
```  
``` 
POST http://127.0.0.1:8000/products/api/create/ - to create the product
fields uuid, name, description, logo (img) 
```
