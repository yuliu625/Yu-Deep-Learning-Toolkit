"""
对 DashScope 平台方法的测试。
"""

from __future__ import annotations
import pytest
from loguru import logger

from natural_language_processing.llm_reader.dashscope_reader import (
    QwenLongReader,
)

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestQwenLongReader:
    # @pytest.mark.parametrize()
    def test_qwen_long_reader(
        self,
    ) -> None:
        QwenLongReader.read_file(
            file_id='001.md',
            system_message_content="You are a helpful assistant.",
            human_message_content="What is your model id?",
            result_path='./t_result.json',
        )

