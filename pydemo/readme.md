# 

```bash
# 客户端
pip install -i https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir open-text-embeddings openai 
```

服务器

intfloat/e5-large-v2 这是个英文模型，所有框架都可复用， 只要配置使用自己找的中文模型即可。

## 向量生成

模型 

https://huggingface.co/intfloat/e5-large-v2

https://github.com/limcheekin/open-text-embeddings

```bash
# 安装服务
pip install --no-cache-dir open-text-embeddings[server]

# 依赖
pip install InstructorEmbedding sentence_transformers huggingface-hub

# 启动服务
python -m open.text.embeddings.server

# 指定使用 cpu 启动
DEVICE=cpu python -m open.text.embeddings.server

# 指定 intfloat/e5-large-v2 模型 和 使用 cpu 启动
MODEL=intfloat/e5-large-v2 DEVICE=cpu python -m open.text.embeddings.server
```


## 模型下载

```bat
@rem 因为墙 需要使用 huggingface_hub 设置镜像

@rem 安装
pip install -U huggingface_hub

@rem 设置镜像
$env:HF_ENDPOINT="https://hf-mirror.com"

@rem 下载到指定路径
huggingface-cli download --resume-download intfloat/e5-large-v2 --local-dir cache/huggingface/hub
```

## 中文


https://github.com/Embedding/Chinese-Word-Vectors


腾讯向量词
https://ai.tencent.com/ailab/nlp/en/embedding.html
