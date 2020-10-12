# <div align="center">Constructing a User Data Pipeline<div>

### <div align="center">Project Overview<div>
Skills Demonstrated: *Data Pipelines, Data Wrangling,*<br>
Libraries and Programs: *Python, merge, request*<br>

For some time, I've been interested in constructing a data pipeline. This project is a fun take on that task, pulling user data from the popular phone game, Clash of Clans, and storing it in a "database" (a csv file). I've broken down my approach into several steps to make it easy to understand and, if you'd like, replicate.<br>

**Step 1:** Generate a token to access to the Clash of Clans API.<br>

![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/create_key.png "Create a Key") ![alt_text](https://github.com/nphorsley59/Clash_Pipeline/blob/main/Figures/ex_token.png "API Token")<br>

**Step 2.** Generate request URLs for a clan and for specific members.<br>

**Step 3.** Build a function (get_clan_data) to collect 'tag' information from all members in a clan.<br>

**Step 4.** Build a function (get_profile_data) to collect user data based on 'tag'.<br>

**Step 5.** Loop through get_profile_data using the tags collected from get_clan_data.<br>

**Step 6.** Clean and export user data.<br>
