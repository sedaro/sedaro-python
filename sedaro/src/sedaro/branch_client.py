from typing import TYPE_CHECKING, Any, Dict, List, Union

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from .block_class_client import BlockClassClient
from .block_client import BlockClient
from .settings import BLOCKS, TYPE
from .utils import check_for_res_error, enforce_id_in_branch

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


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
    DataBus: BlockClassClient
    Modem: BlockClassClient
    OpticalAttitudeSensor: BlockClassClient
    SurfaceMaterial: BlockClassClient
    TempControllerState: BlockClassClient
    DirectionSensor: BlockClassClient
    FullyRegDetPowerProcessor: BlockClassClient
    FuelReservoir: BlockClassClient
    TimeCondition: BlockClassClient
    SphericalFuelTank: BlockClassClient
    ReactionWheel: BlockClassClient
    TargetGroupToScalarCondition: BlockClassClient
    BatteryCell: BlockClassClient
    TwoConvMpptPowerProcessor: BlockClassClient
    DataStorage: BlockClassClient
    TransmitDataInterface: BlockClassClient
    SolarArray: BlockClassClient
    GpsAlgorithm: BlockClassClient
    TargetGroup: BlockClassClient
    CooperativeTransmitInterface: BlockClassClient
    PidAlgorithm: BlockClassClient
    Orbit: BlockClassClient
    VectorInFovCondition: BlockClassClient
    ReceiveInterface: BlockClassClient
    OperationalMode: BlockClassClient
    FixedSurface: BlockClassClient
    RectangularFieldOfView: BlockClassClient
    InternalDataInterface: BlockClassClient
    BodyFrameVector: BlockClassClient
    SolarPanel: BlockClassClient
    GroundTarget: BlockClassClient
    VectorTrackingSurface: BlockClassClient
    ActivePointingMode: BlockClassClient
    ExternalDataInterface: BlockClassClient
    Magnetorquer: BlockClassClient
    PowerProcessor: BlockClassClient
    PassivePointingMode: BlockClassClient
    SunTrackingSurface: BlockClassClient
    BusRegulator: BlockClassClient
    Thruster: BlockClassClient
    PowerLoad: BlockClassClient
    SatelliteToTargetCondition: BlockClassClient
    TargetGroupInFovCondition: BlockClassClient
    VectorSensor: BlockClassClient
    LaserCommModule: BlockClassClient
    BatteryPack: BlockClassClient
    ResistanceLoad: BlockClassClient
    ReferenceVector: BlockClassClient
    PassiveTransmitInterface: BlockClassClient
    PositionSensor: BlockClassClient
    DataInterface: BlockClassClient
    SatelliteToScalarCondition: BlockClassClient
    TargetGroupVector: BlockClassClient
    SpaceTarget: BlockClassClient
    Heater: BlockClassClient
    StaticThrustControlAlgorithm: BlockClassClient
    CelestialTarget: BlockClassClient
    TriadAlgorithm: BlockClassClient
    CompoundCondition: BlockClassClient
    QuasiRegDetPowerProcessor: BlockClassClient
    SingleConvHybridPowerProcessor: BlockClassClient
    DataType: BlockClassClient
    LocalVector: BlockClassClient
    TargetVector: BlockClassClient
    Satellite: BlockClassClient
    AveragingAlgorithm: BlockClassClient
    Antenna: BlockClassClient
    SatelliteToSatelliteCondition: BlockClassClient
    DataMode: BlockClassClient
    BodyInFovCondition: BlockClassClient
    TargetGroupToTargetCondition: BlockClassClient
    EkfAlgorithm: BlockClassClient
    Subsystem: BlockClassClient
    TargetGroupToSatelliteCondition: BlockClassClient
    MaxAlignPointingMode: BlockClassClient
    Battery: BlockClassClient
    CircularFieldOfView: BlockClassClient
    SolarCell: BlockClassClient
    AngularVelocitySensor: BlockClassClient
    CelestialVector: BlockClassClient
    Component: BlockClassClient
    MekfAlgorithm: BlockClassClient
    ThermalInterfaceMaterial: BlockClassClient
    SpherocylinderFuelTank: BlockClassClient
    TargetInFovCondition: BlockClassClient
    Cooler: BlockClassClient
    LoadState: BlockClassClient
    SingleConvMpptPowerProcessor: BlockClassClient
    SlidingModeAlgorithm: BlockClassClient
    ThermalInterface: BlockClassClient
    TargetToScalarCondition: BlockClassClient
    LockPointingMode: BlockClassClient
    TargetToTargetCondition: BlockClassClient
    SameTargetMultiCondition: BlockClassClient

    # SCENARIO
    AgentGroup: BlockClassClient
    ClockConfig: BlockClassClient
    Orbit: BlockClassClient
    Agent: BlockClassClient
