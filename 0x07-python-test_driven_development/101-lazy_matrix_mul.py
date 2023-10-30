#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
The 101-lazy_matrix_mul module supplies, lazy_matrix_mul(m_a, m_b).
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns a new matrix that is the product of m_a and m_b using NumPy.
    """
    return np.matmul(m_a, m_b)
