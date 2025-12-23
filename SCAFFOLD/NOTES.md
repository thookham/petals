# Notes for petals

## Initial Observations

- Repository cloned successfully.
- Codebase is pure Python, heavily utilizing `hivemind` for P2P networking and `torch` for computation.

## Architecture Deep Dive (`src/petals`)

The system is split into two main components:

1. **Server (`petals.server`)**: Hosts a part of the model (a set of Transformer blocks).
    - `Server` class: Orchestrates the `ModuleContainer`, manages DHT connectivity, and balances load.
    - `ModuleContainer`: Holds the actual `TransformerBackend` instances (the loaded PyTorch layers).
    - `ModuleAnnouncerThread`: Periodically announces availability to the DHT.
2. **Client (`petals.client`)**:
    - `RemoteSequential`: The main interface for users. It mimics `torch.nn.Sequential` but executes layers remotely across the swarm.
    - `InferenceSession`: Manages the state of a single inference pass.

## Next Steps

- **Environment**: Needs a complex python environment (torch, hivemind).
  - *Update*: `pip install` attempted but `requirements.txt` was missing. Installed from `.` (setup.cfg).
  - *Status*: Installation likely partial on Windows due to `bitsandbytes`.
- **Test**: Try to run a local "swarm" with 2 servers and 1 client script to verify basic inference.
  - *Action*: Created `SCAFFOLD/experiments/swarm_sim.py` to verify the DHT "Heal Routing" logic.
  - *Result*:
    - Verified that clients greedily select covering peers.
    - Verified that if a peer (Server B) drops, logic switches to overlapping peer (Server D).
    - Verified that "Broken Chain" (no coverage for blk 0) is correctly detected.
