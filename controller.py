# controller.py
<<<<<<< HEAD
from PySide6.QtWidgets import QFileDialog
from model import PPTModel, TranslatorModel
from view import PPTView
=======
import sys, os, subprocess
from model import PPTModel
from translator import TranslatorOVModel
from utils.converter import convert_ppt_to_images  # 画像化関数
>>>>>>> 8dcacc162054909c339723bc5314c76e269a8642

class PPTController:
    def __init__(self, view: PPTView):
        self.view = view
        self.model = None
<<<<<<< HEAD
        self.translator = TranslatorModel()
=======
        self.edited_ppt_path = None
        self.translator = TranslatorOVModel(src_lang="ja", tgt_lang="en")
>>>>>>> 8dcacc162054909c339723bc5314c76e269a8642

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
<<<<<<< HEAD
        if not self.model:
            return
        path = self.model.save()
        self.view.output_text.append(f"\nPPT保存完了: {path}")
=======
        text = self.view.input_text.toPlainText()
        self.edited_ppt_path = self.model.save_with_texts(text)
        self.view.output_text.append(f"PPT出力完了: {self.edited_ppt_path}")
        if self.view.view_box.currentText() == "編集後PPT":
            self.view.slides_pix = convert_ppt_to_images(self.edited_ppt_path)
            self.view.show_slide()

    def run_ai(self):
        input_text = self.view.input_text.toPlainText()
        mode = self.view.mode_box.currentText()

        if mode == "翻訳":
            lang_mode = self.view.lang_box.currentText()
            if lang_mode == "日本語→英語":
                self.translator.set_languages("ja", "en")
            else:
                self.translator.set_languages("en", "ja")

            result = self.translator.translate_text(input_text)
            self.view.output_text.setText(result)
        else:
            engine = self.view.engine_box.currentText()
            result = f"[{engine}] {mode} 処理結果：\n\n" + input_text.upper()
            self.view.output_text.setText(result)

    def open_in_app(self):
        if self.view.view_box.currentText() == "編集後PPT" and self.edited_ppt_path:
            file_to_open = self.edited_ppt_path
        else:
            file_to_open = self.model.ppt_path
        if sys.platform == "darwin":
            subprocess.run(["open", file_to_open])
        elif sys.platform == "win32":
            os.startfile(file_to_open)
        else:
            subprocess.run(["xdg-open", file_to_open])

    def update_slide_view(self):
        if self.view.view_box.currentText() == "元のPPT":
            self.view.slides_pix = convert_ppt_to_images(self.model.ppt_path)
        elif self.edited_ppt_path:
            self.view.slides_pix = convert_ppt_to_images(self.edited_ppt_path)
        self.view.show_slide()
>>>>>>> 8dcacc162054909c339723bc5314c76e269a8642
