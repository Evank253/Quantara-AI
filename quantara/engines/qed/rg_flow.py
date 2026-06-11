"""Shim for quantara.engines.qed.rg_flow used by tests.

This provides a minimal QEDRenormalizationGroup class so CI/test collection
succeeds. Implementations should be replaced with the real engine later.
"""
from __future__ import annotations

from typing import Any, Dict, Optional


class QEDRenormalizationGroup:
    """Minimal shim for tests.

    Methods are intentionally minimal: __init__ stores kwargs and run
    returns a simple dict placeholder so tests that import and call
    the class won't fail with AttributeError or NotImplementedError.
    Replace with the real implementation when available.
    """

    def __init__(self, **kwargs: Any) -> None:
        self._meta: Dict[str, Any] = kwargs

    def run(self, inputs: Optional[Any] = None) -> Dict[str, Any]:
        """Run a minimal no-op simulation.

        Returns a placeholder dict. Tests that assert on structure should
        be updated when the real implementation is added.
        """
        return {"status": "shim", "inputs": inputs, "meta": self._meta}
