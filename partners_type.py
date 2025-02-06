class Partner:

    def __init__(self, partner_type, name, director, email, phone, adress, inn, rating):
        self.partner_type = partner_type
        self.name = name
        self.director = director
        self.email = email
        self.phone = phone
        self.adress = adress
        self.inn = inn
        self.rating = rating


class Product:

    def __init__(self, name, articul, min_cost):
        self.name = name
        self.articul = articul
        self.min_cost = min_cost


class Sale:
    def __init__(self, partner_id, product_id, quantity):
        self.partner_id = partner_id
        self.product_id = product_id
        self.quantity = quantity

    def calculate_discount(self):
        if self.quantity >= 1000:
            return 15
        elif self.quantity >= 500:
            return 10
        elif self.quantity >= 100:
            return 5
        return 0
