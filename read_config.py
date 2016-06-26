import json
with open('client_id.json') as fh:
    config = json.load(fh)

#print config['password']
print config