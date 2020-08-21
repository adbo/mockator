import datetime
import json
import random
import string

ITEMS = 10000
WORDS = 100
DATE_FORMAT = '%d-%m-%Y'
HOUR_FORMAT = '%H:%M'

with open('words.json') as words_file:
    words = json.load(words_file)

with open('expression.json') as json_file:
    data = json.load(json_file)
    docs = data[0]
    documents = []

    for lp in range(ITEMS):
        document = {}
        document_name = random.choice(docs.get('args'))
        document[docs.get('name')] = document_name
        end = datetime.datetime.now()
        start = end - datetime.timedelta(days=365)
        date = start + (end - start) * random.random()

        for field in data[1:]:
            field_type = field.get('type')
            if field_type == 'custom_list':
                document[field.get('name')] = random.choice(field.get('args'))
            elif field_type == 'alphanum':
                alpha = ''.join(random.choices(string.ascii_letters, k=field.get('args').get('alpha')))
                num = ''.join(random.choices(string.digits, k=field.get('args').get('num')))
                document[field.get('name')] = f'{alpha}{num}'
            elif field_type == 'word':
                word = random.choice(words)
                document[field.get('name')] = word
            elif field_type == 'date':
                document[field.get('name')] = date.strftime(DATE_FORMAT)
            elif field_type == 'datetime':
                increment_date = date + datetime.timedelta(days=field.get('args').get('increment'))
                document[field.get('name')] = increment_date.strftime(f'{DATE_FORMAT} {HOUR_FORMAT}')
            elif field_type == 'description':
                document[field.get('name')] = f'{document_name} {word}'
            elif field_type == 'email':
                prefix = ''.join(random.choices(string.ascii_letters, k=random.randrange(5, 10)))
                sufix = ''.join(random.choices(string.ascii_letters, k=random.randrange(3, 6)))
                document[field.get('name')] = f'{prefix}@{sufix}.com'.lower()
 
        documents.append(document)

    with open('output.json', 'w') as output:
        output.write("\n".join(f'{{"index":{{"_id": "{i+1}"}}}}\n{v}' for i, v in enumerate((json.dumps(item) for item in documents))))