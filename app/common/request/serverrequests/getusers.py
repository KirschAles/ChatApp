from app.common.request.serverrequest import ServerRequest, Interface


class GetUsers(ServerRequest):
    def __init__(self, conn, db: Interface):
        super().__init__(conn, db)