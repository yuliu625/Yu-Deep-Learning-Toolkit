"""
Sources:
    https://github.com/yuliu625/Yu-Deep-Learning-Toolkit/blob/main/src/agnostic_utils/pil_image_bridge.py

References:
    None

Synopsis:
    PIL.Image 的部分常见处理方法。

Notes:

"""

from __future__ import annotations
from loguru import logger

import base64
from PIL import Image
from io import BytesIO

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class PILImageBridge:
    """
    PIL.Image 的部分常见处理方法。
    """

    @staticmethod
    def base64_to_pil(
        image_base64: str,
    ) -> Image.Image:
        """
        将 base64 字符串转换为原始图片。

        主要用于:
            - 可视化查看图片。测试转换正常。
            - 读写。转换为模型可接受格式，转换为 VLM-API 可传输格式。

        Args:
            image_base64: 图片的 base64 编码后的字符串。

        Returns:
            Image: 二进制图片格式。
        """
        image_data = base64.b64decode(image_base64)
        image = Image.open(BytesIO(image_data))
        return image

    @staticmethod
    def uri_to_base64(
        uri: str,
    ) -> str:
        """
        从 uri 读取图片转换为 base64 字符串。

        Args:
            uri: 图片的 uri 。

        Returns:
            str: base64 字符串。
        """
        with open(uri, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

