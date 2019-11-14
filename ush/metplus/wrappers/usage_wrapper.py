#!/usr/bin/env python

from metplus.wrappers.command_builder import CommandBuilder

# @namespace UsageWrapper
# @brief Provides a default process for master_metplus.py.  Indicates what
# processes are currently available.
# Call as follows:
# @code{.sh}
# usage_wrapper.py [-c /path/to/user.template.conf]
# @endcode#

class UsageWrapper(CommandBuilder):
    """! A default process, prints out usage when nothing is defined in
         the PROCESS_LIST of the parm/metplus_config/metplus_runtime.conf
         and no lower level config files are included.
    """
    def __init__(self, p, logger):
        super().__init__(p, logger)
        self.app_name = 'Usage'
        self.logger = logger
        self.available_processes = ['CyclonePlotter', 'EnsembleStat',
                                    'ExtractTiles', 'GempakToCF', 'GridStat',
                                    'Mode', 'MTD', 'PB2NC', 'PcpCombine',
                                    'PointStat', 'RegridDataPlane',
                                    'SeriesByLead', 'SeriesByInit', 'TcPairs',
                                    'TcStat', 'TCMPRPlotter']

    def run_all_times(self):
        print("USAGE:\n  This is a default process, please indicate more " +
              " specific processes in the PROCESS_LIST variable in one " +
              "or more of the following configuration files:\n " +
              "-parm/metplus_config/metplus_runtime.conf\n " +
              "-parm/metplus_use_cases/<usecase_name>/<usecase_name>.conf\n " +
              "-parm/metplus_use_cases/<usecase_name>/" +
              "examples/<example_name>.conf \n")
        print("Currently available processes are: ")
        for process in self.available_processes:
            print("  - {}".format(process))
