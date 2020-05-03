## Import DUMP file in to Oracle Autonomous Database

The below process will outline the steps to import a DUMP file from Object Storage Bucket in to Oracle Autonomous Database.

### Pre-requisites

- Oracle Insta Client [Steps Here](/InstaClient/README.MD)
- DUMP file in Object Storage Bucket
- URL to the DUMP file 
- OCI Credentails to Access the Object Storage bucket
- Access to Autonomous Database to create CREDENTIAL and Schema Objects


### Step 1: create CREDNETAIL in Autonomous Database

Before executing CREATE_CREDENTIAL make sure to give Execute on DBMS_CLOUD to user

    GRANT EXECUTE on DBMS_CLOUD to {USER}; # RUN as ADMIN

Now Connect as USER and create credentail using the **DBMS_CLOUD.CREATE_CREDENTIAL** using the below. More detailed steps are avialable [here](/Export/README.md) (Refer to Step 4)   

    BEGIN
    DBMS_CLOUD.CREATE_CREDENTIAL(
    credential_name => 'OS_CRED',
    username => 'oracleidentitycloudservice/xxxxxx.xxxxxx@example.com',
    password => '{AUTH TOKEN}');
    END;
    /
    
  ![alt Text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/Export/Images/OS_CRED.PNG)
  
### Step 2 : Gather necessarty details

Gather below important information as needed for the impdp utility. 

   - Autonomous Database credentails [ Username & Password]
   - Service Name [myadw_low]
   - Object Storage File URL [https://objectstorage.eu-frankfurt-1.oraclecloud.com/n/mytenancy/b/dump_bucket/o/SH_exp01.dmp]
   - Directory [DATA_PUMP_DIR can be used]
   - Credential [ OS_CRED from Step 1]
  
 ### Step 3 : Import using impdp
 
 From the information gathered in Step 2, We can write the below impdp command
 
     impdp SAMPLE_SH/*****@***_low directory=data_pump_dir credential=OS_CRED dumpfile=https://objectstorage.eu-frankfurt-1.oraclecloud.com/n/***/b/dump_bucket/o/SH_exp01.dmp
   
Open a command line window and execute the above command 

