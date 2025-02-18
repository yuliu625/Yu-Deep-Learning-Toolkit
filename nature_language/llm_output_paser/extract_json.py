"""
从字符串中提取用markdown代码块包裹的json结果。

一般面对的情况是：指定LLM进行结构化输出，需要从中提取结果。
"""

import re

import json


def extract_json_from_str(response: str) -> dict | None:
    """从字符串格式中提取json格式的输出结果。"""

    # 正则匹配
    pattern = r'```json(.*?)```'
    matches = re.findall(pattern, response, re.DOTALL)

    # print(matches)
    # 如果没有找到。一般在prompt中指定，就不会发生这种情况。
    if not matches:
        return None

    # 提取结果。可能需要根据任务而定。
    raw_data_str: str = matches[0]
    # 转换为dict
    return json.loads(raw_data_str)


if __name__ == '__main__':
    result = extract_json_from_str("""参与者1的选择：```json
{
    "choice": "合作",
    "reason": "根据之前的博弈结果，选择合作能给我带来更多的收益。"
}
```""")
    print(type(result))
    print(result)
