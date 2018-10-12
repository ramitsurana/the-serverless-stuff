"""Rest API for Demo."""
from chalice import Chalice
from chalice import Response
from demo_dao import DemoDao
from util.logger_utility import LoggerUtility


APP = Chalice(app_name='ramit-test')
APP.debug = True


@APP.route('/info', methods=['POST'])
def info():
    """Info on user."""
    # Set log level
    LoggerUtility.set_level()
    try:
        request = APP.current_request
        demo_dao = DemoDao(request.json_body)
        response = demo_dao.info()
        LoggerUtility.log_info('API Invoke sucessfully!')
        return Response(response, status_code=200)
    except UserNotFoundException as user_not_found_exception:
        body = {'Code': '404 - UserNotFound', 'Message': str(user_not_found_exception)}
        return Response(body, status_code=404)
    except Exception as exception:
        body = {'Code': '500- InternalServerError', 'Message': str(exception)}
        return Response(body, status_code=500)


@APP.route('/favorite-shows', methods=['GET'])
def favorite_shows():
    """My Favourite Shows."""
    # Set log level
    LoggerUtility.set_level()
    try:
        request = APP.current_request
        demo_dao = DemoDao(request.json_body)
        response = demo_dao.favorite_shows()
        return Response(response, status_code=200)
    except Exception as exception:
        body = {'Code': '500- InternalServerError', 'Message': str(exception)}
        return Response(body, status_code=500)
