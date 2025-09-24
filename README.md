# Shouka
pip install -r requirements.txt

▶️ 【1】Windows の場合

コマンドプロンプト（cmd）や PowerShell で：

venv\Scripts\activate


成功すると、プロンプトの前に (venv) と表示されます。


▶️ 【2】Mac / Linux の場合

ターミナルで：

source venv/bin/activate



ppt_app/
├── main.py                # 起動スクリプト
├── model.py               # PPTの読み込み・保存・AI処理
├── view.py                # UI定義（PySide6）
├── controller.py          # ボタンクリック等の処理
├── utils/
│   └── converter.py       # PPT→PNG変換など
└── style.qss              # スタイルシート


Model: データとロジック（例：DB操作、計算など）

View: UI部分（例：GUI、HTML、出力結果）

Controller: ユーザー操作の処理（例：クリック、コマンド実行など）

python main.py

test