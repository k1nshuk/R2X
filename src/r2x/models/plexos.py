# plexos.py
"""
The following file contains Pydantic models for a PLEXOS model
"""
from typing import Annotated, Union, Any
from pydantic import Field, NonNegativeFloat, NonNegativeInt

from r2x.enums import PrimeMoversType, StorageTechs, ThermalFuels
from r2x.models.core import BaseComponent, Device, StaticInjection
from r2x.models.core import Device, InputOutput, MinMax, UpDown
from r2x.models.topology import ACBus
from r2x.units import (
    ActivePower,
    ApparentPower,
    Energy,
    Percentage,
    PowerRate,
    Time,
    VOMPrice,
    ureg,
)

class PlexosGenerator(Device):
    """PLEXOS Generator Class"""

    # We will add the generator properies here. Costing should probably be its
    # own model

    # TODO: Check if this needs to be renamed to bus to be consistent with R2X
    # PLEXOS uses the term node to refer to a bus
    node: Union[Annotated[ACBus, Field(description="Bus where the generator is connected.")], None] = None
    fuel: Union[Annotated[str, Field(description="Fuel type of the generator.")] , None] = None
    max_capacity: Union[Annotated[
        ActivePower,
        Field(ge=0, description="Maximum output power rating of the unit (MW)."),
    ], None] = ActivePower(0, "MW")
    min_stable_level: Annotated[ActivePower, Field(description="Minimum rated power generation.")] = (
        0 * ureg.MW
    )
    units: Union[Annotated[NonNegativeInt, Field(description="Number of generating units")] , None] = None
    load_points : Union[
        Annotated[
            list[NonNegativeFloat],
            Field(description="List of load points for defining multi-point generator heat rate functions")
        ],
        None
    ] = None
    heat_reate : Union[
        Annotated[NonNegativeFloat, Field(description="Average heat rate of the generator at each load point.")],
        None
    ] = None
    heat_rate_base : Union[
        Annotated[NonNegativeFloat, Field(description="Base heat rate of the generator.")],
        None
    ] = None
    heat_rate_incr : Union[
        Annotated[list[NonNegativeFloat], Field(description="Incremental heat rate polynomial coefficeints for the load point.")],
        None
    ] = None
    start_cost: Union[Annotated[NonNegativeFloat, Field(description="Cost in $ of starting a unit.")] , None] = None
    shutdown_cost: Union[
        Annotated[NonNegativeFloat, Field(description="Cost in $ of shuting down a unit.")], None] = None
    min_up_time: (
        Annotated[
            Time,
            Field(ge=0, description="Minimum up time in hours for UC decision."),
        ]
        | None
    ) = None
    min_down_time: (
        Annotated[
            Time,
            Field(ge=0, description="Minimum down time in hours for UC decision."),
        ]
        | None
    ) = None
    max_ramp_up: (
        Annotated[
            PowerRate,
            Field(description="Ramping rate on the positve direction."),
        ]
        | None
    ) = None
    max_ramp_down: (
        Annotated[
            PowerRate,
            Field(description="Ramping rate on the negative direction."),
        ]
        | None
    ) = None
    pump_efficiency: (
        Annotated[
            Percentage
            Field(description="Efficiency of the pump in percent.",)
        ]
        | None
    ) = None
    pump_load: Annotated[
        ActivePower | None,
        Field(description="Load of the pump in MW.",)
    ]
    mean_time_to_repair: (
        Annotated[
            Time,
            Field(gt=0, description="Total hours to repair after outage occur."),
        ]
        | None
    ) = None
    generator_commit: Annotated[
        int,
        Field(
            ge=-1
            description=("Number of units that should be committed. -1 for any period menas the unit commitment is optimized the ususal way.")
        )
    ] | None = None
    forced_outage_rate: (
        Annotated[
            Percentage,
            Field(description="Expected level of unplanned outages in percent."),
        ]
        | None
    ) = None
    
    
    # The following ones below are copied from r2x/models/generators.py and need to be checked for
    # with PLEXOS models
    active_power: Annotated[
        ActivePower,
        Field(
            description=(
                "Initial active power set point of the unit in MW. For power flow, this is the steady "
                "state operating point of the system."
            ),
        ),
    ] = ActivePower(0.0, "MW")
    reactive_power: Annotated[
        ApparentPower | None,
        Field(
            description=(
                "Reactive power set point of the unit in MW. For power flow, this is the steady "
                "state operating point of the system."
            ),
        ),
    ] = ApparentPower(0.0, "MVA")
    base_mva: float = 1
    base_power: Annotated[
        ApparentPower | None,
        Field(
            gt=0,
            description="Base power of the unit (MVA) for per unitization.",
        ),
    ] = None
    must_run: Annotated[int | None, Field(description="If we need to force the dispatch of the device.")] = (
        None
    )
    vom_price: Annotated[VOMPrice, Field(description="Variable operational price $/MWh.")] | None = None
    prime_mover_type: (
        Annotated[PrimeMoversType, Field(description="Prime mover technology according to EIA 923.")] | None
    ) = None
    unit_type: Annotated[
        PrimeMoversType | None, Field(description="Prime mover technology according to EIA 923.")
    ] = None
    planned_outage_rate: (
        Annotated[
            Percentage,
            Field(description="Expected level of planned outages in percent."),
        ]
        | None
    ) = None
    active_power_limits: Annotated[
        MinMax | None, Field(description="Maximum output power rating of the unit (MVA).")
    ] = None
    reactive_power_limits: Annotated[
        MinMax | None, Field(description="Maximum output power rating of the unit (MVA).")
    ] = None