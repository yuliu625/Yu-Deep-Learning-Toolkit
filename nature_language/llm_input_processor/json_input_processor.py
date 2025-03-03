
import json


class JsonInputProcessor:
    def __init__(self):
        pass

    @staticmethod
    def put_in_markdown(json_str: str) -> str:
        """
        将已经转换好的json数据放入markdown的代码块中。
        Args:
            - json_str: 字符串的json，不可以是dict。会有很小的问题是: 引号是单引号。
        Return:
            - 字符串的结构化输入。
        """
        return f"```json\n{json_str}\n```"

    @staticmethod
    def escape_braces(string: str) -> str:
        """
        替换大括号。
        主要为了使得f-string可以正常解析。
        """
        string = string.replace("{", "{{").replace("}", "}}")
        return string


if __name__ == '__main__':
    pass
    # print(JsonInputProcessor.put_in_markdown({"a": 1, "b": 2}))
