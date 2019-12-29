# **GETZ**

To Do list desktop end user application, that can also be used a reminder/alarm clock.

## Requirements :

### To run locally :
External modules installed. Instructions below :
    * To install the external modules, open CMD/Terminal and navigate inside the Getz directory.
    Then run :
* On windows :
    ```bash
    pip install -r requirements.txt
    ```

* On Linux :
    ```bash
    pip3 install -r requirements.txt 
    ```


### Running the Program :
To run the program, open CMD/Terminal and navigate inside the Getz directory.

    Then run :
* On windows :
    Run from IDLE.

* On Linux :
    ```bash
    pip3 install -r requirements.txt 
    ```

## Working (Internal):
The project uses a database to save to entries in To-Do List and Tkinter for GUI.
When we enter a task in To-Do List and select a date, the task is saved in database.
When we enter the time, the task get updated. When we delete the task, it's get deleted from the database.
The APScheduler checks if the current time and the time given in the database is equal or not.
If they are equal, We will get a pop-up.

## Contribution 

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Author and List of Contributors

- [DeboDevelop](https://github.com/DeboDevelop)
- Ayan Pan
- [CGreenP](https://github.com/CGreenP)
- Prithul Banerjee
- [arkajitroy](https://github.com/arkajitroy)
