<b>WHCL FM SONG LIST</b>

Isn't it frustrating when you're listening to a college radio station stream online, but in order to see the songs that are playing you have to go to a different website? I already have too many tabs open!

I began this project picturing a way to use webscraping to make a simple HTML list of the songs that are being entered into the website Spinitron by radio stations so that the list can be integrated into the radio's website. While Spinitron has ways to do this through its API, some small radio stations do not take advantage of this feature. This project is meant to fill that gap.

The code is listed here as whcl.py. I built the code around a radio station in Upstate NY based at Hamilton College - WHCL 88.7 Clinton, NY. Any other station that uses Spinitron can be subbed in by changing the URL in the code to match that station (url = f"https://spinitron.com/your_station_here"). Running the code will produce three documents: a CSV file of all songs scraped, a second CSV file with duplicate songs removed, and the HTML file with the full list of songs. In its current form, the code needs to be run every 6 hours to capture all of the music being played. In the future, I would like this process to be automated.

The code also includes a bonus feature: stumped on making a playlist of music that you like? You can remove the # from line 81 and run the code - it will choose and display 10 songs at random pulled from what has been playing at the station based on its Spinitron entries. The more often you run the code, the more songs will be pulled for your random playlist!

And as always, support small independent radio stations. Stream online at <a href="https://www.whcl.org">whcl.org!</a>
