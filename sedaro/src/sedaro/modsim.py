import datetime
import math
import typing

import numpy as np
import pandas as pd
import pytz
from dateutil import parser

EPSILON = 1e-6
REF_DATETIME = datetime.datetime(2024, 3, 21, 0, 27, 23, tzinfo=datetime.timezone.utc)


def datetime_now_utc() -> datetime.datetime:
    '''Python version agnostic way to get the current UTC datetime.'''
    try:
        return datetime.datetime.now(datetime.UTC)
    except ImportError:
        return datetime.datetime.utcnow() # now deprecated


def datetime_to_mjd(dt: datetime.datetime) -> float:
    '''Convert a UTC datetime.datetime to a Modified Julian Date float.

    Args:
        dt: Datetime object with timezone information.

    Returns:
        float: Modified Julian Date.
    '''
    assert dt.tzinfo is not None, (
        "Datetime must have a timezone. You can define UTC datetimes via the `tzinfo=datetime.timezone.utc` argument."
    )
    return 60390.0190162037 + (dt - REF_DATETIME).total_seconds() / 86400


def mjd_to_datetime(mjd: float) -> datetime.datetime:
    '''Convert Modified Julian Date float to a UTC datetime.datetime.

    Args:
        mjd: Modified Julian Date float.

    Returns:
        datetime.datetime: Datetime object corresponding to the input MJD.
    '''
    return REF_DATETIME + datetime.timedelta(seconds=((mjd - 60390.0190162037)*86400))


def read_csv_time_series(file_path: str, time_column_header: str = 'time', **kwargs):
    '''Read a CSV file with a time column and return a pandas DataFrame with datetime objects for the time column.

    Args:
        file_path: Path to the CSV file.
        time_column_header: Header of the time column in the CSV file. Defaults to 'time'.
        **kwargs: Additional keyword arguments to pass to pandas.read_csv.

    Returns:
        pandas.DataFrame: DataFrame with datetime objects for the time column.
    '''
    data = pd.read_csv(file_path, **kwargs)
    datetimes = [parser.parse(t) for t in data[time_column_header]]
    for i, dt in enumerate(datetimes):
        if dt.tzinfo is None:
            datetimes[i] = pytz.utc.localize(dt)
    data[time_column_header] = datetimes
    return data


def read_excel_time_series(file_path: str, time_column_header: str = 'time', **kwargs):
    '''Read a Excel file with a time column and return a pandas DataFrame with datetime objects for the time column.

    Args:
        file_path: Path to the Excel file.
        time_column_header: Header of the time column in the CSV file. Defaults to 'time'.
        **kwargs: Additional keyword arguments to pass to pandas.read_csv.

    Returns:
        pandas.DataFrame: DataFrame with datetime objects for the time column.
    '''
    data = pd.read_excel(file_path, **kwargs)
    datetimes = []
    for dt in data[time_column_header]:
        if type(dt) is pd.Timestamp:
            datetimes.append(dt.to_pydatetime())
        elif type(dt) is datetime.datetime:
            datetimes.append(dt)
        else:
            datetimes.append(parser.parse(dt))
    for i, dt in enumerate(datetimes):
        if dt.tzinfo is None:
            datetimes[i] = pytz.utc.localize(dt)
    data[time_column_header] = datetimes
    return data


def search_time_series(time_dimension: typing.Union[np.ndarray, list], timestamp: typing.Union[float, datetime.datetime]) -> int:
    '''Proxy for [np.searchsorted](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html).

    Args:
        time_dimension: List or array of time values in ascending order.
        timestamp: Time value to search for.

    Returns:
        int: Index of the rightmost element less than or equal to the target.

    Returns the index of the rightmost element less than or equal to the target.
    '''
    return np.searchsorted(time_dimension, timestamp, 'right')


def quaternion2attitude_mat(quaternion: np.ndarray) -> np.ndarray:
    '''Convert a quaternion to an attitude matrix which transforms vectors between frames specified by the quaternion.

    Args:
        quaternion: Quaternion with shape (4,). Scalar is the last element.

    Returns:
        ndarray: Rotation matrix with shape (3, 3).

    References:
        [1] F. Markley and John Crassidis. Fundamentals of Spacecraft Attitude Determination and Control. Section 2.9.3
    '''
    if len(quaternion) != 4:
        raise ValueError("Bad shape")

    rotation = np.zeros((3, 3))

    rotation[0, 0] = 1 - 2 * (quaternion[1] * quaternion[1] + quaternion[2] * quaternion[2])
    rotation[0, 1] = 2 * (quaternion[0] * quaternion[1] + quaternion[3] * quaternion[2])
    rotation[0, 2] = 2 * (quaternion[0] * quaternion[2] - quaternion[3] * quaternion[1])

    rotation[1, 0] = 2 * (quaternion[0] * quaternion[1] - quaternion[3] * quaternion[2])
    rotation[1, 1] = 1 - 2 * (quaternion[0] * quaternion[0] + quaternion[2] * quaternion[2])
    rotation[1, 2] = 2 * (quaternion[1] * quaternion[2] + quaternion[3] * quaternion[0])

    rotation[2, 0] = 2 * (quaternion[0] * quaternion[2] + quaternion[3] * quaternion[1])
    rotation[2, 1] = 2 * (quaternion[1] * quaternion[2] - quaternion[3] * quaternion[0])
    rotation[2, 2] = 1 - 2 * (quaternion[0] * quaternion[0] + quaternion[1] * quaternion[1])

    return rotation


def quaternion_rotate_frame(vectorIn: np.ndarray, quaternion: np.ndarray) -> np.ndarray:
    '''Rotate a vector into a frame specified by an attitude quaternion according to [1].

    Args:
        vectorIn: Input vector with shape (3,).
        quaternion: Quaternion with shape (4,). Scalar is the last element.

    Returns:
        ndarray: Rotated vector with shape (3,).

    References:
        [1] F. Markley and John Crassidis. Fundamentals of Spacecraft Attitude Determination and Control. Section 2.9.3
    '''
    return quaternion2attitude_mat(quaternion).dot(vectorIn)


def angle_between_quaternion(q1: np.ndarray, q2: np.ndarray) -> float:
    '''Calculate the angle between two quaternion attitudes.

    Args:
        q1: Quaternion with shape (4,).
        q2: Quaternion with shape (4,).

    Returns:
        float: Angle between the two quaternions, in radians.
    '''
    return 2 * np.arccos(min(abs(difference_quaternion(q1, q2)[-1]), 1))


def difference_quaternion(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    '''Calculate quaternion describing rotation from q1 to q2.

    Args:
        q1: Origin quaternion with shape (4,).
        q2: Destination quaternion with shape (4,).

    Returns:
        ndarray: Relative quaternion with shape (4,).
    '''
    return quaternion_dot(q1, quaternion_conjugate(q2))


def quaternion2rotmat(quaternion: np.ndarray) -> np.ndarray:
    '''
    This function produces a rotation matrix corresponding to the ACTIVE rotation by the given quaternion. Don't use
    this for frame conversions; use quaternion2AttitudeMat instead.

    Args:
        quaternion: Quaternion with shape (4,). Scalar is the last element.

    Returns:
        ndarray: Rotation matrix with shape (3, 3).

    References:
        [1] F. Markley and John Crassidis. Fundamentals of Spacecraft Attitude Determination and Control.
    '''
    if len(quaternion) != 4:
        raise ValueError("Bad shape")

    rotation = np.zeros((3, 3))

    rotation[0, 0] = 1 - 2 * (quaternion[1] * quaternion[1] + quaternion[2] * quaternion[2])
    rotation[1, 0] = 2 * (quaternion[0] * quaternion[1] + quaternion[3] * quaternion[2])
    rotation[2, 0] = 2 * (quaternion[0] * quaternion[2] - quaternion[3] * quaternion[1])

    rotation[0, 1] = 2 * (quaternion[0] * quaternion[1] - quaternion[3] * quaternion[2])
    rotation[1, 1] = 1 - 2 * (quaternion[0] * quaternion[0] + quaternion[2] * quaternion[2])
    rotation[2, 1] = 2 * (quaternion[1] * quaternion[2] + quaternion[3] * quaternion[0])

    rotation[0, 2] = 2 * (quaternion[0] * quaternion[2] + quaternion[3] * quaternion[1])
    rotation[1, 2] = 2 * (quaternion[1] * quaternion[2] - quaternion[3] * quaternion[0])
    rotation[2, 2] = 1 - 2 * (quaternion[0] * quaternion[0] + quaternion[1] * quaternion[1])

    return rotation


def orthogonal_vector(vector: np.ndarray) -> np.ndarray:
    '''Produce an orthogonal vector.

    Args:
        vector: Input vector with shape (N,).

    Returns:
        ndarray: Output vector is orthogonal to input but otherwise arbitrarily oriented.
    '''
    cross_vector = np.array([0, 0, 1])
    normed_axis = vector / np.linalg.norm(vector)

    if abs(np.dot(normed_axis, cross_vector)) == 1:
        cross_vector = np.array([0, 1, 0])

    orthogonal_vector = np.cross(cross_vector, normed_axis)
    return orthogonal_vector / np.linalg.norm(orthogonal_vector)


def quaternion_dot(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    '''Quaternion dot product.

    Preserves the order of active rotation matrix multiplication.

    Args:
        q1: Quaternion with shape (4,). Scalar is the last element.
        q2: Quaternion with shape (4,).

    Returns:
        ndarray: Quaternion with shape (4,).

    References:
        [1] F. Markley and John Crassidis. Fundamentals of Spacecraft Attitude Determination and Control.
    '''
    return np.array([q1[3] * q2[0] + q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1],
                    q1[3] * q2[1] - q1[0] * q2[2] + q1[1] * q2[3] + q1[2] * q2[0],
                    q1[3] * q2[2] + q1[0] * q2[1] - q1[1] * q2[0] + q1[2] * q2[3],
                    q1[3] * q2[3] - q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2]])


def random_orthogonal_rotation(
    vector: np.ndarray,
    angle_1sigma: float,
    random: typing.Optional[np.random.RandomState] = None,
) -> np.ndarray:
    '''Calculate a random rotation orthogonal to an input vector.

    Axis of rotation for the perturbation will be orthogonal to the input
    vector and uniformly distributed along the unit circle centered on
    and orthogonal to the input unit vector.

    Args:
        vector: Input vector with shape (N,).
        angle_1sigma: Standard deviation of angular perturbation.
        random: Pre-generated RandomState. Defaults to None.

    Returns:
        ndarray: Quaternion describing the random rotation with shape (4,).
    '''
    if random is None:
        random = np.random.RandomState()

    orth_vector = orthogonal_vector(vector)
    angle_error = angle_1sigma * random.randn()

    rotation_axis = quaternion2rotmat(
        euler_axis_angle2quaternion(vector, random.uniform(0, 2*np.pi))).dot(orth_vector)

    return euler_axis_angle2quaternion(rotation_axis, angle_error)


def euler_axis_angle2quaternion(axis: np.ndarray, angle: float) -> np.ndarray:
    '''Convert an axis-angle representation to a quaternion.

    Args:
        axis: Axis of rotation with shape (3,).
        angle: Angle of rotation in radians.

    Returns:
        ndarray: Quaternion with shape (4,).
    '''
    axis = axis / np.linalg.norm(axis)
    quaternion = np.array([axis[0] * np.sin(angle / 2),
                           axis[1] * np.sin(angle / 2),
                           axis[2] * np.sin(angle / 2),
                           np.cos(angle / 2)])
    return quaternion / np.linalg.norm(quaternion)


def vectors2angle(vector1: np.ndarray, vector2: np.ndarray) -> float:
    '''Find the acute angle between two vectors.

    Args:
        vector1: Vector with shape (3,).
        vector2: Vector with shape (3,).

    Returns:
        float: Angle between the two vectors in radians.
    '''
    cos_ang = np.dot(unit3(vector1), unit3(vector2))
    if abs(cos_ang) - 1 > 0:
        if cos_ang > 0:
            angle = 0.0
        else:
            angle = np.pi
    else:
        angle = math.acos(cos_ang)

    return angle


def eci_vector_to_body(vector_eci: np.ndarray, attitude_body_eci: np.ndarray) -> np.ndarray:
    '''Rotate a vector from ECI into the body frame given a `body_eci` quaternion.

    Args:
        vector_eci: Vector in ECI frame with shape (3,).
        attitude_body_eci: Quaternion with shape (4,). Scalar is the last element.

    Returns:
        ndarray: Rotated vector with shape (3,).
    '''
    rotation = quaternion2attitude_mat(attitude_body_eci)
    return rotation.dot(vector_eci)


def body_vector_to_eci(vector_eci: np.ndarray, attitude_body_eci: np.ndarray) -> np.ndarray:
    '''Rotate a vector from the body frame into ECI given a `body_eci` quaternion.

    Args:
        vector_eci: Vector in body frame with shape (3,).
        attitude_body_eci: Quaternion with shape (4,). Scalar is the last element.

    Returns:
        ndarray: Rotated vector with shape (3,).
    '''
    rotation = quaternion2attitude_mat(attitude_body_eci).T
    return rotation.dot(vector_eci)


def quaternion_conjugate(quaternion: np.ndarray) -> np.ndarray:
    '''Calculate the conjugate of a quaternion.

    Args:
        quaternion: Quaternion with shape (4,). Scalar is the last element.

    Returns:
        ndarray: Conjugate quaternion with shape (4,).
    '''
    quaternion_conj = np.array(-quaternion)
    quaternion_conj[3] = -quaternion_conj[3]

    return quaternion_conj


def rotmat2quaternion(rot_mat: np.ndarray) -> np.ndarray:
    '''Convert a rotation matrix to a quaternion.

    Args:
        rot_mat: Rotation matrix with shape (3, 3).

    Returns:
        ndarray: Quaternion with shape (4,). Scalar is the last element.
    '''
    tr = np.trace(rot_mat)
    idx = np.argmax([*np.diag(rot_mat), tr])
    quaternion = np.zeros(4)
    if idx != 3:
        i = idx
        j = (i + 1) % 3
        k = (j + 1) % 3

        quaternion[i] = 1 - tr + 2 * rot_mat[i, i]
        quaternion[j] = rot_mat[j, i] + rot_mat[i, j]
        quaternion[k] = rot_mat[k, i] + rot_mat[i, k]
        quaternion[3] = rot_mat[k, j] - rot_mat[j, k]
    else:
        quaternion[0] = rot_mat[2, 1] - rot_mat[1, 2]
        quaternion[1] = rot_mat[0, 2] - rot_mat[2, 0]
        quaternion[2] = rot_mat[1, 0] - rot_mat[0, 1]
        quaternion[3] = 1 + tr

    return quaternion / np.linalg.norm(quaternion)


def quaternions_to_rates(q1: np.ndarray, q2: np.ndarray, dt: float) -> np.ndarray:
    '''Finite difference calculation of angular velocity from two quaternions.

    Args:
        q1: Quaternion at time t with shape (4,). Scalar is the last element.
        q2: Quaternion at time t+dt with shape (4,). Scalar is the last element.
        dt: Time step.

    Returns:
        ndarray: Angular velocity vector with shape (3,).

    References:
        [1] https://mariogc.com/post/angular-velocity-quaternions/
    '''
    return (2 / dt) * np.array([
        q1[3]*q2[0] - q1[0]*q2[3] - q1[1]*q2[2] + q1[2]*q2[1],
        q1[3]*q2[1] + q1[0]*q2[2] - q1[1]*q2[3] - q1[2]*q2[0],
        q1[3]*q2[2] - q1[0]*q2[1] + q1[1]*q2[0] - q1[2]*q2[3]])


def invert3(m: np.ndarray) -> np.ndarray:
    '''Invert a 3x3 matrix.

    Faster for looping than np.linalg.inv for 3x3 matrices.

    Args:
        m: Matrix with shape (3, 3).

    Returns:
        ndarray: Inverted matrix with shape (3, 3).
    '''
    if m.shape != (3, 3):
        raise ValueError("Matrix must be 3x3.")
    inv = np.zeros((3, 3))
    inv[0, 0] = m[1, 1] * m[2, 2] - m[1, 2] * m[2, 1]
    inv[1, 0] = m[1, 2] * m[2, 0] - m[1, 0] * m[2, 2]
    inv[2, 0] = m[1, 0] * m[2, 1] - m[1, 1] * m[2, 0]

    inv[0, 1] = m[0, 2] * m[2, 1] - m[0, 1] * m[2, 2]
    inv[1, 1] = m[0, 0] * m[2, 2] - m[0, 2] * m[2, 0]
    inv[2, 1] = m[0, 1] * m[2, 0] - m[0, 0] * m[2, 1]

    inv[0, 2] = m[0, 1] * m[1, 2] - m[0, 2] * m[1, 1]
    inv[1, 2] = m[0, 2] * m[1, 0] - m[0, 0] * m[1, 2]
    inv[2, 2] = m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]

    inv /= inv[0, 0] * m[0, 0] + inv[0, 1] * m[1, 0] + inv[0, 2] * m[2, 0]

    return inv


def unit3(vec: np.ndarray) -> np.ndarray:
    '''Normalize a 3D vector.

    Args:
        vec: Input vector with shape (3,).

    Returns:
        ndarray: Normalized vector with shape (3,).
    '''
    if np.linalg.norm(vec) > EPSILON:
        return vec/np.linalg.norm(vec)
    raise ValueError("Vector cannot be the zero vector.")
