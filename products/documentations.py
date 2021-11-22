from drf_yasg import openapi

class DOCShelperOrder:
    MAKE_AN_ORDER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'payer_email': openapi.Schema(type=openapi.TYPE_STRING,
                                          description='Payer email',
                                          max_lenght=100),
            'amount': openapi.Schema(type=openapi.TYPE_INTEGER,
                                     description='Payment amount',
                                     max_value=999999),
            'currency': openapi.Schema(type=openapi.TYPE_STRING,
                                       description='Payment сurrency\nonly usd/eur/uah',
                                       max_lenght=3),
            'due_to_date': openapi.Schema(type=openapi.TYPE_STRING,
                                          description='Payment due to date',
                                          format='date'),
            'transactionID': openapi.Schema(type=openapi.TYPE_STRING,
                                            description='Unique transactionID\nformat(********-**)',
                                            max_lenght=11),
            'purchased': openapi.Schema(type=openapi.TYPE_INTEGER,
                                        description='Product identifier'),
        }
    )
    
    VALID_ORDER_EXAMPLE_GET = [{
        'payer_email': 'nameuser@gmail.com',
        'amount': '1050',
        'currency': 'usd',
        'request_date': '2021-11-22',
        'due_to_date': '2021-11-22',
        'transactionID': '64382358-51',
        'purchased': '1'
    },
    {
        'payer_email': 'admin12@lnu.edu.ua',
        'amount': '750',
        'currency': 'eur',
        'request_date': '2021-11-23',
        'due_to_date': '2021-11-23',
        'transactionID': '64382358-52',
        'purchased': '3'
    }]
    
    VALID_ORDER_EXAMPLE_POST = {
        'payer_email': 'login@domain',
        'amount': 'unsigned integer',
        'currency': 'usd/eur/uah',
        'request_date': 'yyyy-mm-dd',
        'due_to_date': 'yyyy-mm-dd',
        'transactionID': '********-**',
        'purchased': '1'
    }
   
    INVALID_ORDER_EXAMPLE_ERRORS = {
        'payer_email': 'The user with such email is not registered',
        'amount': 'You have not contributed enough to purchase',
        'transactionID': 'Payment with such transactionID already exists'
    }
   
    VALID_ORDER_EXAMPLE_RESPONSE_GET = {
        "status": 200,
        "number of orders": 2,
        "orders": VALID_ORDER_EXAMPLE_GET[0]
    }
   
    INVALID_ORDER_EXAMPLE_RESPONSE_LOGIN = {
        "status": 403,
        "error": "Access error. You need to log in"
    }
   
    VALID_ORDER_EXAMPLE_RESPONSE_POST = {
        "status": 200,
        "message": "You have successfully purchased the computer, computers left in stock: 97. \n\
            Your rest: 5.0 usd. Thanks for buying :)",
        "payment": VALID_ORDER_EXAMPLE_POST
    }
    
    INVALID_ORDER_EXAMPLE_RESPONSE_POST = {
        "status": 400,
        "message": "Incorrect data entered",
        "errors": INVALID_ORDER_EXAMPLE_ERRORS
    }




class DOCSOrder:
    get = {
        'operation_description': 'The authorized user receives a list of their purchases',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelperOrder.VALID_ORDER_EXAMPLE_RESPONSE_GET},
                                    description='Authorized user order list received successfully'),
            '403': openapi.Response(examples={'application/json': DOCShelperOrder.INVALID_ORDER_EXAMPLE_RESPONSE_LOGIN},
                                    description='Access error. You need to log in')
        }
    }
    
    get_id = {
        'operation_description': 'The authorized user receives his order by ID',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelperOrder.VALID_ORDER_EXAMPLE_RESPONSE_GET},
                                    description='The authorized user received their order by ID successfully'),
            '403': openapi.Response(examples={'application/json': DOCShelperOrder.INVALID_ORDER_EXAMPLE_RESPONSE_LOGIN},
                                    description='Access error. You need to log in')
        }
    }
    
    post = {
        'request_body': DOCShelperOrder.MAKE_AN_ORDER,
        'operation_description': 'An authorized user makes an order',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelperOrder.VALID_ORDER_EXAMPLE_RESPONSE_POST},
                                    description='The payment has been validated, the product has been purchased successfully'),
            '400': openapi.Response(examples={'application/json': DOCShelperOrder.INVALID_ORDER_EXAMPLE_RESPONSE_POST},
                                    description='Invalid data received, purchase failed'),
            '403': openapi.Response(examples={'application/json': DOCShelperOrder.INVALID_ORDER_EXAMPLE_RESPONSE_LOGIN},
                                    description='Access error. You need to log in')
        }  
    }
    
    
    
class DOCShelperProduct:
    ADD_PRODUCT = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'type': openapi.Schema(type=openapi.TYPE_STRING,
                                          description='Product type',
                                          max_lenght=20),
            'price': openapi.Schema(type=openapi.TYPE_INTEGER,
                                     description='Product price',
                                     max_value=999999),
            'availability': openapi.Schema(type=openapi.TYPE_INTEGER,
                                     description='Quantity of product')
        }
    )
    
    VALID_PRODUCT_EXAMPLE_LIST = [{
        "id": 10,
        "type": "DVD",
        "price": 450.0,
        "availability": 25
    },
    {
        "id": 12,
        "type": "MP3 player",
        "price": 75.0,
        "availability": 60
    }]
    
    INVALID_PRODUCT_EXAMPLE_ERRORS = {
        'type': 'A product with this type already exists in the database',
        'price': 'The price cannot be negative or zero',
        'availability': 'The availability cannot be negative'
    }
    
    VALID_PRODUCT_EXAMPLE_RESPONSE_GET = {
        "count": 2,
        "customers": VALID_PRODUCT_EXAMPLE_LIST
    }
    
    INVALID_ORDER_EXAMPLE_RESPONSE_LOGIN = {
        "status": 403,
        "error": "Access error. You need to log in or you are not an administrator"
    }
    
    VALID_PRODUCT_EXAMPLE_RESPONSE_POST = {
        "status": 200,
        "message": "You have successfully added the product to the database",
        "product": VALID_PRODUCT_EXAMPLE_LIST[0]
    }
    
    INVALID_PRODUCT_EXAMPLE_RESPONSE_POST = {
        "status": 400,
        "message": 'You have entered invalid data',
        "errors": INVALID_PRODUCT_EXAMPLE_ERRORS
    }
    
class DOCSProduct:
    get = {
        'operation_description': 'Any user can view the list of products available for purchase',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelperProduct.VALID_PRODUCT_EXAMPLE_RESPONSE_GET},
                                    description='The user has successfully received a list of products available for purchase'),
        }
    }
    
    post = {
        'request_body': DOCShelperProduct.ADD_PRODUCT,
        'operation_description': 'The administrator adds a new product to the database',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelperProduct.VALID_PRODUCT_EXAMPLE_RESPONSE_POST},
                                    description='The administrator has successfully added a new product to the database'),
            '400': openapi.Response(examples={'application/json': DOCShelperProduct.INVALID_PRODUCT_EXAMPLE_RESPONSE_POST},
                                    description='The administrator entered invalid data, adding the product to the database failed'),
            '403': openapi.Response(examples={'application/json': DOCShelperProduct.VALID_PRODUCT_EXAMPLE_RESPONSE_POST},
                                    description='Access error. You need to log in or you are not an administrator'),
        }
    }