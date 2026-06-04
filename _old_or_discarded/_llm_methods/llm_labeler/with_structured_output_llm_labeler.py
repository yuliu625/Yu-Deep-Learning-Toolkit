"""
使用具有with_structured_output功能的LLM进行数据标注。
"""

from __future__ import annotations

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING, cast
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
        self._structured_llm = self._get_structured_llm(
            llm=llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
        )
        self._system_message = system_message

    async def label_data(
        self,
        data: str,
    ) -> BaseModel:
        structured_data = await self._call_llm(
            human_message=HumanMessage(content=data),
        )
        return structured_data

    async def _call_llm(
        self,
        human_message: HumanMessage,
    ) -> BaseModel:
        response = await self._structured_llm.ainvoke(input=[
            self._system_message,
            human_message,
        ])
        return response

    def _get_structured_llm(
        self,
        llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
    ) -> BaseChatModel:
        structured_llm = llm.with_structured_output(
            schema=schema_pydantic_base_model,
        )
        structured_llm = cast('BaseChatModel', structured_llm)
        return structured_llm

