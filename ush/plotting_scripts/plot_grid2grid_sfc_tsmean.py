#!/usr/bin/env python
'''
Program Name: plot_grid2grid_sfc_tsmean.py
Contact(s): Mallory Row
Abstract: Reads mean forecast hour files from plot_grid2grid_sfc_ts.py to make dieoff plots
History Log:  Second version
Usage: 
Parameters: None
Input Files: ASCII files
Output Files: .png images
Condition codes: 0 for success, 1 for failure
'''
############################################################################
##### Import python modules
from __future__ import (print_function, division)
import os
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import warnings
import logging
import plot_defs as pd
import pandas as pandas
#############################################################################
##### Settings
np.set_printoptions(suppress=True)
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelsize'] = 15
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['axes.titlesize'] = 15
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.formatter.useoffset'] = False
warnings.filterwarnings('ignore')
colors = ['black', 'darkgreen', 'darkred', 'indigo', 'blue', 'crimson', 'goldenrod', 'sandybrown', 'thistle']
##############################################################################
##### Read in data and set variables
#forecast dates
month_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sdate = os.environ['START_T']
syear = int(sdate[:4])
smon = int(sdate[4:6])
smonth = month_name[smon-1]
sday = int(sdate[6:8])
edate = os.environ['END_T']
eyear = int(edate[:4])
emon = int(edate[4:6])
emonth = month_name[emon-1]
eday = int(edate[6:8])
date_filter_method = os.environ['DATE_FILTER_METHOD']
#input info
model_names = os.environ['MODEL_NAMES'].replace(" ", ",").split(",")
nmodels = len(model_names)
cycle = os.environ['CYCLE']
lead_list = os.environ['LEAD_LIST'].replace(", ", ",").split(",")
leads = np.asarray(lead_list).astype(float)
region = os.environ['REGION']
grid = "G2"
plot_stats_list = os.environ['PLOT_STATS_LIST'].replace(", ", ",").split(",")
nstats = len(plot_stats_list)
fcst_var_name = os.environ['FCST_VAR_NAME']
fcst_var_level = os.environ['FCST_VAR_LEVEL']
obs_var_name = os.environ['OBS_VAR_NAME']
obs_var_level = os.environ['OBS_VAR_LEVEL']
#ouput info
logging_filename = os.environ['LOGGING_FILENAME']
logger = logging.getLogger(logging_filename)
logger.setLevel("DEBUG")
formatter = logging.Formatter("%(asctime)s.%(msecs)03d (%(filename)s:%(lineno)d) ""%(levelname)s: %(message)s","%m/%d %H:%M:%S")
file_handler = logging.FileHandler(logging_filename, mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
ch = logging.StreamHandler()
logger.addHandler(ch)
plotting_out_dir_base = os.environ['PLOTTING_OUT_DIR']
plotting_out_dir = os.path.join(plotting_out_dir_base, "sfc")
####################################################################
logger.info(" ")
logger.info("------> Running "+os.path.realpath(__file__))
logger.debug("----- for "+date_filter_method+" start date:"+sdate+" "+date_filter_method+" end date:"+edate+" cycle:"+cycle+"Z forecast hour means for region:"+region+" fcst var:"+fcst_var_name+"_"+fcst_var_level+" obs var:"+obs_var_name+"_"+obs_var_level)
#############################################################################
##### Create image directory if does not exist
if not os.path.exists(os.path.join(plotting_out_dir, "imgs", cycle+"Z")):
    os.makedirs(os.path.join(plotting_out_dir, "imgs", cycle+"Z"))
##### Read data in data, compute statistics, and plot
#read in data
s=1
while s <= nstats: #loop over statistics
    stat_now = plot_stats_list[s-1]
    stat_formal_name_now = pd.get_stat_formal_name(stat_now)
    logger.debug("--- "+stat_now)
    m=1
    while m <= nmodels: #loop over models
        model_now = model_names[m-1]
        logger.debug(str(m)+" "+model_now)
        #intialize data array
        model_now_stat_now_means = np.ones_like(leads) * np.nan
        #get forecast hour mean file
        model_now_mean_file = plotting_out_dir+"/data/"+cycle+"Z/"+model_now+"/"+stat_now+"_mean_"+region+"_fcst"+fcst_var_name+fcst_var_level+"_obs"+obs_var_name+obs_var_level+".txt"
        if os.path.exists(model_now_mean_file):
            nrow = sum(1 for line in open(model_now_mean_file))
            if nrow == 0: #file blank
                logger.warning("Model "+str(m)+" "+model_now+": "+model_now_mean_file+" empty")
            else:
                logger.debug("Model "+str(m)+" "+model_now+": found "+model_now_mean_file)
                mean_cols = [ "LEADS", "VALS" ]
                model_now_data = pandas.read_csv(model_now_mean_file, sep=" ", header=None, names=mean_cols)
                model_now_stat_now_leads = model_now_data.loc[:]['LEADS'] 
                model_now_stat_now_vals = model_now_data.loc[:]['VALS']
                #check for any missing data in current model for requested forecast leads
                for l in range(len(leads)):
                    if leads[l] == model_now_stat_now_leads[l]:
                        if model_now_stat_now_vals[l] == '--':
                            model_now_stat_now_means[l] = np.nan
                        else:
                            model_now_stat_now_means[l] = model_now_stat_now_vals[l]
                    else:
                        ll = np.where(model_now_stat_now_leads == leads[l])[0]
                        if len(ll) != 0:
                            if model_now_stat_now_vals[ll[0]] == '--':
                                model_now_stat_now_means[l] = np.nan
                            else:
                                model_now_stat_now_means[l] = model_now_stat_now_vals[ll[0]]
                        else:
                            model_now_stat_now_means[l] = np.nan
        else:
            logger.warning("Model "+str(m)+" "+model_now+": "+model_now_mean_file+" missing")                 
        model_now_stat_now_means = np.ma.masked_invalid(model_now_stat_now_means)
        count_masked = np.ma.count_masked(model_now_stat_now_means)
        #plot individual statistic forecast hour mean with CI time seres
        if m == 1:
            #set up plot
            fig, ax = plt.subplots(1,1,figsize=(10,6))
            #forecast hour means
            ax.grid(True)
            ax.tick_params(axis='x', pad=10)
            ax.set_xlabel("Forecast Hour")
            ax.set_xticks(leads)
            ax.set_xlim([leads[0],leads[-1]])
            ax.tick_params(axis='y', pad=15)
            ax.set_ylabel("Mean")
            #ax.set_ylim()
            logger.debug("Plotting "+stat_now+" lead forecst hour means for "+model_now)
        ax.plot(leads, model_now_stat_now_means, color=colors[m-1], ls='-', linewidth=2.0, marker='o', markersize=7, label=model_now)
        m+=1
    ax.legend(bbox_to_anchor=(1.025, 1.0, 0.375, 0.0), loc='upper right', ncol=1, fontsize='13', mode="expand", borderaxespad=0.)
    ax.set_title("Fcst: "+fcst_var_name+"_"+fcst_var_level+" Obs: "+obs_var_name+"_"+obs_var_level+" "+str(stat_formal_name_now)+'\n'+grid+"-"+region+" "+date_filter_method+" "+cycle+"Z "+str(sday)+smonth+str(syear)+"-"+str(eday)+emonth+str(eyear)+" Means\n\n", fontsize=14, fontweight='bold')
    logger.debug("--- Saving image as "+plotting_out_dir+"/imgs/"+cycle+"Z/"+stat_now+"_fhrmeans_fcst"+fcst_var_name+fcst_var_level+"_obs"+obs_var_name+obs_var_level+"_"+grid+region+".png")
    plt.savefig(plotting_out_dir+"/imgs/"+cycle+"Z/"+stat_now+"_fhrmeans_fcst"+fcst_var_name+fcst_var_level+"_obs"+obs_var_name+obs_var_level+"_"+grid+region+".png", bbox_inches='tight')
    s+=1
