import base64
import json


def lambda_handler(event, context):
    records_count = len(event['Records'])
    print(f'kinesis recourds count: {records_count}')

    for record in event['Records']:
        b64_data = record['kinesis']['data']
        data = base64.b64decode(b64_data).decode('utf-8')

        print(data)

    return {
        'statusCode': 200,
        'body': json.dumps(
            {'message': 'hello world'}
        ),
    }
