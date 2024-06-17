from shop.models import Product


class Cart():
    def __init__(self, request):

        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        # make sure cart is avilable on all pages
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    def cart_total(self):
        #get prod id
        product_id=self.cart.keys()
        #lookup keys in database
        products=Product.objects.filter(id__in=product_id)
        quantities=self.cart
        #
        total=0
        for key,value in quantities.items():
            #conv key str to int
            key=int(key)
            for product in products:
                if product.id==key:
                    if product.is_sale:
                        total=total+(product.sale_price*value)
                    else:
                        total = total + (product.price * value)

        return total


    def get_prods(self):
        # get id from cart
        product_ids = self.cart.keys()
        # use id to lookup products in database
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        # get cart
        ourcart = self.cart
        ourcart[product_id] = int(product_qty)

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        # deleten from dictionary
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
