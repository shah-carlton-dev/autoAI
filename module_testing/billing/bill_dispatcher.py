# imports
import logging
import time

# logging configuration
logging.basicConfig(level=logging.DEBUG, filename="./module_testing/logs/mac_test", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")

# class bill
class Bills: 
    def __init__(self, _job_id, _company, _model, _config_name, _usage, _runtime, _log_file ):
        self.job_id = _job_id
        self.company = _company
        self.model = _model
        self.config_name = _config_name
        self.usage = _usage
        self.runtime = _runtime
        self.log_file = _log_file

# function will be called at the completion of each model configuration
def bill_dispatcher(bill_info: Bills):
    