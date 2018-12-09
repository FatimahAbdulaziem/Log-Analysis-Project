# Logs Analysis 
Log Analysis is an **internal reporting tool** that has been built using Python and Postgresql commands to discover a set of informative information about sets of articlas and thier authors which thier data have been saved into a pre-built database.

## Installation
To Run This Project:
  - Download and Install Python 3 from [here](https://www.python.org/downloads/)
  - Install Linux-based virtual machine from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
  - Install vagrant Software from [here](https://www.vagrantup.com/downloads.html) - this software used to configure the VM and share files between the VN and the Host Computer  
  - Use Github to clone or download the Configuration folder for VM 
     ```
     $git clone  https://github.com/udacity/fullstack-nanodegree-vm.git
     ```
  - Start the VM using `vagrant up ` and `vagrant ssh` command in your command line 
  - Request newsdata.sql from udacity/me then load the data of newsdata.sql file into your local database by changing the directory to `/vagrant` then run `psql -d news -f newsdata.sql`
  - Finally, change directory to the project's directory and write `python Reporting_Tool.py` or `python3 reporting_Tool.py` to see thr results of my project

## Usage
This Project has a set of postgresql views that have been created to get the desired results :
 - AllRequests view has been created to calculate the total requests for all articlas per day 
              ```
                 create view AllRequests as
                 select date(time) as date, Count(Status) as requests from log group by date"
              ```
 - ErrorRequests view has been created to calculate the total for only Error requests that has requested per day
            ```
                  create view ErrorRequests as 
                  select date(time) as date, count(status) as Error_requests from log where (status like '4%' or status like '5%')
                  group by date
                  order by date
            ```




