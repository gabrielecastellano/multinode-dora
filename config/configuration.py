class Configuration:

    AGREEMENT_TIMEOUT = 6
    WEAK_AGREEMENT_TIMEOUT = 12

    ASYNC_TIMEOUT = 0.05

    STABLE_CONNECTIONS = True
    SDO_NUMBER = 10
    LOAD_TOPOLOGY = True
    NEIGHBOR_PROBABILITY = 20
    TOPOLOGY_FILE = "config/topology.json"

    NODE_NUMBER = 4
    BUNDLE_PERCENTAGE = 65

    SCHEDULING_TIME_LIMIT = 1
    SAMPLE_FREQUENCY = .100

    LOG_LEVEL = "WARNING"

    RAP_INSTANCE = "config/rap_instance.json"
    RESULTS_FOLDER = "results"
