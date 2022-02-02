from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
)


class OIDCProviderStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_oidc_provider = iam.CfnOIDCProvider(
            self, "MyCfnOIDCProvider",
            thumbprint_list=["6938fd4d98bab03faadb97b34396831e3780aea1"],
            client_id_list=["sts.amazonaws.com"],
            url="https://token.actions.githubusercontent.com"
        )

        oidc_role = iam.Role(
            self, 
            'OIDCRole', 
            assumed_by=iam.FederatedPrincipal(
                federated=cfn_oidc_provider.attr_arn,
                conditions={
                    "StringLike": {
                        "token.actions.githubusercontent.com:sub": "repo:theo-r/aws-oidc-provider:*",
                        }
                })
            )
        
        oidc_role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name('ReadOnlyAccess'))
