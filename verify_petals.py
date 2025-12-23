import sys
import os
import platform
from unittest.mock import patch, MagicMock

print(f"Testing Petals Import on {platform.system()}...")

# Mock hivemind and other deps so we don't need full installation to test __init__ logic
sys.modules["hivemind"] = type("Mock", (object,), {"compression": type("Mock", (object,), {"base": type("Mock", (object,), {"USE_LEGACY_BFLOAT16": False})})})()
sys.modules["transformers"] = type("Mock", (object,), {"__version__": "4.43.1"})()
sys.modules["packaging"] = type("Mock", (object,), {"version": type("Mock", (object,), {"parse": lambda x: float(str(x).replace(".", "")[:4])})})()
sys.modules["petals.client"] = type("Mock", (object,), {})()
sys.modules["petals.models"] = type("Mock", (object,), {})()

# Mock petals.utils and petals.utils.logging properly
mock_utils = type("Mock", (object,), {})()
# initialize_logs becomes a bound method when accessed from instance, so it receives self.
# We accept *args to handle any arguments safely.
mock_logging = type("Mock", (object,), {"initialize_logs": lambda *args: None})()
mock_utils.logging = mock_logging
sys.modules["petals.utils"] = mock_utils
sys.modules["petals.utils.logging"] = mock_logging

# 1. Test Normal Import (Should pass on Linux/WSL)
try:
    # Add src to path
    sys.path.append("src")
    if "petals" in sys.modules:
        del sys.modules["petals"] # Force reload
    import petals
    print("SUCCESS: Petals imported on Linux/WSL.")
except ImportError as e:
    if "native Windows" in str(e):
        print("FAILURE: Windows check triggered incorrectly on Linux!")
        sys.exit(1)
    else:
        print(f"ImportError (Expected due to missing deps, but not Windows check): {e}")

# 2. Test Windows Mock (Should fail)
print("Testing Windows Mock...")
if "petals" in sys.modules:
    del sys.modules["petals"] 

with patch("platform.system", return_value="Windows"):
    try:
        import petals
        print("FAILURE: Imported petals on Windows without error")
        sys.exit(1)
    except ImportError as e: # It raises ImportError currently, not OSError
        if "native Windows" in str(e):
            print("SUCCESS: Caught expected Windows Native error")
        else:
            print(f"FAILURE: Caught unexpected error: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"FAILURE: Caught unexpected exception type: {type(e)}")
        sys.exit(1)

print("All tests passed.")
sys.exit(0)
