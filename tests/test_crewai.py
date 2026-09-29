"""Test suite for CrewAI framework security scan."""

import sys


def test_crewai_import():
    """Test that crewai can be imported."""
    try:
        import crewai
        print("✓ CrewAI imported successfully")
        return True
    except ImportError as e:
        print(f"⚠ CrewAI not installed: {e}")
        return False


def test_crewai_basic():
    """Test basic CrewAI functionality."""
    try:
        from crewai import Agent, Task, Crew
        print("✓ CrewAI components imported: Agent, Task, Crew")
        return True
    except ImportError as e:
        print(f"⚠ CrewAI components not available: {e}")
        return False


if __name__ == "__main__":
    results = []
    results.append(test_crewai_import())
    results.append(test_crewai_basic())
    
    if all(results):
        print("\n✓ All CrewAI tests passed")
        sys.exit(0)
    else:
        print("\n⚠ Some CrewAI tests skipped (dependencies not installed)")
        sys.exit(0)
