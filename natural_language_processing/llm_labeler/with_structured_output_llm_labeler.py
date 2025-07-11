"""
使用具有with_structured_output功能的LLM进行数据标注。
"""

from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage
    from pydantic import BaseModel


class SimpleLabeler:
    """
    对于本身就具有相关功能的LLM，不需要额外的逻辑。
    """
    def __init__(
        self,
        llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        system_message: SystemMessage,
    ):
        self._llm = llm
        self._schema_pydantic_base_model = schema_pydantic_base_model
        self._system_message = system_message

