# Minutes

---
### Meeting 1

Date: Friday, 9/6

Business:
- Introduced the project
- Defined project scope 
- Discussed project objectives and real world applications

Actions:
- Fork WfInstances-browser repo
- Run the app and populate the database
- Add a ‘simulate’ button that opens a blank popup
---
### Meeting 2

Date: Tuesday, 9/17

Business:
- Discussed the tools needed to start on this project, specifically WRENCH
- Clarified the main goal of the project and its applications

Actions:
- Read WRENCH documentation
- Add tooltip to simulate button
- Add simulation description to usage popup
- Add to the docker compose.yml so that there is a running wrench-daemon process
- Implement a hello world simulation in the simulation popup
---
### Meeting 3

Date: Tuesday, 9/24

Business:
- Reviewed progress since last week's meeting
- Discussed problem areas
- Reviewed REST APIs

Actions:
- Continue working on getting the hello world simulation to run
---
### Meeting 4

Date: Tuesday, 10/1

Business:
- Reviewed progress so far, discussed issues with the current course of action
- Decided to change tactics and use the WRENCH Python API for the duration of the project instead of Javascript and the Rest API.
- Began the process of developing a system to run the simulation on the back-end
  - Edited the api Dockerfile to install WRENCH and related software
  - Edited api/src/wfinstances/router.py to run WRENCH
  - Edited simulator.js to communicate with the back-end to start the simulation

Actions:
- Create a simulation that simulates a "hello world" program using the Python API.
---
### Meeting 5

Date: Tuesday, 10/8

Business:
- Discussed possible improvements to make to code written in the last week
- Discussed next steps to simulate a workflow
- Considered possible output visualization

Actions:
- make do_simulation take three arguments instead of just the request_body
- Figure out where to find the id and pass it to the back end
- Turn the json string into a file so simulation.start has valid input
- use read_workflow_as_json to simulate a workflow
---
### Meeting 6

Date: Tuesday, 10/15

Business:
- Investigated issue of Alyssa's computer being unable to run the simulation
- Discussed options for displaying the input and output of the simulation

Actions:
- Implement a way for the user to customize the hardware specifications of the simulation
- Display the results of the simulation
---
### Meeting 7

Date: Tuesday, 10/22

Business:
- Discussed different options for the UI of the hardware customization and came to a conclusion to create a table with numerical inputs and sliders
- Discussed the upcoming presentation and possibilities for visuals

Actions:
- Move the xml string parsing from the frontend to the backend for better encapsulation
- Modify the UI to include a table with sliders and numerical inputs
- Get output from the simulation including the job completed, its start time, and its end time
- If prev. item completed, begin working on a way to visualize the output data
---
### Meeting 8

Date: Tuesday, 10/29

Business:
- Reviewed progress made in the last week
- Discussed options for visualization and more clearly defined how the Gantt chart may be set up
- Discussed options for unit testing

Actions:
- Change id from 1 base to 0 base
- Change prefix to be the id
- Create a map between the bare metal compute service and the host in order to define which cluster a task is run on
- Find a software that will provide options for visualizing the data and create a graph
---
### Meeting 9

Date: Tuesday, 11/5

Business:
- Attempted unsuccesfully to integrate plotly into the ui docker container and create a graph

Actions:
- Find an alternative to plotly to create the data visualization
- Integrate the visualization software and create a "hello world" graph
---
### Meeting 10

Date: Tuesday, 11/12

Business:
- Discussed options for a Gantt chart
- Decided on apex chart
- Reviewed existing line chart

Actions:
- Merge branches and resolve all conflicts
- Create a poster draft
- Display a Gantt chart
---
### Meeting 11

Date: Tuesday, 11/19

Business:
- Reviewed first draft of poster and made edits
- Drew a rough sketch of the software architecture graph

Actions:
- Draw final sortware architecture graph
- Fix font to be a sans-serif font
- Remove first example of the Gantt chart and the line charts
- Add a screenshot of the simulate button
---
