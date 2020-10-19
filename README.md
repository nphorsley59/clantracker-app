# <div align="center">Constructing a User Data Pipeline<div>
<p align="center">
  <img src="https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/Clash_Banner.png" />
</p>

## <div align="center">Project Overview<div>
Skills Demonstrated: *Data Pipelining, Data Wrangling, Interacting with APIs*<br>
Libraries and Programs: *Python, SQL, merge, request*<br>

For some time, I've been interested in constructing a data pipeline in Python to gather and analyze my own data. This project is a fun take on that task, pulling user data from the popular phone game, Clash of Clans, and storing it in a local MySQL database. I've broken down my approach into several steps to make it easy to understand and, if you'd like, replicate.<br>

## Part 1: Requesting Data from the Clash of Clans API
### Generate a token to gain access to the Clash of Clans API.
Go to https://developer.clashofclans.com/#/, create an account, and (from your account page) create a key.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/create_key.png "Create a Key") ![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/api_token.png "API Token")<br>

### Generate request URLs for a clan and for specific members to check the URL formatting.
Navigate to 'documentation', 'clans' or 'players', and click GET.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/documentation.png "Documentation Page")<br>

Click the 'i' button by 'Response Class' and input your API token.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/authorization.png "Authorize")<br>

Enter a clantag or playertag under 'Parameters' and click 'Try it out!' at the bottom. This generate a request and a request URL.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/clan_URL.png "Request URL")<br>

Compare the request URL to the clantag or playertag you used. We will replicate this formatting in the next two steps.<br>

### Build a function (get_clan_data) to collect clan data based on 'clantag'.
Create a function to request clan data using a clantag. Authorization is required, so be sure to include it as your header.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/request_header.png "Header")<br>
![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/get_clan_data.png "get_clan_data Function")<br>

### Build a function (get_player_data) to collect user data based on 'playertag'.
Repeat the previous step but replace the clantag request URL with a playertag request URL.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/get_player_data.png "get_player_data Function")<br>

### Loop through get_player_data using playertags collected from get_clan_data.
Now that we can request clan data and player data, we need to pull playertags from our clan data and loop them through get_player_data.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/playertag_loop.png "Playertag Loop")<br>

### Clean and export user data.
Clean and export whatever data you're interested in! I focused on 'tag', 'name', trophies', 'donations' and 'donationsReceived', but there are many more columns to explore. I've included a [sample data file]() if you'd like to see how I formatted my CSV.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/clean_and_export.png "Export Data")<br>

## Part 2: Creating and Filling an SQL Database
### 
