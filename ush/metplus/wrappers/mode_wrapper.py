#!/usr/bin/env python

'''
Program Name: mode_wrapper.py
Contact(s): George McCabe
Abstract: Runs mode
History Log:  Initial version
Usage:
Parameters: None
Input Files:
Output Files:
Condition codes: 0 for success, 1 for failure
'''

import os
import metplus.util.met_util as util
from metplus.wrappers.compare_gridded_wrapper import CompareGriddedWrapper

class MODEWrapper(CompareGriddedWrapper):
    """!Wrapper for the mode MET tool"""
    def __init__(self, config, logger):
        super().__init__(config, logger)
        self.app_name = 'mode'
        self.app_path = os.path.join(config.getdir('MET_INSTALL_DIR'),
                                     'bin', self.app_name)

    def add_merge_config_file(self):
        """!If merge config file is defined, add it to the command"""
        if self.c_dict['MERGE_CONFIG_FILE'] != '':
            self.args.append('-config_merge {}'.format(self.c_dict['MERGE_CONFIG_FILE']))

    def create_c_dict(self):
        c_dict = super().create_c_dict()
        c_dict['VERBOSITY'] = self.config.getstr('config', 'LOG_MODE_VERBOSITY',
                                                 c_dict['VERBOSITY'])
        c_dict['CONFIG_FILE'] = self.config.getstr('config', 'MODE_CONFIG_FILE', '')
        c_dict['OBS_INPUT_DIR'] = \
          self.config.getdir('OBS_MODE_INPUT_DIR', '')
        c_dict['OBS_INPUT_TEMPLATE'] = \
          self.config.getraw('filename_templates',
                             'OBS_MODE_INPUT_TEMPLATE')
        c_dict['OBS_INPUT_DATATYPE'] = \
          self.config.getstr('config', 'OBS_MODE_INPUT_DATATYPE', '')
        c_dict['FCST_INPUT_DIR'] = \
          self.config.getdir('FCST_MODE_INPUT_DIR', '')
        c_dict['FCST_INPUT_TEMPLATE'] = \
          self.config.getraw('filename_templates',
                             'FCST_MODE_INPUT_TEMPLATE')
        c_dict['FCST_INPUT_DATATYPE'] = \
          self.config.getstr('config', 'FCST_MODE_INPUT_DATATYPE', '')
        c_dict['OUTPUT_DIR'] = self.config.getdir('MODE_OUTPUT_DIR')
        c_dict['ONCE_PER_FIELD'] = True
        c_dict['QUILT'] = self.config.getbool('config', 'MODE_QUILT', False)
        fcst_conv_radius, obs_conv_radius = \
            self.handle_fcst_and_obs_field('MODE_CONV_RADIUS',
                                           'FCST_MODE_CONV_RADIUS',
                                           'OBS_MODE_CONV_RADIUS')
        c_dict['FCST_CONV_RADIUS'] = fcst_conv_radius
        c_dict['OBS_CONV_RADIUS'] = obs_conv_radius

        fcst_conv_thresh, obs_conv_thresh = self.handle_fcst_and_obs_field('MODE_CONV_THRESH',
                                                                           'FCST_MODE_CONV_THRESH',
                                                                           'OBS_MODE_CONV_THRESH')

        c_dict['FCST_CONV_THRESH'] = fcst_conv_thresh
        c_dict['OBS_CONV_THRESH'] = obs_conv_thresh

        fcst_merge_thresh, obs_merge_thresh = \
                self.handle_fcst_and_obs_field('MODE_MERGE_THRESH',
                                               'FCST_MODE_MERGE_THRESH',
                                               'OBS_MODE_MERGE_THRESH')
        c_dict['FCST_MERGE_THRESH'] = fcst_merge_thresh
        c_dict['OBS_MERGE_THRESH'] = obs_merge_thresh
        fcst_merge_flag, obs_merge_flag = \
                self.handle_fcst_and_obs_field('MODE_MERGE_FLAG',
                                               'FCST_MODE_MERGE_FLAG',
                                               'OBS_MODE_MERGE_FLAG')

        c_dict['FCST_MERGE_FLAG'] = fcst_merge_flag
        c_dict['OBS_MERGE_FLAG'] = obs_merge_flag
        c_dict['ALLOW_MULTIPLE_FILES'] = False

        c_dict['MERGE_CONFIG_FILE'] = self.config.getstr('config', 'MODE_MERGE_CONFIG_FILE', '')

        # handle window variables [FCST/OBS]_[FILE_]_WINDOW_[BEGIN/END]
        self.handle_window_variables(c_dict, 'mode')

        c_dict['VERIFICATION_MASK_TEMPLATE'] = \
            self.config.getraw('filename_templates',
                               'MODE_VERIFICATION_MASK_TEMPLATE')
        c_dict['VERIFICATION_MASK'] = ''

        # check that values are valid
        error_message = 'items must start with a comparison operator '+\
                        '(>,>=,==,!=,<,<=,gt,ge,eq,ne,lt,le)'
        if not util.validate_thresholds(util.getlist(c_dict['FCST_CONV_THRESH'])):
            self.logger.error('MODE_FCST_CONV_THRESH {}'.format(error_message))
            exit(1)
        if not util.validate_thresholds(util.getlist(c_dict['OBS_CONV_THRESH'])):
            self.logger.error('MODE_OBS_CONV_THRESH {}'.format(error_message))
            exit(1)
        if not util.validate_thresholds(util.getlist(c_dict['FCST_MERGE_THRESH'])):
            self.logger.error('MODE_FCST_MERGE_THRESH {}'.format(error_message))
            exit(1)
        if not util.validate_thresholds(util.getlist(c_dict['OBS_MERGE_THRESH'])):
            self.logger.error('MODE_OBS_MERGE_THRESH {}'.format(error_message))
            exit(1)

        return c_dict

    def set_environment_variables(self, fcst_field, obs_field, var_info, time_info):
        print_list = ["MODEL", "FCST_VAR", "OBS_VAR",
                      "LEVEL", "OBTYPE", "CONFIG_DIR",
                      "FCST_FIELD", "OBS_FIELD",
                      "QUILT", "MET_VALID_HHMM",
                      "FCST_CONV_RADIUS", "FCST_CONV_THRESH",
                      "OBS_CONV_RADIUS", "OBS_CONV_THRESH",
                      "FCST_MERGE_THRESH", "FCST_MERGE_FLAG",
                      "OBS_MERGE_THRESH", "OBS_MERGE_FLAG"]

        self.add_env_var("MODEL", self.c_dict['MODEL'])
        self.add_env_var("OBTYPE", self.c_dict['OBTYPE'])
        self.add_env_var("FCST_VAR", var_info['fcst_name'])
        self.add_env_var("OBS_VAR", var_info['obs_name'])
        self.add_env_var("LEVEL", util.split_level(var_info['fcst_level'])[1])
        self.add_env_var("FCST_FIELD", fcst_field)
        self.add_env_var("OBS_FIELD", obs_field)
        self.add_env_var("CONFIG_DIR", self.c_dict['CONFIG_DIR'])
        self.add_env_var("MET_VALID_HHMM", time_info['valid_fmt'][4:8])

        quilt = 'TRUE' if self.c_dict['QUILT'] else 'FALSE'

        self.add_env_var("QUILT", quilt)
        self.add_env_var("FCST_CONV_RADIUS", self.c_dict["FCST_CONV_RADIUS"])
        self.add_env_var("OBS_CONV_RADIUS", self.c_dict["OBS_CONV_RADIUS"])
        self.add_env_var("FCST_CONV_THRESH", self.c_dict["FCST_CONV_THRESH"])
        self.add_env_var("OBS_CONV_THRESH", self.c_dict["OBS_CONV_THRESH"])
        self.add_env_var("FCST_MERGE_THRESH", self.c_dict["FCST_MERGE_THRESH"])
        self.add_env_var("OBS_MERGE_THRESH", self.c_dict["OBS_MERGE_THRESH"])
        self.add_env_var("FCST_MERGE_FLAG", self.c_dict["FCST_MERGE_FLAG"])
        self.add_env_var("OBS_MERGE_FLAG", self.c_dict["OBS_MERGE_FLAG"])

        # add additional env vars if they are specified
        if self.c_dict['VERIFICATION_MASK'] != '':
            self.add_env_var('VERIF_MASK',
                             self.c_dict['VERIFICATION_MASK'])
            print_list.append('VERIF_MASK')

        # set user environment variables
        self.set_user_environment(time_info)

        self.logger.debug("ENVIRONMENT FOR NEXT COMMAND: ")
        self.print_user_env_items()
        for item in print_list:
            self.print_env_item(item)
        self.logger.debug("COPYABLE ENVIRONMENT FOR NEXT COMMAND: ")
        self.print_env_copy(print_list)

    def run_at_time_one_field(self, time_info, var_info):
        """! Runs mode instances for a given time and forecast lead combination
              Overrides run_at_time_one_field function in compare_gridded_wrapper.py
              Args:
                @param time_info dictionary containing timing information
                @param var_info object containing variable information
        """
        # get model to compare
        model_path = self.find_model(time_info, var_info)
        if model_path is None:
            return

        # get observation to compare
        obs_path = self.find_obs(time_info, var_info)
        if obs_path is None:
            return

        # loop over all variables and levels (and probability thresholds) and call the app for each
        self.process_fields_one_thresh(time_info, var_info, model_path, obs_path)


    def process_fields_one_thresh(self, time_info, var_info, model_path, obs_path):
        """! For each threshold, set up environment variables and run mode
              Args:
                @param time_info dictionary containing timing information
                @param var_info object containing variable information
                @param model_path forecast file
                @param obs_path observation file
        """
        # if no thresholds are specified, run once
        fcst_thresh_list = []
        obs_thresh_list = []

        # if probabilistic forecast and no thresholds specified, error and skip
        if self.c_dict['FCST_IS_PROB']:
#            if len(var_info['fcst_thresh']) == 0:
#                self.logger.error('Must specify field threshold value to '+\
#                                  'process probabilistic forecast')
#                return

            # set thresholds for fcst and obs if prob
            fcst_thresh_list = var_info['fcst_thresh']
            obs_thresh_list = var_info['obs_thresh']

        fcst_field_list = self.get_field_info(v_name=var_info['fcst_name'],
                                              v_level=var_info['fcst_level'],
                                              v_extra=var_info['fcst_extra'],
                                              v_thresh=fcst_thresh_list,
                                              d_type='FCST')

        obs_field_list = self.get_field_info(v_name=var_info['obs_name'],
                                             v_level=var_info['obs_level'],
                                             v_extra=var_info['obs_extra'],
                                             v_thresh=obs_thresh_list,
                                             d_type='OBS')

        if fcst_field_list is None or obs_field_list is None:
            return

        # loop through fields and call MODE
        for fcst_field, obs_field in zip(fcst_field_list, obs_field_list):
            self.param = self.c_dict['CONFIG_FILE']
            if self.param == '':
                self.logger.error('Must set MODE_CONFIG_FILE to run MODE')
                return

            self.create_and_set_output_dir(time_info)
            self.infiles.append(model_path)
            self.infiles.append(obs_path)
            self.add_merge_config_file()

            self.set_environment_variables(fcst_field,obs_field, var_info, time_info)
            cmd = self.get_command()
            if cmd is None:
                self.logger.error("Could not generate command")
                return
            self.build()
            self.clear()

if __name__ == "__main__":
    util.run_stand_alone("mode_wrapper", "MODE")
