# HeraldoApi

Guerrilla (unnoficial) Api for ["Heraldo de Aragon"](http://www.heraldo.es/ "Heraldo.es")
</br>
WARNING: Your IP can be banned for the site if you use this library. Use under your own risk.

# Requirements
google-chrome-stable (version >= 59.0) </br>
chromedriver (version >= 2.33)</br>
selenium (version >=3.8.0)</br>
python (version >= 3.4.2) </br>
</br>
Tested and developed on debian 8 server

# Usage
## Import
```from HeraldoApi import HeraldoApi```

## Launch modes
`api = HeraldoApi(<argument, "parser" by default)`
``` 
Modes: 
        parser -> Only start the parser elements (RoboBrowser)
        writer -> Only start the writing elemnts (Selenium)
        join   -> Starts whole system (RoboBrowser and Selenium) 
```

# Functions
`register_account(user, password, email)`
</br>
Creates a new account, ready to use. It use a yopmail email adress, choose your preferred.

# TODO list
- [X] Register in the system
- [ ] Post in a new
- [ ] Read a new
- [ ] Parse all news of a section (implemented but not working)
