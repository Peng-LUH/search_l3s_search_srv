from http import HTTPStatus
from flask_restx import Namespace, Resource

ns_reranker = Namespace("reranker", validate=True)


@ns_reranker.route("/test", endpoint="reranker-test")
class RerankerTest(Resource):
    def get(self):
        return {"message": "Test message of reranker-service"}, HTTPStatus.OK