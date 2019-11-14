.. _sysconf:

System Configuration
====================

This chapter is a guide on configuring METplus Wrappers.

Config Best Practices
---------------------

Below is a list of Best Practices:

1. Set your log level to an appropriate level:

  a. Debug is the most verbose and is useful for developers and when you are troubleshooting problems
  b. Info is less verbose than Debug and is the recommended level to initially set your log level to
  c. Warning - only logs warnings, error, or critical events
  d. Error - only logs errors or critical events
  e. Critical - least verbose

2. Direct your logging either to stdout or to a log file
3. Review your log file to verify that all your processes ran cleanly
4. The order in which you list your METplus Wrappers config files matters. The last config file on the command line will over-ride any key-values defined in an earlier config file
5. Check the master_metplus.conf file, as it contains all the key-valies based on what you have specified. This will help you determine whether you forgot to replace any *</path/to>* with valid paths or to verify that you have defined things as you expected.

Config File Structure
---------------------

METplus Wrappers employs a hierarchy of configuration files employed in METplus Wrappers. At the lowest level are the "set-and-forget" type configuration files that reside in the *<METplus_installation_dir>/parm/metplus_config*. At the next level are the configuration files that pertain to a user's specific needs in the *<METplus_installation_dir>/parm/use_cases/<specific_use_case>*.

Four configuration files are required for METplus Wrappers to be fully configured (i.e. all keywords are defined by either whitespace or a valid value):

  1. metplus_system
  2. metplus_data
  3. metplus_logging
  4. metplus_runtime

By default, key-values that require the user's input are set to *</path/to>*. Make sure to replace these with the appropriate directory for your project.

Additional configuration files are optional and the key-values defined there will over-ride any values defined in the four mandatory METplus Wrappers configuration files. These additional configuration files enable users to use a common set of configuration files and to create customized environments for their verification tasks.

Common Config Variables
-----------------------

Timing Control
~~~~~~~~~~~~~~

This section describes the METplus Wrappers configuration variables that are used to control which times are processed. It also covers functionality that is useful for processing data in realtime by setting run times based on the clock time when METplus Wrappers is started.

LOOP_BY
^^^^^^^

METplus Wrappers can be configured to loop over a set of valid times or a set of initialization times. This is controlled by the METplus Wrappers configuration variable called LOOP_BY. If the value of this variable is set to INIT or RETRO, looping will be relative to initialization time. If the value is set to VALID or REALTIME, looping will be relative to valid time. Older versions of METplus Wrappers used a True/False variable named LOOP_BY_INIT. METplus Wrappers still supports using this variable, although it is recommended that users update their config files to use LOOP_BY instead. LOOP_BY_INIT will eventually be removed.

Looping by Valid Time
^^^^^^^^^^^^^^^^^^^^^

When looping over valid time (LOOP_BY = VALID or LOOP_BY = REALTIME), the following variables must be set:

.. **VALID_TIME_FMT**:

:term:`VALID_TIME_FMT`:
This is the format of the valid times the user can configure in the METplus Wrappers. The valie of VALID_BEG and VALID_END must correspond to this format. Example: VALID_TIME_FMT=%Y%m%d%H. Using this format, the valid time range values specified must be defined as YYYYMMDDHH, i.e. 2019020112.

**VALID_BEG**:
This is the first valid time that will be processed. The format of this variable is controlled by VALID_TIME_FMT. For example, if VALID_TIME_FMT=%Y%m%d, then VALID_BEG must be set to a valid time matching YYYYMMDD, such as 20190201.

**VALID_END**:
This is the last valid time that can be processed. The format of this variable is controlled by VALID_TIME_FMT. For example, if VALID_TIME_FMT=%Y%m%d, then VALID_END must be set to a valid time matching YYYYMMDD, such as 20190202. Note that the time specified for this variable will not necessarily be processed. It is used to determine the cutoff of run times that can be processed. For example, if METplus Wrappers is configured to start at 20190201 and end at 20190202 processing data in 48 hour increments, it will process valid time 20190201 then increment the run time to 20190203. This is later than the VALID_END value, so execution will stop. However, if the increment is set to 24 hours (see VALID_INCREMENT), then METplus Wrappers will process valid times 20190201 and 20190202 before ending execution.

**VALID_INCREMENT**:
This is the number of seconds to add to each run time to determine the next run time to process. This value must be greater than or equal to 60 because METplus Wrappers currently does not support processing intervals of less than one minute.

The following is a configuration that will process valid time 20190201 at 00Z until 20190202 at 00Z in 6 hour (21600 seconds) increments::

   [config]
   LOOP_BY = VALID
   VALID_TIME_FMT = %Y%m%d%H
   VALID_BEG = 2019020100
   VALID_END = 2019020200
   VALID_INCREMENT = 21600

This will process data valid on 20190201 at 00Z, 06Z, 12Z, and 18Z as well as 20190202 at 00Z. For each of these valid times, METplus Wrappers can also loop over a set of forecast leads that are all valid at the current run time. See 'Looping Over Forecast Leads' [sec:4.3.1.4] for more information.

Looping by Initialization Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When looping over initialization time (LOOP_BY = INIT or LOOP_BY = RETRO), the following variables must be set:

**INIT_TIME_FMT**:
This is the format of the initialization times the user can configure in METplus Wrappers. The value of INIT_BEG and INIT_END must correspond to this format. Example: INIT_TIME_FMT = %Y%m%d%H. Using this format, the initialization time range values specified must be defined as YYYYMMDDHH, i.e. 2019020112.

**INIT_BEG**:
This is the first initialization time that will be processed. The format of this variable is controlled by INIT_TIME_FMT. For example, if INIT_TIME_FMT = %Y%m%d, then INIT_BEG must be set to an initialization time matching YYYYMMDD, such as 20190201.

**INIT_END**:
This is the last initialization time that can be processed. The format of this variable is controlled by INIT_TIME_FMT. For example, if INIT_TIME_FMT = %Y%m%d, then INIT_END must be set to an initialization time matching YYYYMMDD, such as 20190202. Note that the time specified for this variable will not necissarily be processed. It is used to determine the cutoff of run times that can be processed. For example, if METplus Wrappers is configured to start at 20190201 and end at 20190202 processing data in 48 hour increments, it will process 20190201 then increment the run time to 20190203. This is later than the INIT_END valid, so execution will stop. However, if the increment is set to 24 hours (see INIT_INCREMENT), then METplus Wrappers will process initialization times 20190201 and 20190202 before ending executaion.

**INIT_INCREMENT**:
This is the number of seconds to add to each run time to determine the next run time to process. This value must be greater than or equal to 60 because METplus Wrappers currently does not support processing intervals of less than one minute.

The following is a configuration that will process initialization time 20190201 at 00Z until 20190202 at 00Z in 6 hour (21600 second) increments::

  [config]
  LOOP_BY = INIT
  INIT_TIME_FMT = %Y%m%d%H
  INIT_BEG = 2019020100
  INIT_END = 2019020200
  INIT_INCREMENT = 21600

This will process data initialized on 20190201 at 00Z, 06Z, 12Z, and 18Z as well as 20190202 at 00Z. For each of these initialization times, METplus Wrappers can also loop over a set of forecast leads that are all initialized at the current run time. See 'Looping Over Forecast Leads' [sec:4.3.1.4] for more information.

Looping over Forecast Leads
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Many of the wrappers METplus Wrappers will also loop over a list of forecast leads relative to the current valid/initialization time that is being processed.

**LEAD_SEQ**:
This variable can be set to a comma-separated list of integers to define the forecast leads (hours) that will be processed relative to the initialization/valid time. Currently only hours are supported for these values. Future versions of METplus Wrappers will allow sub-hourly forecast leads. For example::

  [config]
  LEAD_SEQ = 3,6,9

If LOOP_BY = VALID and the current run time is 20190201 at 00Z, then three times will be processed:

| 1. Initialized on 20190131 at 21Z / valid on 20190201 at 00Z
| 2. Initialized on 20190131 at 18Z / valid on 20190201 at 00Z
| 3. Initialized on 20190131 at 15Z / valid on 20190201 at 00Z

If LOOP_BY = INIT and the current run time is 20190201 at 00Z, then three times will be processed:

| 1. Initialized on 20190201 at 00Z / valid on 20190201 at 03Z
| 2. Initialized on 20190201 at 00Z / valid on 20190201 at 06Z
| 3. Initialized on 20190201 at 00Z / valid on 20190201 at 09Z

You can also define LEAD_SEQ using a special notation for many forecast leads. The notation is **begin_end_incr(b,e,i)** where b = the first lead value, e = the last lead value (inclusive), and i = the increment between leads. For example::

  [config]
  LEAD_SEQ = begin_end_incr(0,12,3)

is equivalent to setting::

  [config]
  LEAD_SEQ = 0,3,6,9,12

Grouping forecast leads is possible as well using a special version of the LEAD_SEQ variable for the **SeriesByLead Wrapper Only**. If SERIES_BY_LEAD_GROUP_FCSTS = True, then you can define groups of forecast leads that will be evaluated together. You can define any number of these groups by setting configuration variables LEAD_SEQ_1, LEAD_SEQ_2, ... LEAD_SEQ_N. You can define the value with a comma-separated list of integers (hours) or using the special begin_end_incr(b,e,i) notation described just above. Each list must have a corresponding label to describe it using LEAD_SEQ_<n>_LABEL, i.e. LEAD_SEQ_1 must have the corresponding variable LEAD_SEQ_1_LABEL set. For example::

  [config]
  SERIES_BY_LEAD_GROUP_FCSTS = True
  LEAD_SEQ_1 = 0,6,12,18
  LEAD_SEQ_1_LABEL = Day1
  LEAD_SEQ_2 = begin_end_incr(24,42,6)
  LEAD_SEQ_2_LABEL = Day2

**INIT_SEQ**:
If METplus Wrappers is configured to loop by valid time (LOOP_BY = VALID), you can use INIT_SEQ instead of LEAD_SEQ. This is a list of initialization hours that are available in the data. This is useful if you know when the data is initialized and you need to use a different list of forecast leads depending on the valid time being evaluated. For example::

  [config]
  LOOP_BY = VALID
  INIT_SEQ = 0,6,12,18

At valid time 20190201/00Z, this initialization sequence will build a forecast lead list of 0,6,12,18,24,30,etc. and at valid time 20190201/01Z, this initialization sequence will build a forecast lead list of 1,7,13,19,25,31,etc.

You can also restrict the forecast leads that will be used by setting LEAD_SEQ_MIN and LEAD_SEQ_MAX. For example, if you want to only process forecast leads between 12 and 24 you can set::

  [config]
  LEAD_SEQ_MIN = 12
  LEAD_SEQ_MAX = 24

At valid time 20190201/00Z, this initialization sequence will build a forecast lead list of 12,18,24 and at valid time 20190201/01Z, this initialization sequence will build a forecast lead list of 13,19.

Setting minimum and maximum values will also affect the list of forecast leads if you use LEAD_SEQ. LEAD_SEQ takes precedence over INIT_SEQ, so if you have both variables set in your configuration, INIT_SEQ will be ignored in favor of LEAD_SEQ.

Realtime Looping
^^^^^^^^^^^^^^^^

To make running in realtime easier, METplus Wrappers supports defining the begin and end times relative to the current clock time. For example, if the current time is 20190426_08:17 and you start METplus Wrappers with::
  
  [config]
  VALID_END = {now?fmt=%Y%m%d%H}

then the value of VALID_END will be set to 2019042608. You can also use {today} to substitute the current YYYYMMDD, i.e. 20190426. You cannot change the formatting for the 'today' keyword.

You can use the 'shift' keyword to shift the current time by any number of seconds. For example, if you start METplus Wrappers at the same clock time with::

  [config]
  VALID_BEG = {now?fmt=%Y%m%d%H?shift=-86400}

then the value of VALID_BEG will be set to the current clock time shifted by -86400 seconds (24 hours backwards), or 2019042508.

If VALID_INCREMENT is set to 21600 seconds (6 hours), then METplus Wrappers will process the following valid times:

| 20190425_08
| 20190425_14
| 20190425_20
| 20190426_02
| 20190426_08

However, you may want to configure METplus Wrappers to process at 00Z, 06Z, 12Z, and 18Z of a given day instead of 02Z, 08Z, 14Z, and 20Z. Having to adjust the shift amount differently if you are running at 08Z or 09Z to get the times to line up would be tedious. Instead, use the 'truncate' keyword. The value set here is the number of seconds that is used to determine the interval of time to round down. If you want to process every 6 hours, set 'truncate' to 21600 seconds::

  [config]
  VALID_BEG = {now?fmt=%Y%m%d%H?shift=-86400?truncate=21600}

This will rounds down the value to the nearest 6 hour interval of time. Starting METplus Wrappers on or after 06Z but before 12Z on 20190426 will result in VALID_BEG = 2019042506 (clock time shifted backwards by 24 hours then truncated to nearest 6 hour time).

Starting METplus Wrappers on 20190426 at 08:16 with the following configuration::

  [config]
  LOOP_BY = VALID
  VALID_TIME_FMT = %Y%m%d%H
  VALID_BEG = {now?fmt=%Y%m%d%H?shift=-86400?truncate=21600}
  VALID_END = {now?fmt=%Y%m%d%H}
  VALID_INCREMENT = 21600

will process valid times starting on 20190425 at 06Z every 6 hours until the current run time is later than 20190426 at 08Z, which will result in processing the following valid times:

| 20190425_06
| 20190425_12
| 20190425_18
| 20190426_00
| 20190426_06

.. note::

   When using the 'now' keyword, the value of VALID_TIME_FMT must be set to the same value as the 'fmt' used in the 'now' item in VALID_BEG and VALID_END. In the above example, this would be the %Y%m%d%H portion within values of the VALID_TIME_FMT, VALID_BEG, and VALID_END variables.

Field Info
~~~~~~~~~~

This section describes how METplus Wrappers configuration variables can be used to define field information that is sent to the MET applications to read forecast and observation fields.

**FCST_VAR<n>_NAME**:
Set this to the name of a forecast variable that you want to evaluate. <n> is any integer greater than or equal to 1, i.e.::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR2_NAME = RH

**FCST_VAR<n>_LEVELS**:
Set this to a comma-separated list of levels or a single value. FCST_VAR1_LEVELS corresponds to FCST_VAR1_NAME, FCST_VAR2_LEVELS corresponds to FCST_VAR2_NAME, etc. For example::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR1_LEVELS = P500, P750

will process TMP at P500 and TMP at P750.

**OBS_VAR<n>_NAME**:
Set this to the corresponding observation variable that you want to evaluate with FCST_VAR<n>_NAME. If this value is not set for a given <n> value, then it will be assumed that the same name as the forecast name will be used.

**OBS_VAR<n>_LEVELS**:
Set this to a comma-separated list of levels or a single value. If OBS_VAR<n>_LEVELS and OBS_VAR<n>_NAME are not set, it will be assumed that the same name/level combination as the forecast data will be used. For example, setting::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR1_LEVELS = P500
  FCST_VAR2_NAME = RH
  FCST_VAR2_LEVELS = P750, P250

without setting OBS_VAR1_NAME or OBS_VAR2_NAME is the equivalent of setting::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR1_LEVELS = P500
  FCST_VAR2_NAME = RH
  FCST_VAR2_LEVELS = P750, P250
  OBS_VAR1_NAME = TMP
  OBS_VAR1_LEVELS = P500
  OBS_VAR2_NAME = RH
  OBS_VAR2_LEVELS = P750, P250

This will compare:

| TMP/P500 in the forecast data to TMP/P500 in the observation data
| RH/P750 in the forecast data to RH/P750 in the observation data
| RH/P250 in the forecast data to RH/P250 in the observation data

If you set::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR1_LEVELS = P500, P750
  OBS_VAR1_NAME = TEMP
  OBS_VAR1_LEVELS = "(0,*,*)","(1,*,*)"

METplus Wrappers will compare:

| TMP/P500 in the forecast data to TEMP at (0,\*,\*) in the observation data
| TMP/P750 in the forecast data to TEMP at (1,\*,\*) in the observation data

.. note::
   NetCDF level values that contain (\*,\*) notation must be surrounded by quotation marks so it will not be misinterpreted as a list of items.

The number of level items must be equal in each list for a given comparison. If you define separate names for a forecast and observation, you will need to define separate levels for both even if they are equivalent. For example, setting FCST_VAR1_NAME, FCST_VAR1_LEVELS, and OBS_VAR1_NAME, but not setting OBS_VAR1_LEVELS will result in an error.

The field information specified using the \*_NAME/\*_LEVELS variables will be formatted to match the field info dictionary in the MET config files and passed to the appropriate config file to evaluate the data. The previous configuration comparing TMP (P500 and P750) in the forecast data and TEMP ((0,*,*)) in the observation data will generate the following in the MET config file::

  fcst = {field = [ {name="TMP"; level="P500";} ];}
  obs = {field = [{name="TEMP"; level="(0,*,*)";} ];}

and then comparing TMP (P500 and P750) in the forecast data and TEMP ((1,*,*)) in the observation data will generate the following in the MET config file::

  fcst = {field = [ {name="TMP"; level="P500";} ];}
  obs = {field = [{name="TEMP"; level="(1,*,*)";} ];}

Note that some MET applications allow multiple fields to be specified for a single run. If the MET tool allows it and METplus Wrappers is configured accordingly, these two comparisons would be configured in a single run.

**[FCST/OBS]_VAR<n>_THRESH**:
Set this to a comma-separated list of threshold values to use in the comparison. Each of these values must begin with a comparison operator (>, >=, =, ==, !=, <, <=, gt, ge, eq, ne, lt, or le). For example, setting::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR1_LEVELS = P500
  FCST_VAR1_THRESH = le0.5, gt0.4, gt0.5, gt0.8

will add the folloing information to the MET config file::

   fcst = {field = [ {name="TMP"; level="P500"; cat_thresh=[ le0.5, gt0.4, gt0.5, gt0.8];} ];}

Note that the value for FCST_VAR<n>_THRESH will not be copied to OBS_VAR<n>_THRESH if it is not set. These items are independent of each other.

**[FCST/OBS_VAR<n>_OPTIONS**:
Set this to add additional information to the field dictionary in the MET config file. The item must end with a semi-colon. For example::

  [config]
  FCST_VAR1_NAME = TMP
  FCST_VAR1_LEVELS = P500
  FCST_VAR1_OPTIONS = GRIB_lvl_typ = 105; ens_phist_bin_size = 0.05;

will add the following to the MET config file::

  fcst = {field = [ {name="TMP"; level="P500"; GRIB_lvl_typ = 105; ens_phist_bin_size = 0.05;} ];}

Note that the value for FCST_VAR<n>_OPTIONS will not be copied to OBS_VAR<n>_OPTIONS if it is not set. These items are independent of each other.

**[ENS_VAR<n>_[NAME/LEVELS/THRESH/OPTIONS]**:
**Used with EnsembleStat Wrapper only.** Users may want to define the ens dictionary item in the MET EnsembleStat config file differently than the fcst dictionary item. If this is the case, you can use these variables. If it is not set, the values in the corresponding FCST_VAR<n>_[NAME/LEVELS/THRESH/OPTIONS] will be used in the ens dictionary.

Directory and Filename Template Info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The METplus Wrappers use directory and filename template configuration variables to find the desired files for a given run.

**Using Templates to find Observation Data:**
The following configuration variables describe input observation data::

  [dir]
  OBS_GRID_STAT_INPUT_DIR = /my/path/to/grid_stat/input/obs

  [filename_templates]
  OBS_GRID_STAT_INPUT_TEMPLATE = {valid?fmt=%Y%m%d}/prefix.{valid?fmt=%Y%m%d%H}.ext

| The input directory is the top level directory containing all of the observation data. The template contains items with keywords that will be substituted with time values for each run. After the values are substituted, METplus Wrappers will check to see if the desired file exists relative to the input directory. At valid time 20190201_12Z, the full desired path of the observation input data to grid_stat will be:
|   /my/path/to/grid_stat/input/obs/20190201/prefix.2019020112.ext

Note that the template contains a dated subdirectory. This cannot go in the OBS_GRID_STAT_INPUT_DIR variable because the dated subdirectory changes based on the run time.

| METplus Wrappers does not need to be configured to loop by valid time to find files using a template containing valid time information. For example, at initialization time 20190201_12Z and forecast lead 3, the valid time is calculated to be 20190201_15Z and the full desired path of the observation input data to grid_stat will be:
|   /my/path/to/grid_stat/input/obs/20190201/prefix.2019020115.ext

The 'init' and 'valid' are keywords used to denote initialization and valid times respectively. Other keywords that are supported include 'lead', 'offset', 'da_init', and 'cycle' which can all be used to find forecast data and data assimilation data depending on the task.

**Using Templates to find Forecast Data:**
Most forecast files contain the initialization time and the forecast lead in the filename. The keywords 'init' and 'lead' can be used to describe the template of these files::

  [dir]
  FCST_GRID_STAT_INPUT_DIR = /my/path/to/grid_stat/input/fcst

  [filename_templates]
  FCST_GRID_STAT_INPUT_TEMPLATE = prefix.{init?fmt=%Y%m%d%H}_f{lead?fmt=%3H}.ext

| For a valid time of 20190201_00Z and a forecast lead of 3, METplus Wrappers will look for the following forecast file:
|   /my/path/to/grid_stat/input/fcst/prefix.2019013121_f003.ext

**Using Templates to find Data Assimilation Data:**
Some data assimilation files contain offset and da_init (data assimilation initialization) values in the filename. These values are used to determine the valid time of the data. Consider the following configuration::

  [config]
  PB2NC_OFFSETS = 6, 3
  
  [dir]
  PB2NC_INPUT_DIR = /my/path/to/prepbufr

  [filename_templates]
  PB2NC_INPUT_TEMPLATE = prefix.{da_init?fmt=%Y%m%d}_{cycle?fmt=%H}_off{offset?fmt=%2H}.ext

| The PB2NC_OFFSETS list tells METplus Wrappers the order in which to prioritize files with offsets in the name. At valid time 20190201_12Z, METplus Wrappers will check if the following file exists:
|   /my/path/to/prepbufr/prefix.20190201_18_off06.ext

| The offset is added to the valid time to get the data assimilation initialization time. Note that 'cycle' can be used interchangeably with 'da_init'. It is generally used to specify the hour of the data that was generated. If that file doesn't exist, it will check if the following file exists:   
|   /my/path/to/prepbufr/prefix.20190201_15_off03.ext

**Shifting Times in Filename Templates:**
Users can use the 'shift' keyword to adjust the time referenced in the filename template relative to the run time. For example, if the input files used contained data from 01Z on the date specified in the filename to 01Z on the following day. In this example, for a run at 00Z you want to use the file from the previous day and for the 01Z to 23Z runs you want to use the file that corresponds to the current day. Here is an example::

  [filename_templates]
  OBS_POINT_STAT_INPUT_TEMPLATE = {valid?fmt=%Y%m%d?shift=-3600}.ext

Running the above configuration at a valid time of 20190201_12Z will shift the valid time backwards by 1 hour (3600 seconds) resulting in 20190201_11Z and will substitute the current day into the template, giving a filename of 20190201.ext. Running at valid time 20190201_00Z, the shift will result in a file time of 20190131_23Z, so the filename will be 20190131.ext that is generated by the template.

**Using Windows to find Valid Files:**
The [FCST/OBS]_FILE_WINDOW_[BEGIN/END] configuration variables can be used if the time information in the input data does not exactly line up with the run time but you still want to process the data. The default value of the file window begin and end variables are both 0 seconds. If both values are set to 0, METplus Wrappers will require that a file matching the template with the exact time requested exists. If either value is non-zero, METplus Wrappers will examine all of the files under the input directory that match the template, pull out the time information from the files, and use the file with the time closest to the run_time. For example, consider the following configuration::

  [config]
  OBS_FILE_WINDOW_BEGIN = -7200
  OBS_FILE_WINDOW_END = 7200

  [dir]
  OBS_GRID_STAT_INPUT_DIR = /my/grid_stat/input/obs
  
  [filename_templates]
  OBS_GRID_STAT_INPUT_TEMPLATE = {valid?fmt=%Y%m%d}/pre.{valid?fmt=%Y%m%d}_{valid?fmt=%H}.ext

| For a run time of 20190201_00Z, and a set of files in the input directory that looks like this:
|   /my/grid_stat/input/obs/20190131/pre.20190131_22.ext
|   /my/grid_stat/input/obs/20190131/pre.20190131_23.ext
|   /my/grid_stat/input/obs/20190201/othertype.20190201_00.ext
|   /my/grid_stat/input/obs/20190201/pre.20190201_01.ext
|   /my/grid_stat/input/obs/20190201/pre.20190201_02.ext

The following behavior can be expected for each file:

  1. The first file matches the template and the file time is within the window, so the filename and time difference relative to the valid time (7200 seconds, or 2 hours) is saved.
  2. The second file matches the template, the file time is within the window, and the time difference is less than the closest file so the filename and time difference relative to the valid time (3600 seconds, or 1 hour) is saved.
  3. The third file does not match the template and is ignored.
  4. The fourth file matches the template and is within the time range, but it is the same distance away from the valid time as the closest file. GridStat only allows one file to be processed so it is ignored (PB2NC is currently the only METplus Wrapper that allows multiple files to be processed).
  5. The fifth file matches the template but it is valid outside of the -2 to +2 hour window range and is ignored.

Therefore, METplus Wrappers will use /my/grid_stat/input/obs/20190131/pre.20190131_23.ext as the input to grid_stat in this example.

**Wrapper Specific Windows:**
A user may need to specify a different window on a wrapper-by-wrapper basis. If this is the case, you can override the file window values for each wrapper. Consider the following configuration::

  [config]
  PROCESS_LIST = PcpCombine, GridStat, EnsembleStat
  OBS_FILE_WINDOW_BEGIN = 0
  OBS_FILE_WINDOW_END = 0
  OBS_GRID_STAT_FILE_WINDOW_BEGIN = -1800
  OBS_GRID_STAT_FILE_WINDOW_END = 1800
  OBS_ENSEMBLE_STAT_FILE_WINDOW_END = 3600

Using the above configuration, PcpCombine will use +/- 0 hours and require exact file times. GridStat will use -1800/+1800 for observation data and EnsembleStat will use -0/+3600 for observation data. OBS_ENSEMBLE_STAT_FILE_WINDOW_BEGIN was not set, so the EnsembleStat wrapper will use OBS_FILE_WINDOW_BEGIN.

Config Quick Start Example
--------------------------

**Track and Intensity Use Case with Sample Data**

  1. Create a directory where you wish to store the sample data. Sample datasets are specific to each use case (see [sec:2.5.1]) and are required in order to be able to run the use case.
  2. Retrieve the sample data from the GitHub repository:
    
    a. In your browser, navigate to https://www.github.com/NCAR/METplus/releases
    b. Locate the latest release and click on the *sample_data-cyclone_track_feature.tgz* link associated with that release
    c. Save it to the directory you created above, hereafter referred to as INPUT_DATA_DIRECTORY
    d. cd to your $INPUT_DATA_DIRECTORY and uncompress the tarballe: *tar xvfz sample_data-cyclone_track_feature.tgz*
    e. when you perform a listing of the sample_data directory, the INPUT_DATA_DIRECTORY/sample_data/GFS contains the data you will need for this use case
  
  3. Set up the configuration file:
    
    a. Your METplus Wrappers install directory will hereafter be referred to as METplus_INSTALL
    b. Verify that all the *</path/to>* values are replaced with valid paths in the METplus_INSTALL/parm/metplus_conf/metplus_data.conf and METplus_INSTALL/parm/metplus_conf/metplus_system.conf files
    c. Two configuration files are used in this use case, track_and_intensity.conf file and tcmp_mean_median.conf to take cyclone track data, and using TcPairs which wraps the MET TC-Pairs tool (to match ADeck and BDeck cyclone tracks to generate matched pairs and error statistics). The TCM-PRPlotter is then used (wraps the MET tool plot_tcmpr.R) to generate a mean and median plots for these matched pairs
    d. In your editor, open the METplus_INSTALL/METplus/parm/use_cases/track_and_intensity.conf file and perform the following:
      
      1. Replace any *</path/to>* with actual paths by setting the following:
        
        a. OUTPUT_BASE to where you wish to save the output:
        b. TCPAIRS_ADECK_INPUT_DIR to INPUT_DATA_DIRECTORY/sample_data/GFS/track_data
      
      2. Save your changes and exit your editor
    
    e. In your editor, open the METplus_INSTALL/METplus/parm/use_cases/track_and_intensity/examples/tcmpr_mean_median.conf
      
      1. Verify that PROCESS_LIST is set to TcPairs, TCMPRPlotter. This instructs METplus Wrappers to run the TcPairs wrapper first (TC-Pairs) followed by the TCMPR plotter wrapper (plot_TCMPR.R).
  
  4. Run the use case:
    
    a. Make sure you have set the following environment in your .cshrc (C Shell) or .bashrc (Bash):
      
      1. csh: setenv RSCRIPTS_BASE $MET_BASE/scripts/Rscripts
      2. bash: export RSCRIPTS_BASE $MET_BASE/scripts/Rscripts
      3. Refer to section [sec:2.7] for the full instructions on setting up the rest of your environment
      4. On your command line, run::
         
           master_metplus.py -c use_cases/track_and_intensity/track_and_intensity.conf -c use_cases/track_and_intensity/examples/tcmpr_mean_median.conf
        
      5. When complete, you will have a log file in the output directory you specified, and under the tc_pairs directory you will see .tcst files under the 201412 subdirectory. These are the matched pairs created by the MET tool Tc-pairs and can be viewed in any text editor.
      6. Plots are generated under the tcmpr_plots subdirectory in .png format. You should have the following plots which can be viewed by any graphics viewers such as 'display' on Linux/Unix hosts:
        
        a. AMAX_WIND-BMAX_WIND_mean.png
        b. AMAX_WIND-BMAX_WIND_median.png
        c. AMSLP-BMSLP_mean.png
        d. AMSLP-BMSLP_median.png
        e. TK_ERR_mean.png
        f. TK_ERR_median.png

User Defined Config
-------------------

You can define your own custom config variables that will be set as environment variables when METplus is run. MET config files can read environment variables, so this is a good way to customize information that is read by those files. To create add a custom config variable, add a section to one of your METplus config files called [user_env_vars]. Under this header, add as many variables as you'd like. For example, if you added the following to your METplus config file::

  [user_env_vars]
  VAR_NAME = some_text_for_feb_1_1987_run

and you added the following to a MET config file that is used::

  output_prefix = ${VAR_NAME}

then at run time, the MET application will be run with the configuration::

  output_prefix = some_text_for_feb_1_1987_run

You can also reference other variables in the METplus config file. For example::

  [config]
  INIT_BEG = 1987020104

  [user_env_vars]
  USE_CASE_TIME_ID = {INIT_BEG}

This is the equivalent of calling (bash example shown)::
  
  $ export USE_CAST_TIME_ID=1987020104 

on the command line at the beginning of your METplus run. You can access the variable in the MET config file with ${USE_CASE_TIME_ID}.

A-Z Config Glossary
-------------------
