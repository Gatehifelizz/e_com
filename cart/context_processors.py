from .cart import Cart


# create context processor
def cart(request):
    # return default data
    return {'cart': Cart(request)}
