import gradio as gr
import torch
from diffusers import LTXVideoPipeline, DPMSolverMultistepScheduler
from diffusers.utils import export_to_video

# --- शिव एआई वेब इंटरफेस (Shri Ram Nag) ---

# CSS फॉर प्रीमियम लुक
custom_css = """
body { background-color: #0b0f19; color: white; font-family: 'Poppins', sans-serif; }
.gradio-container { border: 2px solid #3b82f6; border-radius: 15px; padding: 20px; }
button.primary { background: linear-gradient(90deg, #1d4ed8, #3b82f6) !important; border: none !important; }
h1 { text-align: center; color: #60a5fa; text-transform: uppercase; letter-spacing: 2px; }
"""

def generate_shiv_ai_video(prompt):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = LTXVideoPipeline.from_pretrained(
        "Shriramnag/Shiv-AI-Video-Generator", 
        torch_dtype=torch.float16
    ).to(device)
    
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    
    video_frames = pipe(prompt=prompt, num_inference_steps=25, num_frames=32).frames[0]
    output_path = "shiv_ai_video.mp4"
    export_to_video(video_frames, output_path, fps=12)
    return output_path

# UI डिजाइन
with gr.Blocks(css=custom_css, title="Shiv AI Video Generator") as demo:
    gr.HTML("<h1>🔱 Shiv AI Video Generator 🔱</h1>")
    gr.HTML("<p style='text-align:center;'>Created by: <b>Shri Ram Nag</b> | Paisawala20</p>")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="अपनी स्क्रिप्ट यहाँ लिखें (English)", placeholder="Example: A futuristic city at night...")
            submit_btn = gr.Button("Generate Video ⚡", variant="primary")
        
        with gr.Column():
            output_video = gr.Video(label="Generated Video")

    submit_btn.click(generate_shiv_ai_video, inputs=input_text, outputs=output_video)

demo.launch(share=True)

