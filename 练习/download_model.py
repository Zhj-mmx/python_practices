# download_model.py
import os
from transformers import BertTokenizer, BertForSequenceClassification

# 确保使用镜像
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'

# 下载模型和分词器
model_name = "bert-base-chinese"
print("开始下载模型...")

tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)

# 保存到本地
model.save_pretrained("./bert_base_chinese")
tokenizer.save_pretrained("./bert_base_chinese")
print("模型下载完成！")
