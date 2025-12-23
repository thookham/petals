# Petals: Collaborative LLM Inference

[![Build Status](https://github.com/bigscience-workshop/petals/actions/workflows/tests.yml/badge.svg)](https://github.com/bigscience-workshop/petals/actions)
[![License](https://img.shields.io/github/license/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/1004314169335500851?logo=discord&label=Discord)](https://discord.gg/petals)

**Petals** is a decentralized "swarm" technology that allows you to run and fine-tune large language models (like Llama-3, BLOOM, or Falcon) by distributing the computational load across thousands of consumer-grade GPUs.

---

> [!NOTE]
> **Antigravity Hydrated Fork**
> This repository is a verified hydration of the original Petals codebase. It includes additional verification tools (`SCAFFOLD/`) to simulate swarm behavior and verify routing logic without requiring a full GPU cluster.

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

### 2. Verification (Simulated Swarm)

To understand how Petals routes requests across the DHT (Distributed Hash Table) without needing a GPU:

```bash
# Verify installation
python SCAFFOLD/experiments/check_install.py

# Run Swarm Simulation (Pure Python)
python SCAFFOLD/experiments/swarm_sim.py
```

This script simulates nodes joining a swarm, storing routing information, and retrieving it—validating the core P2P logic.

## 🛠️ Development

### Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.
**Windows Developers**: Use the `SCAFFOLD/` simulations to verify logic changes if you cannot run a full node locally.

### Key Features

- **collaborative inference**: Run 70B+ models on a desktop.
- **Fault Tolerance**: Automatic recovery if nodes drop out.
- **Privacy**: Inputs are processed by multiple peers; no single peer sees the whole context (in some configurations).

## 📚 Documentation

- [Official Documentation](https://petals.readthedocs.io/en/latest/)
- [Benchmarks](https://github.com/bigscience-workshop/petals/wiki/Benchmarks)
- [FAQ](https://github.com/bigscience-workshop/petals/wiki/FAQ)

## 🤝 Community

- [Discord](https://discord.gg/petals) - Join the swarm discussion.
- [GitHub Issues](https://github.com/bigscience-workshop/petals/issues) - Report bugs.

## 📄 License

Released under the [MIT License](LICENSE).
