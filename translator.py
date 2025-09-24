from transformers import pipeline

class TranslatorModel:
    def __init__(self, model_name="Helsinki-NLP/opus-mt-ja-en"):
        # CPU 強制（MPS/GPUを無効化）
        self.translator = pipeline("translation", model=model_name, device=-1)

    def translate_text(self, text: str) -> str:
        if not text.strip():
            return text
        result = self.translator(text, max_length=512)
        return result[0]["translation_text"]
