**Example 1: 示例1 查询实例安全组信息**



Input: 

```
tccli dcdb DescribeDBSecurityGroups --cli-unfold-argument  \
    --Product dcdb \
    --InstanceId tdsqlshard-eb2w7dto
```

Output: 
```
{
    "Response": {
        "RequestId": "31a60135-7057-47ae-8fd3-7a0617deca38",
        "Groups": [
            {
                "ProjectId": 0,
                "CreateTime": "",
                "Inbound": [
                    {
                        "Action": "",
                        "CidrIp": "",
                        "PortRange": "",
                        "IpProtocol": ""
                    }
                ],
                "Outbound": [
                    {
                        "Action": "",
                        "CidrIp": "",
                        "PortRange": "",
                        "IpProtocol": ""
                    }
                ],
                "SecurityGroupId": "",
                "SecurityGroupName": "",
                "SecurityGroupRemark": "dcdb"
            }
        ]
    }
}
```

