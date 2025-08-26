# Deep Learning Toolkit
一个为各种深度学习任务提供可复用工具的集合。

## 概述
这个仓库旨在提供一个通用的工具箱，帮助开发者和研究者快速应对常见的深度学习任务。它包含了一系列精选的模块和工具，特别是在**自然语言处理 (NLP)** 领域。

由于我目前的研究方向主要集中在NLP，`natural_language_processing` 目录下的工具会得到更频繁的更新和维护。


## 主要内容
### 🤖 自然语言处理 (NLP)
此部分包含一系列针对NLP任务的实用工具，特别是与大型语言模型 (LLM) 相关的处理方法。
- **llm_input**: 提供多种处理方法，用于优化不同任务下LLM的输入。
- **llm_output**: 专注于处理LLM的输出，尤其擅长结构化数据提取和处理。
- **llm_labeler**: 提供了多种实现方式，用于利用LLM进行简单的数据标注任务。
- **zero_shot_classification**: 一个零样本分类器，适用于对低级语义文本进行快速分类，可作为项目初期文本处理的有效工具。

### 其他工具集
此部分包含了我在其他深度学习领域实现的一些实用工具。
#### 🎵 音频处理 (Audio)
- **automatic_speech_recognition**: 一个用于音频转录的语音识别工具。
#### 💻 计算机视觉 (Computer Vision)
- **object_detection**: 实现了图像中的目标检测及基于此的目标追踪方法。
- **optical_character_recognition**: 一个OCR工具，用于识别图像中的字符内容。
- **utils**: 包含图像处理相关的通用工具和函数。
#### 🎨 多模态 (Multimodal)
- **sematic_similarity**: 提供了跨模态的语义相似度比较方法。


## 更多资源
本仓库可能不会频繁更新，如果你对更活跃的项目感兴趣，可以查看我的其他工具集仓库，它们针对特定任务提供了更深入的解决方案：
- **Data Science Toolkit**: 一个用于数据科学任务的通用工具集，更新频繁。
  - 🔗 [Data-Science-Toolkit](https://github.com/yuliu625/Yu-Data-Science-Toolkit)
- **Agent Development Toolkit**: 专注于LLM和Agent构建的工具集，是本仓库中部分任务的具体应用实现。
  - 🔗 [Agent-Development-Toolkit](https://github.com/yuliu625/Yu-Agent-Development-Toolkit)
- **PDF Toolkit**: 专门用于处理PDF文件的工具库。
  - 🔗 [PDF-Toolkit](https://github.com/yuliu625/Yu-PDF-Toolkit)
- **RAG Toolkit**: 构建RAG（检索增强生成）系统所需的工具集合。
  - 🔗 [RAG-Toolkit](https://github.com/yuliu625/Yu-RAG-Toolkit)
- **Flash Boilerplate**: 一个用于快速启动标准深度学习项目的模板仓库。
  - 🔗 [Flash-Boilerplate](https://github.com/yuliu625/Yu-Flash-Boilerplate)

