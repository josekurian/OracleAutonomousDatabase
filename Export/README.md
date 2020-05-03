## Export Oracle Autonomous Database Schema

Below steps will outline the process to export a Oracle Autonomous Database Schema using Oracle Insta Client expdp utility.

### Pre-requisites
- Oracle Insta Client setup [Steps Here](/InstaClient/README.md)
- DB User with export privileges
- Object Storage Bucket
- Username and Auth Token for access the Object Storage Bucket

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
 
 ### Step 4: Move DUMP file to Object Storage Bucket
 
 Since we cannot SSH to Autonomous Database to copy/move the dump file, we will move the file to a Object Storage bucket.
 
 This has two steps:
 
   **1. Create CREDENTAIL**

  This credentail will allow Autonomous Database service to authenticate with Object Storage bucket for read/write operations.
  We would need two details to create this CREDENTAIL:
  
   - Cloud UserName
   
   This can be gathered from your OCI Console. Will be as below. 
   
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/UserDetails.PNG)
   
   - Auth Token
   
   From above screen click on UserName and you will be taken to user details screen. Under **Resorces** we have an option to generate **Auth Tokens**
   
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/AuthToken.PNG)
   
   Generate an Auth Token and copy it for next step. Note that it can only be copied now and will not be displayed later.
  
 - Create CREDENTIAL 
 
 Now that we have both UserName and Auth Token, we will run the below code to create a CLOUD CREDENTAIL for Object Storage bucket.
 
    BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(
    credential_name => 'OS_CRED',
    username => 'oracleidentitycloudservice/xxxxxx.xxxxxx@example.com',
    password => '{AUTH TOKEN}');
    END;
    /
 
 ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/OS_CRED.PNG)

  **2. Move File using Credentail**
  
  For this step we would need details like Object Storage URL, Namespace and bukcet name. 
  
  - [Object Storage End Points](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/objectstorage/20160918)
  - Object Storage Namespace ( Usually the tenancy name , can be found in **OCI Console - Governance - Tenancy Details** ) 
  
  So for example if my bucket is in **Frankfurt** region with Namespace **mytenancy** and bucket name **dump_bucket** and my I want my file name to be **SH_exp01.dmp**. The URL will be as below.
  
       https://objectstorage.eu-frankfurt-1.oraclecloud.com/n/mytenancy/b/dump_bucket/o/SH_exp01.dmp
       
 And finally to move my dump file from DATA_PUM_DIR to Object Storage bucket, I use below code:
 
     BEGIN
       DBMS_CLOUD.PUT_OBJECT(credential_name => 'OS_CRED',
         object_uri => 'https://objectstorage.eu-frankfurt-1.oraclecloud.com/n/sehubemeaprod/b/dump_bucket/o/SH_exp01.dmp',
         directory_name => 'DATA_PUMP_DIR',
         file_name => 'SH_exp01.dmp');
    END;
    /

The same can be seen in the below screenshot.

![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/exp_OS_Move.PNG)
