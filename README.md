# NationalParkAnalysis

Analyze National Parks Data. 

Sources of data:

WorkFlow:
https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year) - Reports in csv format

https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Visitation%20By%20Park%20(1979%20-%20Last%20Calendar%20Year)

https://www.nps.gov/state/ca/index.htm - National sites in the state

https://www.infoplease.com/state-abbreviations-and-state-postal-codes - Postal Code data


Multiple reports are available for the national parks data for the last 20 years. The reports did not have location of the parks like State. 
https://irma.nps.gov/Stats/SSRSReports/National%20Reports/Annual%20Park%20Ranking%20Report%20(1979%20-%20Last%20Calendar%20Year)

I decided to scrape the nps.gov website to get the parks by state since my initial investigation only gave a subset of park data (e.g., wikipedia)

After some analysis I figured I could get the parks in the state by this link but I have to loop through all the state codes to get all the parks by each state
https://www.nps.gov/state/ca/index.htm for California data

The html code of interest for extracting the actual park data is 
<code>
<div class="col-md-9 col-sm-9 col-xs-12 table-cell list_left">
<h2></h2># This field has the type. Possible values: National Monument,National Park,National Historic Site, National Recreation Area
<h3><a href="/alca/" id="anch_9">Alcatraz Island</a></h3> #  This has the name of the national site
<h4>San Francisco, CA</h4> # This field has City followed by , and then state code
<p>
Alcatraz Island offers a close-up look at the site of the first lighthouse and US built fort on the West Coast, the infamous federal penitentiary long off-limits to the public, and the history making 18 month occupation by Indians of All Tribes. Rich in history, there is also a natural side to the Rock—gardens, tide pools, bird colonies, and bay views beyond compare.
</p> # this field has the description
</div>
  
 </code>
 
 h2 tag had the type of the national site. Eg: National Monument,National Park,National Historic Site, National Recreation Area
 h3 tag had the name of the national site
 h4 tag had the city and state code separated by ,
  p tag had the description of the park.
 
Since I was scarping the nps.gov for park name. As the data of interest here is name of the national site to get the geographical location I decided to store the information in this format in mongodb
 
 parkname:name of the park
 state:state where the park is located
 city:city of the park location
 type:type of park. Possible values:National Monument,National Park,National Historic Site, National Recreation Area
 description:description of the park

 
