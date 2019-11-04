from aws_cdk import (
    aws_lambda as lambda_,
    aws_lambda_event_sources as les,
    aws_s3 as _s3,
    aws_s3_notifications as notifications,
    core
)


class Mp3PollyLambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function = lambda_.Function(self, "lambda_function",
                                    runtime=lambda_.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    code=lambda_.Code.asset("./lambda"),
                                    )

        s3 = _s3.Bucket(self, "Polly_Stage")

        notification = notifications.LambdaDestination(function)

        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
