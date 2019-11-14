METplus Configuration Glossary
===========================================================

.. glossary::
   :sorted:

   AAAAAA_THIS_IS_A_TEMPLATE
     Text goes here
    
     | *Used by:*
     | *Family:*
     | *Default:*

   [DEPRECATED] ANLY_ASCII_REGEX_LEAD
     Please use OBS_SERIES_ANALYSIS_LEAD_REGEX instead. The regular expression describing the analysis (obs) file name (in ASCII format) of the intermediate file generated when running a series_by_lead process.
    
     | *Used by:* SeriesByLead
     | *Family:* [regex_pattern]
     | *Default:*

   [DEPRECATED] ANLY_NC_TILE_REGEX
     Please use OBS_SERIES_ANALYSIS_NC_TILE_REGEX instead. The regular expression used to search the input files that are in netCDF format and used in the series_by_analysis process.

     | *Used by:* SeriesByLead, SeriesByInit
     | *Family:* [regex_pattern]
     | *Default:*

   OBS_SERIES_ANALYSIS_LEAD_REGEX
     The regular expression describing the analysis (obs) file name (in ASCII format) of the intermediate file generated when running a series_by_lead process.

     | *Used by:* SeriesByLead
     | *Family:* [regex_pattern]
     | *Default:*

   OBS_SERIES_ANALYSIS_NC_TILE_REGEX
     The regular expression used to search the input files that are in netCDF format and used in the series_by_analysis process.

     | *Used by:* SeriesByLead, SeriesByInit
     | *Family:* [regex_pattern]
     | *Default:*
   
   [DEPRECATED] ANLY_TILE_PREFIX
     Please use OBS_EXTRACT_TILES_PREFIX instead. The prefix to the filename for the analysis file that is created as part of a series_analysis process.
    
     | *Used by:* ExtractTiles, SeriesByLead
     | *Family:* [regex_pattern]
     | *Default:*
   
   [DEPRECATED] ANLY_TILE_REGEX
     No longer used. The regular expression for the analysis input file. The file is in GRIBv2 format.
    
     | *Used by:* SeriesByLead, SeriesByInit
     | *Family:* [regex_pattern]
     | *Default:*

   OBS_EXTRACT_TILES_PREFIX
     Prefix for observation tile files. Used to create filename of intermediate files that are created while performing a series analysis.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:* [regex_pattern]
     | *Default:*  Varies

   TESTING_SORTING_THIS_IS_FIRST_BUT_SHOULD_BE_LAST
     Testing
     
     | *Used by:*

   CYCLONE_INPUT_DIR
     Input directory for the cyclone plotter. This should be the output directory for the MET TC-Pairs utility

     | *Used by:* CyclonePlotter
     | *Family:* [dir]
     | *Default:* Varies

   OBS_REGRID_DATA_PLANE_RUN
     The value

   VALID_TIME_FMT
     The format of the valid time string

   ANOTHER_ONE
     Value

   ANOTHER_ONE
     Value

   TESTING2
     Value
     
   FCST_REGRID_DATA_PLANE_VAR<n>_OUTPUT_FIELD_NAME
     Specify the forecast output field name that is created by RegridDataPlane. The name corresponds to FCST_VAR<n>_NAME. This is used when using Python Embedding as input to the MET tool, because the FCST_VAR<n>_NAME defines the python script to call.
    
     | *Used by:* RegridDataPlane
     | *Family:* [config]
     | *Default:* None


   OBS_REGRID_DATA_PLANE_VAR<n>_OUTPUT_FIELD_NAME
     Specify the observation output field name that is created by RegridDataPlane. The name corresponds to OBS_VAR<n>_NAME. This is used when using Python Embedding as input to the MET tool, because the OBS_VAR<n>_NAME defines the python script to call.
    
     | *Used by:* RegridDataPlane
     | *Family:* [config]
     | *Default:* None

   LOG_ASCII2NC_VERBOSITY
     Overrides the log verbosity for Ascii2Nc only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None
     
   LOG_ENSEMBLE_STAT_VERBOSITY
     Overrides the log verbosity for EnsembleStat only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* EnsembleStat
     | *Family:* [config]
     | *Default:* None
     
   LOG_GRID_STAT_VERBOSITY
     Overrides the log verbosity for GridStat only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* GridStat
     | *Family:* [config]
     | *Default:* None
     
   LOG_MODE_VERBOSITY
     Overrides the log verbosity for Mode only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* Mode
     | *Family:* [config]
     | *Default:* None
     
   LOG_MTD_VERBOSITY
     Overrides the log verbosity for MTD only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* MTD
     | *Family:* [config]
     | *Default:* None
     
   LOG_PB2NC_VERBOSITY
     Overrides the log verbosity for PB2NC only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* PB2NC
     | *Family:* [config]
     | *Default:* None
     
   LOG_PCP_COMBINE_VERBOSITY
     Overrides the log verbosity for PcpCombine only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* PcpCombine
     | *Family:* [config]
     | *Default:* None
     
   LOG_POINT_STAT_VERBOSITY
     Overrides the log verbosity for PointStat only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* PointStat
     | *Family:* [config]
     | *Default:* None
     
   LOG_REGRID_DATA_PLANE_VERBOSITY
     Overrides the log verbosity for RegridDataPlane only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* RegridDataPlane
     | *Family:* [config]
     | *Default:* None
     
   LOG_TC_PAIRS_VERBOSITY
     Overrides the log verbosity for TcPairs only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* TcPairs
     | *Family:* [config]
     | *Default:* None
     
   LOG_TC_STAT_VERBOSITY
     Overrides the log verbosity for TcStat only. If not set, the verbosity level is controlled by LOG_MET_VERBOSITY.

     | *Used by:* TcStat
     | *Family:* [config]
     | *Default:* None

   LOG_LINE_FORMAT
     Defines the formatting of each METplus log output line. For more information on acceptable values, see the Python documentation for LogRecord: https://docs.python.org/3/library/logging.html#logging.LogRecord

     | *Used by:* All
     | *Family:* [config]
     | *Default:* %(asctime)s.%(msecs)03d %(name)s (%(filename)s:%(lineno)d) %(levelname)s: %(message)s

   LOG_LINE_DATE_FORMAT
     Defines the formatting of the date in the METplus log output. See LOG_LINE_FORMAT.

     | *Used by:* All
     | *Family:* [config]
     | *Default:* %m/%d %H:%M:%S

   FCST_PCP_COMBINE_COMMAND
     Used only when FCST_PCP_COMBINE_METHOD = CUSTOM. Custom command to run PcpCombine with a complex call that doesn't fit common use cases. Value can include filename template syntax, i.e. {valid?fmt=%Y%m%d}, that will be substituted based on the current runtime. The name of the application and verbosity flag does not need to be included. For example, if set to '-derive min,max /some/file' the command run will be pcp_combine -v 2 -derive min,max /some/file. A corresponding variable exists for observation data called OBS_PCP_COMBINE_COMMAND.

     | *Used by:* PcpCombine
     | *Family:* [config]
     | *Default:* None
     
   OBS_PCP_COMBINE_COMMAND
     Used only when OBS_PCP_COMBINE_METHOD = CUSTOM. Custom command to run PcpCombine with a complex call that doesn't fit common use cases. Value can include filename template syntax, i.e. {valid?fmt=%Y%m%d}, that will be substituted based on the current runtime. The name of the application and verbosity flag does not need to be included. For example, if set to '-derive min,max /some/file' the command run will be pcp_combine -v 2 -derive min,max /some/file. A corresponding variable exists for forecast data called FCST_PCP_COMBINE_COMMAND.

     | *Used by:* PcpCombine
     | *Family:* [config]
     | *Default:* None
     
   CUSTOM_INGEST_<n>_SCRIPT
     Used to use Python embedding to process multiple files. <n> is an integer greater than or equal to 1. Specifies the python script with arguments to run through RegridDataPlane to generate a file that can be read by the MET tools. This variable supports filename template syntax, so you can specify filenames with time information, i.e. {valid?fmt=%Y%m%d}. See also CUSTOM_INGEST<n>_TYPE, CUSTOM_INGEST<n>_OUTPUT_GRID, CUSTOM_INGEST<n>_OUTPUT_TEMPLATE, and CUSTOM_INGEST<n>_OUTPUT_DIR.

     | *Used by:* CustomIngest
     | *Family:* [config]
     | *Default:* None

   CUSTOM_INGEST_<n>_TYPE
     Used to use Python embedding to process multiple files. <n> is an integer greater than or equal to 1. Specifies the type of output generated by the Python script. Valid options are NUMPY, XARRAY, and PANDAS. See also CUSTOM_INGEST<n>_SCRIPT, CUSTOM_INGEST<n>_OUTPUT_GRID, CUSTOM_INGEST<n>_OUTPUT_TEMPLATE, and CUSTOM_INGEST<n>_OUTPUT_DIR.

     | *Used by:* CustomIngest
     | *Family:* [config]
     | *Default:* None

   CUSTOM_INGEST_<n>_OUTPUT_GRID
     Used to use Python embedding to process multiple files. <n> is an integer greater than or equal to 1. Specifies the grid information that RegridDataPlane will use to generate a file that can be read by the MET tools. This can be a file path or a grid definition. See the MET User's Guide section regarding Regrid-Data-Plane for more information. See also CUSTOM_INGEST<n>_TYPE, CUSTOM_INGEST<n>_SCRIPT, CUSTOM_INGEST<n>_OUTPUT_TEMPLATE, and CUSTOM_INGEST<n>_OUTPUT_DIR.

     | *Used by:* CustomIngest
     | *Family:* [config]
     | *Default:* None

   CUSTOM_INGEST_<n>_OUTPUT_TEMPLATE
     Used to use Python embedding to process multiple files. <n> is an integer greater than or equal to 1. Specifies the output filename using filename template syntax. The value will be substituted with time information and appended to CUSTOM_INGEST_<n>_OUTPUT_DIR if it is set. See also CUSTOM_INGEST<n>_TYPE, CUSTOM_INGEST<n>_SCRIPT, and CUSTOM_INGEST<n>_OUTPUT_GRID.

     | *Used by:* CustomIngest
     | *Family:* [filename_templates]
     | *Default:* None

   CUSTOM_INGEST_<n>_OUTPUT_DIR
     Used to use Python embedding to process multiple files. <n> is an integer greater than or equal to 1. Specifies the output diirectory to write data. See also CUSTOM_INGEST<n>_TYPE, CUSTOM_INGEST<n>_SCRIPT, and CUSTOM_INGEST<n>_OUTPUT_GRID, and CUSTOM_INGEST_<n>_OUTPUT_TEMPLATE.

     | *Used by:* CustomIngest
     | *Family:* [dir]
     | *Default:* None

   ASCII2NC_CONFIG_FILE
     Path to optional configuration file read by Ascii2Nc.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_INPUT_FORMAT
     Optional string to specify the format of the input data. Valid options are "met_point", "little_r", "surfrad", "wwsis", "aeronet", "aeronetv2", or "aeronetv3."

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_MASK_GRID
     Named grid or a data file defining the grid for filtering the point observations spatially (optional).

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_MASK_POLY
     A polyline file, the output of gen_vx_mask, or a gridded data file with field information for filtering the point observations spatially (optional).

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_MASK_SID
     A station ID masking file or a comma-separated list of station ID's for filtering the point observations spatially (optional).

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_INPUT_DIR
     Directory containing input data to Ascii2Nc. This variable is optional because you can specify the full path to the input files using ASCII2NC_INPUT_TEMPLATE.

     | *Used by:* Ascii2Nc
     | *Family:* [dir]
     | *Default:* None

   ASCII2NC_INPUT_TEMPLATE
     Filename template of the input file used by Ascii2Nc. See also ASCII2NC_INPUT_DIR.

     | *Used by:* Ascii2Nc
     | *Family:* [filename_templates]
     | *Default:* None

   ASCII2NC_OUTPUT_DIR
     Directory to write output data generated by Ascii2Nc. This variable is optional because you can specify the full path to the output files using ASCII2NC_OUTPUT_TEMPLATE.

     | *Used by:* Ascii2Nc
     | *Family:* [dir]
     | *Default:* None

   ASCII2NC_OUTPUT_TEMPLATE
     Filename template of the output file generated by Ascii2Nc. See also ASCII2NC_OUTPUT_DIR.

     | *Used by:* Ascii2Nc
     | *Family:* [filename_templates]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_FLAG
     Boolean value to turn on/off time summarization. Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* False

   ASCII2NC_TIME_SUMMARY_RAW_DATA
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_BEG
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_END
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_STEP
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_WIDTH
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_GRIB_CODES
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_VAR_NAMES
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_TYPES
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_VALID_FREQ
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_TIME_SUMMARY_VALID_THRESH
     Read by the Ascii2Nc configuration file if specified by ASCII2NC_CONFIG_FILE. See the MET User's Guide section regarding Ascii2Nc configuration files for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   ASCII2NC_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if an Ascii2Nc input file should be used for processing. Overrides OBS_FILE_WINDOW_BEGIN. See 'Use Windows to Find Valid Files' section for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* 0

   ASCII2NC_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if an Ascii2Nc input file should be used for processing. Overrides OBS_FILE_WINDOW_BEGIN. See 'Use Windows to Find Valid Files' section for more information.

     | *Used by:* Ascii2Nc
     | *Family:* [config]
     | *Default:* None

   CLIMO_GRID_STAT_INPUT_DIR
     Directory containing the climatology file used by GridStat. This variable is optional because you can specify the full path to a climatology file using CLIMO_GRID_STAT_INPUT_TEMPLATE.

     | *Used by:* GridStat
     | *Family:* [dir]
     | *Default:* None

   CLIMO_GRID_STAT_INPUT_TEMPLATE
     Filename template of the climatology file used by GridStat. See also CLIMO_GRID_STAT_INPUT_DIR.

     | *Used by:* GridStat
     | *Family:* [filename_templates]
     | *Default:* None

   CLIMO_POINT_STAT_INPUT_DIR
     Directory containing the climatology file used by PointStat. This variable is optional because you can specify the full path to a climatology file using CLIMO_POINT_STAT_INPUT_TEMPLATE.

     | *Used by:* PointStat
     | *Family:* [dir]
     | *Default:* None

   CLIMO_POINT_STAT_INPUT_TEMPLATE
     Filename template of the climatology file used by PointStat. See also CLIMO_POINT_STAT_INPUT_DIR.

     | *Used by:* PointStat
     | *Family:* [filename_templates]
     | *Default:* None

   [DEPRECATED] ADECK_FILE_PREFIX
     Please use TC_PAIRS_ADECK_TEMPLATE..

     | *Used by:*  TcPairs
     | *Family:* [config]
     | *Default:*  Varies

   [DEPRECATED] ADECK_TRACK_DATA_DIR
     Please use TC_PAIRS_ADECK_INPUT_DIR.

     | *Used by:*  TcPairs
     | *Family:* [dir]
     | *Default:*  Varies

   [DEPRECATED] AMODEL
     Please use TC_STAT_AMODEL.

     | *Used by:*  CyclonePlotter, TcStat
     | *Family:* [config]
     | *Default:* 

   SERIES_ANALYSIS_BACKGROUND_MAP
     Control whether or not a background map shows up for series analysis plots. Set to 'yes' if background map desired.

     | *Used by:*  SeriesByLead, SeriesByInit
     | *Family:*  [config]
     | *Default:*  no

   [DEPRECATED] BACKGROUND_MAP
     Please use SERIES_ANALYSIS_BACKGROUND_MAP instead.

     | *Used by:*  SeriesByLead, SeriesByInit
     | *Family:*  [config]
     | *Default:*  no

   [DEPRECATED] BASIN
     Please use TC_PAIRS_BASIN or TC_STAT_BASIN.

     | *Used by:*  TcPairs, TcStat
     | *Family:* [config]
     | *Default:*  Varies

   [DEPRECATED] BDECK_FILE_PREFIX
     Please use TC_PAIRS_BDECK_TEMPLATE.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] BDECK_TRACK_DATA_DIR
     Please use TC_PAIRS_BDECK_INPUT_DIR.

     | *Used by:*  TcPairs
     | *Family:* [dir]
     | *Default:*  Varies

   [DEPRECATED] BEG_TIME
     Please use INIT_BEG or VALID_BEG instead. Beginning time for analysis in YYYYMMDD format.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] BMODEL
     Please use TC_STAT_BMODEL.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:* 

   CI_METHOD
     The method for creating confidence intervals. Valid options are EMC, or NONE.

     | *Used by:*  MakePlots
     | *Family:*  [config]
     | *Default:* 

   CIRCLE_MARKER_SIZE
     Control the size of the circle marker in the cyclone plotter.

     | *Used by:*  CyclonePlotter
     | *Family:*  [config]
     | *Default:*  41

   CLOCK_TIME
     Automatically set by METplus with the time that the run was started. Setting this variable has no effect as it will be overwritten. Can be used for reference in metplus_final.conf or used with other config variables.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Set automatically to current clock time in %Y%m%d%H%M%S format

   CONFIG_DIR
     Directory containing config files relevant to MET tools.

     | *Used by:*  EnsembleStat, GridStat, Mode, StatAnalysis
     | *Family:*  [dir]
     | *Default:*  Varies

   CONFIG_FILE
     Specific configuration file name to use for MET tools.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   CONVERT
     Path to the ImageMagickconvert executable.

     | *Used by:*  PB2NC, PointStat, SeriesByInit, SeriesByLead
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] CONVERT_EXE
     Please use CONVERT.

     | *Used by:*  PB2NC, PointStat, SeriesByInit, SeriesByLead
     | *Family:*  [exe]
     | *Default:*  /path/to

   COV_THRESH
     Specify the values of the COV_THRESH column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   CROSS_MARKER_SIZE
     Control the size of the cross marker in the cyclone plotter.

     | *Used by:*  CyclonePlotter
     | *Family:*  [config]
     | *Default:*  51

   CUT
     Path to the Linuxcut executable.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] CUT_EXE
     Please use CUT.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] CYCLONE
     Please use TC_PAIRS_CYCLONE or TC_STAT_CYCLONE..

     | *Used by:*  TcPairs, TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   CYCLONE_INIT_DATE
     Initialization date for the cyclone forecasts in YYYYMMDD format.

     | *Used by:*  CyclonePlotter
     | *Family:*  [config]
     | *Default:*  Varies

   CYCLONE_INIT_HR
     Initialization hour for the cyclone forecasts in HH format.

     | *Used by:*  CyclonePlotter
     | *Family:*  [config]
     | *Default:*  Varies

   CYCLONE_INPUT_DIR
     Input directory for the cyclone plotter. This should be the output directory for the MET TC Pairs utility.

     | *Used by:*  CyclonePlotter
     | *Family:* [dir]
     | *Default:* Varies

   CYCLONE_MODEL
     Define the model being used for the tropical cyclone forecasts.

     | *Used by:*  CyclonePlotter
     | *Family:*  [config]
     | *Default:*  Varies

   CYCLONE_OUT_DIR
     Specify the directory where the output from the cyclone plotter should go.

     | *Used by:*  CyclonePlotter
     | *Family:*  [dir]
     | *Default:*  Varies

   CYCLONE_PLOT_TITLE
     Title string for the cyclone plotter.

     | *Used by:*  CyclonePlotter
     | *Family:*  [config]
     | *Default:*  Varies

   DEMO_YR
     The demo year. This is an optional value used by the plot_TCMPR.R script, (which is wrapped by TCMPRPlotter). Please refer to Chapter 21 in the MET User's Guide for more details.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   DEP_VARS
     Corresponds to the optional flag -dep in the plot_TCMPR.R script, which is wrapped by TCMPRPlotter. The value to this flag is a comma-separated list (no whitespace) of dependent variable columns to plot ( e.g. AMSLP-BMSLP, AMAX_WIND-BMAX_WIND, TK_ERR). If this is undefined, then the default plot for TK_ERR (track error) is generated. Note, if you want the track error plot generated, in addition to other plots, then you need to explicitly list this with the other variables. Please refer to Chapter 21 in the MET User's Guide for more details.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   DESC
     A single value or list of values used in the stat_analysis data stratification. Specifies the values of the DESC column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] DLAND_FILE
     Please use TC_PAIRS_DLAND_FILE.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:* Varies

   EXTRACT_TILES_DLAT
     The value that defines the resolution of the data (in decimal degrees).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  0.5

   EXTRACT_TILES_DLON
     The longitude value, in degrees. Set to the value that defines the resolution of the data (in decimal degrees).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  0.5

   [DEPRECATED] DLAT
     Please use EXTRACT_TILES_DLAT instead. The value that defines the resolution of the data (in decimal degrees).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  0.5

   [DEPRECATED] DLON
     Please use EXTRACT_TILES_DLON instead. The longitude value, in degrees. Set to the value that defines the resolution of the data (in decimal degrees).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  0.5

   EXTRACT_TILES_PAIRS_INPUT_DIR
     Directory containing matched pairs input to be read by ExtractTiles.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [dir]
     | *Default:*

   DO_NOT_RUN_EXE
     True/False. If True, applications will not run and will only output command that would have been called.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  False

   [DEPRECATED] END_DATE
     Please use INIT_END or VALID_END instead.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] END_HOUR
     Ending hour for analysis with format HH.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] END_TIME
     Ending date string for analysis with format YYYYMMDD.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   ENSEMBLE_STAT_CONFIG_FILE
     Specify the absolute path to the configuration file for the MET ensemble_stat tool.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* 

   ENSEMBLE_STAT_ENS_THRESH
     Threshold for the ratio of the number of valid ensemble fields to the total number of expected ensemble members. This value is passed into the ensemble_stat config file to make sure the percentage of files that are valid meets the expectation.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  1.0

   ENSEMBLE_STAT_GRID_VX
     Used to set the regrid dictionary item 'to_grid' in the MET ensemble_stat config file. See the MET User's Guide for more information.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* FCST

   ENSEMBLE_STAT_MET_OBS_ERROR_TABLE     

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* 

   ENSEMBLE_STAT_N_MEMBERS
     Expected number of ensemble members found. This should correspond to the number of items in FCST_ENSEMBLE_STAT_INPUT_TEMPLATE. If this number differs from the number of files are found for a given run, then ensemble_stat will not run for that time.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* 

   ENSEMBLE_STAT_ONCE_PER_FIELD
     If True, run ensemble_stat separately for each field name/level combination specified in the configuration file. Seereference "sec:SC_Field_Info" for more information on how fields are specified. If False, run ensemble_stat once with all of the fields specified.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  False

   ENSEMBLE_STAT_OUTPUT_DIR
     Specify the output directory where files from the MET ensemble_stat tool are written.

     | *Used by:*  EnsembleStat
     | *Family:*  [dir]
     | *Default:*  Varies

   ENSEMBLE_STAT_OUTPUT_TEMPLATE
     Sets the subdirectories below ENSEMBLE_STAT_OUTPUT_DIR using a template to allow run time information. If LOOP_BY = VALID, default value is valid time YYYYMMDDHHMM/ensemble_stat. If LOOP_BY = INIT, default value is init time YYYYMMDDHHMM/ensemble_stat.

     | *Used by:*  EnsembleStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   ENS_VAR<n>_LEVELS
     Define the levels for the <n>th ensemble variable to be used in the analysis where <n> is an integer >= 1. The value can be a single item or a comma separated list of items. You can define NetCDF levels, such as (0,*,*), but you will need to surround these values with quotation marks so that the commas in the item are not interpreted as an item delimeter. Some examples:

     ENS_VAR1_LEVELS = A06, P500
     ENS_VAR2_LEVELS ="(0,*,*)", "(1,*,*)"

     There can be <n> number of these variables defined in configuration files, simply increment the VAR1_ string to match the total number of variables being used, e.g.:

     ENS_VAR1_LEVELS
     ENS_VAR2_LEVELS
     ...
     ENS_VAR<n>_LEVELS

     See reference *REF*(SC_Field_Info) for more information.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  Varies

   ENS_VAR<n>_NAME
     Define the name for the <n>th ensemble variable to be used in the analysis where <n> is an integer >= 1. There can be <n> number of these variables defined in configuration files, simply increment the VAR1_ string to match the total number of variables being used, e.g.:

     ENS_VAR1_NAME
     ENS_VAR2_NAME
     ...
     ENS_VAR<n>_NAME
     
     See reference *REF*(SC_Field_Info) for more information.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  Varies

   ENS_VAR<n>_OPTIONS
     Define the options for the <n>th ensemble variable to be used in the analysis where <n> is an integer >= 1. These addition options will be applied to every name/level/threshold combination for VAR<n>. There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     ENS_VAR1_OPTIONS
     ENS_VAR2_OPTIONS
     ...
     ENS_VAR<n>_OPTION
 
     See reference *REF*(sec:SC_Field_Info) for more information.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  Varies

   ENS_VAR<n>_THRESH
     Define the threshold(s) for the <n>th ensemble variable to be used in the analysis where <n> is an integer >= 1. The value can be a single item or a comma separated list of items that must start with a comparison operator (>,>=,==,!=,<,<=,gt,ge,eq,ne,lt,le). There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     ENS_VAR1_THRESH
     ENS_VAR2_THRESH
     ...
     ENS_VAR<n>_THRESH
     
     See reference *REF*"sec:SC_Field_Info" for more information.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  Varies

   EVENT_EQUALIZATION
     If event equalization is to be used (True) or not (False). If set to True, if any of the listed models are missing data for a particular time, data for all models will be masked out for this time. If set to False, there are no changes to the data.

     | *Used by:*  MakePlots
     | *Family:*  [config]
     | *Default:*  True

   [DEPRECATED] EXTRACT_OUT_DIR
     Please use EXTRACT_TILES_OUTPUT_DIR. Set the output directory for the METplus extract_tiles utility.

     | *Used by:*  ExtractTiles, SeriesByInit, SeriesByLead
     | *Family:*  [dir]
     | *Default:*  Varies

   EXTRACT_TILES_FILTER_OPTS
     Control what options are passed to the METplus extract_tiles utility.

     | *Used by:*  ExtractTiles
     | *Family:*  [config]
     | *Default:*  Varies

   EXTRACT_TILES_OUTPUT_DIR
     Set the output directory for the METplus extract_tiles utility.

     | *Used by:*  ExtractTiles, SeriesByInit, SeriesByLead
     | *Family:*  [dir]
     | *Default:*  Varies

   EXTRACT_TILES_VAR_LIST
     Control what variables the METplus extract_tiles utility runs on. Additional filtering by summary (via the MET tc_stat tool). Please refer to Chapter 20 in the MET Users Guide (TC-STAT Tools) for all the available options for filtering by summary method in tc-stat. If no additional filtering is required, simply leave the value to EXTRACT_TILES_FILTER_OPTS blank/empty in the METplus configuration file.

     | *Used by:*  ExtractTiles
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_EXACT_VALID_TIME
     No longer used. Please use FCST_WINDOW_BEGIN and FCST_WINDOW_END instead. If both of those variables are set to 0, the functionality is the same as FCST_EXACT_VALID_TIME = True.

     | *Used by:*  GridStat Mode, MTD
     | *Family:*  [config]
     | *Default:*  False

   [DEPRECATED] FCST_<n>_FIELD_NAME
     Please use FCST_PCP_COMBINE_<n>_FIELD_NAME where N >=1 instead.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_ASCII_REGEX_LEAD
     Please use FCST_SERIES_ANALYSIS_LEAD_REGEX instead. Regular expression used to find the forecast file (ASCII format) generated as an intermediate step in the series by lead use case.

     | *Used by:*  SeriesByLead
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   FCST_SERIES_ANALYSIS_LEAD_REGEX
     Regular expression used to find the forecast file (ASCII format) generated as an intermediate step in the series by lead use case.

     | *Used by:*  SeriesByLead
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   FCST_ENSEMBLE_STAT_FILE_WINDOW_BEGIN
     See OBS_ENSEMBLE_STAT_FILE_WINDOW_BEGIN *REF* "sec:SC_O" 

     | *Used by:* 
     | *Family:* 
     | *Default:* OBS_FILE_WINDOW_BEGIN

   FCST_ENSEMBLE_STAT_FILE_WINDOW_END
     See OBS_ENSEMBLE_STAT_FILE_WINDOW_ENDreference "sec:SC_O".

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   FCST_ENSEMBLE_STAT_INPUT_DIR
     Input directory for forecast files to use with the MET tool ensemble_stat. A corresponding variable exists for observation data called OBS_ENSEMBLE_STAT_INPUT_DIR.

     | *Used by:*  EnsembleStat
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_ENSEMBLE_STAT_INPUT_TEMPLATE
     Template used to specify forecast input filenames for the MET tool ensemble_stat. A corresponding variable exists for observation data called OBS_ENSEMBLE_STAT_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  EnsembleStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_FILE_WINDOW_BEGIN
     See OBS_FILE_WINDOW_BEGINreference "sec:SC_O".

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_FILE_WINDOW_END
     See OBS_FILE_WINDOW_ENDreference "sec:SC_O".

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_GEMPAK_INPUT_DIR
     Input directory for GEMPAK formatted forecast files. Use GEMPAKTOCF_INPUT_DIR if GempakToCF is in the PROCESS_LIST.

     | *Used by:*  GempakToCF
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] FCST_GEMPAK_TEMPLATE
     Template used to specify input filenames for GEMPAK formatted forecast files. Use GEMPAKTOCF_INPUT_TEMPLATE if GempakToCF is in the PROCESS_LIST.

     | *Used by:*  GempakToCF
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_GRID_STAT_FILE_WINDOW_BEGIN
     See OBS_GRID_STAT_FILE_WINDOW_BEGINreference "sec:SC_O".

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* FCST_FILE_WINDOW_BEGIN

   FCST_GRID_STAT_FILE_WINDOW_END
     See OBS_GRID_STAT_FILE_WINDOW_ENDreference "sec:SC_O".

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* FCST_FILE_WINDOW_END

   FCST_GRID_STAT_INPUT_DATATYPE
     Specify the data type of the input directory for forecast files used with the MET grid_stat tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF. A corresponding variable exists for observation data called OBS_GRID_STAT_INPUT_DATATYPE.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_GRID_STAT_INPUT_DIR
     Input directory for forecast files to use with the MET tool grid_stat. A corresponding variable exists for observation data called OBS_GRID_STAT_INPUT_DIR.

     | *Used by:*  GridStat
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_GRID_STAT_INPUT_TEMPLATE
     Template used to specify forecast input filenames for the MET tool grid_stat. A corresponding variable exists for observation data called OBS_GRID_STAT_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  GridStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_GRID_STAT_PROB_THRESH
     Threshold values to be used for probabilistic data in grid_stat. The value can be a single item or a comma separated list of items that must start with a comparison operator (>,>=,==,!=,<,<=,gt,ge,eq,ne,lt,le). A corresponding variable exists for observation data called OBS_GRID_STAT_PROB_THRESH.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:*  ==0.1

   [DEPRECATED] FCST_HR_END
     Please use LEAD_SEQ instead.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:* 

   [DEPRECATED] FCST_HR_INTERVAL
     Please use LEAD_SEQ instead.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:* 

   [DEPRECATED] FCST_HR_START
     Please use LEAD_SEQ instead.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:* 

   [DEPRECATED] FCST_INIT_INTERVAL
     Specify the stride for forecast initializations.

     | *Used by:*  EnsembleStat, GridStat, Mode
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_INPUT_DIR_REGEX
     Please use FCST_POINT_STAT_INPUT_DIR instead.

     | *Used by:*  PointStat
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] FCST_INPUT_DIR
     Specify the input directory for the forecast files. Use FCST_[MET-APP]_INPUT_DIR instead, i.e. FCST_GRID_STAT_INPUT_DIR

     | *Used by:*  GridStat, Mode, PointStat, PcpCombine
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] FCST_INPUT_FILE_REGEX
     Regular expression to use when identifying which forecast file to use.

     | *Used by:*  PointStat
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] FCST_INPUT_FILE_TMPL
     Please use FCST_POINT_STAT_INPUT_TEMPLATE instead.

     | *Used by:*  PointStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] FCST_IS_DAILY_FILE
     Please use FCST_PCP_COMBINE_IS_DAILY_FILE instead.Acceptable values: true/false

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  False

   FCST_IS_PROB
     Specify whether the forecast data are probabilistic or not.Acceptable values: true/false

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PointStat
     | *Family:*  [config]
     | *Default:*  False

   FCST_LEAD
     Specify the values of the FCST_LEAD column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_LEVEL
     Please use FCST_PCP_COMBINE_INPUT_ACCUMS instead.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_MAX_FORECAST
     Please use LEAD_SEQ_MAX instead. Specify the maximum forecast lead time to use for the analysis.

     | *Used by:*  EnsembleStat, GridStat, Mode
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_MODE_CONV_RADIUS
     Comma separated list of convolution radius values used by mode for forecast fields. A corresponding variable exists for observation data called OBS_MODE_CONV_RADIUS.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   FCST_MODE_CONV_THRESH
     Comma separated list of convolution threshold values used by mode for forecast fields. A corresponding variable exists for observation data called OBS_MODE_CONV_THRESH.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   FCST_MODE_FILE_WINDOW_BEGIN
     See OBS_MODE_FILE_WINDOW_BEGINreference "sec:SC_O".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* FCST_FILE_WINDOW_BEGIN

   FCST_MODE_FILE_WINDOW_END
     See OBS_MODE_FILE_WINDOW_ENDreference "sec:SC_O".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* FCST_FILE_WINDOW_END

   FCST_MODE_MERGE_FLAG
     Sets the merge_flag value in the mode config file for forecast fields. Valid values are NONE, THRESH, ENGINE, and BOTH. A corresponding variable exists for observation data called OBS_MODE_MERGE_FLAG.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   FCST_MODE_MERGE_THRESH
     Comma separated list of merge threshold values used by mode for forecast fields. A corresponding variable exists for observation data called OBS_MODE_MERGE_THRESH.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   FCST_MODE_INPUT_DATATYPE
     Specify the data type of the input directory for forecast files used with the MET mode tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF. A corresponding variable exists for observation data called OBS_MODE_INPUT_DATATYPE.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_MODE_INPUT_DIR
     Input directory for forecast files to use with the MET tool mode. A corresponding variable exists for observation data called OBS_MODE_INPUT_DIR.

     | *Used by:*  Mode
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_MODE_INPUT_TEMPLATE
     Template used to specify forecast input filenames for the MET tool mode. A corresponding variable exists for observation data called OBS_MODE_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  Mode
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_MTD_CONV_RADIUS
     Comma separated list of convolution radius values used by mode-TD for forecast files. A corresponding variable exists for observation data called OBS_MTD_CONV_RADIUS.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:* 

   FCST_MTD_CONV_THRESH
     Comma separated list of convolution threshold values used by mode-TD for forecast files. A corresponding variable exists for observation data called OBS_MTD_CONV_THRESH.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:* 

   FCST_MTD_FILE_WINDOW_BEGIN
     See OBS_MTD_FILE_WINDOW_BEGINreference "sec:SC_O".

     | *Used by:* MTD
     | *Family:* [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   FCST_MTD_FILE_WINDOW_END
     See OBS_MTD_FILE_WINDOW_ENDreference "sec:SC_O".

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   FCST_MTD_INPUT_DATATYPE
     Specify the data type of the input directory for forecast files used with the MET mode-TD tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF. A corresponding variable exists for observation data called OBS_MTD_INPUT_DATATYPE.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_MTD_INPUT_DIR
     Input directory for forecast files to use with the MET tool mode-TD. A corresponding variable exists for observation data called OBS_MTD_INPUT_DIR.

     | *Used by:* MTD
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_MTD_INPUT_TEMPLATE
     Template used to specify forecast input filenames for the MET tool mode-TD. A corresponding variable exists for observation data called OBS_MTD_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:* MTD
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] FCST_NATIVE_DATA_TYPE
     Specify the data format of the forecast data. Use FCST_PCP_COMBINE_INPUT_DATATYPE instead

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FCST_NC_TILE_REGEX
     Please use FCST_SERIES_ANALYSIS_NC_TILE_REGEX instead. Define the regular expression for input forecast files that are in netCDF.

     | *Used by:*  SeriesByLead, SeriesByInit
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

  FCST_SERIES_ANALYSIS_NC_TILE_REGEX
     Define the regular expression for input forecast files that are in netCDF.

     | *Used by:*  SeriesByLead, SeriesByInit
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   FCST_PCP_COMBINE_<n>_FIELD_NAME
     This variable is used to define a <n> hour accumulation NetCDF field in the forecast dataset used in the MET tool pcp_combine. <n> must be an integer >= 1. A corresponding variable exists for observation data called OBS_PCP_COMBINE_<n>_FIELD_NAME.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_DATA_INTERVAL
     Specify the accumulation interval of the forecast dataset used by the MET pcp_combine tool when processing daily input files. A corresponding variable exists for observation data called OBS_PCP_COMBINE_DATA_INTERVAL.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_DERIVE_LOOKBACK
     Specify how far to look back in time in hours to find files for running the MET pcp_combine tool in derive mode. A corresponding variable exists for observation data called OBS_PCP_COMBINE_DERIVE_LOOKBACK.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* Varies

   FCST_PCP_COMBINE_INPUT_DATATYPE
     Specify the data type of the input directory for forecast files used with the MET pcp_combine tool. Currently valid options are NETCDF, GRIB, and GEMPAK. Required by pcp_combine if FCST_PCP_COMBINE_RUN is True. Replaces deprecated variable FCST_NATIVE_DATA_TYPE. A corresponding variable exists for observation data called OBS_PCP_COMBINE_INPUT_DATA_TYPE.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_INPUT_DIR
     Specify the input directory for forecast files used with the MET pcp_combine tool. A corresponding variable exists for observation data called OBS_PCP_COMBINE_INPUT_DIR.

     | *Used by:*  PcpCombine
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] FCST_PCP_COMBINE_INPUT_LEVEL
     Please use FCST_PCP_COMBINE_INPUT_ACCUMS.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_INPUT_TEMPLATE
     Template used to specify input filenames for forecast files used by the MET pcp_combine tool. A corresponding variable exists for observation data called OBS_PCP_COMBINE_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  PcpCombine
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_PCP_COMBINE_IS_DAILY_FILE
     Specify whether the forecast file is a daily file or not. A corresponding variable exists for observation data called OBS_PCP_COMBINE_IS_DAILY_FILE.Acceptable values: true/false

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  False

   FCST_PCP_COMBINE_METHOD
     Specify the method to be used with the MET pcp_combine tool processing forecast data.Valid options are ADD, SUM, SUBTRACT, DERIVE, and CUSTOM. A corresponding variable exists for observation data called OBS_PCP_COMBINE_METHOD.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* None

   FCST_PCP_COMBINE_MIN_FORECAST
     Specify the minimum forecast lead time to use when finding the lowest forecast lead to use in pcp_combine. A corresponding variable exists for observation data called OBS_PCP_COMBINE_MIN_FORECAST.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_MAX_FORECAST
     Specify the maximum forecast lead time to use when finding the lowest forecast lead to use in pcp_combine. A corresponding variable exists for observation data called OBS_PCP_COMBINE_MAX_FORECAST.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_OUTPUT_DIR
     Specify the output directory for forecast files generated by the MET pcp_combine tool. A corresponding variable exists for observation data called OBS_PCP_COMBINE_OUTPUT_DIR.

     | *Used by:*  PcpCombine
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_PCP_COMBINE_OUTPUT_TEMPLATE
     Template used to specify output filenames for forecast files generated by the MET pcp_combine tool. A corresponding variable exists for observation data called OBS_PCP_COMBINE_OUTPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  PcpCombine
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_PCP_COMBINE_RUN
     Specify whether to run the MET pcp_combine tool on forecast data or not. A corresponding variable exists for observation data called OBS_PCP_COMBINE_RUN.Acceptable values: true/false

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_STAT_LIST
     List of statistics to process when using the MET pcp_combine tool on forecast data in derive mode. A corresponding variable exists for observation data called OBS_PCP_COMBINE_STAT_LIST.Acceptable values: sum, min, max, range, mean, stdev, vld_count

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_TIMES_PER_FILE
     Specify the number of accumulation intervals of the forecast dataset used by the MET pcp_combine tool when processing daily input files. A corresponding variable exists for observation data called OBS_PCP_COMBINE_TIMES_PER_FILE.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* 

   FCST_POINT_STAT_FILE_WINDOW_BEGIN
     See OBS_POINT_STAT_FILE_WINDOW_BEGINreference "sec:SC_O".

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:* FCST_FILE_WINDOW_BEGIN

   FCST_POINT_STAT_FILE_WINDOW_END
     See OBS_POINT_STAT_FILE_WINDOW_ENDreference "sec:SC_O".

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:* FCST_FILE_WINDOW_END

   FCST_POINT_STAT_INPUT_DATATYPE
     Specify the data type of the input directory for forecast files used with the MET point_stat tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF. A corresponding variable exists for observation data called OBS_POINT_STAT_INPUT_DATATYPE.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_POINT_STAT_INPUT_DIR
     Input directory for forecast files to use with the MET tool point_stat. A corresponding variable exists for observation data called OBS_POINT_STAT_INPUT_DIR.

     | *Used by:*  PointStat
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_POINT_STAT_INPUT_TEMPLATE
     Template used to specify forecast input filenames for the MET tool point_stat. A corresponding variable exists for observation data called OBS_POINT_STAT_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  GriPointStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_REGRID_DATA_PLANE_INPUT_DATATYPE
     Specify the data type of the input directory for forecast files used with the MET regrid_data_plane tool. Currently valid options are NETCDF, GRIB, and GEMPAK. Required by pcp_combine. A corresponding variable exists for observation data called OBS_REGRID_DATA_PLANE_INPUT_DATATYPE.

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_REGRID_DATA_PLANE_INPUT_DIR
     Specify the input directory for forecast files used with the MET regrid_data_plane tool. A corresponding variable exists for observation data called OBS_REGRID_DATA_PLANE_INPUT_DIR.

     | *Used by:*  RegridDataPlane
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_REGRID_DATA_PLANE_INPUT_TEMPLATE
     Template used to specify input filenames for forecast data used by the MET regrid_data_plane tool. It not set, METplus will use FCST_REGRID_DATA_PLANE_TEMPLATE. A corresponding variable exists for observation data called OBS_REGRID_DATA_PLANE_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  RegridDataPlane
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_REGRID_DATA_PLANE_OUTPUT_TEMPLATE
     Template used to specify output filenames for forecast data used by the MET regrid_data_plane tool. It not set, METplus will use FCST_REGRID_DATA_PLANE_TEMPLATE. A corresponding variable exists for observation data called OBS_REGRID_DATA_PLANE_OUTPUT_TEMPLATE.

     | *Used by:*  RegridDataPlane
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_REGRID_DATA_PLANE_TEMPLATE
     Template used to specify filenames for forecast data used by the MET regrid_data_plane tool. To specify different templates for input and output files , use FCST_REGRID_DATA_PLANE_INPUT_TEMPLATE and FCST_REGRID_DATA_PLANE_OUTPUT_TEMPLATE. A corresponding variable exists for observation data called OBS_REGRID_DATA_PLANE_TEMPLATE.

     | *Used by:*  RegridDataPlane
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   FCST_REGRID_DATA_PLANE_OUTPUT_DIR
     Specify the output directory for forecast files used with the MET regrid_data_plane tool. A corresponding variable exists for observation data called OBS_REGRID_DATA_PLANE_OUTPUT_DIR.

     | *Used by:*  RegridDataPlane
     | *Family:*  [dir]
     | *Default:*  Varies

   FCST_THRESH
     Specify the values of the FCST_THRESH column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   [DEPRECATED] FCST_TILE_PREFIX
     Please use FCST_EXTRACT_TILES_PREFIX instead. Prefix for forecast tile files. Used to create filename of intermediate files that are created while performing a series analysis.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:* [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] FCST_TILE_REGEX
     No longer used. Regular expression for forecast input files that are in GRIB2.

     | *Used by:*  SeriesByInit, SeriesByLead
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   FCST_EXTRACT_TILES_PREFIX
     Prefix for forecast tile files. Used to create filename of intermediate files that are created while performing a series analysis.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:* [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] FCST_VAR
     Define the name of the forecast variable to be used in the analysis. See FCST_VAR<n>_NAME, FCST_VAR<n>_LEVELS, FCST_VAR<n>_THRESH, and FCST_VAR<n>_OPTIONS where <n> = integer >= 1.

     | *Used by:*  EnsembleStat, MakePlots
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_VAR_LEVEL
     Specify the values of the FCST_VAR_LEVEL column in the MET .stat file to use.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_VAR_NAME
     Specify the values of the FCST_VAR_NAME column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_VAR<n>_LEVELS
     Define the levels for the <n>th forecast variable to be used in the analysis where <n> is an integer >= 1. The value can be a single item or a comma separated list of items. You can define NetCDF levels, such as (0,*,*), but you will need to surround these values with quotation marks so that the commas in the item are not interpreted as an item delimeter. Some examples:

     FCST_VAR1_LEVELS = A06, P500
     FCST_VAR2_LEVELS ="(0,*,*),(1,*,*)"

     There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     FCST_VAR1_LEVELS
     FCST_VAR2_LEVELS
     ...
     FCST_VAR<n>_LEVELS
     
     See reference "sec:SC_Field_Info" for more information.

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_VAR<n>_NAME
     Define the name for the <n>th forecast variable to be used in the analysis where <n> is an integer >= 1. If FCST_VAR<n>_NAME is not set but OBS_VAR<n>_NAME is, the same information will be used for both variables. There can be s<n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     FCST_VAR1_NAME
     FCST_VAR2_NAME
     ...
     FCST_VAR<n>_NAME
     
     See reference "sec:SC_Field_Info" for more information.

     This value can be set to a call to a python script with arguments to supply data to the MET tools via Python Embedding. Filename template syntax can be used here to specify time information of an input file, i.e. {valid?fmt=%Y%m%d%H}. See the MET User's Guide for more information about Python Embedding in the MET tools.

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_VAR<n>_OPTIONS
     Define the options for the <n>th forecast variable to be used in the analysis where <n> is an integer >= 1. These addition options will be applied to every name/level/threshold combination for VAR<n>. There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     FCST_VAR1_OPTIONS
     FCST_VAR2_OPTIONS
     ...
     FCST_VAR<n>_OPTIONS
     
     See reference "sec:SC_Field_Info" for more information.

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_VAR<n>_THRESH
     Define the threshold(s) for the <n>th forecast variable to be used in the analysis where <n> is an integer >= 1. The value can be a single item or a comma separated list of items that must start with a comparison operator (>,>=,==,!=,<,<=,gt,ge,eq,ne,lt,le). If FCST_VAR<n>_THRESH is not set but OBS_VAR<n>_THRESH is, the same information will be used for both variables. There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:
     FCST_VAR1_THRESH
     FCST_VAR2_THRESH
     ...
     FCST_VAR<n>_THRESH
     
     See reference "sec:SC_Field_Info" for more information.

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_WINDOW_BEGIN
     See OBS_WINDOW_BEGINreference "sec:SC_O".

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_WINDOW_END
     See OBS_WINDOW_ENDreference "sec:SC_O".

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   FHR_BEG
     Specify the first forecast lead time to use in the analysis. Use in combination with FHR_END and FHR_INC.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   FHR_END
     Specify the last forecast lead time to use in the analysis. Use in combination with FHR_BEG and FHR_INC.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   FHR_GROUP_BEG
     Define which forecast lead time should be first in a group of forecast leads to use in the analysis. Use in combination with FHR_GROUP_END and FHR_INC.Example:FHR_GROUP_BEG = 24FHR_GROUP_END = 42FHR_INC = 6List of forecast leads processed: [24, 30, 36, 42]

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   FHR_GROUP_END
     Define which forecast lead time should be the last in a group of forecast leads to use in the analysis. Use in combination with FHR_GROUP_BEG and FHR_INC.Example:FHR_GROUP_BEG = 24FHR_GROUP_END = 42FHR_INC = 6List of forecast leads processed: [24, 30, 36, 42]

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   FHR_GROUP_LABELS
     Label strings to use for the forecast groups.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   FHR_INC
     Stride to use for incrementing forecast lead times used in the analysis. Use in combination with FHR_BEG and FHR_END or FHR_GROUP_BEG and FHR_GROUP_END.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   FILTER
     Corresponds to the optional -filter argument to the plot_TCMPR.R script which is wrapped by TCMPRPlotter. This is a list of filtering options for the tc_stat tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   FILTERED_TCST_DATA_FILE
     Corresponds to the optional -tcst argument to the plot_TCMPR.R script which is wrapped by TCMPRPlotter. This is a tcst data file to be used instead of running the tc_stat tool. Indicate a full path to the data file.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   FOOTNOTE_FLAG
     This corresponds to the optional -footnote flag in the plot_TCMPR.R script which is wrapped by TCMPRPlotter. According to the plot_TCMPR.R usage, this flag is used to disable footnote (date).

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] FORECAST_TMPL
     Please use TC_PAIRS_ADECK_TEMPLATE.

     | *Used by:*  TcPairs
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   GEMPAKTOCF_CLASSPATH
     Path to the GempakToCF binary file and the NetCDF jar file required to run GempakToCF.

     | *Used by:*  GempakToCF
     | *Family:*  [exe]
     | *Default:*  Varies

   GEMPAKTOCF_INPUT_DIR
     Specify the input directory for the tool used to convert GEMPAK files to netCDF.

     | *Used by:*  GempakToCF
     | *Family:*  [dir]
     | *Default:*  Varies

   GEMPAKTOCF_INPUT_TEMPLATE
     Filename template used for input files to the tool used to convert GEMPAK files to netCDF.

     | *Used by:*  GempakToCF
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   GEMPAKTOCF_OUTPUT_DIR
     Specify the output directory for files generated by the tool used to convert GEMPAK files to netCDF.

     | *Used by:*  GempakToCF
     | *Family:*  [dir]
     | *Default:*  Varies

   GEMPAKTOCF_OUTPUT_TEMPLATE
     Filename template used for output files from the tool used to convert GEMPAK files to netCDF.

     | *Used by:*  GempakToCF
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   GEMPAKTOCF_SKIP_IF_OUTPUT_EXISTS
     If True, do not run GempakToCF if output file already exists. Set to False to overwrite files.

     | *Used by:*  GempakToCF
     | *Family:*  [config]
     | *Default:*  Varies

   GENERATE_TRACK_ASCII
     Specify whether or not to produce an ASCII file containing all of the tracks in the plot.Acceptable values: true/false

     | *Used by:*  CyclonePlotter
     | *Family:*  [conf]
     | *Default:*  Varies

   [DEPRECATED] GEN_SEQ

     | *Used by:* 
     | *Family:* 
     | *Default:* 

   FCST_EXTRACT_TILES_INPUT_TEMPLATE
     Filename template used to identify forecast input file to ExtractTiles.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_EXTRACT_TILES_INPUT_TEMPLATE
     Filename template used to identify observation input file to ExtractTiles.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] GFS_ANLY_FILE_TMPL
     Please use OBS_EXTRACT_TILES_INPUT_TEMPLATE instead. Filename template used to identify the GFS analysis file.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] GFS_FCST_FILE_TMPL
     Please use FCST_EXTRACT_TILES_INPUT_TEMPLATE instead.Filename templated used to identify the GFS forecast files.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [filename_templates]
     | *Default:*  Varies


   [DEPRECATED] GRID_STAT_CONFIG
     Please use GRID_STAT_CONFIG_FILE instead. Specify the absolute path to the configuration file used by the MET grid_stat tool.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* Varies

   GRID_STAT_CONFIG_FILE
     Specify the absolute path to the configuration file used by the MET grid_stat tool.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* Varies

   GRID_STAT_ONCE_PER_FIELD
     True/False. If True, grid_stat will run once to process all name/level/threshold combinations specified. If False, it will run once for each name/level. Some cases require this to be set to False, for example processing probablistic forecasts or precipitation accumulations.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* False

   [DEPRECATED] GRID_STAT_OUT_DIR
     Specify the output directory where files from the MET grid_stat tool are written. Please use GRID_STAT_OUTPUT_DIR instead.

     | *Used by:*  GridStat
     | *Family:*  [dir]
     | *Default:*  Varies

   GRID_STAT_OUTPUT_DIR
     Specify the output directory where files from the MET grid_stat tool are written.

     | *Used by:*  GridStat
     | *Family:*  [dir]
     | *Default:*  Varies

   GRID_STAT_OUTPUT_TEMPLATE
     Sets the subdirectories below GRID_STAT_OUTPUT_DIR using a template to allow run time information. If LOOP_BY = VALID, default value is valid time YYYYMMDDHHMM/grid_stat. If LOOP_BY = INIT, default value is init time YYYYMMDDHHMM/grid_stat.

     | *Used by:*  GridStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   GRID_STAT_VERIFICATION_MASK_TEMPLATE
     Template used to specify the verification mask filename for the MET tool grid_stat. Now supports a list of filenames.

     | *Used by:*  GridStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   HFIP_BASELINE
     Corresponds to the optional -hfip_bsln flag in the plot_TCMPR.R script which is wrapped by TCMPRPlotter. This is a string that indicates whether to add the HFIP baseline, and indicates the version (no, 0, 5, 10 year goal).

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_BEG
     Specify the beginning initialization time to be used in the analysis. Format can be controlled by INIT_TIME_FMT.Seereference "subsec:SC_Timing_Control_Looping-by-Initialization" for more information.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_END
     Specify the ending initialization time to be used in the analysis. Format can be controlled by INIT_TIME_FMT.Seereference "subsec:SC_Timing_Control_Looping-by-Initialization" for more information.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_EXCLUDE
     Specify which, if any, forecast initializations to exclude from the analysis.

     | *Used by:*  TcPairs, TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_HOUR_BEG
     Specify the beginning initialization hour to be used in the analysis. Format is HHMM.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_HOUR_END
     Specify the ending initialization hour to be used in the analysis. Format is HH or HHMM.

     | *Used by:*  ExtractTiles, MakePlots, StatAnalysis, TcPairs, TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_HOUR_INCREMENT
     Specify a time increment for valid times for use in the analysis. This is an integer defined in seconds.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_HOUR_METHOD
     Specify the method for the treatment of valid hours. Valid options are LOOP or GROUP. LOOP will consider the initialization hours individually, and GROUP will consider them as a whole.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_INCLUDE
     Specify which forecast initializations to include in the analysis.

     | *Used by:*  TcPairs, TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_INCREMENT
     Control the increment or stride to use when stepping between forecast initializations. Units are seconds.Seereference "subsec:SC_Timing_Control_Looping-by-Initialization" for more information. Units are assumed to be seconds unless specified with Y, m, d, H, M, or S.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_SEQ
     Specify a list of initialization hours that are used to build a sequence of forecast lead times to include in the analysis. Used only when looping by valid time (LOOP_BY = VALID). Comma separated list format, e.g.:0, 6, 12Seereference "subsec:SC_Timing_Control_Looping-over-Forecast" for more information.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PcpCombine, PointStat, RegridDataPlane, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   INIT_TIME_FMT
     Specify a formatting string to use for INIT_BEG and INIT_END.Seereference "subsec:SC_Timing_Control_Looping-by-Initialization" for more information.

     | *Used by:*  All
     | *Family:* 
     | *Default:* 

   INTERP
     Specify the interpolation used to create the MET .stat files. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   INTERP_PTS
     Corresponds to the interpolation in the MET .stat files. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   INTERVAL_TIME
     Define the interval time in hours (HH) to be used by the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   JOB_ARGS
     Specify stat_analysis job arguments to run. The job agruments that are to be run with the cooresponding JOB_NAME. If using -dump_row, use -dump_row [dump_row_filename]. If using -out_stat, -out_stat [out_stat_filename]. For more information on these job agruments, please see the MET Users Guide.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   JOB_NAME
     Specify stat_analysis job name to run. Valid options are filter, summary, aggregate, aggregate_stat, go_index, and ramp. For more information on these job names and what they do, please see the MET Users Guide.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   EXTRACT_TILES_LAT_ADJ
     Specify a latitude adjustment, in degrees to be used in the analysis. In the ExtractTiles wrapper, this corresponds to the 2m portion of the 2n x 2m subregion tile.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] LAT_ADJ
     Please use EXTRACT_TILES_LAT_ADJ instead. Specify a latitude adjustment, in degrees to be used in the analysis. In the ExtractTiles wrapper, this corresponds to the 2m portion of the 2n x 2m subregion tile.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD
     For CyclonePlotter, this refers to the column of interest in the input ASCII cyclone file.In the TCMPRPlotter, this corresponds to the optional -lead argument in the plot_TCMPR.R script (which is wrapped by TCMPRPlotter). This argument is set to a comma-separted list of lead times (h) to be plotted.In TcStat, this corresponds to the name of the column of interest in the input ASCII data file.

     | *Used by:*  CyclonePlotter, TCMPRPlotter, TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD_LIST
     Specify a list of forecast leads to include in the analysis. Comma separated list format, e.g.:0, 24, 48, 72, 96, 120

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD_SEQ
     Specify the sequence of forecast lead times to include in the analysis. Comma separated list format, e.g.:0, 6, 12Seereference "subsec:SC_Timing_Control_Looping-over-Forecast" for more information. Units are assumed to be hours unless specified with Y, m, d, H, M, or S.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PcpCombine, PointStat, RegridDataPlane, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD_SEQ_MIN
     Minimum forecast lead to be processed. Used primarily with INIT_SEQ but also affects LEAD_SEQ.Seereference "subsec:SC_Timing_Control_Looping-over-Forecast" for more information. Units are assumed to be hours unless specified with Y, m, d, H, M, or S.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PcpCombine, PointStat, RegridDataPlane, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD_SEQ_MAX
     Maximum forecast lead to be processed. Used primarily with INIT_SEQ but also affects LEAD_SEQ.Seereference "subsec:SC_Timing_Control_Looping-over-Forecast" for more information. Units are assumed to be hours unless specified with Y, m, d, H, M, or S.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PcpCombine, PointStat, RegridDataPlane, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD_SEQ_<n>
     Required when SERIES_BY_LEAD_GROUP_FCSTS=True. Not necessary otherwise. Specify the sequence of forecast lead times to include in the analysis. Comma separated list format, e.g.:0, 6, 12. <n> corresponds to the bin in which the user wishes to aggregate series by lead results.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   LEAD_SEQ_<n>_LABEL
     Required when SERIES_BY_LEAD_GROUP_FCSTS=True. Specify the label of the corresponding bin of series by lead results.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:* 

   LEGEND
     The text to be included in the legend of your plot.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   LINE_TYPE
     Specify the MET STAT line types to be considered. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:* 

   LOG_DIR
     Specify the directory where log files from MET and METplus should be written.

     | *Used by:*  All
     | *Family:*  [dir]
     | *Default:*  Varies

   LOG_LEVEL
     Specify the level of logging.Everything above this level is sent to standard output. To quiet the output to a comfortable level, set this to "ERROR"

     Options (ordered MOST verbose to LEAST verbose):
     NOTSET
     DEBUG
     INFO
     WARNING
     ERROR
     CRITICAL     

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   LOG_METPLUS
     Control the filename of the METplus log file. Control the timestamp appended to the filename with LOG_TIMESTAMP_TEMPLATE. To turn OFF all logging, do not set this option.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   LOG_MET_OUTPUT_TO_METPLUS
     Control whether logging output from the MET tools is sent to the METplus log file, or individual log files for each MET tool.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  yes/no

   LOG_MET_VERBOSITY
     Control the verbosity of the logging from the MET tools.0 = Least amount of logging (lowest verbosity)5 = Most amount of logging (highest verbosity)

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  2

   LOG_TIMESTAMP_TEMPLATE
     Set the timestamp template for the METplus log file. Use Python strftime directives, e.g.%Y%m%d for YYYYMMDD.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  %Y%m%d

   LOG_TIMESTAMP_USE_DATATIME
     True/False. Determines which time to use for the log filenames. If True, use INIT_BEG if LOOP_BY is INIT or VALID_BEG if LOOP_BY is VALID. If False, use current time.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:* False

   EXTRACT_TILES_LON_ADJ
     Specify a longitude adjustment, in degrees to be used in the analysis. In the ExtractTiles wrapper, this corresponds to the 2n portion of the 2n x 2m subregion tile.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] LON_ADJ
     Please use EXTRACT_TILES_LON_ADJ instead. Specify a longitude adjustment, in degrees to be used in the analysis. In the ExtractTiles wrapper, this corresponds to the 2n portion of the 2n x 2m subregion tile.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   LOOP_BY
     Control whether the analysis is processed across valid or initialization times.Seereference "subsec:SC_Timing_Control_LOOP_BY" for more information.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  true

   [DEPRECATED] LOOP_BY_INIT
     Please use LOOP_BY instead.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  true

   LOOP_ORDER
     Control the looping order for METplus. Valid options are "times" or "processes". "times" runs all items in the PROCESS_LIST for a single run time, then repeat until all times have been evaluated. "processes" runs each item in the PROCESS_LIST for all times specified, then repeat for the next item in the PROCESS_LIST.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   METPLUS_BASE
     This variable will automatically be set by METplus when it is started. It will be set to the location of METplus that is currently being run. Setting this variable in a config file will have no effect and will report a warning that it is being overridden.

     | *Used by:*  All
     | *Family:*  [dir]
     | *Default:*  Location METplus is being run from

   METPLUS_CONF
     Provide the absolute path to the METplus final configuration file. This file will contain every configuration option and value used when METplus was run.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   MET_BASE
     The base directory where your MET installation resides.

     | *Used by:*  CyclonePlotter, ExtractTiles, PB2NC, PointStat, SeriesByInit, SeriesByLead, TCMPRPlotter, TcPairs
     | *Family:*  [dir]
     | *Default:* 

   [DEPRECATED] MET_BIN
     The location of MET binaries.

     | *Used by:* 
     | *Family:* 
     | *Default:* 

   MET_BUILD_BASE
     The base directory of the MET install. Only needed if using MET version 6.0

     | *Used by:*  TCMPRPlotter
     | *Family:*  [dir]
     | *Default:*  Varies

   MET_INSTALL_DIR
     The base directory of the MET install. To be defined when using MET version 6.1 and beyond. Used to get the full path of the MET executable when calling from METplus Wrappers.

     | *Used by:*  All
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] MISSING_VAL
     Please use TC_PAIRS_MISSING_VAL.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] MISSING_VAL_TO_REPLACE
     Please use TC_PAIRS_MISSING_VAL_TO_REPLACE.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   MODEL
     Specify the model name. This is the model name listed in the MET .stat files.

     | *Used by:*  EnsembleStat, GridStat, PointStat, PcpCombine, StatAnalysis, TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   MODEL<n>_NAME
     Define the model name for the first model to be used in the analysis. This is the model name listed in the MET .stat files.There can be <n> number of models defined in configuration files, simply increment the "MODEL1_" string to match the total number of models being used, e.g.:

     MODEL1_NAME
     MODEL2_NAME
     ...
     MODELN_NAME   

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:* Varies

   MODEL<n>_NAME_ON_PLOT
     Define the name the first model will be listed as on the plots. There can be <n> number of models defined in configuration files, simply increment the "MODEL1_" string to match the total number of models being used, e.g.:

     MODEL1_NAME_ON_PLOT
     MODEL2_NAME_ON_PLOT
     ...
     MODELN_NAME_ON_PLOT

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:* Varies

   MODEL<n>_OBS_NAME
     Define the observation name that was used to compare the first model to be. This is the observation name listed in the MET .stat files. There can be <n> number of observation names defined in configuration files, simply increment the "MODEL1_" string to match the total number of models being used, e.g.:

     MODEL1_OBS_NAME
     MODEL2_OBS_NAME
     ...
     MODELN_OBS_NAME

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:* Varies

   MODEL<n>_STAT_DIR
     Define the stat file directory for the first model to be used in the analysis. There can be <n> number of model directories defined in configuration files, simply increment the "MODEL1_" string to match the total number of models being used, e.g.:

     MODEL1_DIR
     MODEL2_DIR
     ...
     MODELN_DIR

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:* Varies

   EXTRACT_TILES_GRID_INPUT_DIR
     Directory containing gridded input data to be used in ExtractTiles. Currently contains both forecast and observation data.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] MODEL_DATA_DIR
     Please use EXTRACT_TILES_GRID_INPUT_DIR instead.

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] MODEL_NAME
     Please use MODEL instead.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] MODE_CONFIG
     Please use MODE_CONFIG_FILE instead. Path to mode configuration file.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  Varies

   MODE_CONFIG_FILE
     Path to mode configuration file.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  Varies

   MODE_CONV_RADIUS
     Comma separated list of convolution radius values used by mode for both forecast and observation fields. Has the same behavior as setting FCST_MODE_CONV_RADIUS and OBS_MODE_CONV_RADIUS to the same value.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   MODE_CONV_THRESH
     Comma separated list of convolution threshold values used by mode for both forecast and observation fields. Has the same behavior as setting FCST_MODE_CONV_THRESH and OBS_MODE_CONV_THRESH to the same value.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   MODE_FCST_CONV_RADIUS
     Comma separated list of convolution radius values used by mode for forecast fields.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 5

   MODE_FCST_CONV_THRESH
     Comma separated list of convolution threshold values used by mode for forecast fields.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 5

   MODE_FCST_MERGE_FLAG
     Sets the merge_flag value in the mode config file for forecast fields. Valid values are NONE, THRESH, ENGINE, and BOTH.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* THRESH

   MODE_FCST_MERGE_THRESH
     Comma separated list of merge threshold values used by mode for forecast fields.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  >0.45

   MODE_MERGE_CONFIG_FILE
     Path to mode merge config file.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  Varies

   MODE_MERGE_FLAG
     Sets the merge_flag value in the mode config file for both forecast and observation fields. Has the same behavior as setting MODE_FCST_MERGE_FLAG and MODE_OBS_MERGE_FLAG to the same value. Valid values are NONE, THRESH, ENGINE, and BOTH.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* THRESH

   MODE_MERGE_THRESH
     Comma separated list of merge threshold values used by mode for forecast and observation fields. Has the same behavior as setting MODE_FCST_MERGE_THRESH and MODE_OBS_MERGE_THRESH to the same value.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  >0.45

   [DEPRECATED] MODE_OBS_CONV_RADIUS
     Please use OBS_CONV_MODE_RADIUS instead. Comma separated list of convolution radius values used by mode for observation fields.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  5

   [DEPRECATED] MODE_OBS_CONV_THRESH
     Please use OBS_MODE_CONV_THRESH instead. Comma separated list of convolution threshold values used by mode for observation fields.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  5

   [DEPRECATED] MODE_OBS_MERGE_FLAG
     Please use OBS_MODE_MERGE_FLAG instead. Sets the merge_flag value in the mode config file for observation fields. Valid values are NONE, THRESH, ENGINE, and BOTH.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* THRESH

   [DEPRECATED] MODE_OBS_MERGE_THRESH
     Please use OBS_MODE_MERGE_THRESH_INSTEAD. Comma separated list of merge threshold values used by mode for observation fields.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  >0.45

   [DEPRECATED] MODE_OUT_DIR
     Please use MODE_OUTPUT_DIR instead. Output directory to write mode files.

     | *Used by:*  Mode
     | *Family:*  [dir]
     | *Default:*  Varies
     
   MODE_OUTPUT_DIR
     Output directory to write mode files.

     | *Used by:*  Mode
     | *Family:*  [dir]
     | *Default:*  Varies

   MODE_OUTPUT_TEMPLATE
     Sets the subdirectories below MODE_OUTPUT_DIR using a template to allow run time information. If LOOP_BY = VALID, default value is valid time YYYYMMDDHHMM/mode. If LOOP_BY = INIT, default value is init time YYYYMMDDHHMM/mode.

     | *Used by:*  Mode
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   MODE_VERIFICATION_MASK_TEMPLATE
     Template used to specify the verification mask filename for the MET tool mode. Now supports a list of filenames.

     | *Used by:*  Mode
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   MODE_QUILT
     True/False. If True, run all permutations of radius and threshold.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  False

   [DEPRECATED] MTD_CONFIG
     Please use MTD_CONFIG_FILE instead. Path to mode-TD configuration file. Varies

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:*  Varies

   MTD_CONFIG_FILE
     Path to mode-TD configuration file.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:*  Varies

   MTD_CONV_RADIUS
     Comma separated list of convolution radius values used by mode-TD for both forecast and observation files. Has the same behavior as setting FCST_MTD_CONV_RADIUS and OBS_MTD_CONV_RADIUS to the same value.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* 

   MTD_CONV_THRESH
     Comma separated list of convolution threshold values used by mode-TD for both forecast and observation files. Has the same behavior as setting FCST_MTD_CONV_THRESH and OBS_MTD_CONV_THRESH to the same value.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* 

   MTD_FCST_CONV_RADIUS
     Comma separated list of convolution radius values used by mode-TD for forecast files.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:*  5

   MTD_MIN_VOLUME
     Sets min_volume in the MET Mode-TD config file. Refer to the MET User's Guide for more information.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* 

   MTD_SINGLE_RUN
     Set to True to only process one data set (forecast or observation) in Mode-TD. If True, must set MTD_SINGLE_RUN_SRC to either 'FCST' or 'OBS'.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* 

   MTD_SINGLE_RUN_SRC
     Used only if MTD_SINGLE_RUN is set to True. Valid options are 'FCST' or 'OBS'.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* FCST

   MTD_FCST_CONV_THRESH
     Comma separated list of convolution threshold values used by mode-TD for forecast files.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:*  >0.5

   MTD_OBS_CONV_RADIUS
     Comma separated list of convolution radius values used by mode-TD for observation files.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:*  5

   MTD_OBS_CONV_THRESH
     Comma separated list of convolution threshold values used by mode-TD for observation files.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:*  >0.5

   [DEPRECATED] MTD_OUT_DIR
     Please use MTD_OUTPUT_DIR.

     | *Used by:* MTD
     | *Family:*  [dir]
     | *Default:*  Varies

   MTD_OUTPUT_DIR
     Output directory to write mode-TD files.

     | *Used by:* MTD
     | *Family:*  [dir]
     | *Default:*  Varies

   MTD_OUTPUT_TEMPLATE
     Sets the subdirectories below MTD_OUTPUT_DIR using a template to allow run time information. If LOOP_BY = VALID, default value is valid time YYYYMMDDHHMM/mtd. If LOOP_BY = INIT, default value is init time YYYYMMDDHHMM/mtd.

     | *Used by:* MTD
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   NCDUMP
     Path to thencdump executable.

     | *Used by:*  PB2NC, PointStat, SeriesByLead
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] NCDUMP_EXE
     Please use NCDUMP.

     | *Used by:*  PB2NC, PointStat, SeriesByLead
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] NC_FILE_TMPL
     Please use PB2NC_OUTPUT_TEMPLATE instead.

     | *Used by:*  PB2NC
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   PB2NC_OUTPUT_TEMPLATE
     File template used to create netCDF files generated by PB2NC.

     | *Used by:*  PB2NC
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   EXTRACT_TILES_NLAT
     The number of latitude points, set to a whole number. This defines the number of latitude points to incorporate into the subregion (density).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   EXTRACT_TILES_NLON
     The number of longitude points, set to a whole number. This defines the number of longitude points to incorporate into the subregion (density).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] NLAT
     Please use EXTRACT_TILES_NLAT instead. The number of latitude points, set to a whole number. This defines the number of latitude points to incorporate into the subregion (density).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] NLON
     Please use EXTRACT_TILES_NLON instead. The number of longitude points, set to a whole number. This defines the number of longitude points to incorporate into the subregion (density).

     | *Used by:*  ExtractTiles, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   NO_EE
     Set the

     | *Used by:* 
     | *Family:* 
     | *Default:* 

   NO_EE
      flag for the TC Matched Pairs plotting utility.Acceptable values: yes/no

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  no

   NO_LOG
     Set the

     | *Used by:* 
     | *Family:* 
     | *Default:* 

   NO_LOG
      flag for the TC Matched Pairs plotting utility.Acceptable values: yes/no

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  no

   [DEPRECATED] OBS_<n>_FIELD_NAME
     Please use OBS_PCP_COMBINE_<n>_FIELD_NAME instead. This variable is used to define a <n> hour accumulation NetCDF field in the observation dataset used in the MET tool pcp_combine. <n> must be an integer >= 1.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] OBS_BUFR_VAR_LIST
     Please use PB2NC_OBS_BUFR_VAR_LIST instead. Specify which BUFR codes to use from the observation dataset when using the MET pb2nc tool. Format is comma separated list, e.g.:PMO, TOB, TDO

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] OBS_DATA_INTERVAL
     Specify the accumulation interval of the observation dataset used by the MET pcp_combine tool.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_GRID_INPUT_DATATYPE
     Specify the data type of the input directory for grid observation files used with the MET ensemble_stat tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF. A similar variable exists for forecast data called FCST_ENSEMBLE_STAT_INPUT_DATATYPE.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_GRID_INPUT_DIR
     Input directory for grid observation files to use with the MET tool ensemble_stat. A similar variable exists for forecast data called FCST_ENSEMBLE_STAT_INPUT_DIR.

     | *Used by:*  EnsembleStat
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_GRID_INPUT_TEMPLATE
     Template used to specify grid observation input filenames for the MET tool ensemble_stat. A similar variable exists for forecast data called FCST_ENSEMBLE_STAT_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_NUMPY or PYTHON_XARRAY.

     | *Used by:*  EnsembleStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_POINT_INPUT_DATATYPE
     Specify the data type of the input directory for point observation files used with the MET ensemble_stat tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF. A similar variable exists for forecast data called FCST_ENSEMBLE_STAT_INPUT_DATATYPE.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_POINT_INPUT_DIR
     Input directory for point observation files to use with the MET tool ensemble_stat. A similar variable exists for forecast data called FCST_ENSEMBLE_STAT_INPUT_DIR.

     | *Used by:*  EnsembleStat
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_POINT_INPUT_TEMPLATE
     Template used to specify point observation input filenames for the MET tool ensemble_stat. A similar variable exists for forecast data called FCST_ENSEMBLE_STAT_INPUT_TEMPLATE. To utilize Python Embedding as input to the MET tools, set this value to PYTHON_PANDAS.

     | *Used by:*  EnsembleStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_ENSEMBLE_STAT_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing by EnsembleStat. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_ENSEMBLE_STAT_FILE_WINDOW_BEGIN is not set in the config file, the value of OBS_FILE_WINDOW_BEGIN will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   OBS_ENSEMBLE_STAT_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing by EnsembleStat. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_ENSEMBLE_STAT_FILE_WINDOW_END is not set in the config file, the value of OBS_FILE_WINDOW_END will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  EnsembleStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   OBS_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds.This value will be used for all wrappers that look for an observation file unless it is overridden by a wrapper specific configuration variable. For example, if OBS_GRID_STAT_FILE_WINDOW_BEGIN is set, the GridStat wrapper will use that value. If PB2NC_FILE_WINDOW_BEGIN is not set, then the PB2NC wrapper will use OBS_FILE_WINDOW_BEGIN.A corresponding variable exists for forecast data called FCST_FILE_WINDOW_BEGIN.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds.This value will be used for all wrappers that look for an observation file unless it is overridden by a wrapper specific configuration variable. For example, if OBS_GRID_STAT_WINDOW_END is set, the GridStat wrapper will use that value. If PB2NC_WINDOW_END is not set, then the PB2NC wrapper will use OBS_WINDOW_END.A corresponding variable exists for forecast data called FCST_FILE_WINDOW_END.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_GRID_STAT_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing by GridStat. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_GRID_STAT_FILE_WINDOW_BEGIN is not set in the config file, the value of OBS_FILE_WINDOW_BEGIN will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   OBS_GRID_STAT_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing by GridStat. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_GRID_STAT_FILE_WINDOW_END is not set in the config file, the value of OBS_FILE_WINDOW_END will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   OBS_GRID_STAT_INPUT_DATATYPE
     See FCST_GRID_STAT_INPUT_DATATYPEreference "sec:SC_F".

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_GRID_STAT_INPUT_DIR
     See FCST_GRID_STAT_INPUT_DIRreference "sec:SC_F".

     | *Used by:*  GridStat
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_GRID_STAT_INPUT_TEMPLATE
     See FCST_GRID_STAT_INPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  GridStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_GRID_STAT_PROB_THRESH
     See FCST_GRID_STAT_PROB_THRESHreference "sec:SC_F".

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:*  ==0.1

   [DEPRECATED] OBS_GEMPAK_INPUT_DIR
     Specify the input directory for GEMPAK formatted observation files. Use GEMPAKTOCF_INPUT_DIR if running GempakToCF from the PROCESS_LIST.

     | *Used by:*  PcpCombine
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] OBS_GEMPAK_TEMPLATE
     Filename template used to filter GEMPAK formatted observation files. Use GEMPAKTOCF_INPUT_TEMPLATE if running GempakToCF from the PROCESS_LIST.

     | *Used by:*  PcpCombine
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] OBS_INPUT_DIR
     Please use OBS_POINT_STAT_INPUT_DIR instead. Specify the input directory for observation files.

     | *Used by:*  PointStat
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] OBS_INPUT_DIR_REGEX
     Please use OBS_POINT_STAT_INPUT_DIR instead. Specify the regular expression to use when searching for observation file input directories.

     | *Used by:*  PointStat
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] OBS_INPUT_FILE_REGEX
     Please use OBS_POINT_STAT_INPUT_TEMPLATE instead. Regular expression used to filter observation input files used in the analysis.

     | *Used by:*  PointStat,
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] OBS_INPUT_FILE_TEMPL
     Please use OBS_POINT_STAT_INPUT_TEMPLATE instead. Specify the filename template to use for observation input files.

     | *Used by:*  PointStat,
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] OBS_IS_DAILY_FILE
     Please use OBS_PCP_COMBINE_IS_DAILY_FILE instead. Specify whether the forecast file is a daily file or not.Acceptable values: true/false

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_IS_PROB
     Used when setting OBS_* variables to process forecast data for comparisons with mtd. Specify whether the observation data are probabilistic or not. See FCST_IS_PROBreference "sec:SC_F".Acceptable values: true/false

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PointStat
     | *Family:*  [config]
     | *Default:*  False

   [DEPRECATED] OBS_LEVEL
     Please use OBS_PCP_COMBINE_INPUT_LEVEL instead. Specify what accumulation level should be used from the observation data for the analysis. See FCST_LEVEL for more information

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_MODE_CONV_RADIUS
     See FCST_MODE_CONV_RADIUSreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   OBS_MODE_CONV_THRESH
     See FCST_MODE_CONV_THRESHreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   OBS_MODE_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing by Mode. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_MODE_FILE_WINDOW_BEGIN is not set in the config file, the value of OBS_FILE_WINDOW_BEGIN will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   OBS_MODE_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing by Mode. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_MODE_FILE_WINDOW_END is not set in the config file, the value of OBS_FILE_WINDOW_END will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   OBS_MODE_MERGE_FLAG
     See FCST_MODE_MERGE_FLAGreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   OBS_MODE_MERGE_THRESH
     See FCST_MODE_MERGE_THRESHreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:* 

   OBS_MODE_INPUT_DATATYPE
     See FCST_MODE_INPUT_DATATYPEreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_MODE_INPUT_DIR
     See FCST_MODE_INPUT_DIRreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_MODE_INPUT_TEMPLATE
     See FCST_MODE_INPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  Mode
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_MTD_CONV_RADIUS
     See FCST_MTD_CONV_RADIUSreference "sec:SC_F".

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* 

   OBS_MTD_CONV_THRESH
     See FCST_MTD_CONV_THRESHreference "sec:SC_F".

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* 

   OBS_MTD_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing by MTD. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_MTD_FILE_WINDOW_BEGIN is not set in the config file, the value of OBS_FILE_WINDOW_BEGIN will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:* 
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   OBS_MTD_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing by MTD. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_MTD_FILE_WINDOW_END is not set in the config file, the value of OBS_FILE_WINDOW_END will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   OBS_MTD_INPUT_DATATYPE
     See FCST_MTD_INPUT_DATATYPEreference "sec:SC_F".

     | *Used by:* MTD
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_MTD_INPUT_DIR
     See FCST_MTD_INPUT_DIRreference "sec:SC_F".

     | *Used by:* MTD
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_MTD_INPUT_TEMPLATE
     See FCST_MTD_INPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:* 
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] OBS_NAME
     No longer used. Provide a string to identify the observation dataset name.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] OBS_NATIVE_DATA_TYPE
     Specify the data format of the observation data. Use OBS_PCP_COMBINE_INPUT_DATATYPE instead.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_<n>_FIELD_NAME
     See FCST_PCP_COMBINE_<n>_FIELD_NAMEreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_DATA_INTERVAL
     See FCST_PCP_COMBINE_DATA_INTERVALreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_DERIVE_LOOKBACK
     See FCST_PCP_COMBINE_DERIVE_LOOKBACKreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* Varies

   OBS_PCP_COMBINE_INPUT_DATATYPE
     See FCST_PCP_COMBINE_INPUT_DATA_TYPEreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_INPUT_DIR
     See FCST_PCP_COMBINE_INPUT_DIRreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_PCP_COMBINE_INPUT_LEVEL
     See FCST_PCP_COMBINE_INPUT_LEVELreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_INPUT_TEMPLATE
     See FCST_PCP_COMBINE_INPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_PCP_COMBINE_IS_DAILY_FILE
     See FCST_PCP_COMBINE_IS_DAILY_FILEreference "sec:SC_F".Acceptable values: true/false

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  False

   OBS_PCP_COMBINE_METHOD
     See FCST_PCP_COMBINE_METHODreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* None

   OBS_PCP_COMBINE_MIN_FORECAST
     See FCST_PCP_COMBINE_MIN_FORECASTreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_MAX_FORECAST
     See FCST_PCP_COMBINE_MAX_FORECASTreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_OUTPUT_DIR
     See FCST_PCP_COMBINE_OUTPUT_DIRreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_PCP_COMBINE_OUTPUT_TEMPLATE
     See FCST_PCP_COMBINE_OUTPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_PCP_COMBINE_RUN
     See FCST_PCP_COMBINE_RUNreference "sec:SC_F".Acceptable values: true/false

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_STAT_LIST
     See FCST_PCP_COMBINE_STAT_LISTreference "sec:SC_F".Acceptable values: sum, min, max, range, mean, stdev, vld_count

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_TIMES_PER_FILE
     See FCST_PCP_COMBINE_TIMES_PER_FILEreference "sec:SC_F".

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* 

   OBS_POINT_STAT_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing by PointStat. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_POINT_STAT_FILE_WINDOW_BEGIN is not set in the config file, the value of OBS_FILE_WINDOW_BEGIN will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   OBS_POINT_STAT_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing by PointStat. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If OBS_POINT_STAT_FILE_WINDOW_END is not set in the config file, the value of OBS_FILE_WINDOW_END will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   OBS_POINT_STAT_INPUT_DATATYPE
     See FCST_POINT_STAT_INPUT_DATATYPEreference "sec:SC_F".

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_POINT_STAT_INPUT_DIR
     See FCST_POINT_STAT_INPUT_DIRreference "sec:SC_F".

     | *Used by:*  PointStat
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_POINT_STAT_INPUT_TEMPLATE
     See FCST_POINT_STAT_INPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  GriPointStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_POINT_STAT_WINDOW_BEGIN
     Passed to the point_stat MET config file to determine the range of data within a file that should be used for processing.Units are seconds. If the variable is not set, point_stat will use OBS_WINDOW_BEGIN.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_POINT_STAT_WINDOW_END
     Passed to the point_stat MET config file to determine the range of data within a file that should be used for processing. Units are seconds. If the variable is not set, point_stat will use OBS_WINDOW_END.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_REGRID_DATA_PLANE_INPUT_DATATYPE
     See FCST_REGRID_DATA_PLANE_INPUT_DATATYPEreference "sec:SC_F".

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_REGRID_DATA_PLANE_INPUT_DIR
     See FCST_REGRID_DATA_PLANE_INPUT_DIRreference "sec:SC_F".

     | *Used by:*  RegridDataPlane
     | *Family:*  [dir]
     | *Default:*  Varies

   OBS_REGRID_DATA_PLANE_INPUT_TEMPLATE
     See FCST_REGRID_DATA_PLANE_INPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  RegridDataPlane
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_REGRID_DATA_PLANE_OUTPUT_TEMPLATE
     See FCST_REGRID_DATA_PLANE_OUTPUT_TEMPLATEreference "sec:SC_F".

     | *Used by:*  RegridDataPlane
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_REGRID_DATA_PLANE_TEMPLATE
     See FCST_REGRID_DATA_PLANE_TEMPLATEreference "sec:SC_F".

     | *Used by:*  RegridDataPlane
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   OBS_REGRID_DATA_PLANE_OUTPUT_DIR
     See FCST_REGRID_DATA_PLANE_OUTPUT_DIRreference "sec:SC_F".

     | *Used by:*  RegridDataPlane
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] OBS_VAR
     Specify the string for the observation variable used in the analysis. See OBS_VAR<n>_NAME, OBS_VAR<n>_LEVELS, OBS_VAR<n>_OPTIONS and OBS_VAR<n>_THRESH where n = integer >= 1.

     | *Used by:*  GridStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_VAR_LEVEL
     Specify the values of the OBS_VAR_LEVEL column in the MET .stat file to use.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_VAR_NAME
     Specify the values of the OBS_VAR_NAME column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_VAR<n>_LEVELS
     Define the levels for the <n>th observation variable to be used in the analysis where <n> is an integer >= 1. The value can be a single item or a comma separated list of items. You can define NetCDF levels, such as (0,*,*), but you will need to surround these values with quotation marks so that the commas in the item are not interpreted as an item delimeter. Some examples:

     OBS_VAR1_LEVELS = A06, P500
     OBS_VAR2_LEVELS = "(0,*,*)", "(1,*,*)"

     There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     OBS_VAR1_LEVELS
     OBS_VAR2_LEVELS
     ...
     OBS_VAR<n>_LEVELS    

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_VAR<n>_NAME
     Define the name for the <n>th observation variable to be used in the analysis where <n> is an integer >= 1. If OBS_VAR<n>_NAME is not set but FCST_VAR<n>_NAME is, the same information will be used for both variables. There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     OBS_VAR1_NAME
     OBS_VAR2_NAME
     ...
     OBS_VAR<n>_NAME

     This value can be set to a call to a python script with arguments to supply data to the MET tools via Python Embedding. Filename template syntax can be used here to specify time information of an input file, i.e. {valid?fmt=%Y%m%d%H}. See the MET User's Guide for more information about Python Embedding in the MET tools.

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_VAR<n>_OPTIONS
     Define the options for the <n>th observation variable to be used in the analysis where <n> is an integer >= 1. These addition options will be applied to every name/level/threshold combination for VAR<n>. If OBS_VAR<n>_OPTIONS is not set but FCST_VAR<n>_OPTIONS is, the same information will be used for both variables. There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     OBS_VAR1_OPTIONS
     OBS_VAR2_OPTIONS
     ...
     OBS_VAR<n>_OPTIONS

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_VAR<n>_THRESH
     Define the threshold(s) for the <n>th observation variable to be used in the analysis where <n> is an integer >= 1. The value can be a single item or a comma separated list of items that must start with a comparison operator (>,>=,==,!=,<,<=,gt,ge,eq,ne,lt,le). If OBS_VAR<n>_THRESH is not set but FCST_VAR<n>_THRESH is, the same information will be used for both variables. There can be <n> number of these variables defined in configuration files, simply increment the_VAR1_ string to match the total number of variables being used, e.g.:

     OBS_VAR1_THRESH
     OBS_VAR2_THRESH
     ...
     OBS_VAR<n>_THRESH     

     | *Used by:*  GridStat, EnsembleStat, PointStat, Mode, MTD, PcpCombine
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] OBS_WINDOW_BEG
     Please use OBS_WINDOW_BEGIN.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_WINDOW_BEGIN
     Passed to the MET config file to determine the range of data within a file that should be used for processing.Units are seconds. This value will be used for all wrappers that look for an observation file unless it is overridden by a wrapper specific configuration variable. For example, if OBS_POINT_STAT_WINDOW_BEGIN is set, the PointStat wrapper will use that value. If PB2NC_WINDOW_BEGIN is not set, then the PB2NC wrapper will use OBS_WINDOW_BEGIN.A corresponding variable exists for forecast data called FCST_WINDOW_BEGIN.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_WINDOW_END
     Passed to the MET config file to determine the range of data within a file that should be used for processing.Units are seconds. This value will be used for all wrappers that look for an observation file unless it is overridden by a wrapper specific configuration variable. For example, if OBS_POINT_STAT_WINDOW_END is set, the PointStat wrapper will use that value. If PB2NC_WINDOW_END is not set, then the PB2NC wrapper will use OBS_WINDOW_END.A corresponding variable exists for forecast data called FCST_WINDOW_END.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   OBTYPE
     Provide a string to represent the type of observation data used in the analysis. This is the observation time listed in the MET .stat files and is used in setting output filename.

     | *Used by:*  EnsembleStat, GridStat, Mode, MTD, PointStat, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] OB_TYPE
     Please use OBTYPE instead.

     | *Used by:*  EnsembleStat, GridStat, Mode, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   OUTPUT_BASE
     Provide a path to the top level output directory for METplus.

     | *Used by:*  All
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] OVERWRITE_NC_OUTPUT
     Please use PB2NC_SKIP_IF_OUTPUT_EXISTS instead. Specify whether to overwrite the netCDF output or not when using the MET pb2nc tool.Acceptable values: yes/no

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  yes

   EXTRACT_TILES_OVERWRITE_TRACK
     Specify whether to overwrite the track data or not.Acceptable values: yes/no

     | *Used by:*  ExtractTiles
     | *Family:*  [config]
     | *Default:*  no

   [DEPRECATED] OVERWRITE_TRACK
     Please use EXTRACT_TILES_OVERWRITE_TRACK instead.

     | *Used by:*  ExtractTiles
     | *Family:*  [config]
     | *Default:*  no

   PARM_BASE
     This variable will automatically be set by METplus when it is started. Specifies the top level METplus parameter file directory. You can override this value by setting the environment variable METPLUS_PARM_BASE to another directory containing a copy of the METPlus parameter file directory. If the environment variable is not set, the parm directory corresponding to the calling script is used. It is recommended that this variable is not set by the user. If it is set and is not equivalent to the value determined by METplus, execution will fail.

     | *Used by:*  All
     | *Family:*  [dir]
     | *Default:*  {METPLUS_BASE}/parm

   PB2NC_CONFIG_FILE
     Specify the absolute path to the configuration file for the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies
     
   PB2NC_FILE_WINDOW_BEGIN
     Used to control the lower bound of the window around the valid time to determine if a file should be used for processing by PB2NC. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If PB2NC_FILE_WINDOW_BEGIN is not set in the config file, the value of OBS_FILE_WINDOW_BEGIN will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_BEGIN

   PB2NC_FILE_WINDOW_END
     Used to control the upper bound of the window around the valid time to determine if a file should be used for processing by PB2NC. Seereference "sec:SC_Directory_and_Filename_Template_Info" subsection called 'Use Windows to Find Valid Files.' Units are seconds. If PB2NC_FILE_WINDOW_END is not set in the config file, the value of OBS_FILE_WINDOW_END will be used instead. If both file window begin and window end values are set to 0, then METplus will require an input file with an exact time match to process.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:* OBS_FILE_WINDOW_END

   PB2NC_GRID
     Specify a grid to use with the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_INPUT_DATATYPE
     Specify the data type of the input directory for prepbufr files used with the MET pb2nc tool. Currently valid options are NETCDF, GRIB, and GEMPAK. If set to GEMPAK, data will automatically be converted to NetCDF via GempakToCF.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_MESSAGE_TYPE
     Specify which PREPBUFR (PB) message types to convert using the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_OBS_BUFR_VAR_LIST
     Specify which BUFR codes to use from the observation dataset when using the MET pb2nc tool. Format is comma separated list, e.g.:PMO, TOB, TDO

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_OFFSETS
     A list of potential offsets (in hours) that can be found in the prepbufr input template. METplus will check if a file with a given offset exists in the order specified in this list, to be sure to put favored offset values first.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_OUTPUT_DIR
     Specify the directory where files will be written from the MET pb2nc tool. VariesPB2NC_POLYSpecify a polygon to be used with the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [dir]
     | *Default:*  Varies

   PB2NC_SKIP_IF_OUTPUT_EXISTS
     If True, do not run PB2NC if output file already exists. Set to False to overwrite files. VariesPB2NC_STATION_IDSpecify the ID of the station to use with the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_TIME_SUMMARY_FLAG
     Specify the time summary flag item in the MET pb2nc config file. Refer to the MET User's Guide for more information.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_TIME_SUMMARY_BEG
     Specify the time summary beg item in the MET pb2nc config file. Refer to the MET User's Guide for more information.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_TIME_SUMMARY_END
     Specify the time summary end item in the MET pb2nc config file. Refer to the MET User's Guide for more information.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_TIME_SUMMARY_VAR_NAMES
     Specify the time summary obs_var list item in the MET pb2nc config file. Refer to the MET User's Guide for more information.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_TIME_SUMMARY_TYPES
     Specify the time summary type list item in the MET pb2nc config file. Refer to the MET User's Guide for more information.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_WINDOW_BEGIN
     Passed to the pb2nc MET config file to determine the range of data within a file that should be used for processing.Units are seconds. If the variable is not set, pb2nc will use OBS_WINDOW_BEGIN.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PB2NC_WINDOW_END
     Passed to the pb2nc MET config file to determine the range of data within a file that should be used for processing. Units are seconds. If the variable is not set, pb2nc will use OBS_WINDOW_END.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] PCP_COMBINE_METHOD
     SPlease use [FCST/OBS]_PCP_COMBINE_METHOD instead.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:* ADD

   PCP_COMBINE_SKIP_IF_OUTPUT_EXISTS
     If True, do not run pcp_combine if output file already exists. Set to False to overwrite files.

     | *Used by:*  PcpCombine
     | *Family:*  [config]
     | *Default:*  False

   PLOTTING_OUTPUT_DIR
     Specify the output directory where plots will be saved. This is the base directory where the output from running make_plots_wrapper will be put.

     | *Used by:*  MakePlots
     | *Family:*  [dir]
     | *Default:*  Varies

   PLOTTING_SCRIPTS_DIR
     Specify the directory where the plotting scripts are located. It is recommended to set this to {METPLUS_BASE}/ush/plotting_scripts.

     | *Used by:*  MakePlots
     | *Family:*  [dir]
     | *Default:*  Varies

   PLOT_CONFIG_OPTS
     Specify plot configuration options for the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   PLOT_STATS_LIST
     This is a list of the statistics to calculate and create plots for. Specify the list in a comma-separated list, e.g.:

     acc, bias, rmse

     The list of valid options varies depending on line type that was used during the filtering of stat_analysis_wrapper. For SL1L2, VL1L2 valid options are bias, rms, msess, rsd, rmse_md, rmse_pv, pcor, fbar, and fbar_obar. For SAL1L2, VAL1L2, the valid options is acc. For VCNT, bias, fbar, fbar_obar, speed_err, dir_err, rmsve, vdiff_speed, vdiff_dir, rsd, fbar_speed, fbar_dir, fbar_obar_speed, and fbar_obar_dir.

     | *Used by:*  MakePlots
     | *Family:*  [config]
     | *Default:*  Varies

   PLOT_TIME
     In StatAnalysis, this specifies the way to treat the date information, where valid options are valid and init.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   PLOT_TYPES
     Specify what plot types are desired for the TC Matched Pairs plotting tool. By default, a boxplot is generated if this is undefined in the configuration file. If other plots are requested and a boxplot is also desired, you must explicitly listboxplot in your list of plot types. Supported plot types: BOXPLOT, POINT, MEAN, MEDIAN, RELPERF (relative performance), RANK (time series of ranks for the first model), SCATTER, SKILL_MN (mean skill scores) and SKILL_MD (median skill scores).

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   POINT_STAT_CONFIG_FILE
     Specify the absolute path to the configuration file to be used with the MET point_stat tool.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   POINT_STAT_GRID
     Specify the grid to use with the MET point_stat tool.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   POINT_STAT_MESSAGE_TYPE
     Specify which PREPBUFR message types to process with the MET point_stat tool.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   POINT_STAT_OUTPUT_DIR
     Specify the directory where output files from the MET point_stat tool are written.

     | *Used by:*  PointStat
     | *Family:*  [dir]
     | *Default:*  Varies

   POINT_STAT_OUTPUT_TEMPLATE
     Sets the subdirectories below POINT_STAT_OUTPUT_DIR using a template to allow run time information. If LOOP_BY = VALID, default value is valid time YYYYMMDDHHMM/point_stat. If LOOP_BY = INIT, default value is init time YYYYMMDDHHMM/point_stat.

     | *Used by:*  PointStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   POINT_STAT_POLY
     Specify a polygon to use with the MET point_stat tool.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   POINT_STAT_STATION_ID
     Specify the ID of a specific station to use with the MET point_stat tool.

     | *Used by:*  PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   POINT_STAT_VERIFICATION_MASK_TEMPLATE
     Template used to specify the verification mask filename for the MET tool point_stat. Now supports a list of filenames.

     | *Used by:*  PointStat
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   PREFIX
     This corresponds to the optional -prefix flag of the plot_TCMPR.R script (which is wrapped by TCMPRPlotter). This is the output file name prefix.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] PREPBUFR_DATA_DIR
     Please use PB2NC_INPUT_DIR instead. Specify the directory where the PREPBUFR data are located for the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] PREPBUFR_DIR_REGEX
     Regular expression to use when searching for PREPBUFR data.

     | *Used by:*  PB2NC
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] PREPBUFR_FILE_REGEX
     Regular expression to use when searching for PREPBUFR files.

     | *Used by:*  PB2NC
     | *Family:*  [regex_pattern]
     | *Default:*  Varies

   [DEPRECATED] PREPBUFR_MODEL_DIR_NAME
     Please put the value previously used here in the PB2NC_INPUT_DIR path. Specify the name of the model being used with the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   PROCESS_LIST
     Specify the list of processes for METplus to perform, in a comma separated list.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] PROJ_DIR
     A directory for generic use. The user can store input files (if INPUT_BASE is not defined), intermediate files, and any other project-related files.

     | *Used by:*  PB2NC, PointStat, TcStat
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] REFERENCE_TMPL
     Please use TC_PAIRS_BDECK_TEMPLATE.

     | *Used by:*  TcPairs
     | *Family:*  [filename_templates]
     | *Default:*  Varies

   REGION
     Specify the values of the VX_MASK column in the MET .stat file to use. This is optional in the METplus configuration file for running with LOOP_ORDER = times

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   REGION_LIST
     A list of the regions of interest. This is the list of regions for plotting verification.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   REGRID_DATA_PLANE_METHOD
     Sets the method used by regrid_data_plane. See MET User's Guide for more information.

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:* 

   REGRID_DATA_PLANE_SKIP_IF_OUTPUT_EXISTS
     If True, do not run regrid_data_plane if output file already exists. Set to False to overwrite files.

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:*  False

   REGRID_DATA_PLANE_WIDTH
     Sets the width used by regrid_data_plane. See MET User's Guide for more information.

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:* 1

   REGRID_DATA_PLANE_VERIF_GRID
     Specify the absolute path to a file containing information about the desired output grid from the MET regrid_data_plane tool.

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:*  Varies

   REGRID_TO_GRID
     If supported, provide the output grid that is desired from the MET tool being used in the analysis.

     | *Used by:*  MakePlots, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   RM
     Specify the path to the Linuxrm executable.

     | *Used by:*  PB2NC, PointStat, SeriesByLead
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] RM_EXE
     Please use RM.

     | *Used by:*  PB2NC, PointStat, SeriesByLead
     | *Family:*  [exe]
     | *Default:*  /path/to

   RP_DIFF
     This corresponds to the optional -rp_diff flag of the plot_TCMPR.R script (which is wrapped by TCMPRPlotter). This a comma-separated list of thresholds to specify meaningful differences for the relative performance plot.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   SAVE
     Corresponds to the optional -save flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). This is a yes/no value to indicate whether to save the image (yes).

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   SAVE_DATA
     Corresponds to the optional -save_data flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). Indicates whether to save the filtered track data to a file instead of deleting it.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   SCATTER_X
     Corresponds to the optional -scatter_x flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). This is a comma-separated list of x-axis variable columns to plot.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   SCATTER_Y
     Corresponds to the optional -scatter_y flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). This is a comma-separated list of y-axis variable columns to plot.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   SCRUB_STAGING_DIR
     Remove staging directory after METplus has completed running if set to True. Set to False to preserve data for subsequent runs.

     | *Used by:* All
     | *Family:*  [config]
     | *Default:*  False

   SERIES
     Corresponds to the optional -series flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). This is the column whose unique values define the series on the plot, optionally followed by a comma-separated list of values, including: ALL, OTHER, and colon-separated groups.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   SERIES_ANALYSIS_CONFIG_FILE
     Specify the absolute path for the configuration file to use with the MET series_analysis tool by initialization time.

     | *Used by:*  SeriesByInit, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] SERIES_ANALYSIS_BY_INIT_CONFIG_FILE
     Please use SERIES_ANALYSIS_CONFIG_FILE instead.

     | *Used by:*  SeriesByInit
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] SERIES_ANALYSIS_BY_LEAD_CONFIG_FILE
     Please use SERIES_ANALYSIS_CONFIG_FILE instead.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   SERIES_ANALYSIS_FILTER_OPTS
     Filtering options to be applied during series analysis. Filter options are performed by invoking the MET tc_stat tool within the METplus wrapper. Refer to Chapter 20 of the MET User's Guide for the syntax to use for performing filtering via the MET tc_stat tool.

     | *Used by:*  SeriesByLead, SeriesByInit
     | *Family:*  [config]
     | *Default:*  Varies

   SERIES_ANALYSIS_FILTERED_OUTPUT_DIR
     Specifies the directory where filtered files will be written from the MET SeriesAnalysis tool.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] SERIES_BY_LEAD_FILTERED_OUTPUT_DIR
     Please use SERIES_ANALYSIS_FILTERED_OUTPUT_DIR instead.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   SERIES_ANALYSIS_GROUP_FCSTS
     Set to True to aggregate the series by lead results into bins of time.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] SERIES_BY_LEAD_GROUP_FCSTS
     Please use SERIES_ANALYSIS_GROUP_FCSTS instead.

     | *Used by:*  SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   SERIES_CI
     Corresponds to the optional -series_ci flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). This is a list of true/false for confidence intervals. This list can be optionally followed by a comma-separated list of values, including ALL, OTHER, and colon-separated groups.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] SERIES_INIT_FILTERED_OUT_DIR
     Please use SERIES_ANALYSIS_FILTERED_OUTPUT_DIR instead.

     | *Used by:*  SeriesByInit
     | *Family:*  [dir]
     | *Default:*  Varies

   SERIES_ANALYSIS_INPUT_DIR
     Specify the directory to read input to SeriesAnalysis. It is recommended to set this to {EXTRACT_TILES_OUTPUT_DIR}.

     | *Used by:*  SeriesByLead, SeriesByInit
     | *Family:*  [dir]
     | *Default:*  Varies

   SERIES_ANALYSIS_OUTPUT_DIR
     Specify the directory where files will be written from the MET series analysis tool when processing by initialization time.

     | *Used by:*  SeriesByInit
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] SERIES_INIT_OUT_DIR
     Please use SERIES_ANALYSIS_OUTPUT_DIR instead.

     | *Used by:*  SeriesByInit
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] SERIES_LEAD_FILTERED_OUT_DIR
     Please use SERIES_ANALYSIS_FILTERED_OUTPUT_DIR. Specify the directory where filtered files will be written from the MET series_analysis tool when processing by lead time.

     | *Used by:*  SeriesByLead
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] SERIES_LEAD_OUT_DIR
     Please use SERIES_ANALYSIS_OUTPUT_DIR instead.

     | *Used by:*  SeriesByLead
     | *Family:*  [dir]
     | *Default:*  Varies

   SKILL_REF
     This corresponds to the optional -skill_ref flag in plot_TCMPR.R (which is wrapped by TCMPRPlotter). This is the identifier for the skill score reference.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] START_DATE
     Please use INIT_BEG or VALID_BEG instead.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:*  Varies

   STAGING_DIR
     Directory to uncompress or convert data into for use in METplus.

     | *Used by:* All
     | *Family:*  [dir]
     | *Default:*  OUTPUT_BASE/stage

   [DEPRECATED] START_HOUR
     Please use INIT_BEG or VALID_BEG instead.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [config]
     | *Default:* Varies

   STAT_ANALYSIS_CONFIG
     Specify the absolute path for the configuration file used with the MET stat_analysis tool. It is recommended to set this to {PARM_BASE}/use_cases/plotting/met_config/STATAnalysisConfig.

     | *Used by:*  StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   STAT_ANALYSIS_DUMP_ROW_TMPL
     Specify the template to use for the stat_analysis dump_row file. A user customized template to use for the dump_row file. If left blank and a dump_row file is requested, a default version will be used. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  StatAnalysis
     | *Family:*  [filename_templates]
     | *Default:* 

   STAT_ANALYSIS_LOOKIN_DIR
     Specify the input directory where the MET stat_analysis tool will find input files. This is the directory that the stat_analysis wrapper will use to build the argument to -lookin for the MET stat_analysis tool. It can contain wildcards, i.e. *.

     | *Used by:*  StatAnalysis
     | *Family:*  [dir]
     | *Default:*  Varies

   STAT_ANALYSIS_OUT_STAT_TMPL
     Specify the template to use for the stat_analysis out_stat file. A user customized template to use for the out_stat file. If left blank and a out_stat file is requested, a default version will be used. This is optional in the METplus configuration file for running with LOOP_ORDER = times.

     | *Used by:*  StatAnalysis
     | *Family:*  [filename_templates]
     | *Default:* 

   STAT_ANALYSIS_OUTPUT_DIR
     This is the base directory where the output from running stat_analysis_wrapper will be put.

     | *Used by:*  StatAnalysis
     | *Family:*  [dir]
     | *Default:*  Varies

   STAT_FILES_INPUT_DIR
     Specify the directory where stat files exist that plots can be generated from. This is the directory where the files from running previously running stat_analysis_wrapper are located. These are the files used as the data to create the plots. It is recommended to set this to {STAT_ANALYSIS_OUTPUT_DIR}.

     | *Used by:*  MakePlots
     | *Family:*  [dir]
     | *Default:*  Varies

   SERIES_ANALYSIS_STAT_LIST
     Specify a list of statistics to be computed by the MET series_analysis tool.

     | *Used by:*  SeriesByInit, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] STAT_LIST
     Please use SERIES_ANALYSIS_STAT_LIST instead.

     | *Used by:*  SeriesByInit, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] STORM_ID
     Please use TC_PAIRS_STORM_ID or TC_STAT_STORM_ID.

     | *Used by:*  CyclonePlotter, TcPairs, TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] STORM_NAME
     Please use TC_PAIRS_STORM_NAME.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   SUBTITLE
     The subtitle of the plot.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   TCMPR_DATA_DIR
     Provide the input directory for the track data for the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [dir]
     | *Default:*  Varies

   TCMPR_PLOT_OUT_DIR
     Provide the output directory where the TC Matched Pairs plotting tool will create files.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [dir]
     | *Default:*  Varies

   TC_PAIRS_ADECK_INPUT_DIR
     Directory that contains the ADECK files.

     | *Used by:*  TcPairs
     | *Family:* [dir]
     | *Default:*  Varies

   TC_PAIRS_ADECK_TEMPLATE
     Template of the file names of ADECK data.

     | *Used by:*  TcPairs
     | *Family:* [filename_templates]
     | *Default:*  Varies

   TC_PAIRS_BASIN
     Control what basins are desired for tropical cyclone analysis.Per the MET users' guide, acceptable basin ID's are:WP = Western Northern PacificIO = Northern Indian OceanSH = Southern HemisphereCP = Central Northern PacificEP = Eastern Northern PacificAL = Northern AtlanticSL = Southern Atlantic

     | *Used by:*  TcPairs
     | *Family:* [config]
     | *Default:*  Varies

   TC_PAIRS_BDECK_INPUT_DIR
     Directory that contains the BDECK files.

     | *Used by:*  TcPairs
     | *Family:* [dir]
     | *Default:*  Varies

   TC_PAIRS_BDECK_TEMPLATE
     Template of the file names of BDECK data.

     | *Used by:*  TcPairs
     | *Family:* [filename_templates]
     | *Default:*  Varies

   TC_PAIRS_CONFIG_FILE
     Provide the absolute path to the configuration file for the MET tc_pairs tool.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_CYCLONE
     Specify which cyclone numbers to include in the tropical cyclone analysis. Per the MET users' guide, this can be any number 01-99 (HH format). Use a space or comma separated list, or leave unset if all cyclones are desired.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_DLAND_FILE
     The file generated by the MET tool tc_dland, containing the gridded representation of the minimum distance to land. Please refer to Chapter 18 of the MET User's Guide for more information about the tc_dland tool.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:* Varies

   TC_PAIRS_EDECK_INPUT_DIR
     Directory that contains the EDECK files.

     | *Used by:*  TcPairs
     | *Family:* [dir]
     | *Default:*  Varies

   TC_PAIRS_EDECK_TEMPLATE
     Template of the file names of EDECK data.

     | *Used by:*  TcPairs
     | *Family:* [filename_templates]
     | *Default:*  Varies

   [DEPRECATED] TC_PAIRS_DIR
     Please use TC_PAIRS_OUTPUT_DIR.

     | *Used by:*  TcPairs
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] TC_PAIRS_FORCE_OVERWRITE
     Please use TC_PAIRS_SKIP_IF_OUTPUT_EXISTS.Acceptable values: yes/no

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  no

   TC_PAIRS_MISSING_VAL
     Specify the missing value code.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_MISSING_VAL_TO_REPLACE
     Specify the missing value code to replace.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_OUTPUT_DIR
     Specify the directory where the MET tc_pairs tool will write files.

     | *Used by:*  TcPairs
     | *Family:*  [dir]
     | *Default:*  Varies

   TC_PAIRS_OUTPUT_TEMPLATE
     Template of the output file names created by tc_pairs.

     | *Used by:*  TcPairs
     | *Family:* [filename_templates]
     | *Default:*  Varies

   TC_PAIRS_READ_ALL_FILES
     Specify whether to pass the value specified in TC_PAIRS_[A/B/E]DECK_INPUT_DIR to the MET tc_pairs utility or have the wrapper search for valid files in that directory based on the value of TC_PAIRS_[A/B/E]DECK_TEMPLATE and pass them individually to tc_pairs. Set to false or no to have the wrapper find valid files. This can speed up execution time of tc_pairs.Acceptable values: yes/no

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  no

   TC_PAIRS_REFORMAT_DECK
     Set to true or yes if using cyclone data that needs to be reformatted to match the ATCF (Automated Tropical Cyclone Forecasting) format. If set to true or yes, you will need to set TC_PAIRS_REFORMAT_TYPE to specify which type of reformatting to perform.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_REFORMAT_DIR
     Specify the directory to write reformatted track data to be read by tc_pairs. Used only if TC_PAIRS_REFORMAT_DECK is true or yes.

     | *Used by:*  TcPairs
     | *Family:*  [dir]
     | *Default:* {OUTPUT_BASE}/track_data_atcf

   TC_PAIRS_REFORMAT_TYPE
     Specify which type of reformatting to perform on cyclone data. Currently only SBU extra tropical cyclone reformatting is available. Only used if TC_PAIRS_REFORMAT_DECK is true or yes.Acceptable values: SBU

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_SKIP_IF_REFORMAT_EXISTS
     Specify whether to overwrite the reformatted cyclone data or not. If set to true or yes and the reformatted file already exists for a given run, the reformatting code will not be run. Used only when TC_PAIRS_REFORMAT_DECK is set to true or yes.Acceptable values: yes/no

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  no

   TC_PAIRS_SKIP_IF_OUTPUT_EXISTS
     Specify whether to overwrite the output from the MET tc_pairs tool or not. If set to true or yes and the output file already exists for a given run, tc_pairs will not be run.Acceptable values: yes/no

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  no

   TC_PAIRS_STORM_ID
     The identifier of the storm(s) of interest.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_PAIRS_STORM_NAME
     The name(s) of the storm of interest.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_AMODEL
     Specify the AMODEL for the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_BASIN
     Specify the BASIN for the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_BMODEL
     Specify the BMODEL for the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_CMD_LINE_JOB
     Specify expression(s) that will be passed to the MET tc_stat tool via the command line. Only specify if TC_STAT_RUN_VIA=CLI. Please refer to the MET User's Guide chapter for tc-stat for the details on performing job summaries and job filters.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_COLUMN_STR_NAME
     Specify the string names of the columns for stratification with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_COLUMN_STR_VAL
     Specify the values for the columns set via the TC_STAT_COLUMN_STR_NAME option for use with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_COLUMN_THRESH_NAME
     Specify the string names of the columns for stratification by threshold with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_COLUMN_THRESH_VAL
     Specify the values used for thresholding the columns specified in the TC_STAT_COLUMN_THRESH_NAME option for use with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_CYCLONE
     Specify the CYCLONE of interest for use with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_DESC
     Specify the DESC option for use with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_BEG
     Specify the beginning initialization time for stratification when using the MET tc_stat tool.Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_END
     Specify the ending initialization time for stratification when using the MET tc_stat tool.Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_EXCLUDE
     Specify the initialization times to exclude when using the MET tc_stat tool, via a comma separated list e.g.:20141220_18, 20141221_00Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_HOUR
     The beginning hour (HH) of the initialization time of interest.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_INCLUDE
     Specify the initialization times to include when using the MET tc_stat tool, via a comma separated list e.g.:20141220_00, 20141220_06, 20141220_12Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_MASK
     This corresponds to the INIT_MASK keyword in the MET tc_stat config file. For more information, please refer to Chapter 20 in the MET User's Guide.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_STR_NAME
     This corresponds to the INIT_STR_NAME keyword in the MET tc_stat config file. Please refer to Chapter 20 in the MET User's Guide for more details.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INIT_STR_VAL
     This corresponds to the INIT_STR_VAL keyword in the MET tc_stat config file. Please refer to Chapter 20 in the MET User's Guide for more information.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_INPUT_DIR
     Specify the input directory where the MET tc_stat tool will look for files.

     | *Used by:*  TcStat
     | *Family:*  [dir]
     | *Default:*  Varies

   TC_STAT_JOBS_LIST
     Specify expressions for the MET tc_stat tool to execute.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_LANDFALL
     Specify whether only those points occurring near landfall should be retained when using the MET tc_stat tool.Acceptable values: True/False

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  False

   TC_STAT_LANDFALL_BEG
     Specify the beginning of the landfall window for use with the MET tc_stat tool.Acceptable formats: HH, HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  -24

   TC_STAT_LANDFALL_END
     Specify the end of the landfall window for use with the MET tc_stat tool.Acceptable formats: HH, HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_LEAD
     Specify the lead times to stratify by when using the MET tc_stat tool.Acceptable formats: HH, HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_LEAD_REQ
     Specify the LEAD_REQ when using the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_MATCH_POINTS
     Specify whether only those points common to both the ADECK and BDECK tracks should be written out or not when using the MET tc_stat tool.Acceptable values: True/False

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  false

   TC_STAT_OUTPUT_DIR
     Specify the output directory where the MET tc_stat tool will write files.

     | *Used by:*  TcStat
     | *Family:*  [dir]
     | *Default:*  Varies

   TC_STAT_RUN_VIA
     Specify the method for running the MET tc_stat tool.Acceptable values: CONFIG. If left blank (unset), tc_stat will run via the command line.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:* CONFIG

   TC_STAT_STORM_ID
     Set the STORM_ID(s) of interest with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_STORM_NAME
     Set the STORM_NAME for use with the MET tc_stat tool.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_TRACK_WATCH_WARN
     Specify which watches and warnings to stratify over when using the MET tc_stat tool.Acceptable values: HUWARN, HUWATCH, TSWARN, TSWATCH, ALLIf left blank (unset), no stratification will be done.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_VALID_BEG
     Specify a comma separated list of beginning valid times to stratify with when using the MET tc_stat tool.Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_VALID_END
     Specify a comma separated list of ending valid times to stratify with when using the MET tc_stat tool.Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_VALID_EXCLUDE
     Specify a comma separated list of valid times to exclude from the stratification with when using the MET tc_stat tool.Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_VALID_HOUR
     This corresponds to the VALID_HOUR keyword in the MET tc_stat config file. For more information, please refer to Chapter 20 of the MET User's Guide.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_VALID_INCLUDE
     Specify a comma separated list of valid times to include in the stratification with when using the MET tc_stat tool.Acceptable formats: YYYYMMDD_HH, YYYYMMDD_HHmmss

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_VALID_MASK
     This corresponds to the VALID_MASK in the MET tc_stat config file. Please refer to Chapter 20 of the MET User's Guide for more information.

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   TC_STAT_WATER_ONLY
     Specify whether to exclude points where the distance to land is <= 0. If set to TRUE, once land is encountered the remainder of the forecast track is not used for the verification, even if the track moves back over water.Acceptable values: true/false

     | *Used by:*  TcStat
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] TIME_METHOD
     Please use LOOP_BY instead.

     | *Used by:*  PB2NC, PointStat
     | *Family:* 
     | *Default:* 

   [DEPRECATED] TIME_SUMMARY_BEG
     Please use PB2NC_TIME_SUMMARY_BEG instead. Specify the starting time of the summary when using the MET pb2nc tool.Acceptable formats: HHMMSS

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  000000

   [DEPRECATED] TIME_SUMMARY_END
     Please use PB2NC_TIME_SUMMARY_END instead. Specify the ending time of the summary when using the MET pb2nc tool.Acceptable formats: HHMMSS

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  235959

   [DEPRECATED] TIME_SUMMARY_FLAG
     Please use PB2NC_TIME_SUMMARY_FLAG instead. Specify whether to receive a time summary from the MET pb2nc tool or not.Acceptable values: True/False

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  False

   [DEPRECATED] TIME_SUMMARY_TYPES
     Please use PB2NC_TIME_SUMMARY_TYPES instead. Specify a comma separated list of time summary types to receive from the MET pb2nc tool.

     | *Used by:*  PB2NC PB2NC
     | *Family:*  [config] [config]
     | *Default:*  Varies[deprecated]TIME_SUMMARY_VAR_NAMESPlease use PB2NC_TIME_SUMMARY_VAR_NAMES instead. Specify a comma separated list of time summary variable names to receive from the MET pb2nc tool. Varies

   TITLE
     Specify a title string for the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   TMP_DIR
     Specify the path to a temporary directory where the user has write permissions.

     | *Used by:*  ExtractTiles, PB2NC, PointStat, SeriesByInit, SeriesByLead, TcStat
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] TOP_LEVEL_DIRS
     Please use TC_PAIRS_READ_ALL_FILES.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  no

   [DEPRECATED] TRACK_DATA_DIR
     Please use TC_PAIRS_[A/B/E]DECK_INPUT_DIR.

     | *Used by:*  TcPairs
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] TRACK_DATA_MOD_FORCE_OVERWRITE
     Please use TC_PAIRS_SKIP_IF_REFORMAT_EXISTS.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  no

   [DEPRECATED] TRACK_DATA_SUBDIR_MOD
     No longer used.

     | *Used by:*  TcPairs
     | *Family:*  [dir]
     | *Default:*  Varies

   [DEPRECATED] TRACK_TYPE
     Please use TC_PAIRS_REFORMAT_DECK.

     | *Used by:*  TcPairs
     | *Family:*  [config]
     | *Default:*  Varies

   TR
     Specify the path to the Linux "tr" executable.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [exe]
     | *Default:*  /path/to

   [DEPRECATED] TR_EXE
     Please use TR.

     | *Used by:*  PB2NC, PointStat
     | *Family:*  [exe]
     | *Default:*  /path/to

   VALID_BEG
     Specify a begin time for valid times for use in the analysis. This is the starting date in the format set in the VALID_TIME_FMT. It is named accordingly to the value set for LOOP_BY. However, in StatAnalysis, it is named accordingly to the value set for PLOT_TIME.Seereference "subsec:SC_Timing_Control_Looping-by-Valid" for more information.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_END
     Specify an end time for valid times for use in the analysis. This is the ending date in the format set in the VALID_TIME_FMT. It is named accordingly to the value set for LOOP_BY.Seereference "subsec:SC_Timing_Control_Looping-by-Valid" for more information.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_HOUR_BEG
     Specify a beginning hour for valid times for use in the analysis.Acceptable formats: HHMM

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_HOUR_END
     Specify an end hour for valid times for use in the analysis.Acceptable formats: HHMM

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_HOUR_INCREMENT
     Specify a time increment for valid times for use in the analysis.Acceptable formats: seconds

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_HOUR_METHOD
     Specify the method for the treatment of valid hours. Valid options are LOOP or GROUP. LOOP will consider the valid hours individually, and GROUP will consider them valid hours as a whole.Acceptable formats: LOOP or GROUP

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_INCREMENT
     Specify the time increment for valid times for use in the analysis.Seereference "subsec:SC_Timing_Control_Looping-by-Valid" for more information. Units are assumed to be seconds unless specified with Y, m, d, H, M, or S.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   VALID_TIME_FMT
     Specify a strftime formatting string for use with VALID_BEG and VALID_END.Seereference "subsec:SC_Timing_Control_Looping-by-Valid" for more information.

     | *Used by:*  All
     | *Family:*  [config]
     | *Default:*  Varies

   SERIES_ANALYSIS_VAR_LIST
     Specify a comma separated list of variables to be used in the analysis.

     | *Used by:*  PB2NC, SeriesByInit, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] VAR_LIST
     Please use SERIES_ANALYSIS_VAR_LIST.

     | *Used by:*  PB2NC, SeriesByInit, SeriesByLead
     | *Family:*  [config]
     | *Default:*  Varies

   VAR<n>_FOURIER_DECOMP
     Specify if Fourier decomposition is to be considered (True) or not (False). If this is set to True, data stratification will be done for the Fourier decomposition of FCS_VAR<n>_NAME. This should have been previously run in grid_stat_wrapper. The default value is set to False.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  False

   VAR<n>_WAVE_NUM_LIST
     Specify a comma separated list of wave numbers pairings of the Fourier decomposition.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:* 

   [DEPRECATED] VERIFICATION_GRID
     Please use REGRID_DATA_PLANE_VERIF_GRID. Specify the absolute path to a file containing information about the desired output grid from the MET regrid_data_plane tool.

     | *Used by:*  RegridDataPlane
     | *Family:*  [config]
     | *Default:*  Varies

   VERIF_CASE
     Specify a string identifying the verification case being performed. Valid options are grid2grid, grid2obs, and precip.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   VERIF_GRID
     Specify a string describing the grid the verification was performed on. This is the name of the grid upon which the verification was done on, ex. G002.

     | *Used by:*  MakePlots
     | *Family:*  [config]
     | *Default:* 

   VERIF_TYPE
     Specify a string describing the type of verification being performed. For VERIF_CASE = grid2grid, valid options are anom, pres, and sfc. For VERIF_CASE = grid2obs, valid options are conus_sfc and upper_air. For VERIF_CASE = precip, any accumulation amount is valid, ex. A24.

     | *Used by:*  MakePlots, StatAnalysis
     | *Family:*  [config]
     | *Default:*  Varies

   [DEPRECATED] VERTICAL_LOCATION
     Specify the vertical location desired when using the MET pb2nc tool.

     | *Used by:*  PB2NC
     | *Family:*  [config]
     | *Default:*  Varies

   XLAB
     Specify the x-axis label when using the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   XLIM
     Specify the x-axis limit when using the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   YLAB
     Specify the y-axis label when using the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   YLIM
     Specify the y-axis limit when using the TC Matched Pairs plotting tool.

     | *Used by:*  TCMPRPlotter
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_INPUT_ACCUMS
     Specify what accumulation levels should be used from the forecast data for the analysis. This is a list of input accumulations in the order of preference to use to build the desired accumulation. If an accumulation cannot be used (i.e. it is larger than the remaining accumulation that needs to be built) then the next value in the list is tried. Units are assumed to be hours unless a time identifier such as Y, m, d, H, M, S is specifed at the end of the value, i.e. 30M or 1m.

     If the name and/or level of the accumulation value must be specified for the data, then a list of equal length to this variable must be set for FCST_PCP_COMBINE_INPUT_NAMES and FCST_PCP_COMBINE_INPUT_LEVELS. See this sections for more information.

     This variable can be set to {lead} if the accumulation found in a given file corresponds to the forecast lead of the data. If this is the case, FCST_PCP_COMBINE_BUCKET_INTERVAL can be used to reset the accumulation at a given interval.

     A corresponding variable exists for observation data called OBS_PCP_COMBINE_INPUT_ACCUMS.

     Examples:

     1H, 30M

     This will attempt to use a 1 hour accumulation, then try to use a 30 minute accumulation if the first value did not succeed.

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_INPUT_ACCUMS
     See FCST_PCP_COMBINE_INPUT_ACCUMS

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_BUCKET_INTERVAL
     Used when FCST_PCP_COMBINE_INPUT_ACCUMS contains {lead} in the list. This is the interval to reset the bucket accumulation. For example, if the accumulation is reset every 3 hours (forecast 1 hour has 1 hour accum, forecast 2 hour has 2 hour accum, forecast 3 hour has 3 hour accum, forecast 4 hour has 1 hour accum, etc.) then this should be set to 3 or 3H. Units are assumed to be hours unless specified with Y, m, d, H, M, or S.

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_INPUT_NAMES
     Specify which field names correspond to each accumulation specifed in FCST_PCP_COMBINE_INPUT_ACCUMS for the forecast data for the analysis. See FCST_PCP_COMBINE_INPUT_ACCUMS for more information. A corresponding variable exists for observation data called OBS_PCP_COMBINE_INPUT_NAMES. Examples:

     FCST_PCP_COMBINE_INPUT_ACCUMS = 6, 1
     FCST_PCP_COMBINE_INPUT_NAMES = P06M_NONE, P01M_NONE

     This says that the 6 hour accumulation field name is P06M_NONE and the 1 hour accumulation field name is P01M_NONE.

     To utilize Python Embedding as input to the MET tools, set this value to the python script command with arguments. This value can include filename template syntax such as {valid?fmt=%Y%m%d%H}.

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_INPUT_NAMES
     See FCST_PCP_COMBINE_INPUT_NAMES

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_INPUT_LEVELS
     Specify which levels correspond to each accumulation specifed in FCST_PCP_COMBINE_INPUT_ACCUMS for the forecast data for the analysis. See FCST_PCP_COMBINE_INPUT_ACCUMS for more information. A corresponding variable exists for observation data called OBS_PCP_COMBINE_INPUT_LEVELS. Examples:

     FCST_PCP_COMBINE_INPUT_ACCUMS = 1
     FCST_PCP_COMBINE_INPUT_NAMES = P01M_NONE
     FCST_PCP_COMBINE_INPUT_LEVELS = "(0,*,*)"

     This says that the 1 hour accumulation field name is P01M_NONE and the level (0,*,*), which is NetCDF format to specify the first item of the first dimension.

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   OBS_PCP_COMBINE_INPUT_LEVELS
     See FCST_PCP_COMBINE_INPUT_LEVELS

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_OUTPUT_ACCUM
     Specify desired accumulation to be built from the forecast data. Units are assumed to be hours unless a time identifier such as Y, m, d, H, M, S is specifed at the end of the value, i.e. 30M or 1m. If this variable is not set, then FCST_VAR<n>_LEVELS is used.

     A corresponding variable exists for observation data called OBS_PCP_COMBINE_OUTPUT_ACCUM.

     Examples:

     15H

     This will attempt to build a 15 hour accumulation.

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

   FCST_PCP_COMBINE_OUTPUT_NAME
     Specify the output field name from processing forecast data. If this variable is not set, then FCST_VAR<n>_NAME is used.

     A corresponding variable exists for observation data called OBS_PCP_COMBINE_OUTPUT_NAME.

     Examples:

     APCP

     | *Used by:*  PCPCombine
     | *Family:*  [config]
     | *Default:*  Varies

