# Contributing to Petals

We are building a decentralized future for AI. Join the swarm!

## 🚀 Getting Started

### 1. Windows Limitation

**Using Windows?** You MUST use [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) or Linux.
Native Windows is **not supported** due to `uvloop` dependencies.

**Verify Your Environment**:
Before starting, run this script to confirm your environment is ready:
```bash
python3 verify_petals.py
```

### 2. Antigravity Verification (Simulation)

If you cannot run a full GPU node, verify your logic changes using the **Antigravity Simulation**:

- **Script**: `SCAFFOLD/experiments/swarm_sim.py`
- **Purpose**: Validates DHT routing, peer discovery, and failover logic in pure Python.

### 3. Submission Process

1. **Fork** the repository.
2. Create a **feature branch** (e.g., `feat/new-routing-algo`).
3. **Commit** your changes.
4. **Push** to your fork and submit a **Pull Request**.

### 4. Code Style

- We use `black` and `isort` for Python formatting.
- Run `make style` (inside WSL/Linux) before committing.

## 🧪 Testing

- Run `pytest` to execute the full test suite (requires Linux/WSL).
- Check `SCAFFOLD/experiments/check_install.py` to verify dependencies.

## 🤝 Community Guidelines

- Be kind and respectful.
- Use GitHub Issues for bug reports.
- Join our [Discord](https://discord.gg/petals) for real-time discussion.
