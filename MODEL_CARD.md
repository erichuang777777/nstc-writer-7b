---
license: apache-2.0
base_model:
  - Qwen/Qwen2.5-7B-Instruct
library_name: transformers
pipeline_tag: text-generation
language:
  - zh
tags:
  - traditional-chinese
  - text-generation
  - grant-writing
  - research-assistant
  - nstc
  - taiwan
  - qwen2.5
model_name: NSTC Writer 7B
datasets:
  - unknown
inference: false
---

# NSTC Writer 7B

## Model Summary

NSTC Writer 7B is a Traditional Chinese language model fine-tuned for Taiwan NSTC-style research proposal drafting. It is designed to assist researchers with structured writing, proposal section expansion, formal tone rewriting, and grant-oriented summarization.

## Model Details

- Model name: NSTC Writer 7B
- Model type: causal language model
- Language: Traditional Chinese, with limited English capability inherited from the base model
- Base model: Qwen2.5-7B-Instruct
- Fine-tuning method: supervised fine-tuning / instruction tuning
- Release formats: Hugging Face Transformers, GGUF, Ollama local model
- License: Apache License 2.0
- Library: Transformers
- Primary task: text generation

## Base Model

NSTC Writer 7B is fine-tuned from:

```text
Qwen/Qwen2.5-7B-Instruct
```

The base model is released under the Apache License 2.0. Users should review the upstream model card and license before deployment.

## Intended Use

This model is intended for research writing assistance, especially:

- NSTC-style proposal abstracts.
- Research motivation and significance sections.
- Methodology section drafting.
- Expected contribution and impact writing.
- Formal Traditional Chinese rewriting.

## How to Use

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "ericeric777777/NSTC-Writer-7B"

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
    trust_remote_code=True,
)

messages = [
    {"role": "system", "content": "你是熟悉台灣 NSTC 計畫書格式的繁體中文研究寫作助理。"},
    {"role": "user", "content": "請根據以下研究主題，撰寫一段 NSTC 計畫摘要：以生成式 AI 輔助科研計畫書撰寫。"},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=768,
    temperature=0.7,
    top_p=0.9,
    do_sample=True,
)

generated = outputs[0][inputs["input_ids"].shape[-1]:]
print(tokenizer.decode(generated, skip_special_tokens=True))
```

## Hardware Guidance

Recommended deployment options:

- Colab T4: use 4-bit Transformers loading through the provided notebook.
- Local Ollama CPU: use `NSTC-Writer-7B-Q4_K_M.gguf` with at least 16 GB RAM.
- Local Ollama GPU: use `Q4_K_M` with 8+ GB VRAM, or `Q5_K_M` with 12+ GB VRAM.
- Apple Silicon: use `Q4_K_M` on 16 GB unified memory, or `Q5_K_M` on 24 GB unified memory.
- Production service: use a controlled GPU server rather than free Colab.

## GGUF and Ollama

For local inference, use the GGUF release:

```text
ericeric777777/NSTC-Writer-7B
```

Recommended file:

```text
NSTC-Writer-7B-Q4_K_M.gguf
```

Ollama users can create a local model with the provided `Modelfile` in the GitHub repository:

```bash
ollama create nstc-writer-7b -f Modelfile
ollama run nstc-writer-7b
```

## Out-of-Scope Use

The model should not be used as the sole basis for:

- Final grant submission decisions.
- Legal, financial, procurement, or regulatory decisions.
- Generating fabricated citations, budgets, institutional approvals, or collaborator commitments.
- Processing sensitive personal data without an approved secure deployment environment.

## Public-Sector Deployment Notice

This model is fine-tuned from Qwen2.5-7B-Instruct. Organizations considering public-sector or regulated deployment should review:

- Base model license and acceptable use terms.
- Data provenance and governance requirements.
- Internal procurement and cybersecurity policies.
- Deployment environment and logging behavior.
- Whether the model should be hosted on-premises or in a controlled private cloud.

## Limitations

- The model may hallucinate citations, policies, funding rules, or technical details.
- The model does not verify NSTC regulations or submission requirements in real time.
- The model may produce fluent but incorrect claims.
- The model requires expert human review before any official use.
- The model is optimized for drafting and rewriting, not factual verification.

## Recommended Generation Settings

For drafting:

```text
temperature: 0.6-0.8
top_p: 0.85-0.95
max_new_tokens: 512-1536
```

For conservative rewriting:

```text
temperature: 0.2-0.4
top_p: 0.8-0.9
max_new_tokens: 512-1024
```

## Example Prompt

```text
你是熟悉台灣 NSTC 計畫書格式的繁體中文研究寫作助理。

請根據以下研究主題，撰寫一段計畫摘要，語氣正式、具研究計畫書風格：

主題：以生成式 AI 輔助科研計畫書撰寫
```

## Evaluation

Recommended evaluation dimensions:

- Traditional Chinese fluency.
- Proposal structure quality.
- Relevance to NSTC-style writing.
- Faithfulness to user-provided facts.
- Absence of fabricated citations or regulations.
- Expert review score from domain researchers.

## Training Data

The model owner should complete this section before public release.

Suggested disclosure:

```text
This model was fine-tuned on Traditional Chinese instruction data related to research proposal drafting and NSTC-style writing. Do not include private, confidential, copyrighted, or personal data unless you have the right to redistribute derived model weights.
```

If the training data cannot be disclosed, state the reason clearly and provide high-level characteristics of the dataset.

## Ethical and Safety Considerations

- Generated proposal text should be reviewed by qualified researchers.
- The model should not be used to fabricate research results, citations, budgets, or institutional commitments.
- For public-sector or regulated deployment, organizations should review provenance, licensing, cybersecurity, and data governance requirements.
- Do not submit confidential project ideas to third-party hosted demos unless the deployment environment is approved for that use.

## License

This model is released under the Apache License 2.0, following the base model license. The model owner is responsible for ensuring that the fine-tuning dataset terms are compatible with this release.
