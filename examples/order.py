import analogbridge

analogbridge.api_key = 'sk_test_cbZtmVPuwoyHjN61wq0GYLOZ'
customer_id = "cus_3ab7aa6ec5feda6fe8a3"
order_id = "ord_fe310b878dc3313c3c2e"

print "All orders import-ready"
resp = analogbridge.Order.import_ready()
print resp

print "Get all orders for customer"
resp = analogbridge.Order.where(customer_id=customer_id, order_id=order_id)
print resp