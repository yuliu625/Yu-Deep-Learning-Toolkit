"""
我用我的方法实现的标注器。

必要的依赖:
    - langchain

需要使用的其他我构建的工具:
    - JsonOutputExtractor
"""

from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AIMessage
    from pydantic import BaseModel


class Labeler:
    """
    自实现的标注器。
    """
    def __init__(
        self,
        llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
    ):
        self._llm = llm
        self._schema_pydantic_base_model = schema_pydantic_base_model

    def label_datas(
        self,
        datas: list[str],
    ):
        ...

    def annotate_message(
        self,
    ) -> BaseModel:
        ...

    def _call_llm(
        self,
    ) -> AIMessage:
        ...

