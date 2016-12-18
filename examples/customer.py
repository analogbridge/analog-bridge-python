import analogbridge

analogbridge.api_key = 'sk_test_cbZtmVPuwoyHjN61wq0GYLOZ'
customer_id = "cus_3ab7aa6ec5feda6fe8a3"

print("Find specific customer")

resp = analogbridge.Customer.find(customer_id)
print(resp['auth'])


print("Create new customer")
params = {
    "email": "test@gmail.com",
    "shipping": {
        "first_name": "Abe"
    }
}

resp = analogbridge.Customer.create(params=params)

print(resp['cus_id'])
print(resp['email'])
print(resp['shipping']['first_name'])
print(resp['shipping']['last_name'])

print("Update customer")
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

resp = analogbridge.Customer.update(customer_id=resp['cus_id'], params=params)
t = resp['metadata']


print("Delete customer")
resp = analogbridge.Customer.delete(resp['cus_id'])
print(resp['deleted'])


print("list all customers")
resp = analogbridge.Customer.list(limit=15, offset=10)
print(resp)






