#!/usr/bin/env python3

from aws_cdk import core

from mp3_polly_lambda.mp3_polly_lambda_stack import Mp3PollyLambdaStack


app = core.App()
Mp3PollyLambdaStack(app, "mp3-polly-lambda")

app.synth()
