import logging
from src.ingestion import run_parallel_process

def main()-> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%m%d%Y %I:%M:%S %p"
    )
    logging.info("Starting data ingestion")
    run_parallel_process()
    logging.info("End data ingestion")


if __name__ == "__main__":
    main()
