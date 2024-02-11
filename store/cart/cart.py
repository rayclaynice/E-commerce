from decimal import Decimal
from index.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session


        # returning user obtains his/or existing user
        cart = self.session.get('session_key')  #.get() method returns the key of a dictionary i.e takes two values and a fallback second argument i ncase theres none

        # new user generates a new session key

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart  #makes sure that our cart is available on every page be it new or returning user


    def add(self, product, product_qty):
        
        product_id = str(product.id)
        if product_id in self.cart: #product_id = {"qty":'product_qty} same as assigning values with [product_id]['keys']
            self.cart[product_id]['qty']  = product_qty        #product[index][value] when accessing values of list that are inside a list
                                                    #here we accessed 'qty' thats in that product_id, i.e the same product
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty':product_qty}
            ##self.cart[product_id]['price] accesing the dictionary value of product id [key][value]

        self.session.modified = True


    def delete(self, product):
        
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True



    def update(self, product, qty):
        product_id = str(product)
        product_quantity = qty
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_quantity
        
        self.session.modified = True
        









    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())# same as i for i in range or list
    
    def __iter__(self):             # __init__ method used to iterate through list in a class
        all_product_ids = self.cart.keys()
        products =  Product.objects.filter(id__in = all_product_ids)   #fieldname__in=[value1, value2, value3] used to get record of one of the values in an iterable list, tuple, string,queryset
        cart = self.cart.copy()     #returns a copy of a specific list, thats product ids or keys in the databasehg

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values(): #iterating through selected items in the cart ,,,,,values in self.cart
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['qty']
            yield item
    
    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())