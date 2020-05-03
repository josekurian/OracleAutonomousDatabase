
## Insta Client Setup on Windows for Autonomous Datawarehouse

   The below steps will outline the setup of InstaClient on Windows machine. 

### Pre-requisites

  Below are the pre-requisites to perform this
  - Autonomous Data Warehouse Wallet file needs to be downloaded
  - Access to edit the Environment Variables 


### Step 1: Download the Oracle Insta Client Software 

  Oracle Insta Client can be downloaded from the below URL according to your ADB version.

  https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html

  We would need to download the below three files to perform multiple actions like connect using sqlplus, Data Pump tools like expdp, impdp etc.   

    - instantclient-basic-windows.x64.19.6.0.0.0dbru.zip
    - instantclient-sqlplus-windows.x64.19.6.0.0.0dbru.zip
    - instantclient-tools-windows.x64.19.6.0.0.0dbru.zip
  
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/InstaClientSoftware.PNG)
  
   The important part to remember is all the three zip files should be extracted to the same folder. To achive this we should place all files in same folder and use tools like 7Zip and do **Extract Here** on all three files 

   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/InstaClientAfterExtract.PNG)


### Step 2: Create folders inside the Insta Client Folder
 
   We need to create a path for TNS_ADMIN to place the sqlnet.ora and tnsnames.ora files.
 
   - Create a folder **network** and then inside that **admin** folder

  For example if my Insta Client home is **D:\Programs\instantclient_19_6** then after creating the above folders I will have a path like **D:\Programs\instantclient_19_6\network\admin**



### Step 3: Edit the sqlnet.ora file inside wallet Folder

  Unzip your wallet file lets say the folder is as below.  
        
   **D:\Programs\Wallet_PMADWC**

  This path contains the cwallet.sso file which is needed to authenticate with Autonomous Database.

  We will need to edit the sqlnet.ora file to change the DIRECTORY path to refer to the above location.
  
  ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/sqlnetchange.PNG)



### Step 4: Copy the tnsnames.ora and sqlnet.ora files

   Copy the **tnsnames.ora** and **sqlnet.ora** to the path created in Step2 Ex. **D:\Programs\instantclient_19_6\network\admin**
  
  ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/WalletFiles.PNG)
  
 
 ### Step 5: Add Environment Variables PATH and TNS_ADMIN
 
   Navigate to Environment Variables 
   - Run (Windows + R)  -> "SystemPropertiesAdvanced"
   
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/run.PNG)
   
   - Click on **Environment Variables** 
   
   - Add Insta Client home **D:\Programs\instantclient_19_6** to **Path** variable 
   - Add new variable TNS_ADMIN with path **D:\Programs\instantclient_19_6\network\admin** 
   
   ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/EnvVariables.png)
   

### Step 6: Testing ADW connection from Command line

  We can now test the connectivity to the Autonomous Database using windows command line and sqlplus which we downloaded in step 1
  
  - Open command prompt ( Start --> cmd )
  - Enter command like **sqlplus ADMIN/{password}@{dbname_low}**
  
  ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/InstaClient/Images/ConnectTest.PNG)



 
 
