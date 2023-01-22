import os
from datetime import datetime
from os import environ

from dotenv import load_dotenv


class Utils:

    @staticmethod
    def write_to_log(info: str):
        load_dotenv()
        """
        Name: Ofri Shapira\n
        Date: 18/1/22\n
        Method to write errors and runtime actions to a log file.
        :param func_name: The source function name
        :param info: Information about the exception/runtime action to send the log
        :param exception: The exception's details
        :param type_of_action: Exception or Runtime
        :return: None
        """
        file_path = environ["LOG_PATH"]
        file_name = environ["LOG_FILE_NAME"]

        f = ""
        try:
            if os.path.exists(file_path):
                os.chdir(file_path)
                f = open(f'{file_name}', 'a')
                f.write(
                    f"\n#{datetime.now()}.\nInfo: {info}.\n")
                f.close()
            else:
                os.mkdir(file_path)
                os.chdir(file_path)
                f = open(f'{file_name}', 'w')
                f.write(
                    f"\n#{datetime.now()}.\nInfo: {info}.\n")
                f.close()

        except FileNotFoundError as f:
            print(f"{file_name} not found, Exception is ", f)
        except Exception as e:
            print(e)
        finally:
            f.close()
