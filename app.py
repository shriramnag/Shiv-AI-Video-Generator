import os
import torch
import gradio as gr
from diffusers import LTXVideoPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

# --------------------------------------------------
# 🔱 SHIV AI VIDEO GENERATOR (PRO)
# 👤 OWNER: SHRI RAM NAG | 📺 CHANNEL: PAISAWALA20
# --------------------------------------------------

# मोबाइल फ्रेंडली डार्क प्रीमियम थीम
custom_css = """
body { background-color: #05070a; color: #e5e7eb; font-family: 'Segoe UI', sans-serif; }
.gradio-container { border: 1px solid #1e293b; border-radius: 12px; max-width: 900px !important; margin: auto; }
.main-header { text-align: center; padding: 20px; background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); border-radius: 10px; margin-bottom: 20px; }
.generate-btn { background: #2563eb !important; border: none !important; color: white !important; font-weight: bold !important; }
"""

def load_model():
    model_path = "./shiv_model"
    print("--- शिव एआई इंजन लोड हो रहा है (Shri Ram Nag) ---")
    pipe = LTXVideoPipeline.from_pretrained(model_path, torch_dtype=torch.float16).to("cuda")
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    return pipe

def generate_video(prompt):
    if not prompt: return None
    print(f"--- वीडियो जनरेट हो रहा है: {prompt} ---")
    video_frames = pipe(prompt=prompt, num_inference_steps=25, num_frames=24).frames[0]
    output_path = "shiv_ai_video_output.mp4"
    export_to_video(video_frames, output_path, fps=12)
    return output_path

# मॉडल लोड करें
pipe = load_model()

with gr.Blocks(css=custom_css, title="Shiv AI Pro") as demo:
    gr.HTML("<div class='main-header'><h1 style='color: white;'>🔱 SHIV AI VIDEO GENERATOR 🔱</h1><p>Created by: Shri Ram Nag | PAISAWALA20</p></div>")
    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(label="Script (English)", placeholder="Example: A futuristic city...", lines=3)
            generate_btn = gr.Button("Generate Video ⚡", variant="primary", elem_classes="generate-btn")
        with gr.Column():
            video_output = gr.Video(label="Result")
    generate_btn.click(fn=generate_video, inputs=prompt_input, outputs=video_output)

if __name__ == "__main__":
    demo.launch(share=True)
