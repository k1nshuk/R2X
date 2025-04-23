# Fuels.py
from typing import Annotated, Union, Any, B
from pydantic import Field, NonNegativeFloat, NonNegativeInt, NonPositiveInt

from r2x.enums import PrimeMoversType, StorageTechs, ThermalFuels
from r2x.models.core import BaseComponent, Device, StaticInjection
from r2x.models.core import Device, InputOutput, MinMax, UpDown
from r2x.models.topology import ACBus, Bus
from r2x.units import (
    ActivePower,
    ApparentPower,
    Energy,
    Percentage,
    PowerRate,
    Time,
    VOMPrice,
    DSPBidPrice,
    ureg,
)

class PlexosFuel():
    """Class that holds attributes about PLEXOS Fuels for thermal generators"""

    # Fuel attributes
    energy_density: Annotated[
        NonNegativeFloat,
        Field(
            alias="Energy Density",
            description="Energy per unit of the fuel in MJ",
        ),
    ] = 0.0
    
    unit: Annotated[
        Union[str, int],
        Field(
            alias="Unit",
            description="Unit the fuel is measured in",
        ),
    ] = 0

    # Fuel input properties
    # Fuel storage properties
    balance_period: Annotated[
        int,
        Field(
            alias="Balance Period",
            description="Frequency of storage balance",
            ge=0,
            le=6
        ),
    ] = 0
    
    decomposition_bound_penalty: Annotated[
        NonNegativeFloat,
        Field(
            alias="Decomposition Bound Penalty",
            description="Penalty applied to violation of stockpile bounds when the decomposition implies possible violations.",
            ge=0
        ),
    ] = 1000000.0
    
    decomposition_method: Annotated[
        int,
        Field(
            alias="Decomposition Method",
            description="Method used to pass the optimal stockpile trajectory from one simulation phase to the next.",
            ge=0,
            le=2
        ),
    ] = 1
    
    decomposition_penalty_a: Annotated[
        float,
        Field(
            alias="Decomposition Penalty a",
            description="Decomposition stockpile target penalty function 'a' term.",
        ),
    ] = 0.0489
    
    decomposition_penalty_b: Annotated[
        float,
        Field(
            alias="Decomposition Penalty b",
            description="Decomposition stockpile target penalty function 'b' term.",
        ),
    ] = 0.6931
    
    decomposition_penalty_c: Annotated[
        float,
        Field(
            alias="Decomposition Penalty c",
            description="Decomposition stockpile target penalty function 'c' term.",
        ),
    ] = 0
    
    decomposition_penalty_x: Annotated[
        float,
        Field(
            alias="Decomposition Penalty x",
            description="Decomposition stockpile target penalty function 'x' term.",
        ),
    ] = 1.1
    
    delivery: Annotated[
        float,
        Field(
            alias="Delivery",
            description="Fuel delivered to the stockpile",
        ),
    ] = 0.0
    
    delivery_charge: Annotated[
        float,
        Field(
            alias="Delivery Charge",
            description="Cost of delivering fuel to the stockpile",
        ),
    ] = 0.0
    
    fom_charge: Annotated[
        float,
        Field(
            alias="FO&M Charge",
            description="Annual fixed operation and maintenance charge",
        ),
    ] = 0.0
    
    internal_volume_scalar: Annotated[
        float,
        Field(
            alias="Internal Volume Scalar",
            description="Storage volume scaling factor used internal to the mathematical program.",
            gt=0
        ),
    ] = 1.0
    
    inventory_charge: Annotated[
        float,
        Field(
            alias="Inventory Charge",
            description="Cost applied to closing inventory in the stockpile",
        ),
    ] = 0.0
    
    max_inventory: Annotated[
        float,
        Field(
            alias="Max Inventory",
            description="Maximum fuel allowed in stockpile",
        ),
    ] = 0.0
    
    max_offtake: Annotated[
        float,
        Field(
            alias="Max Offtake",
            description="Maximum fuel offtake per interval",
        ),
    ] = 1e30
    
    max_offtake_day: Annotated[
        float,
        Field(
            alias="Max Offtake Day",
            description="Maximum fuel offtake in day",
        ),
    ] = 1e30
    
    max_offtake_hour: Annotated[
        float,
        Field(
            alias="Max Offtake Hour",
            description="Maximum fuel offtake in hour",
        ),
    ] = 1e30
    
    max_offtake_month: Annotated[
        float,
        Field(
            alias="Max Offtake Month",
            description="Maximum fuel offtake in month",
        ),
    ] = 1e30
    
    max_offtake_penalty: Annotated[
        float,
        Field(
            alias="Max Offtake Penalty",
            description="Penalty applied to violations of [Max Offtake]constraints",
        ),
    ] = -1.0
    
    max_offtake_week: Annotated[
        float,
        Field(
            alias="Max Offtake Week",
            description="Maximum fuel offtake in week",
        ),
    ] = 1e30
    
    max_offtake_year: Annotated[
        float,
        Field(
            alias="Max Offtake Year",
            description="Maximum fuel offtake in year",
        ),
    ] = 1e30
    
    max_withdrawal: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Withdrawal",
            description="Maximum amount of fuel that can be taken from stockpile",
            ge=0
        ),
    ] = 1e30
    
    max_withdrawal_day: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Withdrawal Day",
            description="Maximum amount of fuel that can be taken from stockpile in a day",
            ge=0
        ),
    ] = 1e30
    
    max_withdrawal_hour: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Withdrawal Hour",
            description="Maximum amount of fuel that can be taken from stockpile in a hour",
            ge=0
        ),
    ] = 1e30
    
    max_withdrawal_month: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Withdrawal Month",
            description="Maximum amount of fuel that can be taken from stockpile in a month",
            ge=0
        ),
    ] = 1e30
    
    max_withdrawal_week: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Withdrawal Week",
            description="Maximum amount of fuel that can be taken from stockpile in a week",
            ge=0
        ),
    ] = 1e30
    
    max_withdrawal_year: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Withdrawal Year",
            description="Maximum amount of fuel that can be taken from stockpile in a year",
            ge=0
        ),
    ] = 1e30
    
    min_inventory: Annotated[
        float,
        Field(
            alias="Min Inventory",
            description="Minimum fuel required in stockpile",
        ),
    ] = 0.0
    
    min_offtake: Annotated[
        float,
        Field(
            alias="Min Offtake",
            description="Minimum fuel offtake per interval",
        ),
    ] = 0.0
    
    min_offtake_day: Annotated[
        float,
        Field(
            alias="Min Offtake Day",
            description="Minimum fuel offtake in day",
        ),
    ] = 0.0
    
    min_offtake_hour: Annotated[
        float,
        Field(
            alias="Min Offtake Hour",
            description="Minimum fuel offtake in hour",
        ),
    ] = 0.0
    
    min_offtake_month: Annotated[
        float,
        Field(
            alias="Min Offtake Month",
            description="Minimum fuel offtake in month",
        ),
    ] = 0.0
    
    min_offtake_penalty: Annotated[
        float,
        Field(
            alias="Min Offtake Penalty",
            description="Penalty applied to violations of [Min Offtake] constraints",
        ),
    ] = 1000.0
    
    min_offtake_week: Annotated[
        float,
        Field(
            alias="Min Offtake Week",
            description="Minimum fuel offtake in week",
        ),
    ] = 0.0
    
    min_offtake_year: Annotated[
        float,
        Field(
            alias="Min Offtake Year",
            description="Minimum fuel offtake in year",
        ),
    ] = 0.0
    
    min_withdrawal: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Withdrawal",
            description="Amount of fuel that must be taken from stockpile",
        ),
    ] = 0.0
    
    min_withdrawal_day: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Withdrawal Day",
            description="Amount of fuel that must be taken from stockpile each day",
            ge=0
        ),
    ] = 0.0
    
    min_withdrawal_hour: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Withdrawal Hour",
            description="Amount of fuel that must be taken from stockpile each hour",
            ge=0
        ),
    ] = 0.0
    
    min_withdrawal_month: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Withdrawal Month",
            description="Amount of fuel that must be taken from stockpile each month",
            ge=0
        ),
    ] = 0.0
    
    min_withdrawal_week: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Withdrawal Week",
            description="Amount of fuel that must be taken from stockpile each week",
            ge=0
        ),
    ] = 0.0
    
    min_withdrawal_year: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Withdrawal Year",
            description="Amount of fuel that must be taken from stockpile each year",
            ge=0
        ),
    ] = 0.0
    
    opening_inventory: Annotated[
        NonNegativeFloat,
        Field(
            alias="Opening Inventory",
            description="Initial fuel in the stockpile",
        ),
    ] = 0.0
    
    # Fuel price attributes
    price: Annotated[
        float,
        Field(
            alias="Price",
            description="Fuel price",
        ),
    ] = 0.0
    
    price_incr: Annotated[
        float,
        Field(
            alias="Price Incr",
            description="Increment to the price of the fuel",
        ),
    ] = 0.0
    
    price_scalar: Annotated[
        float,
        Field(
            alias="Price Scalar",
            description="Multiplier on the price of the fuel",
        ),
    ] = 1.0
    
    reservation_charge: Annotated[
        float,
        Field(
            alias="Reservation Charge",
            description="Cost applied to unused inventory capacity in the stockpile",
        ),
    ] = 0.0
    
    shadow_price: Annotated[
        float,
        Field(
            alias="Shadow Price",
            description="Shadow price of fuel (if defined as input, sets the internal price for fuel)",
        ),
    ] = 0.0
    
    shadow_price_incr: Annotated[
        float,
        Field(
            alias="Shadow Price Incr",
            description="Increment to the shadow price of the fuel (use only when Shadow Price is defined)",
        ),
    ] = 0.0
    
    shadow_price_scalar: Annotated[
        float,
        Field(
            alias="Shadow Price Scalar",
            description="Multiplier on the shadow price of the fuel (use only when Shadow Price is defined)",
        ),
    ] = 1.0
    
    tax: Annotated[
        float,
        Field(
            alias="Tax",
            description="Fuel tax",
            # Multi-band=True in the table
        ),
    ] = 0.0
    
    units: Annotated[
        int,
        Field(
            alias="Units",
            description="Flag if fuel exists",
            ge=0,
            le=1
        ),
    ] = 1
    
    withdrawal_charge: Annotated[
        float,
        Field(
            alias="Withdrawal Charge",
            description="Incremental cost of taking fuel from stockpile",
        ),
    ] = 0.0
    
    # Pass-through values
    x: Annotated[
        float,
        Field(
            alias="x",
            description="Value to pass-through to solution",
            # Multi-band=True in the table
        ),
    ] = 0.0
    
    y: Annotated[
        float,
        Field(
            alias="y",
            description="Value to pass-through to solution",
            # Multi-band=True in the table
        ),
    ] = 0.0
    
    z: Annotated[
        float,
        Field(
            alias="z",
            description="Value to pass-through to solution",
            # Multi-band=True in the table
        ),
    ] = 0.0

    # Fuel Companies Input Properties
    share: Annotated[
        Percentage,
        Field(
            alias="Share",
            description="Percentage share of ownership",
            ge=0.0,
            le=100.0
        ),
    ] = Percentage(100.0, "%")

    # Fuel Facilities Input Properties
    consumption_rate: Annotated[
        float,
        Field(
            alias="Consumption Rate",
            description="Fuel consumed per unit of the Primary Output from the Facility",
        ),
    ] = 0.0

    # Fuel constraints Input Properties
    closing_inventory_coefficient: Annotated[
        float,
        Field(
            alias="Closing Inventory Coefficient",
            description="Coefficient of fuel stockpile closing inventory.",
        ),
    ] = 0.0

    delivery_coefficient: Annotated[
        float,
        Field(
            alias="Delivery Coefficient",
            description="Coefficient of delivery to fuel stockpile.",
        ),
    ] = 0.0

    emission_coefficient: Annotated[
        float,
        Field(
            alias="Emission Coefficient",
            description="Coefficient of fuel emission",
        ),
    ] = 0.0

    generation_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Coefficient",
            description="Coefficient of generation with given fuel",
        ),
    ] = ActivePower(0.0, "MW")

    in_use_coefficient: Annotated[
        float,
        Field(
            alias="In Use Coefficient",
            description="Boolean value (1 if the Fuel is in use, 0 otherwise)",
        ),
    ] = 0.0

    inventory_change_coefficient: Annotated[
        float,
        Field(
            alias="Inventory Change Coefficient",
            description="Coefficient of change in fuel stockpile level.",
        ),
    ] = 0.0

    offtake_coefficient: Annotated[
        float,
        Field(
            alias="Offtake Coefficient",
            description="Coefficient of fuel offtake",
        ),
    ] = 0.0

    withdrawal_coefficient: Annotated[
        float,
        Field(
            alias="Withdrawal Coefficient",
            description="Coefficient of withdrawal from fuel stockpile.",
        ),
    ] = 0.0

    # Fuel Objectives input properties
    objective_closing_inventory_coefficient: Annotated[
        float,
        Field(
            alias="Closing Inventory Coefficient",
            description="Coefficient of fuel stockpile closing inventory",
        ),
    ] = 0.0

    objective_delivery_coefficient: Annotated[
        float,
        Field(
            alias="Delivery Coefficient",
            description="Coefficient of delivery to fuel stockpile",
        ),
    ] = 0.0

    objective_emission_coefficient: Annotated[
        float,
        Field(
            alias="Emission Coefficient",
            description="Coefficient of fuel emission",
        ),
    ] = 0.0

    objective_generation_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Coefficient",
            description="Coefficient of generation with given fuel",
        ),
    ] = ActivePower(0.0, "MW")

    objective_in_use_coefficient: Annotated[
        float,
        Field(
            alias="In Use Coefficient",
            description="Boolean value (1 if the Fuel is in use, 0 otherwise)",
        ),
    ] = 0.0

    objective_inventory_change_coefficient: Annotated[
        float,
        Field(
            alias="Inventory Change Coefficient",
            description="Coefficient of change in fuel stockpile level",
        ),
    ] = 0.0

    objective_offtake_coefficient: Annotated[
        float,
        Field(
            alias="Offtake Coefficient",
            description="Coefficient of fuel offtake",
        ),
    ] = 0.0

    objective_withdrawal_coefficient: Annotated[
        float,
        Field(
            alias="Withdrawal Coefficient",
            description="Coefficient of withdrawal from fuel stockpile",
        ),
    ] = 0.0

    # Fuel Conditions Input Properties
    offtake_coefficients: Annotated[
        float,
        Field(
            alias="Offtake Coefficients",
            description="Coefficient of fuel offtake",
        ),
    ] = 0.0

    # TODO: Do we need output properties?