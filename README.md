# Analog Bridge

Analog Bridge is comprised of a JavaScript client and REST API which enables
your users to import analog media directly into your app or website.

Full documentation at the [Analog Bridge docs](https://analogbridge.io/docs#python)

## Installation

Install with pip:

```python
pip install analogbridge
```

Or download the source:

```sh
$ git clone https://github.com/analogbridge/analog-bridge-python.git
```

## Configure

Once you have your API Keys from Analog Bridge, you can initialize your configuration with your `secret_key` as

```python
import analogbridge
analogbridge.api_key = 'YOUR_SECRET_KEY'
```

## Usage

### Customer

#### Create Customer

To create a new customer using the API, usage

```python
params = {
    "email": "test@gmail.com",
    "shipping": {
        "first_name": "Abe"
    }
}

resp = analogbridge.Customer.create(params=params)
```

#### Retrieve a Customer

We can easily retrieve a customer's details using their `customer_id`, for
example to find a customer with details with id `cus_12345678`

```python
resp = analogbridge.Customer.find('cus_12345678')
```

### Retrieve all customers

Analog Bridge provides an interface to retrieve all your customers very easily.
To retrieve all of your customers, you can use

```python
resp = analogbridge.Customer.list(limit=15, offset=10)
```

#### Update a customer

Update an existing customer's information by using the `cus_id` from customer
creation. Any unprovided parameters will have no effect on the customer object.
The arguments for this call are mainly the same as for the customer creation
call.

```python
params = {
    "email": "test@gmail.com",
    "shipping": {
        "first_name": "Abe",
        "last_name": "Smith",
        "city": "Chicago"
    },
    "metadata": {
        "user_class": "VIP"
    }
}

resp = analogbridge.Customer.update(customer_id='cus_12345678', params=params)
```

#### Delete a customer

If we need to delete a customer, for example id `cus_123456789`, then we can
use

```python
resp = analogbridge.Customer.delete('cus_123456789')
```

### Order

#### List all customer orders

The Analog Bridge API allow us to retrieve all orders by a specific `customer`.
For example we want to retrieve all `orders` by customer id `cus_12345678`,
we can use

```python
resp = analogbridge.Order.where(customer_id='cus_12345678')
```

#### List order details

If we need to retrieve the details for a specific order then we can use

```python
resp = analogbridge.Order.where(customer_id='cus_12345678', order_id='ord_12345678')
```

#### Retrieve import ready orders
Once customer orders have been processed and uploaded to our Cloud, they are import-ready for your system.
To retrieve the list of import ready orders, we can use

```python
resp = analogbridge.Order.import_ready()
```

### Listing Product

To retrieve the `products` simply use the following interface

```python
resp = analogbridge.Product.list()
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/analogbridge/analog-bridge-python. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

This package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).