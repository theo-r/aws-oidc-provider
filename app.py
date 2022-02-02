#!/usr/bin/env python

import aws_cdk as cdk

from oidc_provider_stack import OIDCProviderStack


app = cdk.App()
OIDCProviderStack(app, "aws")

app.synth()
