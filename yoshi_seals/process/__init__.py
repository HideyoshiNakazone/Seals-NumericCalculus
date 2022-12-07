import yoshi_seals.process.process as ps

import numpy as np


def det(a: np.ndarray) -> float:
    return ps.det(a)


def inverse(a: np.ndarray) -> np.ndarray:
    return ps.inverse(a)


def hstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return ps.hstack(a, b)


def vstack(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return ps.vstack(a, b)


def gauss(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return ps.gauss(a, b)


def cholesky(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return ps.cholesky(a, b)


def decomposition(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return ps.decomposition(a, b)


def cramer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return ps.cramer(a, b)
