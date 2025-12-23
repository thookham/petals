# Petals: Collaborative LLM Inference

[![Build Status](https://github.com/bigscience-workshop/petals/actions/workflows/tests.yml/badge.svg)](https://github.com/bigscience-workshop/petals/actions)
[![License](https://img.shields.io/github/license/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/1004314169335500851?logo=discord&label=Discord)](https://discord.gg/petals)

**Petals** is a decentralized "swarm" technology that allows you to run and fine-tune large language models (like Llama-3, BLOOM, or Falcon) by distributing the computational load across thousands of consumer-grade GPUs.

---

> [!NOTE]
> **Antigravity Hydrated Fork**
> This repository is a verified hydration of the original Petals codebase. It is configured for standard swarm inference.

---

## 🚀 Quick Start

### 1. Installation (Windows Users)

> [!URGENT]
> **WSL / Linux Required**: Petals relies on `uvloop`, which does **not** support native Windows.
> You **MUST** use [WSL2 (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install) or a Linux container.

**In WSL (Ubuntu 22.04+):**

```bash
pip install petals
```

### 2. Basic Usage

Run a distributed inference session:

```python
from petals import AutoDistributedModelForCausalLM
from transformers import AutoTokenizer

model_name = "petals-team/StableBeluga2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

inputs = tokenizer("A cat sat on a mat", return_tensors="pt")["input_ids"]
outputs = model.generate(inputs, max_new_tokens=5)
print(tokenizer.decode(outputs[0]))
```

## 🛠️ Development

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Key Features

- **collaborative inference**: Run 70B+ models on a desktop.
- **Fault Tolerance**: Automatic recovery if nodes drop out.
- **Privacy**: Inputs are processed by multiple peers.

## 📚 Documentation

- [Official Documentation](https://petals.readthedocs.io/en/latest/)
- [Benchmarks](https://github.com/bigscience-workshop/petals/wiki/Benchmarks)
- [FAQ](https://github.com/bigscience-workshop/petals/wiki/FAQ)

## 🤝 Community

- [Discord](https://discord.gg/petals) - Join the swarm discussion.
- [GitHub Issues](https://github.com/bigscience-workshop/petals/issues) - Report bugs.

## 📄 License

Released under the [MIT License](LICENSE).
