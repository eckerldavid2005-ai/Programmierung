import math
import numpy as np
import pandas as pd
import pytest
import p3


# ------------------------------------------------------------
# NumPy
# ------------------------------------------------------------

def test_create_array():
    a = p3.create_array()
    assert isinstance(a, np.ndarray)
    assert list(a) == [1, 2, 3]


def test_create_x_values():
    x = p3.create_x_values()
    assert isinstance(x, np.ndarray)
    assert len(x) == 360
    assert math.isclose(x[0], 0.0)
    # erlaubt sind arange (letzter Wert < 2*pi) oder linspace (letzter = 2*pi)
    assert 2 * math.pi - x[-1] <= np.pi / 180 + 1e-9


def test_create_data():
    zeros, ones, eye = p3.create_data(5)
    assert isinstance(zeros, np.ndarray)
    assert isinstance(ones, np.ndarray)
    assert isinstance(eye, np.ndarray)
    assert len(zeros) == 5
    assert (zeros == 0).all()
    assert (ones == 1).all()
    assert eye.shape == (5, 5)
    assert (eye == np.eye(5)).all()


def test_array_info():
    m = np.array([np.arange(5), np.arange(5, 10)])
    assert p3.array_info(m) == (2, (2, 5))


def test_reshape_array():
    m = np.array([np.arange(5), np.arange(5, 10)])
    r = p3.reshape_array(m, (5, 2))
    assert r.shape == (5, 2)
    assert list(r[0]) == [0, 1]
    assert list(r.flatten()) == list(range(10))


def test_boolean_mask():
    a = np.array([np.arange(5), [5, 0, 7, 0, 9]])
    result = p3.boolean_mask(a)
    assert list(result) == [7, 9]


def test_skalarprodukt():
    u = np.array([0, 1, 0])
    v = np.array([1, 0, 0])
    assert p3.skalarprodukt(u, v) == 0
    u2 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    assert p3.skalarprodukt(u2, v2) == 32


# ------------------------------------------------------------
# Pandas: Series
# ------------------------------------------------------------

def test_create_series():
    s = p3.create_series()
    assert isinstance(s, pd.Series)
    assert list(s.index) == ["w", "x", "y", "z"]
    assert list(s.values) == [42, 44, 45, 47]


def test_series_slice():
    s = pd.Series([42, 44, 45, 47], index=["w", "x", "y", "z"])
    teil = p3.series_slice(s)
    assert list(teil.index) == ["x", "y"]
    assert list(teil.values) == [44, 45]


def test_series_sum():
    my_index = ["w", "x", "y", "z"]
    my_index2 = ["a", "x", "y", "z"]
    s1 = pd.Series([1, 2, 3, 4], index=my_index)
    s2 = pd.Series([4, 5, 4, 5], index=my_index2)
    a = p3.series_sum(s1, s2)
    assert math.isnan(a["w"])
    assert math.isnan(a["a"])
    assert a["x"] == 7
    assert a["y"] == 7
    assert a["z"] == 9


def test_drop_nan():
    a = pd.Series([np.nan, 7.0, np.nan, 9.0], index=["a", "x", "w", "z"])
    d = p3.drop_nan(a)
    assert list(d.index) == ["x", "z"]
    assert list(d.values) == [7.0, 9.0]


def test_fill_nan():
    a = pd.Series([np.nan, 7.0, np.nan, 9.0], index=["a", "x", "w", "z"])
    f = p3.fill_nan(a, 42)
    assert f["a"] == 42
    assert f["w"] == 42
    assert f["x"] == 7.0


def test_is_nan():
    a = pd.Series([np.nan, 7.0, np.nan, 9.0], index=["a", "x", "w", "z"])
    n = p3.is_nan(a)
    assert bool(n["a"]) is True
    assert bool(n["x"]) is False
    assert bool(n["w"]) is True


# ------------------------------------------------------------
# Pandas: DataFrames
# ------------------------------------------------------------

def _erwartetes_df():
    jahre = range(2018, 2022)
    la = pd.Series([4926, 4796, 4601, 4490], index=jahre, name="HAW")
    reg = pd.Series([11328, 11167, 11020, 11003], index=jahre, name="OTH")
    deg = pd.Series([5928, 6454, 6369, 6809], index=jahre, name="THD")
    return pd.DataFrame([la, reg, deg])


def test_create_dataframe():
    df = p3.create_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert list(df.index) == ["HAW", "OTH", "THD"]
    assert list(df.columns) == [2018, 2019, 2020, 2021]
    assert df.loc["HAW"][2019] == 4796


def test_column_2020():
    df = _erwartetes_df()
    col = p3.column_2020(df)
    assert isinstance(col, pd.Series)
    assert col["HAW"] == 4601
    assert col["OTH"] == 11020
    assert col["THD"] == 6369


def test_row_haw():
    df = _erwartetes_df()
    row = p3.row_haw(df)
    assert isinstance(row, pd.Series)
    assert row[2018] == 4926
    assert row[2021] == 4490


def test_value_haw_2020():
    df = _erwartetes_df()
    assert p3.value_haw_2020(df) == 4601


def test_more_4700():
    df = _erwartetes_df()
    m = p3.more_4700(df)
    assert math.isnan(m.loc["HAW"][2020])
    assert math.isnan(m.loc["HAW"][2021])
    assert m.loc["HAW"][2018] == 4926
    assert m.loc["OTH"][2021] == 11003
