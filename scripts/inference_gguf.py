import argparse

from llama_cpp import Llama


def main() -> None:
    parser = argparse.ArgumentParser(description="Run NSTC Writer 7B GGUF with llama-cpp-python.")
    parser.add_argument("--model", required=True, help="Path to NSTC-Writer-7B GGUF file.")
    parser.add_argument("--prompt", default="請根據以下研究主題，撰寫一段 NSTC 計畫摘要：以生成式 AI 輔助科研計畫書撰寫。")
    parser.add_argument("--ctx-size", type=int, default=4096)
    parser.add_argument("--max-tokens", type=int, default=768)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--top-p", type=float, default=0.9)
    parser.add_argument("--n-gpu-layers", type=int, default=-1)
    args = parser.parse_args()

    llm = Llama(
        model_path=args.model,
        n_ctx=args.ctx_size,
        n_gpu_layers=args.n_gpu_layers,
        verbose=False,
    )

    prompt = (
        "<|im_start|>system\n"
        "你是熟悉台灣 NSTC 計畫書格式的繁體中文研究寫作助理。"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"{args.prompt}"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    result = llm(
        prompt,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        top_p=args.top_p,
        stop=["<|im_end|>"],
    )

    print(result["choices"][0]["text"].strip())


if __name__ == "__main__":
    main()
