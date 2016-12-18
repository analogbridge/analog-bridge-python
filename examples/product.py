import analogbridge

print "Get Products API Call"

resp = analogbridge.Product.list()
print resp
