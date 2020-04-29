#############################################################################################################
# Copyright(c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.
# StopADB.py
#
# @author: Rampradeep Pakalapati
#
# Supports Python 3 and above
#
# coding: utf-8
##############################################################################################################
# PythonSDK for OCI:
#
# One should install "oci" package into the python environment for the usage of 
# this script
#
# 			pip install oci 
#
###################################################################################################################
import time
import oci
import os
import json
from pandas.io.json import json_normalize
import pandas as pd
from oci import config
print("\n")
print(".........................................................................................................")
print("................................. The Program Starts Here................................................")
print(".........................................................................................................")
print("\n")

compartment_id = 'ocid1.compartment.oc1..xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
reg = ['us-phoenix-1','us-ashburn-1','uk-london-1','ap-seoul-1','ap-tokyo-1','eu-frankfurt-1','ca-toronto-1']

print("\n")
print("Gathering ADB information from regions :", reg)
print("\n")
print(".........................................................................................................")
print("............................Stopping the Autonomous Databases............................................")
print(".........................................................................................................")
adwlist = pd.DataFrame([])
for i in range(0,len(reg)):
    config = {
        "user": "ocid1.user.oc1..zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
        "key_file": "/home/opc/Scripts/keys/oci_api_key.pem",
        "fingerprint": "33:22:91:ae:h1:37:0z:24:be:ca:9b:79:ff:bb:42:21",
        "tenancy": "ocid1.tenancy.oc1..yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
        "region": reg[i],
        "compartment_id": compartment_id }
    adw = oci.database.DatabaseClient(config)
    df = adw.list_autonomous_databases(compartment_id,lifecycle_state='AVAILABLE' )
    adwlisttemp = pd.DataFrame([])
    print("\n")
    print(" Stopping ADB instances from :",reg[i])
    print("\n")
    if len(df.data)>0:
        for x in range(0,len(df.data)):
            row = df.data[x]
            row = str(row)
            row = json.loads(row)
            adwlisttemp = adwlisttemp.append(json_normalize(row),sort=False)
            region = reg[i]
            adwlisttemp['region']= region
            adwins = adwlisttemp['id'].tolist()
            instance = adwins[x]
            print("     Stopping the instance #",x+1,":",instance)
            print("\n")
                
            try:
                adw.stop_autonomous_database(autonomous_database_id=instance)
                time.sleep(72)
                print("Stopped ADW Instance...")
                print("\n")
            except Exception as e:
                print("\n\t" + e.message)
                print("Unabled to Stop ADW Instance")
                print("\n")
            
    else:
        print("#############   No Instances Running Currently   ########################")
    
    adwlist = pd.concat([adwlist, adwlisttemp])
print("\n")
print(".........................................................................................................")
print("............................Completed Stopping the Autonomous Databases..................................")
print(".........................................................................................................")
if len(adwlist.index)>0:
    adwins = adwlist['id'].tolist()
    print("\n")
    print("###############  No of ADB Instances Stopped :", len(adwins))
    print("\n")
    print(".........................................................................................................")
    print("..............................Below is the list of Autonomous Datbases STOPPED...........................")
    print(".........................................................................................................")
    print("\n")
    print(adwlist[['db_name','license_model','cpu_core_count','region']])
    print("\n")
else:
    print("\n")
    print("No of ADB Instances Stopped : 0")
    print("\n")
    print(".........................................................................................................")
    print("..............................Below is the list of Autonomous Datbases STOPPED...........................")
    print(".........................................................................................................")
    print("\n")
    print("NONE")
    print("\n")
print(".........................................................................................................")
print("...............................Program Ends Here.........................................................")
print(".........................................................................................................")
