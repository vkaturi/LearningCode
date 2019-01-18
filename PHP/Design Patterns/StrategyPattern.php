<?php

/*

We consider use of the strategy design pattern when we need to choose between similar classes that are different only in their implementation. For these cases, the strategy pattern instructs us to create an interface that the classes can implement, while the choice of which of the classes to implement is done during the program runtime.

What are the strategy design pattern characteristics?
-----------------------------------------------------
There are three main code sections that are the hallmarks of the strategy pattern:

	- Several classes that implement the same interface.
	- A code that chooses from which of the classes to create an object.
	- A client class that is fed with the object, and performs the task that the program is meant to do.

When to consider the use of the strategy design pattern?
--------------------------------------------------------
The strategy pattern is a good solution for those cases in which we need the program to select which code alternative, of several similar code alternatives, to implement at runtime (i.e. when the program is running).

*/

interface InterfaceLogger {
    function log($message);
}

class FileLogger implements InterfaceLogger {
    public function log($message) {
        // code to write logging information to file system
    }   
}

class DatabaseLogger implements InterfaceLogger {
    public function log($message) {
        // code to write logging information to database
    }   
}

class EmailLogger implements InterfaceLogger {
    public function log($message) {
        // code to write logging information to email
    }   
}

// Let's assume users of our framework are allowed to choose an specific logger through some configuration file by typing file, database or email and our framework is able to know it:

$loggerType = App::getConfig('logger');

// Now we can easily find out which logger to use using strategy design pattern:

switch($loggerType) {
    case "file":
        $logger = new FileLogger();
        break;
    case "database":
        $logger = new DatabaseLogger();
        break;
    case "email":
        $logger = new EmailLogger();
        break;
    default:
        $logger = new FileLogger();
}

// And then throughout our framework, we can use $logger->log() method which would automatically know which logger type to use.

// Hence to conclude, when we have multiple ways to perform the same task (in software language when we have multiple algorithms to perform the same operation), we should consider implementing the Strategy pattern. 


?>
