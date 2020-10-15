# <div align="center">Constructing a User Data Pipeline<div>

<p align="center">
  <img src="https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/Clash_Banner.png" />
</p>

## <div align="center">Project Overview<div>
Skills Demonstrated: *Data Pipelines, Data Wrangling, Interacting with APIs*<br>
Libraries and Programs: *Python, merge, request*<br>

For some time, I've been interested in constructing a data pipeline to gather my own data. This project is a fun take on that task, pulling user data from the popular phone game, Clash of Clans, and storing it in a "database" (a csv file). I've broken down my approach into several steps to make it easy to understand and, if you'd like, replicate.<br>

NOTE: In the future, I'd like to use Task Scheduler to automatically run this script on a daily or bi-daily basis. This would quickly turn my "database" into an actual database that I could explore and model.<br>

### **Step 1:** Generate a token to gain access to the Clash of Clans API.<br>

Go to https://developer.clashofclans.com/#/, create an account, and (from your account page) create a key.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/create_key.png "Create a Key") ![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/api_token.png "API Token")<br>

### **Step 2.** Generate request URLs for a clan and for specific members to check the URL formatting.<br>

Navigate to 'documentation', 'clans' or 'players', and click GET.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/documentation.png "Documentation Page")<br>

Click the 'i' button by 'Response Class' and input your API token.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/authorization.png "Authorize")<br>

Enter a clantag or playertag under 'Parameters' and click 'Try it out!' at the bottom. This generate a request and a request URL.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/clan_URL.png "Request URL")<br>

Compare the request URL to the clantag or playertag you used. We will replicate this formatting in the next two steps.<br>

### **Step 3.** Build a function (get_clan_data) to collect 'tag' information from all members in a clan.<br>

Create a function to request clan data using a clantag. Authorization is required, so be sure to include it as your header.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/request_header.png "Header")<br>
![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/get_clan_data.png "get_clan_data Function")<br>

### **Step 4.** Build a function (get_profile_data) to collect user data based on 'tag'.<br>

Repeat the previous step but replace the clantag request URL with a playertag request URL.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/get_player_data.png "get_player_data Function")<br>

### **Step 5.** Loop through get_profile_data using the tags collected from get_clan_data.<br>

### **Step 6.** Clean and export user data.<br>
