# line.py

"""
The following file contains Pydantic models for a Plexos zone
"""
from typing import Annotated, Union, Any, List
from pydantic import Field, NonNegativeFloat, NonNegativeInt, NonPositiveInt

from r2x.enums import PrimeMoversType, StorageTechs, ThermalFuels
from r2x.models.core import BaseComponent, Device, StaticInjection
from r2x.models.core import Device, InputOutput, MinMax, UpDown
from r2x.models.branch import Line
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
    Currency,
)

class PlexosLine(Line):
    """
    Class that holds all attributes of a PLEXOS Line Class
    """
    
    # Line properties
    ac_line_charging_susceptance: Annotated[
        float,
        Field(
            alias="AC Line Charging Susceptance",
            description="The line-charging susceptance of a transmission line",
        ),
    ] = 0.0
    
    build_cost: Annotated[
        float,
        Field(
            alias="Build Cost",
            description="Cost of building the line",
        ),
    ] = 0.0
    
    build_non_anticipativity: Annotated[
        float,
        Field(
            alias="Build Non-anticipativity",
            description="Price for violating non-anticipativity constraints in scenario-wise decomposition mode",
        ),
    ] = -1.0
    
    circuits: Annotated[
        NonNegativeInt,
        Field(
            alias="Circuits",
            description="Number of circuits in the notional interconnector for the purposes of outage modelling",
            ge=1,
        ),
    ] = 1
    
    commission_date: Annotated[
        NonNegativeInt,
        Field(
            alias="Commission Date",
            description="Date the line was commissioned for use with [Technical Life]",
        ),
    ] = 1
    
    contingency_limit_penalty: Annotated[
        float,
        Field(
            alias="Contingency Limit Penalty",
            description="Penalty for exceeding contingency flow limits",
        ),
    ] = -1.0
    
    debt_charge: Annotated[
        float,
        Field(
            alias="Debt Charge",
            description="Annual debt charge",
        ),
    ] = 0.0
    
    economic_life: Annotated[
        NonNegativeFloat,
        Field(
            alias="Economic Life",
            description="Economic life of the line (period over which fixed costs are recovered).",
        ),
    ] = 30.0
    
    enforce_limits: Annotated[
        NonNegativeInt,
        Field(
            alias="Enforce Limits",
            description="Controls when flow limits are enforced with regard to Transmission [Constraint Voltage Threshold].",
            le=3,
        ),
    ] = 1
    
    equity_charge: Annotated[
        float,
        Field(
            alias="Equity Charge",
            description="Annual required return on equity",
        ),
    ] = 0.0
    
    expansion_optimality: Annotated[
        NonNegativeInt,
        Field(
            alias="Expansion Optimality",
            description="Expansion planning integerization scheme.",
            le=2,
        ),
    ] = 2
    
    firm_capacity: Annotated[
        ActivePower,
        Field(
            alias="Firm Capacity",
            description="Net capacity reserves exported",
        ),
    ] = ActivePower(0.0, "MW")
    
    fixed_charge: Annotated[
        float,
        Field(
            alias="Fixed Charge",
            description="Generic annual fixed charge in $/kW/yr",
        ),
    ] = 0.0
    
    fixed_flow: Annotated[
        ActivePower,
        Field(
            alias="Fixed Flow",
            description="Fixed flow on line",
        ),
    ] = ActivePower(0.0, "MW")
    
    fixed_flow_method: Annotated[
        NonNegativeInt,
        Field(
            alias="Fixed Flow Method",
            description="Method of interpreting zero values of the [Fixed Flow] property.",
            le=1,
        ),
    ] = 1
    
    fixed_flow_penalty: Annotated[
        float,
        Field(
            alias="Fixed Flow Penalty",
            description="Penalty for violation of [Fixed Flow].",
        ),
    ] = -1.0
    
    fixed_loss: Annotated[
        ActivePower,
        Field(
            alias="Fixed Loss",
            description="Fixed loss on line",
        ),
    ] = ActivePower(0.0, "MW")
    
    flow_non_anticipativity: Annotated[
        float,
        Field(
            alias="Flow Non-anticipativity",
            description="Price for violating non-anticipativity constraints in scenario-wise decomposition mode",
        ),
    ] = Currency(0.0, "usd")
    
    flow_non_anticipativity_time: Annotated[
        NonNegativeFloat,
        Field(
            alias="Flow Non-anticipativity Time",
            description="Window of time over which to enforce non-anticipativity constraints in scenario-wise decomposition",
            ge=0,
        ),
    ] = 0.0
    
    fom_charge: Annotated[
        float,
        Field(
            alias="FO&M Charge",
            description="Annual fixed operation and maintenance charge",
        ),
    ] = 0.0
    
    forced_outage_rate: Annotated[
        Percentage,
        Field(
            alias="Forced Outage Rate",
            description="Expected proportion of time the facility is unavailable due to forced outage",
            ge=0,
            le=100,
        ),
    ] = Percentage(0.0, "%")
    
    formulate_npl_upfront: Annotated[
        NonPositiveInt,
        Field(
            alias="Formulate NPL Upfront",
            description="If integer conditions that control non-physical losses should be formulated upfront rather than checked iteratively",
            ge=-1,
            le=0,
        ),
    ] = 0
    
    formulate_upfront: Annotated[
        NonPositiveInt,
        Field(
            alias="Formulate Upfront",
            description="If constraints should all be formulated upfront rather than checked iteratively.",
            ge=-1,
            le=0,
        ),
    ] = 0
    
    hint_units_built: Annotated[
        NonNegativeInt,
        Field(
            alias="Hint Units Built",
            description="Capacity expansion solution to be passed to the optimizer as a hint or initial solution",
        ),
    ] = 0
    
    hint_units_retired: Annotated[
        NonNegativeInt,
        Field(
            alias="Hint Units Retired",
            description="Capacity expansion solution to be passed to the optimizer as a hint or initial solution",
        ),
    ] = 0
    
    integerization_horizon: Annotated[
        int,
        Field(
            alias="Integerization Horizon",
            description="Number of years over which the expansion decisions are integerized",
            ge=-1,
        ),
    ] = -1
    
    lead_time: Annotated[
        Time,
        Field(
            alias="Lead Time",
            description="Number of years after which the expansion project can begin (yr)",
            ge=0,
        ),
    ] = Time(0.0, "year")
    
    limit_penalty: Annotated[
        float,
        Field(
            alias="Limit Penalty",
            description="Penalty for exceeding the flow limits on the line ($/MWh).",
        ),
    ] = -1.0
    
    loss_allocation: Annotated[
        float,
        Field(
            alias="Loss Allocation",
            description="Proportion of line losses allocated to the receiving node",
            ge=0,
            le=1,
        ),
    ] = 0.5
    
    loss_base: Annotated[
        float,
        Field(
            alias="Loss Base",
            description="Interconnector loss function constant parameter for reference direction flows",
        ),
    ] = 0.0
    
    loss_base_back: Annotated[
        float,
        Field(
            alias="Loss Base Back",
            description="Interconnector loss function constant parameter for counter-reference direction flows",
        ),
    ] = 0.0
    
    loss_incr: Annotated[
        float,
        Field(
            alias="Loss Incr",
            description="Interconnector loss function linear parameter for reference direction flows",
        ),
    ] = [0.0]
    
    loss_incr_back: Annotated[
        float,
        Field(
            alias="Loss Incr Back",
            description="Interconnector loss function linear parameter for counter-reference direction flows",
        ),
    ] = 0.0
    
    loss_incr2: Annotated[
        float,
        Field(
            alias="Loss Incr2",
            description="Interconnector loss function quadratic parameter for reference direction flows",
        ),
    ] = 0.0
    
    loss_incr2_back: Annotated[
        float,
        Field(
            alias="Loss Incr2 Back",
            description="Interconnector loss function quadratic parameter for counter-reference direction flows",
        ),
    ] = 0.0
    
    maintenance_frequency: Annotated[
        List[NonNegativeInt],
        Field(
            alias="Maintenance Frequency",
            description="Frequency of maintenance outages in an annual timeframe",
            ge=0,
        ),
    ] = [0]
    
    maintenance_rate: Annotated[
        Percentage,
        Field(
            alias="Maintenance Rate",
            description="Expected proportion of time the facility is unavailable due to maintenance",
            ge=0,
            le=100,
        ),
    ] = Percentage(0.0, "%")
    
    marginal_loss_factor: Annotated[
        float,
        Field(
            alias="Marginal Loss Factor",
            description="Transmission marginal loss factor (MLF or TLF) for exports",
        ),
    ] = 1.0
    
    marginal_loss_factor_back: Annotated[
        float,
        Field(
            alias="Marginal Loss Factor Back",
            description="Transmission marginal loss factor (MLF or TLF) for imports",
        ),
    ] = 1.0
    
    max_capacity_reserves: Annotated[
        ActivePower,
        Field(
            alias="Max Capacity Reserves",
            description="Maximum amount of capacity reserves supplied to the receiving Region/Zone.",
        ),
    ] = ActivePower(1e30, "MW")
    
    max_flow: Annotated[
        List[ActivePower],
        Field(
            alias="Max Flow",
            description="Maximum flow",
        ),
    ] = [ActivePower(1e30, "MW")]
    
    max_loss_tranches: Annotated[
        NonNegativeInt,
        Field(
            alias="Max Loss Tranches",
            description="Maximum number of tranches in piecewise linear loss function.",
            ge=2,
        ),
    ] = 2
    
    max_ramp_down: Annotated[
        PowerRate,
        Field(
            alias="Max Ramp Down",
            description="Maximum ramp down rate",
            ge=0,
        ),
    ] = PowerRate(1e30, "MW/min")
    
    max_ramp_up: Annotated[
        PowerRate,
        Field(
            alias="Max Ramp Up",
            description="Maximum ramp up rate",
            ge=0,
        ),
    ] = PowerRate(1e30, "MW/min")
    
    max_rating: Annotated[
        ActivePower,
        Field(
            alias="Max Rating",
            description="Rated maximum (overrides Max Flow)",
        ),
    ] = ActivePower(1e30, "MW")
    
    max_time_to_repair: Annotated[
        Time,
        Field(
            alias="Max Time To Repair",
            description="Maximum time to repair (hr)",
            ge=0,
        ),
    ] = Time(0.0, "hour")
    
    max_units_built: Annotated[
        int,
        Field(
            alias="Max Units Built",
            description="Maximum number of units automatically constructed in aggregate over the planning horizon",
            ge=0,
            le=1,
        ),
    ] = 0
    
    max_units_built_in_year: Annotated[
        int,
        Field(
            alias="Max Units Built in Year",
            description="Maximum number of units automatically constructed in any single year of the planning horizon",
            ge=0,
            le=1,
        ),
    ] = 1
    
    max_units_retired: Annotated[
        int,
        Field(
            alias="Max Units Retired",
            description="Maximum number of units automatically retired in aggregate over the planning horizon",
            ge=0,
            le=1,
        ),
    ] = 0
    
    max_units_retired_in_year: Annotated[
        int,
        Field(
            alias="Max Units Retired in Year",
            description="Maximum number of units automatically retired in any single year of the planning horizon",
            ge=0,
            le=1,
        ),
    ] = 1
    
    mean_time_to_repair: Annotated[
        Time,
        Field(
            alias="Mean Time to Repair",
            description="Mean time to repair",
            ge=0,
        ),
    ] = Time(24.0, "hour")
    
    min_capacity_reserves: Annotated[
        ActivePower,
        Field(
            alias="Min Capacity Reserves",
            description="Minimum amount of capacity reserves supplied to the receiving Region/Zone.",
        ),
    ] = ActivePower(-1e30, "MW")
    
    min_flow: Annotated[
        ActivePower,
        Field(
            alias="Min Flow",
            description="Minimum flow",
        ),
    ] = ActivePower(-1e30, "MW")
    
    min_rating: Annotated[
        ActivePower,
        Field(
            alias="Min Rating",
            description="Rated minimum (overrides Min Flow)",
        ),
    ] = ActivePower(-1e30, "MW")
    
    min_time_to_repair: Annotated[
        Time,
        Field(
            alias="Min Time To Repair",
            description="Minimum time to repair (hr)",
            ge=0,
        ),
    ] = Time(0.0, "hour")
    
    min_units_built: Annotated[
        int,
        Field(
            alias="Min Units Built",
            description="Minimum number of lines automatically constructed",
            ge=0,
            le=1,
        ),
    ] = 0
    
    min_units_built_in_year: Annotated[
        int,
        Field(
            alias="Min Units Built in Year",
            description="Minimum number of units automatically constructed in any single year of the planning horizon",
            ge=0,
            le=1,
        ),
    ] = 0
    
    min_units_retired: Annotated[
        int,
        Field(
            alias="Min Units Retired",
            description="Minimum number of lines automatically retired",
            ge=0,
            le=1,
        ),
    ] = 0
    
    min_units_retired_in_year: Annotated[
        int,
        Field(
            alias="Min Units Retired in Year",
            description="Minimum number of units automatically retired in any single year of the planning horizon",
            ge=0,
            le=1,
        ),
    ] = 0
    
    must_report: Annotated[
        NonPositiveInt,
        Field(
            alias="Must Report",
            description="If the Line must be reported regardless of Transmission [Report Voltage Threshold].",
            ge=-1,
        ),
    ] = 0
    
    offer_base: Annotated[
        ActivePower,
        Field(
            alias="Offer Base",
            description="Base dispatch point for balancing offer",
        ),
    ] = ActivePower(0.0, "MW")
    
    offer_price: Annotated[
        float,
        Field(
            alias="Offer Price",
            description="Price offered in band for reference direction flows ($/MWh)",
        ),
    ] = 10000.0
    
    offer_price_back: Annotated[
        float,
        Field(
            alias="Offer Price Back",
            description="Price offered in band for counter-reference direction flows",
        ),
    ] = 10000.0
    
    offer_quantity: Annotated[
        List[ActivePower],
        Field(
            alias="Offer Quantity",
            description="Quantity offered in band for reference direction flows",
        ),
    ] = [ActivePower(0.0, "MW")]
    
    offer_quantity_back: Annotated[
        ActivePower,
        Field(
            alias="Offer Quantity Back",
            description="Quantity offered in band for counter-reference direction flows",
        ),
    ] = ActivePower(0.0, "MW")
    
    offer_quantity_format: Annotated[
        int,
        Field(
            alias="Offer Quantity Format",
            description="Format for [Offer Quantity] and [Offer Price]",
            ge=0,
            le=1,
        ),
    ] = 0
    
    outage_max_rating: Annotated[
        ActivePower,
        Field(
            alias="Outage Max Rating",
            description="Line rating in the reference direction during outage",
        ),
    ] = ActivePower(0.0, "MW")
    
    outage_min_rating: Annotated[
        List[ActivePower],
        Field(
            alias="Outage Min Rating",
            description="Line rating in the counter-reference direction during outage",
        ),
    ] = ActivePower(0.0, "MW")
    
    overload_max_rating: Annotated[
        ActivePower,
        Field(
            alias="Overload Max Rating",
            description="Emergency line rating in the reference direction",
        ),
    ] = ActivePower(0.0, "MW")
    
    overload_min_rating: Annotated[
        ActivePower,
        Field(
            alias="Overload Min Rating",
            description="Emergency line rating in the counter-reference direction",
        ),
    ] = ActivePower(0.0, "MW")
    
    price_setting: Annotated[
        NonPositiveInt,
        Field(
            alias="Price Setting",
            description="Flag if the Line can transfer price across the network",
            ge=-1,
            le=0,
        ),
    ] = -1
    
    project_start_date: Annotated[
        NonNegativeInt,
        Field(
            alias="Project Start Date",
            description="Start date of transmission project, for expansion planning.",
            ge=0,
        ),
    ] = 36526
    
    ramp_down_point: Annotated[
        ActivePower,
        Field(
            alias="Ramp Down Point",
            description="Flow for use with multi-band Max Ramp Down constraints",
        ),
    ] = ActivePower(1e30, "MW")
    
    ramp_penalty: Annotated[
        float,
        Field(
            alias="Ramp Penalty",
            description="Penalty for changes in flow on the line",
        ),
    ] = 0.0
    
    ramp_up_point: Annotated[
        ActivePower,
        Field(
            alias="Ramp Up Point",
            description="Flow for use with multi-band Max Ramp Up constraints",
        ),
    ] = ActivePower(1e30, "MW")
    
    random_number_seed: Annotated[
        NonNegativeInt,
        Field(
            alias="Random Number Seed",
            description="Random number seed assigned to the Line for the generation of outages",
            le=2147483647,
        ),
    ] = 0
    
    reactance: Annotated[
        float,
        Field(
            alias="Reactance",
            description="Together with any resistance this makes up the lines impedance",
        ),
    ] = 0.0
    
    repair_time_distribution: Annotated[
        List[int],
        Field(
            alias="Repair Time Distribution",
            description="Distribution used to generate repair times (Auto,Constant,Uniform,Triangular,Exponential,Weibull,Lognormal,SEV,LEV)",
            ge=-1,
            le=7,
        ),
    ] = [-1]
    
    repair_time_scale: Annotated[
        float,
        Field(
            alias="Repair Time Scale",
            description="Repair time function scale parameter (for exponential,Weibull,lognormal,SEV,LEV)",
        ),
    ] = 0.0
    
    repair_time_shape: Annotated[
        float,
        Field(
            alias="Repair Time Shape",
            description="Repair time function shape parameter (for Weibull,lognormal)",
        ),
    ] = 0.0
    
    resistance: Annotated[
        float,
        Field(
            alias="Resistance",
            description="A measure of the line's opposition to the flow of electric charge (pu)",
        ),
    ] = 0.0
    
    retire_non_anticipativity: Annotated[
        float,
        Field(
            alias="Retire Non-anticipativity",
            description="Price for violating non-anticipativity constraints in scenario-wise decomposition mode ($/MW).",
        ),
    ] = -1.0
    
    retirement_cost: Annotated[
        float,
        Field(
            alias="Retirement Cost",
            description="Cost of retiring the line",
        ),
    ] = 0.0
    
    screening_mode: Annotated[
        int,
        Field(
            alias="Screening Mode",
            description="The set of lines that should be screened for post-contingency flow under screen contingencies",
            ge=0,
            le=2,
        ),
    ] = 1
    
    susceptance: Annotated[
        float,
        Field(
            alias="Susceptance",
            description="The reciprocal of the reactance of a circuit and thus the imaginary part of its admittance",
        ),
    ] = 0.0
    
    technical_life: Annotated[
        NonNegativeFloat,
        Field(
            alias="Technical Life",
            description="Technical lifetime of the line",
        ),
    ] = 1e30
    
    type: Annotated[
        int,
        Field(
            alias="Type",
            description="Line expansion type",
            ge=0,
            le=1,
        ),
    ] = 0
    
    units: Annotated[
        int,
        Field(
            alias="Units",
            description="Flag if the line is in service (0,1)",
            ge=0,
            le=1,
        ),
    ] = 1
    
    units_out: Annotated[
        NonNegativeInt,
        Field(
            alias="Units Out",
            description="Number of units (circuits) out of service",
            ge=0,
        ),
    ] = 0
    
    wacc: Annotated[
        Percentage,
        Field(
            alias="WACC",
            description="Weighted average cost of capital",
            ge=0,
        ),
    ] = Percentage(10.0, "%")
    
    wheeling_charge: Annotated[
        float,
        Field(
            alias="Wheeling Charge",
            description="Wheeling charge for reference direction flows",
        ),
    ] = 0.0
    
    wheeling_charge_back: Annotated[
        float,
        Field(
            alias="Wheeling Charge Back",
            description="Wheeling charge for counter-reference direction flows",
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
    
    # Line companies input properties
    share: Annotated[
        Percentage,
        Field(
            alias="Share",
            description="Percentage share of ownership",
            ge=0.0,
            le=100.0,
        ),
    ] = Percentage(100.0, "%")
    
    # Line constraints input properties
    build_cost_coefficient: Annotated[
        Currency,
        Field(
            alias="Build Cost Coefficient",
            description="Coefficient of total build cost",
        ),
    ] = Currency(0.0, "usd")
    
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
    
    export_capacity_retired_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Export Capacity Retired Coefficient",
            description="Coefficient of export capacity retired",
        ),
    ] = ActivePower(0.0, "MW")
    
    flow_back_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Flow Back Coefficient",
            description="Coefficient of counter-reference direction flow",
        ),
    ] = ActivePower(0.0, "MW")
    
    flow_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Flow Coefficient",
            description="Coefficient of flow",
        ),
    ] = ActivePower(0.0, "MW")
    
    flow_forward_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Flow Forward Coefficient",
            description="Coefficient of reference direction flow",
        ),
    ] = ActivePower(0.0, "MW")
    
    flow_squared_coefficient: Annotated[
        float,
        Field(
            alias="Flow Squared Coefficient",
            description="Coefficient of square of line flow",
        ),
    ] = 0.0
    
    flowing_back_coefficient: Annotated[
        float,
        Field(
            alias="Flowing Back Coefficient",
            description="Boolean value (1 if the line is flowing in the counter-reference direction, 0 otherwise)",
        ),
    ] = 0.0
    
    flowing_forward_coefficient: Annotated[
        float,
        Field(
            alias="Flowing Forward Coefficient",
            description="Boolean value (1 if the line is flowing in the reference direction, 0 otherwise)",
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
    
    import_capacity_retired_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Import Capacity Retired Coefficient",
            description="Coefficient of import capacity retired",
        ),
    ] = ActivePower(0.0, "MW")
    
    in_service_coefficient: Annotated[
        float,
        Field(
            alias="In Service Coefficient",
            description="Coefficient of 0,1 flag indicating if the Line is installed and in service",
        ),
    ] = 0.0
    
    out_of_service_coefficient: Annotated[
        float,
        Field(
            alias="Out of Service Coefficient",
            description="Coefficient of 0,1 flag indicating if the Line is either not installed or out of service",
        ),
    ] = 0.0
    
    sharing_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Sharing Coefficient",
            description="Coefficient of reserve shared on the line",
        ),
    ] = ActivePower(0.0, "MW")
    
    spare_export_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Spare Export Capacity Coefficient",
            description="Coefficient on spare line capacity in the reference direction",
        ),
    ] = ActivePower(0.0, "MW")
    
    spare_import_capacity_coefficient: Annotated[
        ActivePower,
        Field(
            alias="Spare Import Capacity Coefficient",
            description="Coefficient on spare line capacity in the counter-reference direction",
        ),
    ] = ActivePower(0.0, "MW")
    
    units_built_coefficient: Annotated[
        float,
        Field(
            alias="Units Built Coefficient",
            description="Coefficient of number of units built",
        ),
    ] = 0.0
    
    units_built_in_year_coefficient: Annotated[
        float,
        Field(
            alias="Units Built in Year Coefficient",
            description="Coefficient of number of lines built in the year",
        ),
    ] = 0.0
    
    units_out_coefficient: Annotated[
        float,
        Field(
            alias="Units Out Coefficient",
            description="Coefficient of units out",
        ),
    ] = 0.0
    
    units_retired_coefficient: Annotated[
        float,
        Field(
            alias="Units Retired Coefficient",
            description="Coefficient of number of units retired",
        ),
    ] = 0.0
    
    units_retired_in_year_coefficient: Annotated[
        float,
        Field(
            alias="Units Retired in Year Coefficient",
            description="Coefficient of number of lines retired in the year",
        ),
    ] = 0.0