**Example 1: 句向量示例**

特别说明：为方便观看，如下示例中，向量维度仅显示10维。实际维度以原API说明为准。

Input: 

```
tccli nlp SentenceEmbedding --cli-unfold-argument  \
    --Text '"自然语言处理（英语：Natural Language Processing，缩写作 NLP）是人工智能和语言学领域的分支学科。"'
```

Output: 
```
{
    "Response": {
        "RequestId": "8dd99adb-5144-43ca-8213-f6a929ce5075",
        "Dimension": 10,
        "Vector": [
            0.030723740675431842,
            -0.01908946710446959,
            -0.011224565822083284,
            -0.022616868427790263,
            0.03715618769980639,
            0.013664625324856709,
            -0.0033610665978973404,
            -0.0128242685664993,
            -0.002694337080944987,
            0.025049578069764024
        ]
    }
}
```

