#!/usr/bin/env python3
import os
from aws_cdk import core

from psc_ebs.psc_ebs_stack import PscEbsStack


app = core.App()
PscEbsStack(app, "psc-ebs", env=core.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"])))

app.synth()
