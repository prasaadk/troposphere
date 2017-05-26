from . import AWSObject, AWSProperty
from .validators import boolean, integer

class IdentityPool(AWSObject):
    resource_type = "AWS::Cognito::IdentityPool"

    props = {
        'IdentityPoolName': (basestring, False),
        'AllowUnauthenticatedIdentities': (boolean, True),
        'DeveloperProviderName': (basestring, False),
        'SupportedLoginProviders': (dict, False),
        'CognitoIdentityProviders': ([CognitoIdentityProvider], False),
        'SamlProviderARNs': (list, False),
        'OpenIdConnectProviderARNs': (list, False),
        'CognitoStreams': (CognitoStreams, False),
        'PushSync': (PushSync, False),
        'CognitoEvents': (dict, False)
    }

    def validate(self):
        # Check that DeveloperProviderName - letters and
        # periods (.), underscores (_), and dashes (-)
        developer_provider_name = self.properties.get('DeveloperProviderName')
        #TODO

        return True


class IdentityPoolRoleAttachment(AWSObject):
    resource_type = "AWS::Cognito::IdentityPoolRoleAttachment"

    props = {
        'IdentityPoolId': (basestring, True),
        'RoleMappings': (dict, False),
        'Roles': (dict, False)
    }


class UserPool(AWSObject):
    resource_type = "AWS::Cognito::UserPool"

    props = {
        'AdminCreateUserConfig' : (AdminCreateUserConfig, False),
        'AliasAttributes' : ([basestring],False),
        'AutoVerifiedAttributes' : ([basestring],False),
        'DeviceConfiguration' : (DeviceConfiguration,False),
        'EmailConfiguration' : (EmailConfiguration,False),
        'EmailVerificationMessage' : (basestring,False),
        'EmailVerificationSubject' : (basestring,False),
        'LambdaConfig' : (LambdaConfig,False),
        'MfaConfiguration' : (basestring,False),
        'Policies' : (Policies,False),
        'UserPoolName' : (basestring,True),
        'Schema' : ([SchemaAttribute],False),
        'SmsAuthenticationMessage' : (basestring,False),
        'SmsConfiguration' : (SmsConfiguration,False),
        'SmsVerificationMessage' : (basestring,False),
        'UserPoolTags' : (dict, False),
    }

    def validate(self):
        #TODO

        return True


class UserPoolClient(AWSObject):
    resource_type = "AWS::Cognito::UserPoolClient"

    props = {
        'ClientName' : (basestring,False),
        'ExplicitAuthFlows' : ([basestring],False),
        'GenerateSecret' : (boolean,False),
        'ReadAttributes' : ([basestring],False),
        'RefreshTokenValidity' : (integer,False),
        'UserPoolId' : (basestring,True),
        'WriteAttributes' : ([basestring],False)
    }

    def validate(self):
        #TODO

        return True


class UserPoolGroup(AWSObject):
    resource_type = "AWS::Cognito::UserPoolGroup"

    props = {
        'Description' : (basestring,False),
        'GroupName' : (basestring,True),
        'Precedence' : (number,False),
        'RoleArn' : (basestring,False),
        'UserPoolId' : (basestring,True)
    }


class UserPoolUser(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUser"

    props = {
      'DesiredDeliveryMediums' : ([basestring],False),
      'ForceAliasCreation' : (boolean,False),
      'UserAttributes' : ([AttributeType],False),
      'MessageAction' : (basestring,False),
      'Username' : (basestring,False),
      'UserPoolId' : (basestring,True),
      'ValidationData' : ([AttributeType],False)
    }

    def validate(self):
        # TODO
        return True

class UserPoolUserToGroupAttachment(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUserToGroupAttachment"

    props = {
      'GroupName' : (basestring,True),
      'Username' : (basestring,True),
      'UserPoolId' : (basestring,True)
    }

class CognitoIdentityProvider(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitoidentityprovider.html
    props = {
        'ClientId': (basestring, False),
        'ProviderName': (basestring, False),
        'ServerSideTokenCheck': (boolean, False)
    }

class CognitoStreams(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-cognitostreams.html
    props = {
        'RoleArn': (basestring, False),
        'StreamingStatus': (basestring, False),
        'StreamName': (basestring, False)
    }

class PushSync(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypool-pushsync.html
    props = {
        'ApplicationArns': (list, False),
        'RoleArn': (basestring, False)
    }
