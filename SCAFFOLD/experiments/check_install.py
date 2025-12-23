import sys

print(f"Python: {sys.version}")

try:
    import torch
    print(f"Torch: {torch.__version__}")
except ImportError as e:
    print(f"Torch missing: {e}")

try:
    import hivemind
    print(f"Hivemind: {hivemind.__version__}")
except ImportError as e:
    print(f"Hivemind missing: {e}")

try:
    import bitsandbytes
    print(f"BitsAndBytes: {bitsandbytes.__version__}")
except ImportError as e:
    print(f"BitsAndBytes missing: {e}")
except Exception as e:
    print(f"BitsAndBytes error: {e}")

try:
    import petals
    print(f"Petals: {petals.__version__}")
except ImportError as e:
    print(f"Petals missing: {e}")
except Exception as e:
    print(f"Petals error: {e}")
