The Assignment
Please build an application that does the following:

For individuals using the weather API:
- Using the Forecast API, request the weather forecast for the next 3 days for your local zip code
- Extract daily forecast information into a csv file named “daily_forecast.csv” with the following fields:
	- zipcode
	- date
	- maxtemp_f
	- mintemp_f
	- avgtemp_f
	- daily_chance_of_rain
	- daily_chance_of_snow
	- condition.text
	- condition.icon
- Extract hourly forecast information into a csv file named “hourly_forecast.csv” with the following fields:
- zipcode
	- date
	- time
	- temp_f
	- feelslike_f
	- heatindex_f
	- windchill_f
	- humidity
	- cloud
	- chance_of_rain
	- chance_of_snow
	- condition.text
	- condition.icon

For individuals using a different data source:
- Using no more than two API calls, extract two data sets that can be joined together.
- Your application should transform the raw payload in some way. For example, you could:
	-  Reduce the number of fields
	- Change the payload schema
	- Convert a JSON/XML/etc payload into a csv file
	- Generate aggregate metrics
	- Etc
- Your data should be stored in two separate csv files. Please include the schemas for each file in your documentation.

For all individuals:
- Please include a brief readme containing any instructions needed to execute your application and where to find the output files.
- Do not include any API keys directly in your code. Store them in a separate yaml file named “config.yaml”. Your application should read any API Keys from this file.
- This application should be completely portable; we should not need to download any dependent libraries for it to run. As such, it is encouraged that you leverage a container service such as Docker. This is not a requirement, however. You may include code in your application to download any dependent libraries. 
- You may assume that we have the necessary programing language, docker, and package manager (pip, npm, etc) installed. If you are using a language other than Python or JavaScript, please indicate which in your readme. Please do the same if using a container service other than docker.

Extra Credit
For bonus points, configure your application to expose your csv files on port 8000.