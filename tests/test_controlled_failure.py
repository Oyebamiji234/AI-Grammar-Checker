import os
import pytest


@pytest.mark.skipif(
    os.getenv("INJECT_FAILURE") != "1",
    reason="Controlled failure is disabled"
)
def test_controlled_failure():
    assert False, "CONTROLLED_FAILURE: demonstration failure"