# Analyzing-Twitter-in-real-time-with-Kinesis-Lambda-Comprehend-and-ElasticSearch

 we are going to set a system to evaluate in real time the sentiment of all Tweets made with a specific Twitter hashtag.
 
 ![](images/1_k_HBTukyqzRFxa8HQz-jkA.png)
 
 We are going to use a basic Python script to obtain real time Tweets thanks to the Twitter API, from the script we’ll put the Tweets directly in a Kinesis Firehose delivery stream where we have a transformation Lambda function, in that moment we are going to obtain the sentiment information using Amazon Comprehend and obtain a clean Twitter comment, finally the Tweet and its sentiment data will be stored in an Elasticsearch domain where we can see real time information using custom charts.


Twitter API
First we’ll need credentials to access the Twitter API so if you don’t have them this is where you can start: https://apps.twitter.com/

Amazon Elasticsearch
Amazon Elasticsearch Service, is a fully managed service that makes it easy for you to deploy, secure, operate, and scale Elasticsearch to search, analyze, and visualize data in real-time.

Lambda Function
Next it’s time to create the Lambda function responsible of data transformation in the delivery stream and add the sentiment information using Amazon Comprehend.

Amazon Kinesis Firehose
Amazon Kinesis Data Firehose is the easiest way to reliably load streaming data into data stores and analytics tools.

