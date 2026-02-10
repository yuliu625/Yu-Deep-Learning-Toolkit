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

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class QwenLongReader:
    ...

