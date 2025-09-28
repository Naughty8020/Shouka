from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

class TranslatorModel:
    def __init__(self, src_lang="ja", tgt_lang="en", quantized=True):
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        
        # モデル選択
        model_name = "staka/fugumt-en-ja-int4" if quantized else "staka/fugumt-en-ja"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.int8 if quantized else torch.float32
        )
        
    def set_languages(self, src_lang, tgt_lang):
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    def translate_text(self, text, max_length=512):
        # 入力をトークナイズ
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length).to(self.model.device)
        
        # 翻訳生成
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=max_length)
        
        # トークンを文字列に変換
        translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text
