# utils/converter.py
import os, subprocess

def convert_ppt_to_images(ppt_path):
    out_dir = os.path.join(os.path.dirname(ppt_path), "slides_tmp")
    os.makedirs(out_dir, exist_ok=True)
    subprocess.run([
        "soffice", "--headless", "--convert-to", "png",
        "--outdir", out_dir, ppt_path
    ], check=True)
    return sorted([
        os.path.join(out_dir, f) for f in os.listdir(out_dir) if f.endswith(".png")
    ])
