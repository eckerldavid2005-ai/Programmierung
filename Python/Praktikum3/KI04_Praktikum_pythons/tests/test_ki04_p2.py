import numpy as np
import pytest
import ki04_p2


# ------------------------------------------------------------
# Fehlermasse
# ------------------------------------------------------------

def test_fehler_summe():
    y_ist = np.array([3.0, 5.0, 7.0])
    y_pred = np.array([2.5, 5.5, 6.0])
    # 0.5 - 0.5 + 1.0 = 1.0
    assert np.isclose(ki04_p2.fehler_summe(y_ist, y_pred), 1.0)


def test_fehler_betrags_summe():
    y_ist = np.array([3.0, 5.0, 7.0])
    y_pred = np.array([2.5, 5.5, 6.0])
    # |0.5| + |-0.5| + |1.0| = 2.0
    assert np.isclose(ki04_p2.fehler_betrags_summe(y_ist, y_pred), 2.0)


def test_sse():
    y_ist = np.array([3.0, 5.0, 7.0])
    y_pred = np.array([2.5, 5.5, 6.0])
    # 0.25 + 0.25 + 1.0 = 1.5
    assert np.isclose(ki04_p2.sse(y_ist, y_pred), 1.5)


def test_mse():
    y_ist = np.array([3.0, 5.0, 7.0])
    y_pred = np.array([2.5, 5.5, 6.0])
    # (0.25 + 0.25 + 1.0) / 3 = 0.5
    assert np.isclose(ki04_p2.mse(y_ist, y_pred), 0.5)


def test_rmse():
    y_ist = np.array([3.0, 5.0, 7.0])
    y_pred = np.array([2.5, 5.5, 6.0])
    # sqrt(0.5) -- NICHT der Mittelwert der Einzelwurzeln!
    assert np.isclose(ki04_p2.rmse(y_ist, y_pred), np.sqrt(0.5))


def test_rmse_nicht_mae():
    # Sicherstellen, dass RMSE wirklich erst mittelt und dann die
    # Wurzel zieht (nicht den MAE als "RMSE" zurueckgibt):
    y_ist = np.array([0.0, 4.0])
    y_pred = np.array([0.0, 0.0])
    # MSE = 8, RMSE = sqrt(8) ~ 2.83 -- waere MAE 2.0
    assert not np.isclose(ki04_p2.rmse(y_ist, y_pred), 2.0)
    assert np.isclose(ki04_p2.rmse(y_ist, y_pred), np.sqrt(8.0))


# ------------------------------------------------------------
# Regression von Hand
# ------------------------------------------------------------

def test_steigung_a_perfekte_gerade():
    # perfekte Gerade y = 2x + 1 -> a muss exakt 2 sein
    x = np.array([1.0, 2.0, 3.0, 4.0])
    y = 2 * x + 1
    assert np.isclose(ki04_p2.steigung_a(x, y), 2.0)


def test_steigung_a_vorlesungsbeispiel():
    # verrauschte Daten (aus VL4_1, Selbsttest-Werte):
    x = np.array([1.0, 2.0, 4.0, 5.0, 7.0, 8.0])
    y = np.array([7.0, 9.5, 16.0, 19.0, 26.5, 28.5])
    a = ki04_p2.steigung_a(x, y)
    assert 3.1 < a < 3.3  # Steigung betraegt exakt 3.18


def test_achsenabschnitt_b():
    x = np.array([1.0, 2.0, 3.0, 4.0])
    y = 2 * x + 1
    assert np.isclose(ki04_p2.achsenabschnitt_b(x, y), 1.0)


def test_vorhersage():
    x = np.array([1.0, 2.0, 3.0, 4.0])
    y = 2 * x + 1
    # Vorhersage fuer x_neu = 10 -> 21
    assert np.isclose(ki04_p2.vorhersage(10.0, x, y), 21.0)


def test_vorhersage_sklearn_konsistenz():
    # "von Hand" muss dasselbe liefern wie sklearn
    from sklearn import linear_model
    x = np.array([1.0, 2.0, 4.0, 5.0, 7.0, 8.0, 9.0])
    y = 3.17 * x + 3.93 + np.array([0.5, -0.3, 0.2, -0.5, 0.4, -0.2, 0.1])
    lin = linear_model.LinearRegression()
    lin.fit(x.reshape(-1, 1), y)
    y_hand = ki04_p2.vorhersage(6.0, x, y)
    y_skl = lin.predict([[6.0]])[0]
    assert np.isclose(y_hand, y_skl, atol=1e-10)
