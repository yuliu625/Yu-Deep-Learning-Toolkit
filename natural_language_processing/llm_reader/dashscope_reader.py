"""
Sources:
    https://github.com/yuliu625/Yu-Deep-Learning-Toolkit/natural_language_processing/llm_reader/dashscope_reader.py

References:
    https://help.aliyun.com/zh/model-studio/long-context-qwen-long

Synopsis:
    针对 DashScope 平台的长文本处理方法。

Notes:
    对于极长文本，dashscope 需要上传文件并处理。

    默认支持的模型为 qwen-long ，目前做对于该模型的适配。
"""

from __future__ import annotations
from loguru import logger

from openai import OpenAI

import os
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class QwenLongReader:
    @staticmethod
    def read_file(
        file_id: str,
        system_message_str: str,
        human_message_str: str,
        result_path: str,
    ):
        # 构造client，使用OpenAI Client兼容方法。
        client = OpenAI(
            # HARDCODED
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
        )
        completion = client.chat.completions.create(
            # HARDCODED
            model="qwen-long",
            messages=[
                # sys1: 角色定义
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                # sys2: 文档内容（纯文本或file-id）
                {'role': 'system', 'content': f'fileid://{file_id}'},
                #
                {'role': 'user', 'content': '这篇文章讲了什么?'}
            ],
        )
        logger.info(f"completion: \n{completion}")

