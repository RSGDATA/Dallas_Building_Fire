[comment]: <> (filename: task_list.md)


| **Data Preparation:**                                                                                                 	| **branch name** 	| **taker** 	| **pull requested** 	|   **merged** 	|
|-----------------------------------------------------------------------------------------------------------------------	|-----------------	|-----------	|--------------------	|------------	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Drop Columns:**                                                                                                     	|                 	|           	|                    	|            	|
| MAPSCO                                                                                                                	| main            	| RSGDATA   	|                    	|            	|
| Census Tract                                                                                                          	| main            	| RSGDATA   	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Drop Rows:**                                                                                                        	|                 	|           	|                    	|            	|
| stories < 100                                                                                                         	| main            	| RSGDATA   	|                    	|            	|
| total_saved > 0                                                                                                       	| main            	| RSGDATA   	|                    	|            	|
| total_value > 1                                                                                                       	| main            	| RSGDATA   	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Create Columns:**                                                                                                   	|                 	|           	|                    	|            	|
| % loss                                                                                                                	| main            	| RSGDATA   	|                    	|            	|
| lat                                                                                                                   	|                 	|           	|                    	|            	|
| lon                                                                                                                   	|                 	|           	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Save starter data to new CSV file**,     will need down to here in main branch to      continue with further tasks. 	|                 	|           	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Analysis Tasks:**                                                                                                   	|                 	|           	|                    	|            	|
| **Basics:**                                                                                                           	|                 	|           	|                    	|            	|
| Regression Table / heat chart                                                                                         	|                 	|           	|                    	|            	|
| Describe basic statistics                                                                                             	|                 	|           	|                    	|            	|
| chart types of fires (pie)                                                                                            	|                 	|           	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Analyze fire frequency sources:**                                                                                   	|                 	|           	|                    	|            	|
| Time vs frequency frequency                                                                                           	|                 	|           	|                    	|            	|
| weather vs fire frequency                                                                                             	|                 	|           	|                    	|            	|
| heat map of all fires, might be nice to include city borders if we can find that.                                     	|                 	|           	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| **Analyze extent of damage:**                                                                                         	|                 	|           	|                    	|            	|
| Sprinkler & Fire Alarm vs % Loss  compare none, one of each, and both. Box chart?                                     	|                 	|           	|                    	|            	|
| battalion vs % loss                                                                                                   	|                 	|           	|                    	|            	|
| distance to battalion vs % loss                                                                                       	|                 	|           	|                    	|            	|
|    above, per structure type                                                                                          	|                 	|           	|                    	|            	|
| stories vs % loss                                                                                                     	|                 	|           	|                    	|            	|
| structure type vs % loss                                                                                              	|                 	|           	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|
| Still probably should demonstrate whether some inputs affect likelihood of a fire.                                    	|                 	|           	|                    	|            	|
|                                                                                                                       	|                 	|           	|                    	|            	|

Other notes if we want more to do:
Pull past weather data for City of Dallas for every day in range.  Use this to correlate frequency of fires with all available weather data (regression chart).
