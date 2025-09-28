from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

class TranslatorModel:
    def __init__(self, src_lang="ja", tgt_lang="en"):
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        model_name = "staka/fugumt-en-ja"  # 日本語→英語
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate_text(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=512)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
