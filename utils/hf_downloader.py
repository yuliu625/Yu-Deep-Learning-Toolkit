"""
从huggingface上下载模型和数据集的方法。

我因为网络原因构建了这个工具。
单独配置和运行这个文件，将指定仓库下载到本地。
"""


from huggingface_hub import hf_hub_download, snapshot_download

import os
from pathlib import Path
import asyncio

from abc import ABC, abstractmethod


class HFDownloaderInterface(ABC):
    @abstractmethod
    async def download_models(self, *args, **kwargs):
        ...

    @abstractmethod
    async def download_datasets(self, *args, **kwargs):
        ...


class HFDownloader(HFDownloaderInterface):
    def __init__(
        self,
        local_model_dir: str,
        local_dataset_dir: str,
        is_only_torch: bool = True,
        is_batch_download: bool = True,
    ):
        """
        Args:
            local_model_dir: 本地存储仓库这个文件夹的路径。
            local_dataset_dir: 本地存储仓库这个文件夹的路径。
            is_only_torch: 是否仅下载torch相关的文件。默认为了空间和速度，仅下载torch相关。
            is_batch_download: 是否使用多线程批量下载。
        """
        self.local_model_dir = Path(local_model_dir)
        self.local_dataset_dir = Path(local_dataset_dir)
        self.is_only_torch = is_only_torch
        self.is_batch_download = is_batch_download

        self.set_mirror()

    async def download_models(self, repo_ids: list[str]):
        task = [
            self.download_model(repo_id)
            for repo_id in repo_ids
        ]
        await asyncio.gather(*task)

    async def download_datasets(self, repo_ids: list[str]):
        task = [
            self.download_dataset(repo_id)
            for repo_id in repo_ids
        ]
        await asyncio.gather(*task)

    async def download_model(self, repo_id: str):
        """
        从huggingface上下载模型。

        Args:
            repo_id: huggingface上仓库的id，一般是 "用户名/仓库名" ，可以自动复制的。
        """
        try:
            # 下载模型
            if self.is_only_torch:
                snapshot_download(
                    repo_id=repo_id, local_dir=self.local_model_dir / repo_id,  # 基础选项。
                    allow_patterns=[
                        '*.pt', '*.pth', '*.bin',
                        '*.json', '*.txt', '*.md',
                        '*.safetensors',
                        # '*.tar'
                    ]  # 我不断在检查和总结的torch相关的文件。
                )
            else:
                # 服务器上可以选择这个，完全避免出错。
                snapshot_download(repo_id=repo_id, local_dir=self.local_model_dir / repo_id)
            print(f"下载完成: {repo_id} 已保存到 {self.local_model_dir / repo_id}")
        except Exception as e:
            print(f"下载失败: {e}")

    async def download_dataset(self, repo_id: str):
        """
        从huggingface上下载数据集。
        相比较下载模型，其实仅多了一个kwarg指定仓库类型为数据集。

        Args:
            repo_id: huggingface上仓库的id，一般是 "用户名/仓库名" ，可以自动复制的。
        """
        try:
            # 下载数据集
            snapshot_download(repo_id=repo_id, local_dir=self.local_dataset_dir / repo_id, repo_type="dataset")  # 如果是数据集
            print(f"下载完成: {repo_id} 已保存到 {self.local_dataset_dir / repo_id}")
        except Exception as e:
            print(f"下载失败: {e}")

    def set_mirror(self):
        # 这里更改使用一个镜像。
        os.environ['HF_ENDPOINT'] = "https://hf-mirror.com"
        # os.environ['HF_HOME'] = "~/.cache/huggingface"


if __name__ == "__main__":
    downloader = HFDownloader(
        local_model_dir=r"D:/model/",
        local_dataset_dir=r"D:/dataset/",
        is_only_torch=True,
        is_batch_download=True,
    )

    # 仓库id。
    model_repo_ids = [r"Qwen/Qwen2.5-0.5B-Instruct", r"Qwen/Qwen2-VL-2B-Instruct"]
    dataset_repo_ids = [r"HuggingFaceTB/smoltalk"]

    # asyncio.run(downloader.download_models(model_repo_ids))
    asyncio.run(downloader.download_datasets(dataset_repo_ids))
