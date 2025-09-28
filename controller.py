# controller.py
from PySide6.QtWidgets import QFileDialog
from model import PPTModel, TranslatorModel
from view import PPTView

class PPTController:
    def __init__(self, view: PPTView):
        self.view = view
        self.model = None
        self.translator = TranslatorModel()

        view.open_btn.clicked.connect(self.load_ppt)
        view.slide_select.currentIndexChanged.connect(self.display_slide_text)
        view.translate_btn.clicked.connect(self.translate_slide)
        view.save_btn.clicked.connect(self.save_ppt)

    def load_ppt(self):
        path, _ = QFileDialog.getOpenFileName(self.view, "PPTを選択", "", "PowerPoint Files (*.pptx)")
        if not path:
            return
        self.model = PPTModel(path)
        slides_text = self.model.extract_slides_text()
        self.view.slide_select.clear()
        self.view.slide_select.addItems([f"Slide {i+1}" for i in range(len(slides_text))])
        self.view.model_path_label.setText(f"PPTパス: {path}")
        self.view.input_text.setText(slides_text[0])
        self.view.output_text.clear()

    def display_slide_text(self):
        if not self.model:
            return
        idx = self.view.slide_select.currentIndex()
        slides_text = self.model.extract_slides_text()
        if 0 <= idx < len(slides_text):
            self.view.input_text.setText(slides_text[idx])
            self.view.output_text.clear()

    def translate_slide(self):
        if not self.model:
            return
        idx = self.view.slide_select.currentIndex()
        text = self.view.input_text.toPlainText()
        translated = self.translator.translate_text(text)
        self.view.output_text.setText(translated)
        self.model.update_slide_text(idx, translated)

    def save_ppt(self):
        if not self.model:
            return
        path = self.model.save()
        self.view.output_text.append(f"\nPPT保存完了: {path}")
