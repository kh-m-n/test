import threading
from concurrent import futures

import grpc

from app.rpc.generated import mission_pb2
from app.rpc.generated import mission_pb2_grpc


class BaseVehicle(mission_pb2_grpc.VehicleServiceServicer):

    def __init__(self, vehicle_id: str, vehicle_type: str):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type

        self.state = mission_pb2.IDLE
        self.progress = 0
        self.result_message = ""

        self.current_mission = None

    # -------------------------------------------------
    # RPC: AssignMission
    # -------------------------------------------------
    def AssignMission(self, request, context):

        print(
            f"[{self.vehicle_id}] mission received: "
            f"{request.mission_id}"
        )

        if not self.is_compatible(request):

            return mission_pb2.MissionAck(
                mission_id=request.mission_id,
                vehicle_id=self.vehicle_id,
                accepted=False,
                message="Mission incompatible with vehicle role",
            )

        self.current_mission = request
        self.state = mission_pb2.ASSIGNED
        self.progress = 0
        self.result_message = ""

        thread = threading.Thread(
            target=self.execute_mission,
            daemon=True,
        )
        thread.start()

        return mission_pb2.MissionAck(
            mission_id=request.mission_id,
            vehicle_id=self.vehicle_id,
            accepted=True,
            message="Mission accepted",
        )

    # -------------------------------------------------
    # RPC: GetVehicleStatus
    # -------------------------------------------------
    def GetVehicleStatus(self, request, context):

        return mission_pb2.VehicleStatus(
            vehicle_id=self.vehicle_id,
            state=self.state,
            assigned_mission_id=(
                self.current_mission.mission_id
                if self.current_mission
                else ""
            ),
            progress_percent=self.progress,
            result=self.result_message,
        )

    # -------------------------------------------------
    # OVERRIDES
    # -------------------------------------------------
    def execute_mission(self):
        raise NotImplementedError

    def is_compatible(self, request) -> bool:
        return True


# -------------------------------------------------
# gRPC SERVER
# -------------------------------------------------
def run_rpc_server(vehicle: BaseVehicle, rpc_port: int):

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    mission_pb2_grpc.add_VehicleServiceServicer_to_server(
        vehicle,
        server,
    )

    server.add_insecure_port(f"[::]:{rpc_port}")

    server.start()

    print(
        f"[{vehicle.vehicle_id}] "
        f"RPC server listening on port {rpc_port}"
    )

    server.wait_for_termination()