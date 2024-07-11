import unittest
import pytest

@pytest.mark.usefixtures("setUp_and_teaDown")
class BaseFixture:
    pass