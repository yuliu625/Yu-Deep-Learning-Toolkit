"""
Sources:

References:

Synopsis:

Notes:
    因为 pytorch_lightning.utilities 中有 move_data_to_device 方法，后续我再没有使用过该自实现的方法。
    lightning 可以自动处理嵌套数据结构，对分布式环境非常有效，因此我再没有使用过相关方法。
"""

import torch


def move_batch_to_device(batch, device):
    """如果数据是dict，然后需要将里面的tensor移动到gpu，用这个方法。"""
    """默认可以发生在：定义好dataset在collate_fn时，在model最开始的forward。"""
    return {key: value.to(device) for key, value in batch.items()}


if __name__ == '__main__':
    pass
