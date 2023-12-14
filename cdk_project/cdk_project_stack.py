from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as _s3,
)
from constructs import Construct

class CdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="cdkproject2159562",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED


        )

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        
