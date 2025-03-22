"""

"""

from abc import ABC, abstractmethod


class PromptFactoryInterface(ABC):
    """
    prompt factory必要协议。

    很多时候会面对prompt template的复杂字符串处理，因此更好的处理方法是将所有的方法统一封装。
    这个工厂通常有2个
    """
    @abstractmethod
    def get_system_prompt(self) -> str:
        """
        system prompt，用于设置agent角色。
        """

    @abstractmethod
    def get_message_prompt(self) -> str:
        """
        message prompt，后续信息传递。
        可以由2部分实现，history prompt和inference prompt，然后2者拼接。
        """


class BasePromptFactory(PromptFactoryInterface):
    def __init__(
        self,
    ):
        ...

    def get_system_prompt(self, *args, **kwargs) -> str:
        return ""

    def get_message_prompt(self, *args, **kwargs) -> str:
        return self.get_history_prompt(*args, **kwargs) + self.get_inference_prompt(*args, **kwargs)

    def get_history_prompt(self, *args, **kwargs) -> str:
        return ""

    def get_inference_prompt(self, *args, **kwargs) -> str:
        return ""


if __name__ == '__main__':
    pass
