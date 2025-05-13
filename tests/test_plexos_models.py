# test_plexos_models.py
import pytest

from r2x.enums import PrimeMoversType
from r2x.models import Generator, ACBus, Emission, HydroPumpedStorage, ThermalStandard
from r2x.models import MinMax
from r2x.parser.handler import create_model_instance
from r2x.units import EmissionRate, ureg

from r2x.models import Transformer2W, TapTransformer, PhaseShiftingTransformer
from r2x.models.plexos.transformers import PlexosTransformer
from

@pytest.fixture
def create_transformer_2w():
    return Transformer2W.example()

@pytest.fixture
def create_tap_transformer():
    return TapTransformer.example()

@pytest.fixture
def create_phase_shifting_transformer():
    return PhaseShiftingTransformer.example()


def test_plexos_transformer():
    transformer = PlexosTransformer.example()
    assert isinstance(transformer, PlexosTransformer)

def test_plexos_transformer_2w():
    pass