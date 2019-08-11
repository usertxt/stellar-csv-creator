## Stellar CSV Creator
This app's aim is to fetch inflation transactions from the Stellar network and automatically add them to a CSV file 
for easy tracking purposes.

### Information
**Start Date** (required): The date of the oldest transaction received  
**End Date** (optional): Create a range of transactions received with a specific end date  
**Stellar Address** (required): A Stellar address to receive transactions from  

An example of the output CSV file:  
**Date,Action,Volume,Symbol,Source,Memo**  
**2019-08-06T00:02:58Z,INCOME,8.3535963,XLM,Stellar Inflation,Inflation Payment**

### Configuring
Use the Settings tab to change the configuration to fit your needs. The CSV's **Source** and **Memo** fields can 
be changed. Use the **Minimum Threshold** and **Maximum Threshold** to target your typical inflation 
transactions. For example, if you usually receive an inflation payment of around 8.3535963 XLM, then set your 
Minimum Threshold to 8 and your Maximum Threshold to 8.6. Give yourself some room on either side of the 
threshold as inflation payments tend to vary.