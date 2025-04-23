# plexos.py
"""
The following file contains Pydantic models for a PLEXOS model
"""
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

class PlexosGenerator(Device):
    """PLEXOS Generator Class"""

    # We will add the generator properties here. Costing should probably be its
    # own model

    # TODO: Check if this needs to be renamed to bus to be consistent with R2X
    # PLEXOS uses the term node to refer to a bus
    node: Union[Annotated[Bus, Field(description="Bus where the generator is connected.")], None] = None
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
            Percentage,
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
            ge=-1,
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
    vom_price: Annotated[
        VOMPrice, 
        Field(alias="VO&M Price", description="Variable operational price $/MWh.")
    ] | None = None
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

class PlexosNode(Bus):
    """PLEXOS Node Class for a transmission Node/Bus"""

    # name: Annotated[str, Field(description="Name of the node.")] = None
    # Node attributes
    latitude: Annotated[float, Field(description="Latitude of the node.")] = 0.
    longitude: Annotated[float, Field(description="Longitude of the node.")] = 0.

    # Node input properties
    ac_reactive_power : Annotated[
        ApparentPower,
        Field(
            alias="AC Reactive Power",
            description="Reactive power in/out of the bus.",
        ),
    ] = ApparentPower(0.0, "MVAr")
    ac_voltage_magnitude: Annotated[
        NonNegativeFloat,
        Field(
            alias="AC Voltage Magnitude",
            description="per-unit voltage magnitude",
        ),
    ] = 1.0
    allow_dump_energy: Annotated[
        NonPositiveInt,
        Field(
            alias="Allow Dump Energy",
            description="Model Node [Dump Energy] in the mathematical program.",
            ge=-1,
        ),
    ] = 0
    allow_unserved_energy: Annotated[
        NonPositiveInt,
        Field(
            alias="Allow Unserved Energy",
            description="Model Node [Unserved Energy] in the mathematical program.",
            ge=-1,
        ),
    ] = False
    always_calculate_ptdf: Annotated[
        NonPositiveInt,
        Field(
            alias="Always Calculate PTDF",
            description="Flag if the PTDFs associated with the node and transmission constraints will be calculated",
            ge=-1,
        ),
    ] = False
    dsp_bid_price: Annotated[
        DSPBidPrice,
        Field(
            alias="DSP Bid Price",
            description="Demand-side participation bid price $/MWh",
        ),
    ] = DSPBidPrice(0.0, "USD/MWh")
    dsp_bid_quantity: Annotated[
        ActivePower,
        Field(
            alias="DSP Bid Quantity",
            description="Demand-side participation bid quantity MW",
        ),
    ] = ActivePower(0.0, "MW")
    dsp_bid_ratio: Annotated[
        Percentage,
        Field(
            alias="DSP Bid Ratio",
            description="Demand-side participation quantity as a percentage of nodal load",
        ),
    ] = Percentage(0.0, "%")
    enable_atc_calculation: Annotated[
        NonNegativeInt,
        Field(
            alias="Enable ATC Calculation",
            description="Flag if the ATC associated with the node and transmission constraints will be calculated",
            ge=0, 
            le=3
        ),
    ] = 0
    fixed_generation: Annotated[
        ActivePower,
        Field(
            alias="Fixed Generation",
            description="Fixed (or embedded) generation at the node in MW",
        ),
    ] = ActivePower(0.0, "MW")
    fixed_load: Annotated[
        ActivePower,
        Field(
            alias="Fixed Load",
            description="Fixed (or embedded) load at the node in MW",
        ),
    ] = ActivePower(0.0, "MW")
    formulate_load: Annotated[
        NonPositiveInt,
        Field(
            alias="Formulate Load",
            description="Flag if the load at the node will be formulated in the mathematical program as a decision variable",
            ge=-1,
        ),
    ] = False
    is_slack_bus: Annotated[
        NonPositiveInt,
        Field(
            alias="Is Slack Bus",
            description="Flag if the node is a slack bus",
            ge=-1,
        ),
    ] = False
    is_unmapped_resource_bus: Annotated[
        NonPositiveInt,
        Field(
            alias="Is Unmapped Resource Bus",
            description="Flag if the node is an unmapped resource bus",
            ge=-1,
        ),
    ] = False
    load: Annotated[
        ActivePower,
        Field(
            alias="Load",
            description="Load at the node in MW",
        ),
    ] = ActivePower(0.0, "MW")
    load_participation_factor: Annotated[
        float,
        Field(
            alias="Load Participation Factor",
            description="Proportion of region load that occurs at the node",
            le=1.0,
            ge=-1.0),
    ] = 1.0
    maintenance_factor: Annotated[
        NonNegativeFloat,
        Field(
            alias="Maintenance Factor",
            description="Maintenance biasing factor",
        ),
    ] = 1.0
    max_maintenance: Annotated[
        ActivePower,
        Field(
            alias="Max Maintenance",
            description="Maximum generation capacity allowed to be scheduled on maintenance",
        ),
    ] = ActivePower(1.e30, "MW")
    max_net_injection: Annotated[
        ActivePower,
        Field(
            alias="Max Net Injection",
            description="Maximum net injection at the node in MW",
        ),
    ] = ActivePower(1.e30, "MW")
    nax_net_offtake: Annotated[
        ActivePower,
        Field(
            alias="Max Net Offtake",
            description="Maximum net offtake at the node in MW",
        ),
    ] = ActivePower(1.e30, "MW")
    max_unserved_energy: Annotated[
        ActivePower,
        Field(
            alias="Max Unserved Energy",
            description="Maximum unserved energy at the node in MW",
        ),
    ] = ActivePower(0.0, "MW")
    min_capacity_reserve_margin: Annotated[
        Percentage,
        Field(
            alias="Min Capacity Reserve Margin",
            description="Minimum capacity reserve margin at the node in percent",
        ),
    ] = Percentage(0.0, "%")
    min_capacity_reserves: Annotated[
        ActivePower,
        Field(
            alias="Min Capacity Reserves",
            description="Minimum capacity reserves at the node in MW",
        ),
    ] = ActivePower(-1.e30, "MW")
    must_report: Annotated[
        NonPositiveInt,
        Field(
            alias="Must Report",
            description="Flag if the node must report its results",
            ge=-1,
        ),
    ] = 0
    price: Annotated[
        NonNegativeFloat,
        Field(
            alias="Price",
            description="Locational marginal price at the node in $/MWh",
        ),
    ] = 0.0
    rating: Annotated[
        ApparentPower,
        Field(
            alias="Rating",
            description="Rating of the node in MW",
        ),
    ] = ApparentPower(1.e30, "MW")
    reference_generation: Annotated[
        ActivePower,
        Field(
            alias="Reference Generation",
            description="Reference generation at the node in MW",
        ),
    ] = ActivePower(1.0, "MW")
    reference_load: Annotated[
        ActivePower,
        Field(
            alias="Reference Load",
            description="Reference load at the node in MW",
        ),
    ] = ActivePower(1.0, "MW")
    units: Annotated[
        NonNegativeInt,
        Field(
            alias="Units",
            description="Flag if bus is in service",
            le=1,
        ),
    ] = 1
    voltage: Annotated[
        NonNegativeFloat,
        Field(
            alias="Voltage",
            description="Voltage at the node in kV",
        ),
    ] = 0.0
    x: Annotated[
        float,
        Field(
            alias="x",
            description="Value to pass-through to solution",
        ),
    ] = 0.0
    y: Annotated[
        float,
        Field(
            alias="y",
            description="Value to pass-through to solution",
        ),
    ] = 0.0
    z: Annotated[
        float,
        Field(
            alias="z",
            description="Value to pass-through to solution",
        ),
    ] = 0.0

    # Node virtual emissions input properties
    emission_charge: Annotated[
        float,
        Field(
            alias="Emission Charge",
            description="Emission charge for emissions consumed at the node in a virtual emission network in $/kg or $/lb",
        ),
    ] = 0.0
    max_emissions: Annotated[
        float,
        Field(
            alias="Max Emissions",
            description="Maximum amount of emissions consumed at the node in a virtual emission network",
        ),
    ] = 1.e30

    # Node hubs input properties
    pricing_weight: Annotated[
        float,
        Field(
            alias="Pricing Weight",
            description="Wheeling charge for exports to the zone",
        ),
    ] = 1.0

    # Node companies input properties
    load_share: Annotated[
        Percentage,
        Field(
            alias="Load Share",
            description="Percentage share of load ownership",
            ge=0.0,
            le=100.0
        ),
    ] = Percentage(100.0, "%")

    # Node facilities input properties
    consumption_coefficient: Annotated[
        float,
        Field(
            alias="Consumption Coefficient",
            description="Electric Load for each unit of consumption",
        ),
    ] = 0.0
    facility_node_type: Annotated[
        NonNegativeInt,
        Field(
            alias="Facility Node Type",
            description="Specifies whether Node is an input or an output for the Facility",
            ge=0,
            le=2
        ),
    ] = 0
    production_coefficient: Annotated[
        float,
        Field(
            alias="Production Coefficient",
            description="Electric Generation for each unit of production",
        ),
    ] = 0.0
    units_coefficient: Annotated[
        float,
        Field(
            alias="Units Coefficient",
            description="Electric Load for each installed unit",
        ),
    ] = 0.0
    units_operating_coefficient: Annotated[
        float,
        Field(
            alias="Units Operating Coefficient",
            description="Electric Load for each operating unit",
        ),
    ] = 0.0

    # Node constraints input properties
    dump_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Dump Energy Coefficient",
            description="Coefficient of dump energy (over generation)",
        ),
    ] = ActivePower(0.0, "MW")
    
    generation_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Generation Coefficient",
            description="Coefficient of node generation",
        ),
    ] = ActivePower(0.0, "MW")
    
    load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Load Coefficient",
            description="Coefficient of node load",
        ),
    ] = ActivePower(0.0, "MW")
    
    mlf_coefficient: Annotated[
        float,
        Field(
            alias="MLF Coefficient",
            description="Coefficient of marginal loss factor",
        ),
    ] = 0.0
    
    net_injection_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Net Injection Coefficient",
            description="Coefficient of node net injection",
        ),
    ] = ActivePower(0.0, "MW")
    
    net_load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Net Load Coefficient",
            description="Coefficient of load net of unserved and dump energy",
        ),
    ] = ActivePower(0.0, "MW")
    
    phase_angle_coefficient: Annotated[
        float,
        Field(
            alias="Phase Angle Coefficient",
            description="Coefficient of node phase angle in degrees",
        ),
    ] = 0.0
    
    unserved_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Unserved Energy Coefficient",
            description="Coefficient of unserved energy",
        ),
    ] = ActivePower(0.0, "MW")

    # Node decision variables input properties
    net_injection_definition_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Net Injection Definition Coefficient",
            description="Coefficient of Decision Variable in Node net injection definition equation",
        ),
    ] = ActivePower(0.0, "MW")

    # Node conditions input properties
    condition_load_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Load Coefficient",
            description="Coefficient of node demand in condition",
        ),
    ] = ActivePower(0.0, "MW")
    
    condition_unserved_energy_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Unserved Energy Coefficient",
            description="Coefficient of unserved energy in condition",
        ),
    ] = ActivePower(0.0, "MW")

    # Node output properties
    ac_mismatch: Annotated[
        ApparentPower,
        Field(
            alias="AC Mismatch - MVA",
            description="The magnitude of the complex power mismatch between the left- and right-hand sides of the AC power balance equation",
        ),
    ] = ApparentPower(0.0, "MVA")
    
    battery_generation: Annotated[
        ActivePower,
        Field(
            alias="Battery Generation - MW",
            description="Generation from batteries",
        ),
    ] = ActivePower(0.0, "MW")
    
    battery_load: Annotated[
        ActivePower,
        Field(
            alias="Battery Load - MW",
            description="Charging load from batteries",
        ),
    ] = ActivePower(0.0, "MW")
    
    capacity_reserves: Annotated[
        ActivePower,
        Field(
            alias="Capacity Reserves - MW",
            description="Capacity reserves (net of Peak Load)",
        ),
    ] = ActivePower(0.0, "MW")
    
    charging_station_deferred_load: Annotated[
        ActivePower,
        Field(
            alias="Charging Station Deferred Load - MW",
            description="Load from Charging Stations deferred",
        ),
    ] = ActivePower(0.0, "MW")
    
    charging_station_generation: Annotated[
        ActivePower,
        Field(
            alias="Charging Station Generation - MW",
            description="Generation from Charging Stations",
        ),
    ] = ActivePower(0.0, "MW")
    
    charging_station_hours_deferred: Annotated[
        Time,
        Field(
            alias="Charging Station Hours Deferred - h",
            description="Average hours Charging Station load is deferred in the period",
        ),
    ] = Time(0.0, "h")
    
    charging_station_load: Annotated[
        ActivePower,
        Field(
            alias="Charging Station Load - MW",
            description="Load from Charging Stations",
        ),
    ] = ActivePower(0.0, "MW")
    
    cleared_dsp_bid_cost: Annotated[
        float,
        Field(
            alias="Cleared DSP Bid Cost - $",
            description="Value of cleared demand-side participation bids",
        ),
    ] = 0.0
    
    cleared_dsp_bid_price: Annotated[
        DSPBidPrice,
        Field(
            alias="Cleared DSP Bid Price - $/MWh",
            description="Price of marginal demand-side participation bid band",
        ),
    ] = DSPBidPrice(0.0, "USD/MWh")
    
    congestion_charge: Annotated[
        float,
        Field(
            alias="Congestion Charge - $/MWh",
            description="Congestion component of locational marginal price",
        ),
    ] = 0.0
    
    contract_generation_capacity: Annotated[
        ActivePower,
        Field(
            alias="Contract Generation Capacity - MW",
            description="Physical contract generation capacity",
        ),
    ] = ActivePower(0.0, "MW")
    
    contract_load_obligation: Annotated[
        ActivePower,
        Field(
            alias="Contract Load Obligation - MW",
            description="Physical contract load obligation",
        ),
    ] = ActivePower(0.0, "MW")
    
    curtailable_load: Annotated[
        ActivePower,
        Field(
            alias="Curtailable Load - MW",
            description="Curtailable (dispatchable) load",
        ),
    ] = ActivePower(0.0, "MW")
    
    customer_load: Annotated[
        ActivePower,
        Field(
            alias="Customer Load - MW",
            description="Load served to customers at the node",
        ),
    ] = ActivePower(0.0, "MW")
    
    demand_curtailed: Annotated[
        ActivePower,
        Field(
            alias="Demand Curtailed - MW",
            description="Demand-side participation bids cleared",
        ),
    ] = ActivePower(0.0, "MW")
    
    discrete_maintenance: Annotated[
        ActivePower,
        Field(
            alias="Discrete Maintenance - MW",
            description="Discrete maintenance (defined by Units Out)",
        ),
    ] = ActivePower(0.0, "MW")
    
    distributed_maintenance: Annotated[
        ActivePower,
        Field(
            alias="Distributed Maintenance - MW",
            description="Maintenance notionally allocated to period",
        ),
    ] = ActivePower(0.0, "MW")
    
    dump_energy: Annotated[
        ActivePower,
        Field(
            alias="Dump Energy - MW",
            description="Dump energy (over generation)",
        ),
    ] = ActivePower(0.0, "MW")
    
    edns: Annotated[
        ActivePower,
        Field(
            alias="EDNS - MW",
            description="Expected Demand Not Served",
        ),
    ] = ActivePower(0.0, "MW")
    
    eens: Annotated[
        Energy,
        Field(
            alias="EENS - MWh",
            description="Expected Energy Not Served",
        ),
    ] = Energy(0.0, "MWh")
    
    energy_charge: Annotated[
        float,
        Field(
            alias="Energy Charge - $/MWh",
            description="Energy component of locational marginal price",
        ),
    ] = 0.0
    
    export_capacity: Annotated[
        ActivePower,
        Field(
            alias="Export Capacity - MW",
            description="Total export capacity from the Node",
        ),
    ] = ActivePower(0.0, "MW")
    
    exports: Annotated[
        ActivePower,
        Field(
            alias="Exports - MW",
            description="Exports from the node",
        ),
    ] = ActivePower(0.0, "MW")
    
    facility_generation: Annotated[
        ActivePower,
        Field(
            alias="Facility Generation - MW",
            description="Generation from connected Facilities",
        ),
    ] = ActivePower(0.0, "MW")
    
    facility_load: Annotated[
        ActivePower,
        Field(
            alias="Facility Load - MW",
            description="Load from connected Facilities",
        ),
    ] = ActivePower(0.0, "MW")
    
    flow: Annotated[
        ActivePower,
        Field(
            alias="Flow - MW",
            description="Flow through the node",
        ),
    ] = ActivePower(0.0, "MW")
    
    import_capacity: Annotated[
        ActivePower,
        Field(
            alias="Import Capacity - MW",
            description="Total import capacity to the Node",
        ),
    ] = ActivePower(0.0, "MW")
    
    imports: Annotated[
        ActivePower,
        Field(
            alias="Imports - MW",
            description="Imports to the node",
        ),
    ] = ActivePower(0.0, "MW")
    
    injection_mismatch: Annotated[
        ActivePower,
        Field(
            alias="Injection Mismatch - MW",
            description="Absolute value of mismatch of injection due to PTDF threshold",
        ),
    ] = ActivePower(0.0, "MW")
    
    losses: Annotated[
        ActivePower,
        Field(
            alias="Losses - MW",
            description="Losses allocated to the node",
        ),
    ] = ActivePower(0.0, "MW")
    
    marginal_loss_charge: Annotated[
        float,
        Field(
            alias="Marginal Loss Charge - $/MWh",
            description="Marginal loss component of locational marginal price",
        ),
    ] = 0.0
    
    marginal_loss_factor: Annotated[
        float,
        Field(
            alias="Marginal Loss Factor",
            description="Marginal loss factor to slack bus(es)",
        ),
    ] = 0.0
    
    min_load: Annotated[
        ActivePower,
        Field(
            alias="Min Load - MW",
            description="Minimum load across the current period",
        ),
    ] = ActivePower(0.0, "MW")
    
    native_load: Annotated[
        ActivePower,
        Field(
            alias="Native Load - MW",
            description="Native load",
        ),
    ] = ActivePower(0.0, "MW")
    
    net_capacity_interchange: Annotated[
        ActivePower,
        Field(
            alias="Net Capacity Interchange - MW",
            description="Export Capability - Import Capability",
        ),
    ] = ActivePower(0.0, "MW")
    
    net_contract_load: Annotated[
        ActivePower,
        Field(
            alias="Net Contract Load - MW",
            description="Net of contract sales and generation",
        ),
    ] = ActivePower(0.0, "MW")
    
    net_dc_export: Annotated[
        ActivePower,
        Field(
            alias="Net DC Export - MW",
            description="Export from the node on DC lines net of losses",
        ),
    ] = ActivePower(0.0, "MW")
    
    net_injection: Annotated[
        ActivePower,
        Field(
            alias="Net Injection - MW",
            description="Net injection (exports - imports)",
        ),
    ] = ActivePower(0.0, "MW")
    
    net_market_sales: Annotated[
        ActivePower,
        Field(
            alias="Net Market Sales - MW",
            description="Net sales to external energy markets",
        ),
    ] = ActivePower(0.0, "MW")
    
    peak_load: Annotated[
        ActivePower,
        Field(
            alias="Peak Load - MW",
            description="Peak load across the current period",
        ),
    ] = ActivePower(0.0, "MW")
    
    phase_angle: Annotated[
        float,
        Field(
            alias="Phase Angle - °",
            description="Node phase angle",
        ),
    ] = 0.0
    
    pump_generation: Annotated[
        ActivePower,
        Field(
            alias="Pump Generation - MW",
            description="Generation from pumped storage",
        ),
    ] = ActivePower(0.0, "MW")
    
    pump_load: Annotated[
        ActivePower,
        Field(
            alias="Pump Load - MW",
            description="Pump load",
        ),
    ] = ActivePower(0.0, "MW")
    
    purchaser_load: Annotated[
        ActivePower,
        Field(
            alias="Purchaser Load - MW",
            description="Load from cleared purchaser bids",
        ),
    ] = ActivePower(0.0, "MW")
    
    unserved_energy: Annotated[
        ActivePower,
        Field(
            alias="Unserved Energy - MW",
            description="Unserved energy (USE)",
        ),
    ] = ActivePower(0.0, "MW")

    water_plant_load: Annotated[
        ActivePower,
        Field(
            alias="Water Plant Load - MW",
            description="Load from water plants",
        ),
    ] = ActivePower(0.0, "MW")

    # TODO: Node Virtual Emissions output properties
    # TODO: Node Market output properties