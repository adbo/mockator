import json
import random

ITEMS = 10000

with open('expression.json') as json_file:
    data = json.load(json_file)
    docs = data[0]
    documents = []

    for lp in range(ITEMS):
        document = {}
        document[docs.get('name')] = random.choice(docs.get('args'))
        documents.append(document)

    with open('output.json', 'w') as output:
        output.write(json.dumps(documents))