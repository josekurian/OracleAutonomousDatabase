## Export Oracle Autonomous Database Schema

Below steps will outline the steps to export a Oracle Autonomous Database Schema using Oracle Insta Client expdp utility.

### Pre-requisites
- Oracle Insta Client setup [Steps Here](/InstaClient/README.md)
- User with export privileges

### Step 1 : Gather Necessary Details

To export a schema we would need below details
  - UserName [ ADMIN user can be used ]
  - Password
  - Schema Name [ Name of schema to be exported ]
  - Directory  [ Default DIRECTORY **DATA_PUMP_DIR** ]
  - Connection Name [ example myadw_low ]
  
### Step 2 : Form expdp Command and execute it 

We need to form a command something like below 

     expdp ADMIN/{password}@{service_name} schemas=SAMPLE_SH directory=data_pump_dir dumpfile=SH_exp%U.dmp logfile=export.log
     
Make sure to change the values as per your environment and execute it from command line 
