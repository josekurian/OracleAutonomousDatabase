## Export Oracle Autonomous Database Schema

Below steps will outline the process to export a Oracle Autonomous Database Schema using Oracle Insta Client expdp utility.

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
     
Make sure to change the values as per your environment and execute it from command line. Example below.
  
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/exportdmp.PNG)
   
 The export will take time depending your Schema size, You can check the size of your schema using below SQL statement.
 
    SELECT sum(bytes)/1024/1024/1024 as "Size in GB" from dba_segments where OWNER='SAMPLE_SH';
    
 ### Step 3 : Verify the export file
 
 The file will be available in **DATA_PUMP_DIR** which can be verified using below SQL statement
 
    SELECT * FROM DBMS_CLOUD.LIST_FILES('DATA_PUMP_DIR');
    
    
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/Data_Pump_Dir.PNG)
 
 
