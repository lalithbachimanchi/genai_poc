# Ingest Performance Test Results into Database
How to run the application?

1. Install Docker
   
3. Clone the repo

4. Go to the repo folder in terminal

5. run the command docker-compose up

You will see log of installations happening....

In the log, you will find below stack trace

  | 2023-07-30T11:55:26.145384Z 0 [Note] Event Scheduler: Loaded 0 events
db     | 2023-07-30T11:55:26.145803Z 0 [Note] mysqld: ready for connections.
db     | Version: '5.7.35'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
web_1  | No changes detected in app 'test_result_data_ingestion'
web_1  | Operations to perform:
web_1  |   Apply all migrations: admin, auth, contenttypes, sessions, test_result_data_ingestion
web_1  | Running migrations:
web_1  |   No migrations to apply.
web_1  | Watching for file changes with StatReloader
web_1  | Performing system checks...
web_1  | 
web_1  | System check identified no issues (0 silenced).
web_1  | July 30, 2023 - 11:55:29
web_1  | Django version 3.2.20, using settings 'genai_poc.settings'
web_1  | Starting development server at http://0.0.0.0:8001/
web_1  | Quit the server with CONTROL-C.

Copy the URL from stack trace

4. Hit in browser or postman [http://127.0.0.1:8000/ ](http://0.0.0.0:8001/)
  You should see a message "App is running"
