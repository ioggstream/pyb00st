import os
from pyb00st.movehub import MoveHub
from pyb00st.constants import *
import pytest
from time import sleep

MY_MOVEHUB_ADD = os.environ['hub']
MY_BTCTRLR_HCI = 'hci1'


@pytest.fixture
def hub():
    return MoveHub(MY_MOVEHUB_ADD, 'BlueZ', MY_BTCTRLR_HCI)


def test_connection(hub):
    try:
        hub.start()
        hub.subscribe_all()
        hub.listen_hubtilt(MODE_HUBTILT_BASIC)

        for i in range(3):
            is_connected = hub.is_connected()
            print('Is connected: ', is_connected)
            sleep(1)
    finally:
        hub.stop()


def test_motor_a(hub):
    raise NotImplementedError


def test_motor_b(hub):
    raise NotImplementedError

def test_motor_x(hub):
    raise NotImplementedError
