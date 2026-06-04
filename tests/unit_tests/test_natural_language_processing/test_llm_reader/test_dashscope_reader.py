"""
对 DashScope 平台方法的测试。
"""

from __future__ import annotations

from _old_or_discarded._llm_methods.llm_reader.dashscope_reader import (
    QwenLongReader,
)


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

