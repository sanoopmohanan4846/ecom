#  this is the session Page 
from ecomapp.models import Product, Profile



class Cart():
    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # for getting the current session key if the key is existing
        cart = self.session.get('session_key')
        
        # if the user is new then lets create a new " session_key "
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
            
        # lets make sure that the cart page is availabe for all the other pages 
        self.cart = cart
        
    
    def db_add(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)
        # logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            
        self.session.modified = True
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id = self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("/'", "/'")
            # Save carty to the Profile Model
            current_user.update(old_cart = str(carty))    
    
        
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
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
            # Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
            # Save carty to the Profile Model
            current_user.update(old_cart=str(carty))
            
        
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total

        
    def __len__(self):
        return len(self.cart)
    
    
    def get_prods(self):
        # get id from cart
        product_ids = self.cart.keys()
        #  use ids to lookup products in the database
        products = Product.objects.filter(id__in=product_ids )
        
        # return those lookup products in database
        return products
    
    
    def get_quants(self):
        quantites = self.cart
        return quantites
    
    
    def update(self, product, quantity):
        product_id=str(product)
        product_qty=int(quantity)
        
        # get the cart
        ourcart = self.cart
        # update dictnory/cart
        ourcart[product_id] = product_qty
        self.session.modified = True
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))
        
        thing = self.cart
        return thing
    
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True
        
        # Deal with logged in user
        if self.request.user.is_authenticated:
			# Get the current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
            current_user.update(old_cart=str(carty))