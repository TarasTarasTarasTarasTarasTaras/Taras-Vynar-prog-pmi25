from drf_yasg import openapi

class DOCShelper:
    inputPayment = openapi.Schema(
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
            'request_date': openapi.Schema(type=openapi.TYPE_STRING,
                                           description='Payment request date',
                                           format='date'),
            'due_to_date': openapi.Schema(type=openapi.TYPE_STRING,
                                          description='Payment due to date',
                                          format='date'),
            'transactionID': openapi.Schema(type=openapi.TYPE_STRING,
                                            description='Unique transactionID\nformat(********-**)',
                                            max_lenght=11)
        }
    )
    
    validPaymentExample = {
        'payer_email': 'login@domain',
        'amount': 'unsigned integer',
        'currency': 'usd/eur/uah',
        'request_date': 'yyyy-mm-dd',
        'due_to_date': 'yyyy-mm-dd',
        'transactionID': '********-**'
    }
    
    
    responseInvalidGetPaymentByID = {
        'status': '404',
        'message': 'Payment with id [id] not found',
    }
    
    responseValidPost = {
        'status': '200',
        'message': 'Payment has been successfully created.',
        'payment': validPaymentExample
    }
    
    responseInvalidPost = {
        'status': '400',
        'errors': {
            'field': 'error description'
        }
    }
    
    responseValidPut = {
        'status': '200',
        'message': 'Payment with id [id] has been successfully updated.',
        'payment': validPaymentExample
    }
    
    responseValidDelete = {
        'status': '200',
        'message': 'Payment with id [id] has been successfully deleted.',
    }
    

class DOCS:
    get = {
        'operation_name': 'Get a list of all payments from the database',
        'responses': {
            '200': openapi.Response(examples={'application/json': (DOCShelper.validPaymentExample,
                                                                   DOCShelper.validPaymentExample)},
                                    description='List of payments from the database received successfully'),
        }
    }
    
    
    getId = {
        'operation_name': 'Get a payment from the database by ID',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.validPaymentExample},
                                    description='Payment from database successfully received by id'),
            '404': openapi.Response(examples={'application/json': DOCShelper.responseInvalidGetPaymentByID},
                                    description='Payment is missing in the database')
        }
    }
    
    
    post = {
        'body': DOCShelper.inputPayment,
        'operation_name': 'Create new payment and record to the database',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.responseValidPost},
                                    description='Valid data received, payment added to database successfully'),
            '400': openapi.Response(examples={'application/json': DOCShelper.responseInvalidPost},
                                    description='Invalid data received, failed to add payment to database')
        }  
    }
    
    
    put = {
        'body': DOCShelper.inputPayment,
        'operation_name': 'Edit an existing payment in the database',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.responseValidPut},
                                    description='Payment was successfully found in the database and edited'),
            '404': openapi.Response(examples={'application/json': DOCShelper.responseInvalidGetPaymentByID},
                                    description='Payment is missing in the database')
        }
    }
    
    
    delete = {
        'operation_name': 'Delete an existing payment from database by ID',
        'responses': {
            '200': openapi.Response(examples={'application/json': DOCShelper.responseValidDelete},
                                    description='Payment was successfully found in the database and deleted'),
            '404': openapi.Response(examples={'application/json': DOCShelper.responseInvalidGetPaymentByID},
                                    description='Payment is missing in the database')
        }
    }