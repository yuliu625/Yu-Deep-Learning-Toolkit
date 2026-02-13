"""
Sources:
    https://github.com/yuliu625/Yu-Deep-Learning-Toolkit/natural_language_processing/llm_reader/openai_file_manager.py

References:

Synopsis:
    基于 OpenAI SDK 的文件管理方法。

Notes:

"""

from __future__ import annotations
from loguru import logger

from openai import OpenAI

import os
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class OpenAIFileManager:
    @staticmethod
    def create_files():
        ...

    @staticmethod
    def retrieve_files():
        ...

    @staticmethod
    def list_files():
        ...

    @staticmethod
    def delete_files():
        ...

