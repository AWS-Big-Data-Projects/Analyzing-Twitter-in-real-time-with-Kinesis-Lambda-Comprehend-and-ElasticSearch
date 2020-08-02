from __future__ import print_function

import base64
import json
import boto3

print('Loading function')

def lambda_handler(event, context):
    output = []

    for record in event['records']:
        
        dict_data = base64.b64decode(record['data']).decode('utf-8').strip()
        print(dict_data)
        
        comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
        sentiment_all = comprehend.detect_sentiment(Text=dict_data, LanguageCode='en')
        sentiment = sentiment_all['Sentiment']
        print(sentiment)
        positive = sentiment_all['SentimentScore']['Positive']
        negative = sentiment_all['SentimentScore']['Negative']
        total = positive - negative
        print(total)
        
        data_record = {
            'message': dict_data,
            'sentiment': sentiment,
            'total': total
        }
        print(data_record)
        
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(data_record).encode('utf-8')).decode('utf-8')
        }
        print(output_record)
        
        output.append(output_record)

    print(output)
    return {'records': output}
