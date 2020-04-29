
# OracleAutonomousDatabase
This project has some scripts that will help in automation of Oracle Autonomous Database administration activities.

Inorder for the scripts to work, one should have a working python environment and should install Oracle Clould python SDK package "oci"

      pip install oci 
  
## StopADB.py

  This script will pick all the running instances from the list of specified regions and stops them one by one and finally provides the
  number of instances stopped followed by the list of instances.
  
  Sample output below
      ![alt text](https://github.com/prampradeep/OracleAutonomousDatabase/blob/master/images/StopADB_output.JPG)
  
