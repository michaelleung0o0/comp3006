Stock Monitoring System
============

Python software to view stocks.<br>
This is a stock monitoring system in 2015 autumn.

## Requirements
- for macOS only
- python 2.7
- homebrew( optional --> http://brew.sh )
- wxpython ( brew install wxpython )
- requests library ( pip install requests or https://github.com/kennethreitz/requests )
- sqldb library ( brew install mysql-connector-c && pip install mysql-python )
- requirement mysql at localhost

# Reference

## MainWindow (class)
main.py

### Terminal
    python main.py
- run the program in terminal, and then find the coding directory. Type "python main.py" to run the program.

### Localhost server
    sms
    table name = userinfo
    table row = uid(int) primarykey,
    			username(varchar), 
    			password(varchar),
    			refresh_rate(int)
    
 