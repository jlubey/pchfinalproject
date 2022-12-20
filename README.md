<b>WHCL SONG LIST</b>

This project can be used as a simple way to view songs being entered into Spinitron by a radio station as an HTML table. The Spinitron API that can be integrated with radio station websites not extremely useful, and for any small college station looking to list the songs that have been played on their website in an easy way this project can fill the gap.

In its current form, the project needs to be run every 6 hours to capture all of the music being played. I envision this process being automated to run alone and update the song list.

The radio station in my code is WHCL 88.7 Clinton, NY, run out of Hamilton College. Any other station that uses Spinitron can be subbed in by changing the URL to match that station (url = f"https://spinitron.com/your_station_here").

Stumped on making a playlist of music that you like? You can also remove the # from line 81 and run the code - it will choose and display 10 songs at random pulled from what has been playing at the station and entered into Spinitron. The more you run the code, the more songs will be pulled for your random playlist!
