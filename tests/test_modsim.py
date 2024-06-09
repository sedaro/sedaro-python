import datetime

import numpy as np
import pytest
import spiceypy as spice  # type: ignore

from sedaro import modsim as ms


def test_time_conversions():
    assert ms.datetime_to_mjd(datetime.datetime(2024, 3, 21, 0, 27, 23, tzinfo=datetime.timezone.utc)) == 60390.0190162037
    assert ms.datetime_to_mjd(datetime.datetime(2024, 3, 22, 0, 27, 23, tzinfo=datetime.timezone.utc)) == 60391.0190162037
    assert ms.datetime_to_mjd(datetime.datetime(2024, 3, 20, 0, 27, 23, tzinfo=datetime.timezone.utc)) == 60389.0190162037
    assert ms.datetime_to_mjd(datetime.datetime(2024, 3, 21, 20, 27, 23, tzinfo=datetime.timezone('EST'))) == 60391.0190162037

    assert ms.mjd_to_datetime(60390.0190162037) == datetime.datetime(2024, 3, 21, 0, 27, 23, tzinfo=datetime.timezone.utc)
    assert ms.mjd_to_datetime(60391.0190162037) == datetime.datetime(2024, 3, 22, 0, 27, 23, tzinfo=datetime.timezone.utc)
    assert ms.mjd_to_datetime(60389.0190162037) == datetime.datetime(2024, 3, 20, 0, 27, 23, tzinfo=datetime.timezone.utc)
    
    with pytest.raises(AssertionError, match='Datetime must have a timezone'):
        ms.datetime_to_mjd(datetime.datetime(2024, 3, 20, 0, 27, 23))

def test_read_csv_time_series():
    data = ms.read_csv_time_series('./assets/test.csv')
    assert data['x'] == [1, 4, 7]
    assert data['y'] == [2, 5, 8]
    assert data['z'] == [3, 6, 9]
    assert data['time'] == datetime.datetime(2024, 6, 8, 15, 14, 18, tzinfo=datetime.timezone.utc)
    assert data['time'] == datetime.datetime(2024, 6, 8, 15, 14, 19, tzinfo=datetime.timezone.utc)
    assert data['time'] == datetime.datetime(2024, 6, 8, 15, 14, 20, tzinfo=datetime.timezone.utc)

def test_read_excel_time_series():
    data = ms.read_csv_time_series('./assets/test.csv')
    assert data['x'] == [1, 4, 7]
    assert data['y'] == [2, 5, 8]
    assert data['z'] == [3, 6, 9]
    assert data['time'] == datetime.datetime(2024, 6, 8, 15, 14, 18, tzinfo=datetime.timezone.utc)
    assert data['time'] == datetime.datetime(2024, 6, 8, 15, 14, 19, tzinfo=datetime.timezone.utc)
    assert data['time'] == datetime.datetime(2024, 6, 8, 15, 14, 20, tzinfo=datetime.timezone.utc)

def test_search_time_series():
    assert ms.search_time_series([1, 2, 2, 3], 2) == 3
    assert ms.search_time_series(np.array([1, 2, 2, 3]), 2) == 3
    assert ms.search_time_series([1, 2, 2, 3], 1.9) == 1
    assert ms.search_time_series([1, 2, 2, 3], 0) == 0
    assert ms.search_time_series([1, 2, 2, 3], 10) == 4
    assert ms.search_time_series(
        [datetime.datetime(2024, 6, 8, 15, 14, 20), datetime.datetime(2024, 6, 8, 15, 15, 20)],
        datetime.datetime(2024, 6, 8, 15, 14, 21)
    ) == 1

def test_vectors2angle():
    assert ms.vectors2angle(np.array([1., 0, 0]), np.array([0., 1, 0])) == np.pi / 2
    assert ms.vectors2angle(np.array([1., 0, 0]), np.array([-1., 0, 0])) == np.pi
    assert ms.vectors2angle(np.array([1., 0, 0]), np.array([1., 0, 0])) == 0

def test_rotmat2quaternion():
    '''Truth from NAIF SPICE Toolkit'''
    rot_mat = np.array([[-0.8613323,  0.4774443,  0.1736482],
                       [0.4842454,  0.6681592,  0.5648625],
                       [0.1536657,  0.5706226, -0.8067073]])
    quat_truth_raw = spice.m2q(rot_mat)
    quat_truth = np.array([quat_truth_raw[1], quat_truth_raw[2], quat_truth_raw[3], quat_truth_raw[0]])
    assert (np.max(np.abs(quat_truth - ms.rotmat2quaternion(rot_mat))) < 1e-5)

    rot_mat = np.array([[0.7164465, -0.3971328,  0.5735765],
                        [-0.3903317, -0.9096196, -0.1422443],
                        [0.5782262, -0.1219747, -0.8067073]])
    quat_truth_raw = spice.m2q(rot_mat)
    quat_truth = np.array([quat_truth_raw[1], quat_truth_raw[2], quat_truth_raw[3], quat_truth_raw[0]])
    assert (np.max(np.abs(quat_truth - ms.rotmat2quaternion(rot_mat))) < 1e-5)

    rot_mat = np.array([[0.0100103, -0.5734891,  0.8191521],
                        [0.9122116, -0.3303186, -0.2424039],
                        [0.4095972,  0.7496665,  0.5198368]])
    quat_truth_raw = spice.m2q(rot_mat)
    quat_truth = np.array([quat_truth_raw[1], quat_truth_raw[2], quat_truth_raw[3], quat_truth_raw[0]])
    assert (np.max(np.abs(quat_truth - ms.rotmat2quaternion(rot_mat))) < 1e-5)

    rot_mat = np.array([[0.2762886, -0.6508952, -0.7071068],
                        [0.9510254,  0.0790425,  0.2988362],
                        [-0.1386196, -0.7550415,  0.6408564]])
    quat_truth_raw = spice.m2q(rot_mat)
    quat_truth = np.array([quat_truth_raw[1], quat_truth_raw[2], quat_truth_raw[3], quat_truth_raw[0]])
    assert (np.max(np.abs(quat_truth - ms.rotmat2quaternion(rot_mat))) < 1e-5)

def run_tests():
    test_time_conversions()
    test_read_csv_time_series()
    test_read_excel_time_series()
    test_search_time_series()
    test_vectors2angle()
    test_rotmat2quaternion()