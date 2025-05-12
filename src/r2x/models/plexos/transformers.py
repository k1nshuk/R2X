# plexos_transformers.py
from typing import Annotated, List, Union
from pydantic import Field, NonNegativeFloat, NonNegativeInt, NonPositiveInt
from r2x.models.core import Device
from r2x.models.branch import Transformer2W, TapTransformer, PhaseShiftingTransformer
from r2x.units import Angle, ActivePower, Percentage

class PlexosTransformer(Device):
    """"
    Class that represents a transformer in PLEXOS.
    """

    ac_fixed_shift_angle: Annotated[
        Angle,
        Field(
            alias="AC Fixed Shift Angle",
            description="The fixed phase shift angle between the two windings of a single-phase transformer",
        ),
    ] = 0.0
    
    ac_line_charging_susceptance: Annotated[
        float,
        Field(
            alias="AC Line Charging Susceptance",
            description="The line-charging susceptance of a transformer",
        ),
    ] = 0.0
    
    ac_tap_ratio: Annotated[
        NonNegativeFloat,
        Field(
            alias="AC Tap Ratio",
            description="The turns ratio of the primary winding of a transformer",
        ),
    ] = 1.0
    
    contingency_limit_penalty: Annotated[
        float,
        Field(
            alias="Contingency Limit Penalty",
            description="Penalty for exceeding contingency flow limits ($/MWh)",
        ),
    ] = -1.0
    
    enforce_limits: Annotated[
        int,
        Field(
            alias="Enforce Limits",
            description="If flow limits are enforced regardless of Transmission [Constraint Voltage Threshold].",
            ge=0,
            le=3,
        ),
    ] = 1
    
    fixed_loss: Annotated[
        ActivePower,
        Field(
            alias="Fixed Loss",
            description="Fixed loss on transformer",
        ),
    ] = ActivePower(0.0, "MW")
    
    forced_outage_rate: Annotated[
        Percentage,
        Field(
            alias="Forced Outage Rate",
            description="Expected proportion of time the facility is unavailable due to forced outage",
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
    
    limit_penalty: Annotated[
        float,
        Field(
            alias="Limit Penalty",
            description="Penalty for exceeding the flow limits on the Transformer. ($/MWh)",
        ),
    ] = -1.0
    
    loss_allocation: Annotated[
        NonNegativeFloat,
        Field(
            alias="Loss Allocation",
            description="Proportion of transformer losses allocated to the receiving node",
            ge=0,
            le=1,
        ),
    ] = 0.5
    
    maintenance_frequency: Annotated[
        NonNegativeFloat,
        Field(
            alias="Maintenance Frequency",
            description="Frequency of maintenance outages in an annual timeframe",
            ge=0,
        ),
    ] = 0.
    
    maintenance_rate: Annotated[
        Percentage,
        Field(
            alias="Maintenance Rate",
            description="Expected proportion of time the facility is unavailable due to maintenance",
            ge=0,
            le=100,
        ),
    ] = Percentage(0.0, "%")
    
    max_loss_tranches: Annotated[
        NonNegativeInt,
        Field(
            alias="Max Loss Tranches",
            description="Maximum number of tranches in piecewise linear loss function.",
            ge=2,
        ),
    ] = 2
    
    max_time_to_repair: Annotated[
        NonNegativeFloat,
        Field(
            alias="Max Time To Repair",
            description="Maximum time to repair (hr)",
            ge=0,
        ),
    ] = 0.0
    
    mean_time_to_repair: Annotated[
        NonNegativeFloat,
        Field(
            alias="Mean Time to Repair",
            description="Mean time to repair (hr)",
            ge=0,
        ),
    ] = 24.0
    
    min_time_to_repair: Annotated[
        NonNegativeFloat,
        Field(
            alias="Min Time To Repair",
            description="Minimum time to repair (hr)",
            ge=0,
        ),
    ] = 0.0
    
    must_report: Annotated[
        NonPositiveInt,
        Field(
            alias="Must Report",
            description="If the Transformer must be reported regardless of Transmission [Report Voltage Threshold].",
            ge=-1,
            le=0,
        ),
    ] = 0
    
    outage_max_rating: Annotated[
        ActivePower,
        Field(
            alias="Outage Max Rating",
            description="Transformer rating in the reference direction during outage",
        ),
    ] = ActivePower(0.0, "MW")
    
    outage_min_rating: Annotated[
        ActivePower,
        Field(
            alias="Outage Min Rating",
            description="Transformer rating in the counter-reference direction during outage",
        ),
    ] = ActivePower(0.0, "MW")
    
    overload_rating: Annotated[
        ActivePower,
        Field(
            alias="Overload Rating",
            description="Emergency rating in the reference direction",
            ge=0,
        ),
    ] = ActivePower(0.0, "MW")
    
    random_number_seed: Annotated[
        NonNegativeInt,
        Field(
            alias="Random Number Seed",
            description="Random number seed assigned to the Line for the generation of outages",
            le=2147483647,
        ),
    ] = 0
    
    rating: Annotated[
        ActivePower,
        Field(
            alias="Rating",
            description="Maximum MW rating",
            ge=0,
        ),
    ] = ActivePower(0.0, "MW")
    
    reactance: Annotated[
        float,
        Field(
            alias="Reactance",
            description="Together with any resistance this makes up the lines impedance",
        ),
    ] = 0.0
    
    repair_time_distribution: Annotated[
        int,
        Field(
            alias="Repair Time Distribution",
            description="Distribution used to generate repair times (Auto,Constant,Uniform,Triangular,Exponential,Weibull,Lognormal,SEV,LEV)",
            ge=-1,
            le=7,
        ),
    ] = -1
    
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
            description="A measure of the transformer's opposition to the flow of electric charge (pu)",
        ),
    ] = 0.0
    
    screening_mode: Annotated[
        int,
        Field(
            alias="Screening Mode",
            description="The set of transformers that should be screened for post-contingency flow under screen contingencies",
            ge=0,
            le=2,
        ),
    ] = 1
    
    susceptance: Annotated[
        float,
        Field(
            alias="Susceptance",
            description="The reciprocal of the reactance of a circuit and thus the imaginary part of its admittance (pu)",
        ),
    ] = 0.0
    
    units: Annotated[
        int,
        Field(
            alias="Units",
            description="Flag if transformer is in service",
            ge=0,
            le=1,
        ),
    ] = 1
    
    units_out: Annotated[
        int,
        Field(
            alias="Units Out",
            description="Number of [Units] out of service",
            ge=0,
            le=1,
        ),
    ] = 0
    
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

    @classmethod
    def example(cls) -> "PlexosTransformer":
        return PlexosTransformer(
            name="ExampleTransformer",
            ac_fixed_shift_angle=Angle(0.0, "degree"),
            ac_line_charging_susceptance=0.0,
            ac_tap_ratio=1.0,
            contingency_limit_penalty=-1.0,
            enforce_limits=1,
            fixed_loss=ActivePower(0.0, "MW"),
            forced_outage_rate=Percentage(0.0, "%"),
            limit_penalty=-1.0,
            loss_allocation=0.5,
            max_loss_tranches=2,
            max_time_to_repair=24.0,
            mean_time_to_repair=24.0,
            min_time_to_repair=0.0,
            outage_max_rating=ActivePower(100, "MW"),
            outage_min_rating=ActivePower(100, "MW"),
            overload_rating=ActivePower(100, "MW"),
            rating=ActivePower(100, "MW"),
            reactance=0.0,
            repair_time_distribution=-1,
            repair_time_scale=0.0,
            repair_time_shape=0.0,
            resistance=0.0,
            screening_mode=1,
            susceptance=0.0,
        )
    
    @classmethod
    def create_plexos_transformer_2w(transformer: Transformer2W) -> "PlexosTransformer":
        # Check if available
        if transformer.available is True:
            forced_outage_rate = Percentage(0.0, "%")
        else:
            forced_outage_rate = Percentage(100.0, "%")


        return PlexosTransformer(
            name = transformer.name,
            rating = transformer.rating,
            resistance=transformer.r,
            reactance=transformer.x,
            forced_outage_rate = forced_outage_rate,
        )
    
    @classmethod
    def create_plexos_tap_tansformer(transformer: TapTransformer) -> "PlexosTransformer":
        # Check if available
        if transformer.available is True:
            forced_outage_rate = Percentage(0.0, "%")
        else:
            forced_outage_rate = Percentage(100.0, "%")

        return PlexosTransformer(
            name = transformer.name,
            rating = transformer.rating,
            resistance=transformer.r,
            reactance=transformer.x,
            forced_outage_rate = forced_outage_rate,
            ac_tap_ratio=transformer.tap
        )
    
    @classmethod
    def create_plexos_phase_shifting_transformer(transformer: PhaseShiftingTransformer) -> "PlexosTransformer":
        # Check if available
        if transformer.available is True:
            forced_outage_rate = Percentage(0.0, "%")
        else:
            forced_outage_rate = Percentage(100.0, "%")

        return PlexosTransformer(
            name = transformer.name,
            rating = transformer.rating,
            resistance=transformer.r,
            reactance=transformer.x,
            forced_outage_rate = forced_outage_rate,
            ac_fixed_shift_angle=transformer.angle
        )
