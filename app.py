#!/usr/bin/env python3

from aws_cdk import core

from psc_ebs.psc_ebs_stack import PscEbsStack


app = core.App()
PscEbsStack(app, "psc-ebs")

app.synth()
