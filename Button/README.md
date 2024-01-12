# APG-Progect
Send the number of count each button click to Firebase with "to_database.js".

# How to use?
You set "to_database.js" in the directory inculding HTML file.<br>
Please add HTML code like below.<br>
``` diff_html
...
<head>
  ...
  <script type="module" src="to_database.js"></script> <!-- NOT FORGET set type "module"-->
  ...
</head>
<body>
  ...
  <button id="button1">button1</button> <!-- please set id "button1"-->
  <button id="button2">button2</button> <!-- please set id "button2"-->
  ...
</body>
...
```
Id "button1" is related to button1 count.<br>
Id "button2" is related to button2 count.<br>

# Parameter
database_name: database name<br>
interval: Interval of sending count(milliseconds)

# Note
When you debug, please run code on the local host server or site like Twitch. If you run html directry, code is NOT run.
