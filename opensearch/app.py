#!/usr/bin/env python3
import os

import aws_cdk as cdk

from opensearch.opensearch_stack import OpensearchStack


app = cdk.App()
OpensearchStack(app, "OpensearchStack",
    env=cdk.Environment(region='eu-central-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
