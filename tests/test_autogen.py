"""Test suite for AutoGen framework security scan."""

import pytest


def test_autogen_import():
    """Test that autogen can be imported."""
    try:
        import autogen
        assert autogen is not None
    except ImportError:
        pytest.skip("AutoGen not installed")


def test_autogen_basic():
    """Test basic AutoGen functionality."""
    try:
        from autogen import Agent
        assert Agent is not None
    except ImportError:
        pytest.skip("AutoGen not installed")
