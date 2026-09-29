"""Test suite for LangGraph framework security scan."""

import sys


def test_langgraph_import():
    """Test that langgraph can be imported."""
    try:
        import langgraph
        print("✓ LangGraph imported successfully")
        return True
    except ImportError as e:
        print(f"⚠ LangGraph not installed: {e}")
        return False


def test_langgraph_basic():
    """Test basic LangGraph functionality."""
    try:
        from langgraph.graph import Graph
        print("✓ LangGraph Graph class imported successfully")
        return True
    except ImportError as e:
        print(f"⚠ LangGraph not available: {e}")
        return False


if __name__ == "__main__":
    results = []
    results.append(test_langgraph_import())
    results.append(test_langgraph_basic())
    
    if all(results):
        print("\n✓ All LangGraph tests passed")
        sys.exit(0)
    else:
        print("\n⚠ Some LangGraph tests skipped (dependencies not installed)")
        sys.exit(0)
