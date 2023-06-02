from typing import TYPE_CHECKING, Any, Dict, List, Union

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ..block_class_client import BlockClassClient
from ..block_client import BlockClient
from ..settings import BLOCKS, TYPE
from ..utils import check_for_res_error, enforce_id_in_branch

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


class BranchClient:
    data: 'Dict[str, Any]'

    def __ingest_branch_res(self, branch_res_dict: dict):
        for k, v in branch_res_dict.items():
            setattr(self, k, v)

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, client: 'SedaroApiClient'):
        self.__ingest_branch_res(body)
        self._sedaro_client = client

    def __str__(self):
        return f'BranchClient(id: {self.id}, name: "{self.name}")'

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, block_type: str) -> BlockClassClient:

        # -- check block type
        if block_type not in self.data['_supers']:
            raise AttributeError(
                f'Unable to create a "BlockClassClient" from string: "{block_type}". Please check the name and try again.')

        return BlockClassClient(block_type, self)

    def crud(
        self,
        *,
        root: 'Dict[str, Any]' = None,
        blocks: 'List[Dict]' = None,
        delete: 'List[str]' = None
    ) -> 'dict':
        """Method to perform multiple CRUD operations at the same time.

        Args:
            root (dict, optional): a `dict` of field/value pairs to update on the `root` of the branch template this\
                method is called on. Defaults to `None`.
            blocks (list, optional): a `list` of Block dictionaries. If there is an `id` in the `dict`, updates an\
                existing Block, otherwise creates a new Block. Defaults to `None`.
            delete (list, optional): a list of `id`s of Blocks to be deleted. Defaults to `None`.

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            dict: the response dictionary from the request
        """
        root = {} if root is None else root
        blocks = [] if blocks is None else blocks
        delete = [] if delete is None else delete

        if not isinstance(root, dict):
            raise ValueError('The "root" arg must be an dictionary.')
        if not all(isinstance(el, list) for el in [blocks, delete]):
            raise ValueError('Each of the following args must be lists: "blocks" and "delete".')
        if blocks == [] and delete == [] and root == {}:
            raise ValueError(
                'Must provide at least one or more of the following args: "root" as a non-empty object, "blocks" and/or "delete" as non-empty arrays.')

        res = self._sedaro_client.send_request(
            f'/models/branches/{self.id}/template/',
            'PATCH',
            {
                'root': root,
                'blocks': blocks,
                'delete': delete
            }
        )

        check_for_res_error(res)
        self.__ingest_branch_res(res['branch'])

        return res

    def get_block(self, id: Union[str, int]):
        """Creates a `BlockClient` associated with the Sedaro Block of the given `id`.

        Args:
            id (Union[str, int]): `id` of the desired Sedaro Block

        Raises:
            KeyError: if no corresponding Block exists in the Branch

        Returns:
            BlockClient: a client to interact with the corresponding Sedaro Block
        """
        enforce_id_in_branch(self, id)
        return BlockClient(
            id,
            getattr(self, self.data[BLOCKS][id][TYPE])
        )

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # AGENT TEMPLATE
    AngularVelocitySensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Antenna: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    AveragingAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Battery: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BatteryCell: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BatteryPack: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BodyFrameVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BodyInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BusRegulator: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CelestialTarget: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CelestialVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CircularFieldOfView: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Component: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ComponentToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CompoundCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Cooler: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CooperativeTransmitInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataBus: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataStorage: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataType: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DirectionSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    EkfAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FixedSurface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FuelReservoir: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FullyRegDetPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GpsAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GroundTarget: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Heater: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    InternalDataInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LaserCommModule: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LoadState: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LocalVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LockPointingMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Magnetorquer: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    MaxAlignPointingMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    MekfAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Modem: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    OperationalMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    OpticalAttitudeSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Orbit: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PassivePointingMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PassiveTransmitInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PidAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PositionSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PowerLoad: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    QuasiRegDetPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ReactionWheel: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ReceiveInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    RectangularFieldOfView: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ResistanceLoad: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SameTargetMultiCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Satellite: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToSatelliteCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToTargetCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SingleConvHybridPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SingleConvMpptPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SlidingModeAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarArray: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarCell: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarPanel: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpaceTarget: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SphericalFuelTank: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpherocylinderFuelTank: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    StaticThrustControlAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Subsystem: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SunTrackingSurface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SurfaceMaterial: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroup: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToSatelliteCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToTargetCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetToTargetCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TempControllerState: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalInterfaceMaterial: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Thruster: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TimeCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TriadAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TwoConvMpptPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorTrackingSurface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""

    # SCENARIO
    Agent: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    AgentGroup: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    ClockConfig: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    Orbit: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""

    # BOTH (overwrites above)
    Orbit: BlockClassClient  # TODO: will be removed from AgentTemplate at some point
    """A Sedaro `Block` class on an `AgentTemplate` or a `ScenarioTemplate` branch"""
