import base64
import json
import time

from datetime import datetime

def lambda_handler(event, context):
    print(datetime.now().isoformat())

    records_count = len(event['Records'])
    print(f'kinesis recourds count: {records_count}')

    for record in event['Records']:
        b64_data = record['kinesis']['data']
        data = base64.b64decode(b64_data).decode('utf-8')

        print(data)

    time.sleep(0.05)
    # time.sleep(1)
    # time.sleep(5)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {'message': 'hello world'}
        ),
    }
