from flask import Flask
from flask import request, render_template
import sys
import json
import logging 

from FizzBuzz import FizzBuzz
from api_response import api_response

# create app
class flask_app():
    def __init__(self, cfg_path):
        self.__cfg = self.__read_config(cfg_path)
        self.__set_logger()
        self.fizzbuzz = FizzBuzz()

    def __read_config(self, cfg_path):
        """read json config file"""
        with open(cfg_path,"r") as file:
            d = json.load(file)
        return d

    def __set_logger(self):
        self.__logger = logging.getLogger(self.__cfg["app"]["logger"]["logger_name"])  
        self.__logger.setLevel(self.__cfg["app"]["logger"]["log_level"])

        # log formatter
        formatter = logging.Formatter("[{0}][%(levelname)s] %(asctime)s %(message)s".format(self.__cfg["app"]["logger"]["logger_name"]), datefmt="%Y-%m-%d %H:%M:%S")

        # stream handler
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.__logger.addHandler(stream_handler)

        # file handler
        file_handler = logging.FileHandler(self.__cfg["app"]["logger"]["logger_file"])
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)


    def create_app(self):
        """creates flask app"""
        self.__logger.info("creating fizzbuzz app")

        # flask app
        app = Flask(__name__)
        app.config["DEBUG"] = self.__cfg["app"]["debug"]
        app.secret_key = self.__cfg["app"]["secret"]

        @app.route('/', methods=['GET'])
        def home():
            return render_template("index.html")

        @app.route('/api', methods=['GET', 'POST'])
        def api():
            # check parameters
            try:
                start = int(self.__cfg["api"]["defaults"]["start"])
                stop = int(self.__cfg["api"]["defaults"]["stop"])
                to_list = self.__cfg["api"]["defaults"]["to_list"]

                if 'to_list' in request.args:
                    to_list = True

                if 'start' in request.args:
                    start = int(request.args["start"])

                if 'stop' in request.args:
                    stop = int(request.args["stop"])

                if abs(start - stop) <= 0:
                    raise ValueError

                if abs(abs(start) - abs(stop)) >= int(self.__cfg["api"]["max_fizzbuzz_amount"]):
                    raise ValueError

            except:
                self.__logger.warning("api request failed, wrong parameters passed")

                api_resp = api_response(self.__cfg["api"]["statuses"]["fail"], self.__cfg["api"]["errors"]["wrong_parameter"], "")

                return api_resp.get_api_response()

            # handle post request for custom api response
            if(request.method == 'POST'):
                try:
                    self.__logger.info("custom fizzbuzz api is requested with params start:{0} stop:{1} to_list:{2}".format(start, stop, to_list))

                    # parse posted json
                    custom_fizzbuzz_array = json.loads(request.data.decode('utf-8'))

                    # check max size for the custom array
                    if(len(custom_fizzbuzz_array["custom_fizzbuzz"]) > int(self.__cfg["api"]["max_custom_fizzbuzz_amount"])):
                        raise ValueError

                    # get custom fizzbuzz
                    data = self.fizzbuzz.fizzbuzz_custom(custom_fizzbuzz_array, start=start, stop=stop, to_list=to_list)

                    api_resp = api_response(self.__cfg["api"]["statuses"]["success"], "", data)

                except ZeroDivisionError:
                    self.__logger.warning("api request failed with ZeroDivisionError")
                    api_resp = api_response(self.__cfg["api"]["statuses"]["fail"], self.__cfg["api"]["errors"]["divide_by_zero"], "")

                except json.decoder.JSONDecodeError:
                    self.__logger.warning("api request failed with JSONDecodeError")
                    api_resp = api_response(self.__cfg["api"]["statuses"]["fail"], self.__cfg["api"]["errors"]["json_decode_error"], "")

                except ValueError:
                    self.__logger.warning("api request failed with ValueError")
                    api_resp = api_response(self.__cfg["api"]["statuses"]["fail"], self.__cfg["api"]["errors"]["wrong_parameter"], "")

                except:
                    self.__logger.warning("api request failed with unknown error", exc_info=True)
                    api_resp = api_response(self.__cfg["api"]["statuses"]["fail"], self.__cfg["api"]["errors"]["general_error"], "")

                return api_resp.get_api_response()

            # handle get request for regular api response
            else:
                try:
                    self.__logger.info("regular fizzbuzz api is requested with params start:{0} stop:{1} to_list:{2}".format(start, stop, to_list))
                    data = self.fizzbuzz.fizzbuzz(start=start, stop=stop, to_list=to_list)
                    api_resp = api_response(self.__cfg["api"]["statuses"]["success"], "", data)
                except:
                    self.__logger.warning("api request failed with unknown error", exc_info=True)
                    api_resp = api_response(self.__cfg["api"]["statuses"]["fail"], self.__cfg["api"]["errors"]["general_error"], "")

                return api_resp.get_api_response()

        # return flask app for serving
        return app


if __name__ == '__main__':
    f = flask_app("fizzbuzz_api/config/fizzbuzz.cfg")
    f.create_app().run()
