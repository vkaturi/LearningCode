<?php

/*
When class A cannot do its job without class B, we say that class A is dependent on class B. In order
to perform this dependency, many programmers create the object from class B in the constructor of
class A.

For example, if we have the classes of Car and HumanDriver, the Car class is dependent on the
HumanDriver class, so we might be tempted to create the HumanDriver class object in the
constructor of the Car class.

*/

class HumanDriver {
	// Method to return the driver name.
	public function sayYourName($name)
	{
		return $name;
	}
}

// Car is dependent on HumanDriver
class Car {
	protected $driver;
	// We create the driver object in the constructor,
	// and use this object to populate the $driver variable.
	public function __construct()
	{
		$this->driver = new HumanDriver();
	}

	// A getter method that returns the driver object
	// from within the car object

	public function getDriver()
	{
		return $this -> driver;
	}
}

/*
Although creating the human driver object inside the Car class might look like the right thing to do,
we are going to face a real problem the first time that we need to switch dependencies. For example,
if the technological advancements dictate us a car that is driven by a robot, we will find our self in
a problem since the Car class only knows how to handle human drivers.

The problem that stems from directly creating the driver object inside the Car class is also known
as tight coupling between classes, something that should be avoided as much as possible. In fact,
tight coupling is considered to be a bad practice for the following reasons:

	- The programmers need to be concerned with more than one class when they introduce new classes to their code. In our example, if we would like to change the class on which the Car class is dependent from HumanDriver to RobotDriver, except for introducing the new class to our code, we also need to change the Car class so it can handle the new type of driver.
	- We will have difficulties in performing unit testing since it is meant to check one class at a time.

In fact, when we do tight coupling between classes, we violate a fundamental principle of well
designed code called the “single responsibility principle” (SRP), according to which a class should
have only one responsibility. In order to respect this principle, the only code that the Car class needs
to handle is that of cars, without messing with any other code

The solution: dependency injection
----------------------------------
Now that we understand why creating an object from one class inside the constructor of another
class is unfavorable, let’s see how to fix the problem by using dependency injection.
First, let’s rewrite the Car class so it can set its own $driver property that is passed as a parameter
to the constructor
*/

// The Car class gets the driver object injected
// to its constructor
class Car {
	protected $driver;
	// The constructor sets the value of the $driver
	public function __construct($driver)
	{
		$this -> driver = $driver;
	}
	// A getter method that returns the driver object
	// from within the car object
	public function getDriver()
	{
		return $this -> driver;
	}
}

// We can now perform the dependency injection by first creating the Driver object and then injecting this object into the newly created Car object through the constructor.

$humanDriver = new HumanDriver();
$car = new Car($humanDriver);

// And Voila! We just performed dependency injection.
// Let’s test the code:

$humanDriver = new HumanDriver();
$car = new Car($humanDriver);
echo $car -> getDriver() -> sayYourName("Bob");

// Result:
// Bob


// Now that we have seen how dependency injection works, let’s see how easy it is to switch the
// dependency from HumanDriver to RobotDriver, saving us from changing the code in the Car class.
// First, let’s write the RobotDriver class with the sayYourName method.

class RobotDriver {
	public function sayYourName($name)
	{
		return $name;
	}
}

// We can leave the Car class without any changes since it depends on a driver but does not require any
// commitment to the type of the driver. The driver can be a robot, human, alien, etc. It really doesn’t
// matter as long as we supply a driver object.

class Car {
	protected $driver;
	// The constructor sets the value of the $driver
	public function __construct($driver)
	{
		$this -> driver = $driver;
	}
	// A getter method that returns the driver object
	// from within the car object
	public function getDriver()
	{
		return $this -> driver;
	}
}

// Now, we can create the driver object from the RobotDriver and inject it to the Car class without too much of a hassle.

$robotDriver = new RobotDriver();
$car = new Car($robotDriver);
echo $car -> getDriver() -> sayYourName("R2-D2");

/*
Result:
R2-D2
It is easy to switch dependencies if only we adopt the good practice of injecting the
objects from the outside.

The message to take home from this example would be that it is easy to switch dependencies if
only we avoid the bad practice of creating the objects on which the main class depends inside the
constructor, and adopt the good practice of injecting the objects on which the class depends from
the outside

How to make a dependency injection through a setter method?
-----------------------------------------------------------
We may also choose to inject the objects on which the class is dependent through a setter method.
Let’s start again by writing the HumanDriver class with exactly the same code as in the previous
example.

*/

interface Driver {
	public function sayYourName($name);
}

class HumanDriver implements Driver {
	public function sayYourName($name)
	{
		return $name;
	}
}

// We will equip the Car class with a setDriver() method that is responsible for setting the $driver value.

class Car {
	protected $driver;
	// The setDriver method sets
	// the value for the driver property
	public function setDriver(Driver $driver)
	{
		$this -> driver = $driver;
	}
	public function getDriver()
	{
		return $this -> driver;
	}
}

// Now, we can create the driver object outside the car, inject it to the car with the setDriver() method, and echo the driver’s name.

$driver = new HumanDriver();
$car = new Car();
// Inject the driver to the car object
$car -> setDriver($driver);
echo $car -> getDriver() -> sayYourName("Bob");

// Result:
// Bob

/*
Conclusion
-----------
When we use dependency injection we pass the objects on which our class depends
to the class from the outside.
When we use dependency injection we pass the objects on which our class depends to the class
from the outside, instead of creating these objects within the class. By doing so, we make our code
more maintainable and flexible. It is also advisable to type hint the injected objects in order to make
it clear on which type of objects does the main class depend.
*/

?>