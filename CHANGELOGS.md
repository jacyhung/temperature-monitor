# Temperature-Monitor 0.1 (09/25/2022)

* Modified temp function to only retrieve value from database.
* Added a scheduler to automatically query the sensor in 1 second intervals.
  * Client sessions are now independent from sensor querying.
  * Previously, the query function was under the same temp function, and would run every 1 second from the ajax call. 
  The issue with this method was that multiple sessions to the webpage would cause the query function to run more often, causing issues. This was noticeable on the BME280 as querying the sensor faster than 1 second intervals would cause erroneous values (e.g. -62, 215).
  * Now, the querySensor function runs every 1 seconds and is determined by the scheduleTask function. The interval can be adjusted by modifying the `seconds=1` value in scheduleTask().