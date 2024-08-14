# Importing module
import importlib
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if os.path.exists('jobs.zip'):
    logging.info("jobs.zip exists")
    sys.path.insert(0, 'jobs.zip')
else:
    logging.info("jobs.zip not exists")
    sys.path.insert(0, './jobs')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.fatal("Usage: pyspark_main <job>")
        sys.exit(1)

    logging.info('Program name: %s', sys.argv[0])

    job = importlib.import_module('jobs.{0}'.format(sys.argv[1]))
    logger.info(job.__name__)

    # process_param = "${SCHEMA}"
    with open("../tmp/info.log", "r") as log_info:
        process_param = log_info.read()

    job.process(process_param)
