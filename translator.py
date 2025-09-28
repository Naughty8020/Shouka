<<<<<<< HEAD
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
=======
# translator_ov.py
from openvino.runtime import Core
from transformers import AutoTokenizer
import numpy as np
import os

class TranslatorOVModel:
    def __init__(self, model_dir="openvino_model", src_lang="ja", tgt_lang="en"):
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.core = Core()

        # OpenVINO IR ファイル
        xml_path = os.path.join(model_dir, "fugumt.xml")
        bin_path = os.path.join(model_dir, "fugumt.bin")
        if not os.path.exists(xml_path) or not os.path.exists(bin_path):
            raise FileNotFoundError(f"OpenVINO IRモデルが存在しません: {xml_path}")

        # モデル読み込み
        self.model = self.core.read_model(xml_path)
        self.compiled_model = self.core.compile_model(self.model, "CPU")
        self.input_layer = self.model.inputs[0]
        self.output_layer = self.model.outputs[0]

        # トークナイザー
        self.tokenizer = AutoTokenizer.from_pretrained("staka/fugumt-en-ja-int4")

    def set_languages(self, src_lang, tgt_lang):
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    def translate_text(self, text, max_length=512):
        # 入力トークナイズ
        inputs = self.tokenizer(text, return_tensors="np", truncation=True, max_length=max_length)
        input_ids = np.array(inputs["input_ids"], dtype=np.int32)

        # OpenVINO 推論
        input_dict = {self.input_layer.any_name: input_ids}
        output = self.compiled_model(input_dict)[self.output_layer.any_name]

        # デコード
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
>>>>>>> 8dcacc162054909c339723bc5314c76e269a8642
