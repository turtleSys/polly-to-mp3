# transforms object data into polly mp3 based on s3 event

import boto3
from botocore.exceptions import BotoCoreError, ClientError
import os
from urllib.parse import unquote_plus

s3 = boto3.client('s3')
polly = boto3.client("polly")


def main(event, context):
    s3_ = boto3.resource('s3')
    for record in event['Records']:
        key = unquote_plus(record['s3']['object']['key'])
        obj = s3_.Object('your-bucket-with-events', key)
        rawText = obj.get()['Body'].read().decode('utf-8')

    try:
        response = polly.synthesize_speech(Text=rawText, OutputFormat="mp3",
                                           VoiceId="Joanna")

    #  not much is being done with this error statement, why is it here?
    except (BotoCoreError, ClientError) as error:
        # print(error)
        print("Polly did not respond with speech.")

    if "AudioStream" in response:
        try:
            with open("/tmp/file.txt", "wb") as file:
                file.write(response['AudioStream'].read())
                file.close()

            s3.upload_file("/tmp/file.txt", "your-output-bucket",
                           f"{key}.mp3")

            with open("/tmp/file.txt", "w") as f:
                f.write('')

        except IOError as error:
            print("Could not write Audio stream to file.")

    else:
        print("Audio stream not returned.")
