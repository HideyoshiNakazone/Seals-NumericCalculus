from yoshi_seals import process as ps

import numpy as np

from numpy import testing as npt
import unittest


class TestProcess(unittest.TestCase):

    def test_det(self):
        a = np.array(([1., 0.], [0., 1.]))

        a_det = ps.det(a)

        self.assertEqual(a_det, 1)

    def test_inverse(self):
        a = np.array(([1., 0.], [0., 1.]))
        a_inv = ps.inverse(a)

        npt.assert_array_equal(a, a_inv)

    def test_hstack_returns_stacked_array(self):
        a = np.array(([1., ], [1., ]))
        b = np.array(([1., ], [1., ]))

        stacked = ps.hstack(a, b)
        expected_stacked_array = np.array(([1., 1.], [1., 1.]))

        npt.assert_array_equal(stacked, expected_stacked_array)

    def test_hstack_throws_exception(self):
        a = np.array(([1., ], [1., ]))
        b = np.array(([1., ]))

        with self.assertRaises(ValueError):
            ps.hstack(a, b)

    def test_vstack_returns_stacked_array(self):
        a = np.array(([[1., 1.]]))
        b = np.array(([[1., 1.]]))

        stacked = ps.vstack(a, b)
        expected_stacked_array = np.array(([1., 1.], [1., 1.]))

        npt.assert_array_equal(stacked, expected_stacked_array)

    def test_vstack_throws_exception(self):
        a = np.array(([[1., 1.]]))
        b = np.array(([[1.]]))

        with self.assertRaises(ValueError):
            ps.vstack(a, b)

    def test_gauss(self):
        a = np.array(([4., 10., 8.], [10., 26., 26], [8., 26., 61.]))
        b = np.array(([44.], [128.], [214.]))

        matrix = ps.gauss(a, b)
        expected_matrix = np.array([[-8.], [6.], [2.]])

        npt.assert_almost_equal(matrix, expected_matrix)

    def test_cholesky(self):
        a = np.array(([4., 10., 8.], [10., 26., 26], [8., 26., 61.]))
        b = np.array(([44.], [128.], [214.]))

        matrix = ps.cholesky(a, b)
        expected_matrix = np.array([[-8.], [6.], [2.]])

        npt.assert_almost_equal(matrix, expected_matrix)

    def test_decomposition(self):
        a = np.array(([4., 10., 8.], [10., 26., 26], [8., 26., 61.]))
        b = np.array(([44.], [128.], [214.]))

        matrix = ps.decomposition(a, b)
        expected_matrix = np.array([[-8.], [6.], [2.]])

        npt.assert_almost_equal(matrix, expected_matrix)

    def test_cramer(self):
        a = np.array(([4., 10., 8.], [10., 26., 26], [8., 26., 61.]))
        b = np.array(([44.], [128.], [214.]))

        matrix = ps.cramer(a, b)
        expected_matrix = np.array([[-8.], [6.], [2.]])

        npt.assert_almost_equal(matrix, expected_matrix)
