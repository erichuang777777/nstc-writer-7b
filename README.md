# NSTC Writer 7B

NSTC Writer 7B is a Traditional Chinese research proposal drafting model optimized for Taiwan NSTC-style grant writing workflows.

The model helps draft, rewrite, structure, and polish research proposal content. It should be used as a writing assistant, not as a substitute for domain review, budget validation, institutional compliance checks, or final PI approval.

## Release Channels

- Hugging Face model: `https://huggingface.co/ericeric777777/NSTC-Writer-7B`
- Colab demo: `notebooks/NSTC_Writer_7B_Colab.ipynb`
- Ollama local setup: `ollama/Modelfile`

## Recommended User Paths

Use Colab if you want the easiest GPU-based demo:

- Open `notebooks/NSTC_Writer_7B_Colab.ipynb`.
- The notebook uses `ericeric777777/NSTC-Writer-7B` by default.
- Keep `LOAD_MODE = "auto"`.
- On most free Colab T4 runtimes, the notebook uses 4-bit loading automatically.

Use Ollama if you want to run the GGUF model locally:

- Download `NSTC-Writer-7B-Q4_K_M.gguf` from the GGUF Hugging Face repo.
- Install Ollama.
- Create the local model with the provided `ollama/Modelfile`.

Use Transformers if you want Python integration:

- Install `requirements.txt`.
- Run `scripts/inference_transformers.py`.

## Hardware Requirements

These are practical recommendations, not strict guarantees. Actual speed depends on context length, operating system, CPU/GPU generation, and memory bandwidth.

| Mode | Recommended model file | Minimum hardware | Expected experience |
| --- | --- | --- | --- |
| Colab T4 | HF model with 4-bit loading | T4 16 GB VRAM | Good for demos and single-user drafting |
| Colab A100/L4 | HF model 16-bit or 4-bit | 24+ GB VRAM recommended | Faster and more stable for longer outputs |
| Ollama CPU | `Q4_K_M.gguf` | 16 GB system RAM | Works, but slow |
| Ollama NVIDIA GPU | `Q4_K_M.gguf` | 8+ GB VRAM, 16+ GB RAM | Usable local inference |
| Apple Silicon | `Q4_K_M.gguf` | 16 GB unified memory | Usable on M-series Macs |

Available GGUF file:

```text
NSTC-Writer-7B-Q4_K_M.gguf
```

## Ollama Local Usage

Download the GGUF file into the `ollama/` directory:

```text
ollama/NSTC-Writer-7B-Q4_K_M.gguf
```

Then create the local Ollama model:

```bash
cd ollama
ollama create nstc-writer-7b -f Modelfile
```

Run it:

```bash
ollama run nstc-writer-7b
```

Example prompt:

```text
請根據以下研究主題，撰寫一段 NSTC 計畫摘要：以生成式 AI 輔助科研計畫書撰寫。
```

## Quick Start: Transformers

```bash
pip install -r requirements.txt
python scripts/inference_transformers.py --model ericeric777777/NSTC-Writer-7B
```

## Quick Start: GGUF with llama-cpp-python

```bash
pip install llama-cpp-python
python scripts/inference_gguf.py --model NSTC-Writer-7B-Q4_K_M.gguf
```

## Base Model Disclosure

NSTC Writer 7B is fine-tuned from Qwen2.5-7B-Instruct.

Users deploying this model in public-sector, regulated, or procurement-sensitive environments should independently review the base model license, model provenance, data governance requirements, and internal policy requirements before use.

## Suggested Use Cases

- Drafting NSTC-style project abstracts.
- Rewriting proposal sections in formal Traditional Chinese.
- Expanding research objectives, significance, and methodology sections.
- Producing reviewer-friendly summaries.
- Converting bullet-point research ideas into structured proposal text.

## Not Recommended For

- Producing final grant submissions without expert review.
- Legal, procurement, financial, or regulatory decisions.
- Generating fabricated citations, budgets, collaborators, or institutional approvals.
- Handling confidential or personal data unless deployed in an approved secure environment.

## Repository Structure

```text
.
├── README.md
├── MODEL_CARD.md
├── requirements.txt
├── notebooks/
│   └── NSTC_Writer_7B_Colab.ipynb
├── ollama/
│   └── Modelfile
└── scripts/
    ├── inference_transformers.py
    └── inference_gguf.py
```

## License

Add the final license here after confirming compatibility with the base model license and your fine-tuning dataset terms.
