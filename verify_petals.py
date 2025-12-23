import sys
import os
import platform

print(f"Testing Petals Import on {platform.system()}...")

# Mock hivemind and other deps so we don't need full installation to test __init__ logic
sys.modules["hivemind"] = type("Mock", (object,), {"compression": type("Mock", (object,), {"base": type("Mock", (object,), {"USE_LEGACY_BFLOAT16": False})})})()
sys.modules["transformers"] = type("Mock", (object,), {"__version__": "4.43.1"})()
sys.modules["packaging"] = type("Mock", (object,), {"version": type("Mock", (object,), {"parse": lambda x: float(str(x).replace(".", "")[:4])})})()
sys.modules["petals.client"] = type("Mock", (object,), {})()
sys.modules["petals.models"] = type("Mock", (object,), {})()
sys.modules["petals.utils"] = type("Mock", (object,), {"logging": type("Mock", (object,), {"initialize_logs": lambda: None})})()

try:
    # Add src to path
    sys.path.append("src")
    import petals
    print("SUCCESS: Petals imported without raising Windows error.")
except ImportError as e:
    if "native Windows" in str(e):
        print("FAILURE: Windows check triggered incorrectly on Linux!")
        sys.exit(1)
    else:
        print(f"ImportError (Expected due to missing deps, but not Windows check): {e}")
        # This is fine for our specific test case
        sys.exit(0)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)
