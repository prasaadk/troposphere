from . import AWSObject, AWSProperty
from .validators import boolean, integer, positive_integer, string_length_range, string_list_item
from .constants import AMBIGUOUS_ROLE_RESOLUTION_VALUES as ROLE_RESOLUTION_VALUES,
                       MATCH_TYPE, MFA_CONFIGURATION, EXPLICIT_AUTH_FLOWS, DESIRED_DELIVERY_MEDIUMS,
                       MESSAGE_ACTION

class IdentityPool(AWSObject):
    resource_type = "AWS::Cognito::IdentityPool"

    props = {
        'IdentityPoolName': (string_length_range(1, 128), False),
        'AllowUnauthenticatedIdentities': (boolean, True),
        'DeveloperProviderName': (string_length_range(1, 100), False),
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
        'MfaConfiguration' : (string_list_item(MFA_CONFIGURATION),False),
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
        'ClientName' : (string_length_range(1,128),False),
        'ExplicitAuthFlows' : ([string_list_item(EXPLICIT_AUTH_FLOWS)],False),
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
        'Description' : (string_length_range(0,2048),False),
        'GroupName' : (basestring,True),
        'Precedence' : (positive_integer,False),
        'RoleArn' : (basestring,False),
        'UserPoolId' : (basestring,True)
    }


class UserPoolUser(AWSObject):
    resource_type = "AWS::Cognito::UserPoolUser"

    props = {
      'DesiredDeliveryMediums' : ([string_list_item(DESIRED_DELIVERY_MEDIUMS)],False),
      'ForceAliasCreation' : (boolean,False),
      'UserAttributes' : ([AttributeType],False),
      'MessageAction' : (string_list_item(MESSAGE_ACTION),False),
      'Username' : (string_length_range(1,128),False),
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

# ----- Properties for AWSObject IdentityPool ------
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

# ----- Properties for AWSObject IdentityPoolRoleAttachment ------
class RoleMapping(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping.html
    props = {
        'AmbiguousRoleResolution': (string_list_item(ROLE_RESOLUTION_VALUES), False),
        'RulesConfiguration': (RulesConfiguration, False),
        'ServerSideTokenCheck': (boolean, False)
    }

# ----- Properties for AWSObject UserPool ------
class AdminCreateUserConfig(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig.html
    props = {
        'AllowAdminCreateUserOnly': (boolean, False),
        'InviteMessageTemplate': (InviteMessageTemplate, False),
        'UnusedAccountValidityDays': (integer, False)
    }

class DeviceConfiguration(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-deviceconfiguration.html
    props = {
        'ChallengeRequiredOnNewDevice': (boolean, False),
        'DeviceOnlyRememberedOnUserPrompt': (boolean, False)
    }

class EmailConfiguration(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-emailconfiguration.html
    props = {
        'ReplyToEmailAddress': (basestring, False),
        'SourceArn': (basestring, False)
    }

class LambdaConfig(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-lambdaconfig.html
    props = {
        'CreateAuthChallenge': (basestring, False),
        'CustomMessage': (basestring, False),
        'DefineAuthChallenge': (basestring, False),
        'PostAuthentication': (basestring, False),
        'PostConfirmation': (basestring, False),
        'PreAuthentication': (basestring, False),
        'PreSignUp': (basestring, False),
        'VerifyAuthChallengeResponse': (basestring, False)
    }

class Policies(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-policies.html
    props = {
        'PasswordPolicy': (PasswordPolicy, False)
    }

class SchemaAttribute(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute.html
    props = {
        'AttributeDataType': (basestring, False),
        'DeveloperOnlyAttribute': (boolean, False),
        'Mutable': (boolean, False),
        'Name': (basestring, False),
        'NumberAttributeConstraints': (NumberAttributeConstraints, False),
        'StringAttributeConstraints': (StringAttributeConstraints, False),
        'Required': (boolean, False)
    }

class SmsConfiguration(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-smsconfiguration.html
    props = {
        'ExternalId': (basestring, False),
        'SnsCallerArn': (basestring, True)
    }

# ----- Properties for AWSObject UserPoolUser ------
class AttributeType(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpooluser-attributetype.html
    props = {
        'Name': (basestring, True),
        'Value': (basestring, False)
    }

# ----- Properties for AWSProperty AdminCreateUserConfig ------
class InviteMessageTemplate(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-admincreateuserconfig-invitemessagetemplate.html
    props = {
        'EmailMessage': (basestring, False),
        'EmailSubject': (basestring, False),
        'SMSMessage': (basestring, False)
    }

# ----- Properties for AWSProperty Policies ------
class PasswordPolicy(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-passwordpolicy.html
    props = {
        'MinimumLength': (integer, False),
        'RequireLowercase': (boolean, False),
        'RequireNumbers': (boolean, False),
        'RequireSymbols': (boolean, False),
        'RequireUppercase': (boolean, False)
    }

# ----- Properties for AWSProperty Policies ------
class NumberAttributeConstraints(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute-numberattributeconstraints.html
    props = {
        'MaxLength': (basestring, False),
        'MinLength': (basestring, False)
    }

class StringAttributeConstraints(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-userpool-schemaattribute-stringattributeconstraints.html
    props = {
        'MaxLength': (basestring, False),
        'MinLength': (basestring, False)
    }

# ----- Properties for AWSProperty RoleMapping ------
class RulesConfiguration(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-rolemapping-rulesconfiguration.html
    props = {
        'Rules': ([MappingRule], True)
    }

class MappingRule(AWSProperty):
    # http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cognito-identitypoolroleattachment-mappingrule.html
    props = {
        'Claim': (basestring, True),
        'MatchType': (string_list_item(MATCH_TYPE), True),
        'RoleARN': (basestring, True),
        'Value': (basestring, True)
    }
