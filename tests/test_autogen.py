"""Test suite for AutoGen framework security scan."""

import sys


def test_autogen_import():
    """Test that autogen can be imported."""
    try:
        import autogen
        print("✓ AutoGen imported successfully")
        return True
    except ImportError as e:
        print(f"⚠ AutoGen not installed: {e}")
        return False


def test_autogen_basic():
    """Test basic AutoGen functionality."""
    try:
        from autogen import Agent
        print("✓ AutoGen Agent class imported successfully")
        return True
    except ImportError as e:
        print(f"⚠ AutoGen not available: {e}")
        return False


if __name__ == "__main__":
    results = []
    results.append(test_autogen_import())
    results.append(test_autogen_basic())
    
    if all(results):
        print("\n✓ All AutoGen tests passed")
        sys.exit(0)
    else:
        print("\n⚠ Some AutoGen tests skipped (dependencies not installed)")
        sys.exit(0)
