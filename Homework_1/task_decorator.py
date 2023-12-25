Создайте декоратор в python , который ограничивает доступ к функции определенным типам пользователей. Предполагается, что тип пользователя будет передаваться 
# в качестве аргумента user_type (str) в декорируемую функцию. 
# Типы пользователей: "admin", "user", "auth_user". Результат должен быть вида:
# "access", если разрешен
# "denied", если нет.


# def access_control(*allowed_user_types):
#     def decorator(func):
#         def wrapper(user_type, *args, **kwargs):
#             if user_type in allowed_user_types:
#                 return "access"
#             else:
#                 return "denied"
#         return wrapper
#     return decorator


# @access_control("admin", "auth_user")
# def restricted_function(user_type):
#     return "This function has restricted access"


# print(restricted_function("admin")) 
# print(restricted_function("user"))




#Напишите функцию, которая принимает два аргумента: кол-во денег в наличии(str) и корзина покупателя (list[dict]). 
# Далее проверяет хватает ли денег на оплату всех товаров из корзины. В случае, если хватает возвращает ответ вида: 
# {
# "status": "success",
# "comment": "Покупки оплачены"
# }

# Если денег не хватает ответ должен быть:
# { 
# "status": "fail", 
# "comment": "Недостаточно средств. Внесите n сумму денег" 
# }
# n - количество денег, которое не хватает для оплаты всех товаров 
# корзина представляет собой список словарей с ключами название, количество, стоимость.


# def check_payment(money_available, basket):
#     total_cost = sum([item["quantity"] * item["price"] for item in basket])
#     if total_cost <= int(money_available):
#         return {"status": "success", "comment": "Покупки оплачены"}
#     else:
#         return {"status": "fail", "comment": f"Недостаточно средств. Внесите {total_cost - int(money_available)} сумму денег"}


# basket = [
#     {"name": "apple", "quantity": 2, "price": 10},
#     {"name": "banana", "quantity": 1, "price": 20},
#     {"name": "orange", "quantity": 3, "price": 15}
# ]

# print(check_payment("50", basket)) # output: {"status": "success", "comment": "Покупки оплачены"}
# print(check_payment("30", basket)) # output: {"status": "fail", "comment": "Недостаточно средств. Внесите 25 сумму денег"}

