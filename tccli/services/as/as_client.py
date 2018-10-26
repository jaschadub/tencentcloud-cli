# -*- coding: utf-8 -*-
import os
import json
import tccli.options_define as OptionsDefine
import tccli.format_output as FormatOutput
from tccli.nice_command import NiceCommand
import tccli.error_msg as ErrorMsg
import tccli.help_template as HelpTemplate
from tccli import __version__
from tccli.utils import Utils
from tccli.configure import Configure
from tencentcloud.common import credential
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.as.v20180419 import as_client as as_client_v20180419
from tencentcloud.as.v20180419 import models as models_v20180419
from tccli.services.as import v20180419
from tccli.services.as.v20180419 import help as v20180419_help


def doRemoveInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("RemoveInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.RemoveInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.RemoveInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupName": Utils.try_to_json(argv, "--AutoScalingGroupName"),
        "LaunchConfigurationId": Utils.try_to_json(argv, "--LaunchConfigurationId"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "DefaultCooldown": Utils.try_to_json(argv, "--DefaultCooldown"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "LoadBalancerIds": Utils.try_to_json(argv, "--LoadBalancerIds"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "ForwardLoadBalancers": Utils.try_to_json(argv, "--ForwardLoadBalancers"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),
        "TerminationPolicies": Utils.try_to_json(argv, "--TerminationPolicies"),
        "Zones": Utils.try_to_json(argv, "--Zones"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteScheduledAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteScheduledAction", g_param[OptionsDefine.Version])
        return

    param = {
        "ScheduledActionId": Utils.try_to_json(argv, "--ScheduledActionId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteScheduledActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteScheduledAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDetachInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DetachInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DetachInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DetachInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateScheduledAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateScheduledAction", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),
        "ScheduledActionName": Utils.try_to_json(argv, "--ScheduledActionName"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "Recurrence": Utils.try_to_json(argv, "--Recurrence"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateScheduledActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateScheduledAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyScheduledAction(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyScheduledAction", g_param[OptionsDefine.Version])
        return

    param = {
        "ScheduledActionId": Utils.try_to_json(argv, "--ScheduledActionId"),
        "ScheduledActionName": Utils.try_to_json(argv, "--ScheduledActionName"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "StartTime": Utils.try_to_json(argv, "--StartTime"),
        "EndTime": Utils.try_to_json(argv, "--EndTime"),
        "Recurrence": Utils.try_to_json(argv, "--Recurrence"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyScheduledActionRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyScheduledAction(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doCreateLaunchConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("CreateLaunchConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationName": Utils.try_to_json(argv, "--LaunchConfigurationName"),
        "InstanceType": Utils.try_to_json(argv, "--InstanceType"),
        "ImageId": Utils.try_to_json(argv, "--ImageId"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "SystemDisk": Utils.try_to_json(argv, "--SystemDisk"),
        "DataDisks": Utils.try_to_json(argv, "--DataDisks"),
        "InternetAccessible": Utils.try_to_json(argv, "--InternetAccessible"),
        "LoginSettings": Utils.try_to_json(argv, "--LoginSettings"),
        "SecurityGroupIds": Utils.try_to_json(argv, "--SecurityGroupIds"),
        "EnhancedService": Utils.try_to_json(argv, "--EnhancedService"),
        "UserData": Utils.try_to_json(argv, "--UserData"),
        "InstanceChargeType": Utils.try_to_json(argv, "--InstanceChargeType"),
        "InstanceMarketOptions": Utils.try_to_json(argv, "--InstanceMarketOptions"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.CreateLaunchConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.CreateLaunchConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),
        "AutoScalingGroupName": Utils.try_to_json(argv, "--AutoScalingGroupName"),
        "DefaultCooldown": Utils.try_to_json(argv, "--DefaultCooldown"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),
        "LaunchConfigurationId": Utils.try_to_json(argv, "--LaunchConfigurationId"),
        "MaxSize": Utils.try_to_json(argv, "--MaxSize"),
        "MinSize": Utils.try_to_json(argv, "--MinSize"),
        "ProjectId": Utils.try_to_json(argv, "--ProjectId"),
        "SubnetIds": Utils.try_to_json(argv, "--SubnetIds"),
        "TerminationPolicies": Utils.try_to_json(argv, "--TerminationPolicies"),
        "VpcId": Utils.try_to_json(argv, "--VpcId"),
        "Zones": Utils.try_to_json(argv, "--Zones"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doEnableAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("EnableAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.EnableAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.EnableAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAutoScalingInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAutoScalingInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAutoScalingInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAutoScalingGroups(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAutoScalingGroups", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupIds": Utils.try_to_json(argv, "--AutoScalingGroupIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAutoScalingGroupsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAutoScalingGroups(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeScheduledActions(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeScheduledActions", g_param[OptionsDefine.Version])
        return

    param = {
        "ScheduledActionIds": Utils.try_to_json(argv, "--ScheduledActionIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Offset": Utils.try_to_json(argv, "--Offset"),
        "Limit": Utils.try_to_json(argv, "--Limit"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeScheduledActionsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeScheduledActions(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDeleteLaunchConfiguration(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DeleteLaunchConfiguration", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationId": Utils.try_to_json(argv, "--LaunchConfigurationId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DeleteLaunchConfigurationRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DeleteLaunchConfiguration(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDisableAutoScalingGroup(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DisableAutoScalingGroup", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DisableAutoScalingGroupRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DisableAutoScalingGroup(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeLaunchConfigurations(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeLaunchConfigurations", g_param[OptionsDefine.Version])
        return

    param = {
        "LaunchConfigurationIds": Utils.try_to_json(argv, "--LaunchConfigurationIds"),
        "Filters": Utils.try_to_json(argv, "--Filters"),
        "Limit": Utils.try_to_json(argv, "--Limit"),
        "Offset": Utils.try_to_json(argv, "--Offset"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeLaunchConfigurationsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeLaunchConfigurations(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doDescribeAccountLimits(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("DescribeAccountLimits", g_param[OptionsDefine.Version])
        return

    param = {

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.DescribeAccountLimitsRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.DescribeAccountLimits(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doAttachInstances(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("AttachInstances", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),
        "InstanceIds": Utils.try_to_json(argv, "--InstanceIds"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.AttachInstancesRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.AttachInstances(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


def doModifyDesiredCapacity(argv, arglist):
    g_param = parse_global_arg(argv)
    if "help" in argv:
        show_help("ModifyDesiredCapacity", g_param[OptionsDefine.Version])
        return

    param = {
        "AutoScalingGroupId": Utils.try_to_json(argv, "--AutoScalingGroupId"),
        "DesiredCapacity": Utils.try_to_json(argv, "--DesiredCapacity"),

    }
    cred = credential.Credential(g_param[OptionsDefine.SecretId], g_param[OptionsDefine.SecretKey])
    http_profile = HttpProfile(
        reqTimeout=60 if g_param[OptionsDefine.Timeout] is None else int(g_param[OptionsDefine.Timeout]),
        reqMethod="POST",
        endpoint=g_param[OptionsDefine.Endpoint]
    )
    profile = ClientProfile(httpProfile=http_profile, signMethod="HmacSHA256")
    mod = CLIENT_MAP[g_param[OptionsDefine.Version]]
    client = mod.AsClient(cred, g_param[OptionsDefine.Region], profile)
    client._sdkVersion += ("_CLI_" + __version__)
    models = MODELS_MAP[g_param[OptionsDefine.Version]]
    model = models.ModifyDesiredCapacityRequest()
    model.from_json_string(json.dumps(param))
    rsp = client.ModifyDesiredCapacity(model)
    result = rsp.to_json_string()
    jsonobj = None
    try:
        jsonobj = json.loads(result)
    except TypeError as e:
        jsonobj = json.loads(result.decode('utf-8')) # python3.3
    FormatOutput.output("action", jsonobj, g_param[OptionsDefine.Output], g_param[OptionsDefine.Filter])


CLIENT_MAP = {
    "v20180419": as_client_v20180419,

}

MODELS_MAP = {
    "v20180419": models_v20180419,

}

ACTION_MAP = {
    "RemoveInstances": doRemoveInstances,
    "CreateAutoScalingGroup": doCreateAutoScalingGroup,
    "DeleteScheduledAction": doDeleteScheduledAction,
    "DetachInstances": doDetachInstances,
    "CreateScheduledAction": doCreateScheduledAction,
    "ModifyScheduledAction": doModifyScheduledAction,
    "CreateLaunchConfiguration": doCreateLaunchConfiguration,
    "ModifyAutoScalingGroup": doModifyAutoScalingGroup,
    "EnableAutoScalingGroup": doEnableAutoScalingGroup,
    "DescribeAutoScalingInstances": doDescribeAutoScalingInstances,
    "DescribeAutoScalingGroups": doDescribeAutoScalingGroups,
    "DescribeScheduledActions": doDescribeScheduledActions,
    "DeleteAutoScalingGroup": doDeleteAutoScalingGroup,
    "DeleteLaunchConfiguration": doDeleteLaunchConfiguration,
    "DisableAutoScalingGroup": doDisableAutoScalingGroup,
    "DescribeLaunchConfigurations": doDescribeLaunchConfigurations,
    "DescribeAccountLimits": doDescribeAccountLimits,
    "AttachInstances": doAttachInstances,
    "ModifyDesiredCapacity": doModifyDesiredCapacity,

}

AVAILABLE_VERSION_LIST = [
    v20180419.version,

]
AVAILABLE_VERSIONS = {
     'v' + v20180419.version.replace('-', ''): {"help": v20180419_help.INFO,"desc": v20180419_help.DESC},

}


def as_action(argv, arglist):
    if "help" in argv:
        versions = sorted(AVAILABLE_VERSIONS.keys())
        opt_v = "--" + OptionsDefine.Version
        version = versions[-1]
        if opt_v in argv:
            version = 'v' + argv[opt_v].replace('-', '')
        if version not in versions:
            print("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
            return
        action_str = ""
        docs = AVAILABLE_VERSIONS[version]["help"]
        desc = AVAILABLE_VERSIONS[version]["desc"]
        for action, info in docs.items():
            action_str += "        %s\n" % action
            action_str += Utils.split_str("        ", info["desc"], 120)
        helpstr = HelpTemplate.SERVICE % {"name": "as", "desc": desc, "actions": action_str}
        print(helpstr)
    else:
        print(ErrorMsg.FEW_ARG)


def version_merge():
    help_merge = {}
    for v in AVAILABLE_VERSIONS:
        for action in AVAILABLE_VERSIONS[v]["help"]:
            if action not in help_merge:
                help_merge[action] = {}
            help_merge[action]["cb"] = ACTION_MAP[action]
            help_merge[action]["params"] = []
            for param in AVAILABLE_VERSIONS[v]["help"][action]["params"]:
                if param["name"] not in help_merge[action]["params"]:
                    help_merge[action]["params"].append(param["name"])
    return help_merge


def register_arg(command):
    cmd = NiceCommand("as", as_action)
    command.reg_cmd(cmd)
    cmd.reg_opt("help", "bool")
    cmd.reg_opt(OptionsDefine.Version, "string")
    help_merge = version_merge()

    for actionName, action in help_merge.items():
        c = NiceCommand(actionName, action["cb"])
        cmd.reg_cmd(c)
        c.reg_opt("help", "bool")
        for param in action["params"]:
            c.reg_opt("--" + param, "string")

        for opt in OptionsDefine.ACTION_GLOBAL_OPT:
            stropt = "--" + opt
            c.reg_opt(stropt, "string")


def parse_global_arg(argv):
    params = {}
    for opt in OptionsDefine.ACTION_GLOBAL_OPT:
        stropt = "--" + opt
        if stropt in argv:
            params[opt] = argv[stropt]
        else:
            params[opt] = None
    if params[OptionsDefine.Version]:
        params[OptionsDefine.Version] = "v" + params[OptionsDefine.Version].replace('-', '')

    config_handle = Configure()
    profile = config_handle.profile
    if ("--" + OptionsDefine.Profile) in argv:
        profile = argv[("--" + OptionsDefine.Profile)]

    is_conexist, conf_path = config_handle._profile_existed(profile + "." + config_handle.configure)
    is_creexist, cred_path = config_handle._profile_existed(profile + "." + config_handle.credential)
    config = {}
    cred = {}
    if is_conexist:
        config = config_handle._load_json_msg(conf_path)
    if is_creexist:
        cred = config_handle._load_json_msg(cred_path)

    for param in params.keys():
        if param == OptionsDefine.Version:
            continue
        if params[param] is None:
            if param in [OptionsDefine.SecretKey, OptionsDefine.SecretId]:
                if param in cred:
                    params[param] = cred[param]
                else:
                    raise Exception("%s is invalid" % param)
            else:
                if param in config:
                    params[param] = config[param]
                elif param == OptionsDefine.Region:
                    raise Exception("%s is invalid" % OptionsDefine.Region)
    try:
        if params[OptionsDefine.Version] is None:
            version = config["as"][OptionsDefine.Version]
            params[OptionsDefine.Version] = "v" + version.replace('-', '')

        if params[OptionsDefine.Endpoint] is None:
            params[OptionsDefine.Endpoint] = config["as"][OptionsDefine.Endpoint]
    except Exception as err:
        raise Exception("config file:%s error, %s" % (conf_path, str(err)))
    versions = sorted(AVAILABLE_VERSIONS.keys())
    if params[OptionsDefine.Version] not in versions:
        raise Exception("available versions: %s" % " ".join(AVAILABLE_VERSION_LIST))
    return params


def show_help(action, version):
    docs = AVAILABLE_VERSIONS[version]["help"][action]
    desc = AVAILABLE_VERSIONS[version]["desc"]
    docstr = ""
    for param in docs["params"]:
        docstr += "        %s\n" % ("--" + param["name"])
        docstr += Utils.split_str("        ", param["desc"], 120)

    helpmsg = HelpTemplate.ACTION % {"name": action, "service": "as", "desc": desc, "params": docstr}
    print(helpmsg)


def get_actions_info():
    config = Configure()
    new_version = max(AVAILABLE_VERSIONS.keys())
    version = new_version
    try:
        profile = config._load_json_msg(os.path.join(config.cli_path, "default.configure"))
        version = profile["as"]["version"]
        version = "v" + version.replace('-', '')
    except Exception:
        pass
    if version not in AVAILABLE_VERSIONS.keys():
        version = new_version
    return AVAILABLE_VERSIONS[version]["help"]
