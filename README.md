**/api/shop/products/** - returns products list

**/api/shop/products/?status=1** - filters product list by status
    В наличии = 1
    Под заказ = 2
    Ожидается поступление = 3
    Нет в наличии = 4
    Не производится = 5
 
**/api/shop/products/?search=p** - searches by title and sku

**/api/shop/products/<pk>** - returns product details
