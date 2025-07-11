"""
我用我的方法实现的标注器。

必要的依赖:
    - langchain

需要使用的其他我构建的工具:
    - JsonOutputExtractor

暂时的实现:
    - 仅基于文本任务。
"""

from __future__ import annotations
import asyncio

# 解析和验证结构化数据的工具。可以是我自构建的，需要在具体项目指定具体路径。
from natural_language_processing.llm_output.structured_data_extractor import StructuredDataExtractor
from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage, AIMessage
    from pydantic import BaseModel


class YuLabeler:
    """
    我实现的标注器。

    需要使用其他的自构建的工具。
    """
    def __init__(
        self,
        llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        system_message: SystemMessage,
        max_retries: int = 10,
    ):
        self._llm = llm
        self._schema_pydantic_base_model = schema_pydantic_base_model
        self._system_message = system_message
        self._max_retries = max_retries

    # ====暴露方法。====
    async def batch_label_datas(
        self,
        datas: list[str],
    ) -> list[str]:
        tasks = [self.label_data(data=data) for data in datas]
        return await asyncio.gather(*tasks)

    # ====主要方法。====
    async def label_data(
        self,
        data: str,
    ) -> BaseModel:
        for _ in range(self._max_retries):
            response = await self._call_llm(
                human_message=HumanMessage(content=data),
            )
            structured_data = StructuredDataExtractor.extract_structured_data_from_str(
                raw_str=response.content,
                schema_pydantic_base_model=self._schema_pydantic_base_model,
                index_to_choose=-1,
                json_loader_name='json-repair',
                schema_check_type='dict',
            )
            if structured_data:
                return structured_data

    # ====基础方法。====
    async def _call_llm(
        self,
        human_message: HumanMessage,
    ) -> AIMessage:
        response = await self._llm.ainvoke(input=[
            self._system_message,
            human_message,
        ])
        return response

