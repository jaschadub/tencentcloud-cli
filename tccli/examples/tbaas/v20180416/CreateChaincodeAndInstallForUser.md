**Example 1: CreateChaincodeAndInstallForUser**



Input: 

```
tccli tbaas CreateChaincodeAndInstallForUser --cli-unfold-argument  \
    --Module chaincode_mng \
    --Operation chaincode_create_and_install_for_user \
    --ClusterId 251005746envnew \
    --GroupName hellorog \
    --PeerName peer0-neworg02.envnew \
    --ChaincodeName query \
    --ChaincodeVersion v1.0 \
    --ChaincodeFileType gozip \
    --Chaincode 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
```

Output: 
```
{
    "Response": {
        "RequestId": "ccdc6830-a23e-4bd6-a092-0ec6ee7e6bfe"
    }
}
```

