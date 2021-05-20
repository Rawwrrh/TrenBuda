import pytest

from ..metro import Metro


def test_that_metro_loads():
    metro = Metro.fromJson()
    assert len(metro.stations) > 1


def test_that_valid_station_works():
    metro = Metro.fromJson()
    station = metro.station(1)
    assert station.id == 1

    station = metro.station("1")
    assert station.id == 1


def test_that_valid_station_label_works():
    metro = Metro.fromJson()
    station = metro.station("B")
    assert station.id == 1


def test_that_invalid_station_throws():
    metro = Metro.fromJson()
    with pytest.raises(Exception):
        metro.station("R")


def test_that_labels_and_stations_are_the_same():
    metro = Metro.fromJson()
    stations = metro.stations.values()
    labels = metro.labels.values()

    assert len(stations) == len(labels)
