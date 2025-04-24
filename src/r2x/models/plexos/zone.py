# Zone.py
"""
The following file contains Pydantic models for a Plexos zone
"""
from typing import Annotated, Union, Any, List
from pydantic import Field, NonNegativeFloat, NonNegativeInt, NonPositiveInt

from r2x.enums import PrimeMoversType, StorageTechs, ThermalFuels
from r2x.models.core import BaseComponent, Device, StaticInjection
from r2x.models.core import Device, InputOutput, MinMax, UpDown
from r2x.models.topology import ACBus, Bus, LoadZone
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

class PlexosZone(LoadZone):
    """
    Class that holds all attributes of a PLEXOS Zone Class
    """

    # Capacity pricing attributes
    capacity_excess_price: Annotated[
        NonNegativeFloat,
        Field(
            alias="Capacity Excess Price",
            description="Penalty for an excess of capacity reserves",
            ge=0,
        ),
    ] = 0.0
    
    capacity_price_cap: Annotated[
        float,
        Field(
            alias="Capacity Price Cap",
            description="Cap on the capacity price",
        ),
    ] = 1e30
    
    capacity_price_floor: Annotated[
        float,
        Field(
            alias="Capacity Price Floor",
            description="Floor on the capacity price",
        ),
    ] = -1e30
    
    capacity_shortage_price: Annotated[
        NonNegativeFloat,
        Field(
            alias="Capacity Shortage Price",
            description="Penalty for a shortage of capacity reserves",
            ge=0,
        ),
    ] = 0.0
    
    firm_capacity_incr: Annotated[
        ActivePower,
        Field(
            alias="Firm Capacity Incr",
            description="Firm Capacity not explicitly modeled that should be included in reserve margin calculations",
        ),
    ] = ActivePower(0.0, "MW")
    
    firm_capacity_values: Annotated[
        List[ActivePower],
        Field(
            alias="Firm Capacity Values",
            description="Firm capacity values corresponding to the Capacity Points of connected Firm Capacity Groups",
        ),
    ] = []
    
    # Load attributes
    formulate_load: Annotated[
        NonPositiveInt,
        Field(
            alias="Formulate Load",
            description="Flag if the Load is formulated as a decision variable",
            ge=-1,
            le=0,
        ),
    ] = 0
    
    load: Annotated[
        ActivePower,
        Field(
            alias="Load",
            description="Load",
        ),
    ] = ActivePower(0.0, "MW")
    
    load_participation_factor: Annotated[
        float,
        Field(
            alias="Load Participation Factor",
            description="Proportion of region load that occurs in the zone",
            ge=-1,
            le=1,
        ),
    ] = 0.0
    
    load_scalar: Annotated[
        float,
        Field(
            alias="Load Scalar",
            description="Scale factor for input [Load]",
        ),
    ] = 1.0
    
    load_settlement_model: Annotated[
        int,
        Field(
            alias="Load Settlement Model",
            description="Model used to determine energy prices reported in the zone.",
            ge=0,
            le=2,
        ),
    ] = 0
    
    lolp_target: Annotated[
        Percentage,
        Field(
            alias="LOLP Target",
            description="Loss of Load Probability target for this zone",
            ge=0,
            le=100,
        ),
    ] = Percentage(0.0, "%")
    
    maintenance_factor: Annotated[
        NonNegativeFloat,
        Field(
            alias="Maintenance Factor",
            description="Maintenance factor",
            ge=0,
        ),
    ] = 1.0
    
    # Capacity reserve margin attributes
    max_capacity_reserve_margin: Annotated[
        Percentage,
        Field(
            alias="Max Capacity Reserve Margin",
            description="Maximum capacity reserve margin for capacity planning",
        ),
    ] = [Percentage(1e30, "%")]
    
    max_capacity_reserves: Annotated[
        ActivePower,
        Field(
            alias="Max Capacity Reserves",
            description="Maximum capacity reserves allowed",
        ),
    ] = ActivePower(1e30, "MW")
    
    # Dump energy constraints
    max_dump_energy: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Dump Energy",
            description="Maximum dump energy",
            ge=0,
        ),
    ] = 1e30
    
    max_dump_energy_day: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Dump Energy Day",
            description="Maximum dump energy in day",
            ge=0,
        ),
    ] = 1e30
    
    max_dump_energy_factor: Annotated[
        Percentage,
        Field(
            alias="Max Dump Energy Factor",
            description="Maximum proportion of energy dumped",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_dump_energy_factor_day: Annotated[
        Percentage,
        Field(
            alias="Max Dump Energy Factor Day",
            description="Maximum proportion of energy dumped in day",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_dump_energy_factor_hour: Annotated[
        Percentage,
        Field(
            alias="Max Dump Energy Factor Hour",
            description="Maximum proportion of energy dumped in hour",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_dump_energy_factor_month: Annotated[
        Percentage,
        Field(
            alias="Max Dump Energy Factor Month",
            description="Maximum proportion of energy dumped in month",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_dump_energy_factor_week: Annotated[
        Percentage,
        Field(
            alias="Max Dump Energy Factor Week",
            description="Maximum proportion of energy dumped in week",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_dump_energy_factor_year: Annotated[
        Percentage,
        Field(
            alias="Max Dump Energy Factor Year",
            description="Maximum proportion of energy dumped in year",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_dump_energy_hour: Annotated[
        ActivePower,
        Field(
            alias="Max Dump Energy Hour",
            description="Maximum dump energy in hour",
            ge=0,
        ),
    ] = ActivePower(1e30, "MW")
    
    max_dump_energy_month: Annotated[
        Energy,
        Field(
            alias="Max Dump Energy Month",
            description="Maximum dump energy in month in GWh",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_dump_energy_week: Annotated[
        Energy,
        Field(
            alias="Max Dump Energy Week",
            description="Maximum dump energy in week",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_dump_energy_year: Annotated[
        Energy,
        Field(
            alias="Max Dump Energy Year",
            description="Maximum dump energy in year",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    # Generation curtailment constraints
    max_generation_curtailed: Annotated[
        Energy,
        Field(
            alias="Max Generation Curtailed",
            description="Maximum generation curtailed",
            ge=0,
        ),
    ] = Energy(1e30, "MWh")
    
    max_generation_curtailed_day: Annotated[
        Energy,
        Field(
            alias="Max Generation Curtailed Day",
            description="Maximum generation curtailed in day",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_generation_curtailed_hour: Annotated[
        ActivePower,
        Field(
            alias="Max Generation Curtailed Hour",
            description="Maximum generation curtailed in hour",
            ge=0,
        ),
    ] = ActivePower(1e30, "MW")
    
    max_generation_curtailed_month: Annotated[
        Energy,
        Field(
            alias="Max Generation Curtailed Month",
            description="Maximum generation curtailed in month",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    
    max_generation_curtailed_week: Annotated[
        Energy,
        Field(
            alias="Max Generation Curtailed Week",
            description="Maximum generation curtailed in week",
            ge=0,
        ),
    ] = 1e30
    
    max_generation_curtailed_year: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Generation Curtailed Year",
            description="Maximum generation curtailed in year",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_generation_curtailment_factor: Annotated[
        Percentage,
        Field(
            alias="Max Generation Curtailment Factor",
            description="Maximum proportion of generation curtailed",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_generation_curtailment_factor_day: Annotated[
        Percentage,
        Field(
            alias="Max Generation Curtailment Factor Day",
            description="Maximum proportion of generation curtailed in day",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_generation_curtailment_factor_hour: Annotated[
        Percentage,
        Field(
            alias="Max Generation Curtailment Factor Hour",
            description="Maximum proportion of generation curtailed in hour",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_generation_curtailment_factor_month: Annotated[
        Percentage,
        Field(
            alias="Max Generation Curtailment Factor Month",
            description="Maximum proportion of generation curtailed in month",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_generation_curtailment_factor_week: Annotated[
        Percentage,
        Field(
            alias="Max Generation Curtailment Factor Week",
            description="Maximum proportion of generation curtailed in week",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_generation_curtailment_factor_year: Annotated[
        Percentage,
        Field(
            alias="Max Generation Curtailment Factor Year",
            description="Maximum proportion of generation curtailed in year",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_maintenance: Annotated[
        ActivePower,
        Field(
            alias="Max Maintenance",
            description="Maximum generation capacity allowed to be scheduled on maintenance",
            ge=0,
        ),
    ] = ActivePower(1e30, "MW")
    
    # Unserved energy constraints
    max_unserved_energy: Annotated[
        Energy,
        Field(
            alias="Max Unserved Energy",
            description="Maximum unserved energy",
            ge=0,
        ),
    ] = Energy(1e30, "MWh")
    
    max_unserved_energy_day: Annotated[
        Energy,
        Field(
            alias="Max Unserved Energy Day",
            description="Maximum unserved energy in day",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_unserved_energy_factor: Annotated[
        Percentage,
        Field(
            alias="Max Unserved Energy Factor",
            description="Maximum proportion of energy unserved",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_unserved_energy_factor_day: Annotated[
        Percentage,
        Field(
            alias="Max Unserved Energy Factor Day",
            description="Maximum proportion of energy unserved in day",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_unserved_energy_factor_hour: Annotated[
        Percentage,
        Field(
            alias="Max Unserved Energy Factor Hour",
            description="Maximum proportion of energy unserved in hour",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_unserved_energy_factor_month: Annotated[
        Percentage,
        Field(
            alias="Max Unserved Energy Factor Month",
            description="Maximum proportion of energy unserved in month",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_unserved_energy_factor_week: Annotated[
        Percentage,
        Field(
            alias="Max Unserved Energy Factor Week",
            description="Maximum proportion of energy unserved in week",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_unserved_energy_factor_year: Annotated[
        Percentage,
        Field(
            alias="Max Unserved Energy Factor Year",
            description="Maximum proportion of energy unserved in year",
            ge=0,
        ),
    ] = Percentage(100.0, "%")
    
    max_unserved_energy_hour: Annotated[
        ActivePower,
        Field(
            alias="Max Unserved Energy Hour",
            description="Maximum unserved energy in hour",
            ge=0,
        ),
    ] = ActivePower(1e30, "MW")
    
    max_unserved_energy_month: Annotated[
        Energy,
        Field(
            alias="Max Unserved Energy Month",
            description="Maximum unserved energy in month",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_unserved_energy_week: Annotated[
        Energy,
        Field(
            alias="Max Unserved Energy Week",
            description="Maximum unserved energy in week",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    max_unserved_energy_year: Annotated[
        Energy,
        Field(
            alias="Max Unserved Energy Year",
            description="Maximum unserved energy in year",
            ge=0,
        ),
    ] = Energy(1e30, "GWh")
    
    # Minimum capacity constraints
    min_capacity_reserve_margin: Annotated[
        Percentage,
        Field(
            alias="Min Capacity Reserve Margin",
            description="Minimum capacity reserve margin for capacity planning",
        ),
    ] = Percentage(-1e30, "%")
    
    min_capacity_reserves: Annotated[
        ActivePower,
        Field(
            alias="Min Capacity Reserves",
            description="Minimum capacity reserves allowed",
        ),
    ] = ActivePower(-1e30, "MW")
    
    min_native_capacity_reserve_margin: Annotated[
        Percentage,
        Field(
            alias="Min Native Capacity Reserve Margin",
            description="Minimum capacity reserve margin supplied only by sources in the Zone",
        ),
    ] = Percentage(-1e30, "%")
    
    min_native_capacity_reserves: Annotated[
        List[ActivePower],
        Field(
            alias="Min Native Capacity Reserves",
            description="Minimum capacity reserves supplied only by sources in the Zone",
        ),
    ] = [ActivePower(-1e30, "MW")]
    
    # Other zone attributes
    peak_period: Annotated[
        NonPositiveInt,
        Field(
            alias="Peak Period",
            description="Indicates periods that include the peak load",
            ge=-1,
            le=0,
        ),
    ] = -1
    
    seasonal_reserve_constraint_active: Annotated[
        NonPositiveInt,
        Field(
            alias="Seasonal Reserve Constraint Active",
            description="Specifies when a seasonal capacity reserve is active",
            ge=-1,
            le=0,
        ),
    ] = 0
    
    transmission_clustering_level: Annotated[
        int,
        Field(
            alias="Transmission Clustering Level",
            description="Cluster nodes until this number of equivalent nodes remain (-1 means no clustering)",
        ),
    ] = -1
    
    transmission_clustering_tolerance: Annotated[
        Percentage,
        Field(
            alias="Transmission Clustering Tolerance",
            description="Cluster nodes until this level of accuracy is reached (100% means no clustering)",
            ge=0,
            le=100,
        ),
    ] = Percentage(100.0, "%")
    
    units: Annotated[
        int,
        Field(
            alias="Units",
            description="Flag if the Zone is in service",
            ge=0,
            le=1,
        ),
    ] = 1
    
    wheeling_charge: Annotated[
        float,
        Field(
            alias="Wheeling Charge",
            description="Wheeling charge on exports from the zone",
        ),
    ] = 0.0
    
    wheeling_method: Annotated[
        int,
        Field(
            alias="Wheeling Method",
            description="Export wheeling charge method",
            ge=1,
            le=2,
        ),
    ] = 1
    
    # Pass-through values
    x: Annotated[
        float,
        Field(
            alias="x",
            description="Value to pass-through to solution",
        ),
    ] = [0.0]
    
    y: Annotated[
        float,
        Field(
            alias="y",
            description="Value to pass-through to solution",
        ),
    ] = 0.0
    
    z: Annotated[
        List[float],
        Field(
            alias="z",
            description="Value to pass-through to solution",
        ),
    ] = 0.0

    # Zone Firm Capacity Groups Input Properties
    capacity_points: Annotated[
        ActivePower,
        Field(
            alias="Capacity Points",
            description="Capacity points used for approximating the firm capacity surface",
        ),
    ] = ActivePower(0.0, "MW")

    # Zone Zones Input Properties
    balancing_area_interchange_hurdle: Annotated[
        float,
        Field(
            alias="Balancing Area Interchange Hurdle",
            description="Financial hurdle rate for exports from the parent zone to child zone. $/MWh",
        ),
    ] = 0.0

    max_balancing_area_interchange: Annotated[
        ActivePower,
        Field(
            alias="Max Balancing Area Interchange",
            description="Maximum financial exports from parent zone to child zone.",
        ),
    ] = ActivePower(1e30, "MW")

    max_flow: Annotated[
        ActivePower,
        Field(
            alias="Max Flow",
            description="Maximum flow allowed between the zones",
        ),
    ] = ActivePower(1e30, "MW")

    zone_wheeling_charge: Annotated[
        float,
        Field(
            alias="Wheeling Charge",
            description="Wheeling charge for exports to the zone. $/MWh",
        ),
    ] = 0.0

    # Zone Constraints Input Properties
    capacity_reserves_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Capacity Reserves Coefficient",
            description="Coefficient of total capacity reserves",
        ),
    ] = ActivePower(0.0, "MW")

    committed_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Committed Capacity Coefficient",
            description="Coefficient of generation capacity committed in the zone",
        ),
    ] = ActivePower(0.0, "MW")

    dump_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Dump Energy Coefficient",
            description="Coefficient of dump energy (over generation)",
        ),
    ] = ActivePower(0.0, "MW")

    export_capacity_built_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Export Capacity Built Coefficient",
            description="Coefficient of export capacity built",
        ),
    ] = ActivePower(0.0, "MW")

    export_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Export Capacity Coefficient",
            description="Coefficient of export capacity",
        ),
    ] = ActivePower(0.0, "MW")

    exports_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Exports Coefficient",
            description="Coefficient of zone exports",
        ),
    ] = ActivePower(0.0, "MW")

    firm_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Firm Capacity Coefficient",
            description="Coefficient of total generator [Firm Capacity]",
        ),
    ] = ActivePower(0.0, "MW")

    generation_capacity_built_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Capacity Built Coefficient",
            description="Coefficient of generation capacity built",
        ),
    ] = ActivePower(0.0, "MW")

    generation_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Capacity Coefficient",
            description="Coefficient of total generation capacity",
        ),
    ] = ActivePower(0.0, "MW")

    generation_capacity_retired_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Capacity Retired Coefficient",
            description="Coefficient of generation capacity retired",
        ),
    ] = ActivePower(0.0, "MW")

    generation_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Coefficient",
            description="Coefficient of zone generation",
        ),
    ] = ActivePower(0.0, "MW")

    generation_curtailed_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Curtailed Coefficient",
            description="Coefficient of generation curtailed",
        ),
    ] = ActivePower(0.0, "MW")

    generator_build_cost_coefficient: Annotated[
        float,
        Field(
            alias="Generator Build Cost Coefficient",
            description="Coefficient of total cost of generator builds",
        ),
    ] = 0.0

    generators_built_coefficient: Annotated[
        float,
        Field(
            alias="Generators Built Coefficient",
            description="Coefficient on binary variable indicating if any generation capacity was built",
        ),
    ] = 0.0

    generators_built_in_year_coefficient: Annotated[
        float,
        Field(
            alias="Generators Built in Year Coefficient",
            description="Coefficient on binary variable indicating if any generation capacity is built in the year",
        ),
    ] = 0.0

    import_capacity_built_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Import Capacity Built Coefficient",
            description="Coefficient of import capacity built",
        ),
    ] = ActivePower(0.0, "MW")

    import_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Import Capacity Coefficient",
            description="Coefficient of import capacity",
        ),
    ] = ActivePower(0.0, "MW")

    imports_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Imports Coefficient",
            description="Coefficient of zone imports",
        ),
    ] = ActivePower(0.0, "MW")

    load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Load Coefficient",
            description="Coefficient of zone load",
        ),
    ] = [ActivePower(0.0, "MW")]

    load_squared_coefficient: Annotated[
        float,
        Field(
            alias="Load Squared Coefficient",
            description="Coefficient of the square of zone load",
        ),
    ] = 0.0

    net_load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Net Load Coefficient",
            description="Coefficient of load net of unserved and dump energy",
        ),
    ] = ActivePower(0.0, "MW")

    peak_load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Peak Load Coefficient",
            description="Coefficient of annual peak load",
        ),
    ] = ActivePower(0.0, "MW")

    unserved_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Unserved Energy Coefficient",
            description="Coefficient of unserved energy",
        ),
    ] = ActivePower(0.0, "MW")

    # Zone Objectives Input Properties
    capacity_reserves_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Capacity Reserves Coefficient",
            description="Coefficient of total capacity reserves",
        ),
    ] = ActivePower(0.0, "MW")
    
    committed_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Committed Capacity Coefficient",
            description="Coefficient of generation capacity committed in the zone",
        ),
    ] = ActivePower(0.0, "MW")
    
    dump_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Dump Energy Coefficient",
            description="Coefficient of dump energy (over generation)",
        ),
    ] = ActivePower(0.0, "MW")
    
    export_capacity_built_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Export Capacity Built Coefficient",
            description="Coefficient of export capacity built",
        ),
    ] = ActivePower(0.0, "MW")
    
    export_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Export Capacity Coefficient",
            description="Coefficient of export capacity",
        ),
    ] = ActivePower(0.0, "MW")
    
    exports_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Exports Coefficient",
            description="Coefficient of zone exports",
        ),
    ] = ActivePower(0.0, "MW")
    
    firm_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Firm Capacity Coefficient",
            description="Coefficient of total generator [Firm Capacity]",
        ),
    ] = ActivePower(0.0, "MW")
    
    generation_capacity_built_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Capacity Built Coefficient",
            description="Coefficient of generation capacity built",
        ),
    ] = ActivePower(0.0, "MW")
    
    generation_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Capacity Coefficient",
            description="Coefficient of total generation capacity",
        ),
    ] = ActivePower(0.0, "MW")
    
    generation_capacity_retired_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Capacity Retired Coefficient",
            description="Coefficient of generation capacity retired",
        ),
    ] = ActivePower(0.0, "MW")
    
    generation_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Coefficient",
            description="Coefficient of zone generation",
        ),
    ] = ActivePower(0.0, "MW")
    
    generation_curtailed_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Curtailed Coefficient",
            description="Coefficient of generation curtailed",
        ),
    ] = ActivePower(0.0, "MW")
    
    generator_build_cost_coefficient: Annotated[
        float,
        Field(
            alias="Generator Build Cost Coefficient",
            description="Coefficient of total cost of generator builds",
        ),
    ] = 0.0
    
    generators_built_coefficient: Annotated[
        float,
        Field(
            alias="Generators Built Coefficient",
            description="Coefficient on binary variable indicating if any generation capacity is built to date",
        ),
    ] = 0.0
    
    generators_built_in_year_coefficient: Annotated[
        float,
        Field(
            alias="Generators Built in Year Coefficient",
            description="Coefficient on binary variable indicating if any generation capacity is built in the year",
        ),
    ] = 0.0
    
    import_capacity_built_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Import Capacity Built Coefficient",
            description="Coefficient of import capacity built",
        ),
    ] = ActivePower(0.0, "MW")
    
    import_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Import Capacity Coefficient",
            description="Coefficient of import capacity",
        ),
    ] = ActivePower(0.0, "MW")
    
    imports_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Imports Coefficient",
            description="Coefficient of zone imports",
        ),
    ] = ActivePower(0.0, "MW")
    
    load_squared_coefficient: Annotated[
        List[float],
        Field(
            alias="Load Squared Coefficient",
            description="Coefficient of the square of zone load",
        ),
    ] = [0.0]
    
    net_load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Net Load Coefficient",
            description="Coefficient of load net of unserved and dump energy",
        ),
    ] = ActivePower(0.0, "MW")
    
    peak_load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Peak Load Coefficient",
            description="Coefficient of annual peak load",
        ),
    ] = ActivePower(0.0, "MW")
    
    unserved_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Unserved Energy Coefficient",
            description="Coefficient of unserved energy",
        ),
    ] = ActivePower(0.0, "MW")

    # Zone Conditions Input Properties
    capacity_reserves_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Capacity Reserves Coefficient",
            description="Coefficient of zone capacity reserves in condition",
        ),
    ] = ActivePower(0.0, "MW")


    unserved_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Unserved Energy Coefficient",
            description="Coefficient of unserved energy in condition",
        ),
    ] = ActivePower(0.0, "MW")