"""
src/utils.py

Small shared helpers used across the pipeline.
"""

import time


def timed(func, *args, **kwargs):
    """
    Call a function and measure its wall-clock execution time.

    Parameters
    ----------
    func : callable
    *args, **kwargs : passed through to func

    Returns
    -------
    (result, elapsed_seconds)
    """
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start
    return result, elapsed

