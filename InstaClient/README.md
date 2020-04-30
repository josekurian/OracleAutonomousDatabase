
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
  
   The important part to remember is all the three zip files should be extracted to the same folder. To achive this we should place all files in same folder and use tools like 7Zip and do **Extract Here** on all three files 


 ### Step 2: Create folders inside the Insta Client Folder
 
   We need to create a path for TNS_ADMIN to place the sqlnet.ora and tnsnames.ora files.
 
   - Create a folder **network** and then inside that **admin** folder

  For example if my Insta Client home is **D:\Programs\instantclient_19_6** then after creating the above folders I will have a path like **D:\Programs\instantclient_19_6\network\admin**



### Step 3: Edit the sqlnet.ora file inside wallet Folder

  Unzip your wallet file lets say the folder is as below.  
        
        **D:\Programs\Wallet_PMADWC**

  This path contains the cwallet.sso file which is needed to authenticate with Autonomous Database.

  We will need to edit the sqlnet.ora file to change the DIRECTORY path to refer to the above location.



### Step 4: Copy the tnsnames.ora and sqlnet.ora files

   Copy the **tnsnames.ora** and **sqlnet.ora** to the path created in Step2 Ex. **D:\Programs\instantclient_19_6\network\admin**
  


Make the edit as needed


 
 
