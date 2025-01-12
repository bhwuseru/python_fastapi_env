from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import subprocess
import os

app = FastAPI()

@app.get("/")
async def read_root():
    html_content = """
    <html>
    <body>
        <h1>AI Upscaling Web UI</h1>
        <form action="/process" enctype="multipart/form-data" method="post">
            <input name="file" type="file">
            <button type="submit">Upload and Process</button>
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.post("/process")
async def process_video(file: UploadFile = File(...)):
    input_path = f"/tmp/{file.filename}"
    output_path = f"/tmp/output_{file.filename}"
    
    # ファイルを保存
    with open(input_path, "wb") as f:
        f.write(await file.read())
    
    # Real-ESRGANでアップスケーリング
    subprocess.run([
        "python3", "/app/Real-ESRGAN/inference_realesrgan.py",
        "-i", input_path, "-o", output_path, "--model", "RealESRGAN_x4plus"
    ])
    
    # RIFEでフレーム補間
    interpolated_path = f"/tmp/interpolated_{file.filename}"
    subprocess.run([
        "python3", "/app/RIFE/inference_video.py",
        "--input", output_path, "--output", interpolated_path, "--fps", "60"
    ])
    
    return {"status": "success", "output": interpolated_path}
