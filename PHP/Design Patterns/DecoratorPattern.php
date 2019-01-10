<?php

/* 
Decorator pattern, falls under the category of structural patterns. In the Decorator pattern a class will add funtionality to another class, without changing the other classes structure. 

We use the decorator design pattern to add new optional features to our code without changing the existing classes. The new features are added by creating new classes that belong to the same type as the existing classes.

We can use the decorator pattern when we just want to give some added responsibility to our base class. This design pattern is a great alternative to a sub‑classing feature for extending functionality with some added advantages.

Example 1: 
Explanation: 
------------
An auto manufacturing company uses an interface to dictate to all of the implementing classes that they need to have price and description methods.

The company manufactures different types of cars, including: compact, sedan, SUV and luxury.

So an interface and it is implemented for the SUV and etc types

Possible Problem:
-----------------
The problem starts when customers are given the choice to add optional features to their car, like high end wheels, a car rear spoiler, or a sun roof. We wouldn't like to change the existing classes to include optional features, so we need a better solution.

Solution:
---------
When we want to add optional features to our code we use the decorator pattern, which instructs us to add to the basic classes that implement the interface, an abstract class that also implements the same interface. The abstract class is used as a super-class that the features classes inherit from.

The decorator pattern thus has the following structure:
	A decorator which is an abstract class that implements the interface.
	Sub-classes that inherit the decorator class.

The abstract class CarFeature implements the Car interface while, at the same time, it is used as the super-class that the concrete features classes inherit from.

The abstract class CarFeature implements the Car interface in an unusual way by re-defining the interface methods as abstract methods. The abstract class also holds a reference to an object that was created from one of the basic classes.

Source of the example:
----------------------
*/

interface Car {
  function cost();
  function description();
}


class Suv implements Car {
    function cost()
    {
      return 30000;
    }

    function description ()
    {
      return "Suv";
    }
}


abstract class CarFeature implements Car {
  protected $car;

  function __construct(Car $car)
  {
    $this->car = $car;
  }

  abstract function cost();
  
  abstract function description();
}

class SunRoof extends CarFeature {
    function cost ()
    {
        return $this->car->cost() + 1500;
    }

    function description()
    {
        return $this->car->description() . ",  sunroof";
    }
}


class HighEndWheels extends CarFeature {
    function cost ()
    {
        return $this->car->cost() + 2000;
    }

    function description()
    {
        return $this->car->description() . ",  high end wheels";
    }
}

// Create an object from one of the basic classes.
$basicCar = new Suv();

// Pass the object from the basic class as a parameter to the first feature class.
$carWithSunRoof = new SunRoof($basicCar);

// Run the methods on the last object that was created.
echo $carWithSunRoof -> description();
echo " costs ";
echo $carWithSunRoof -> cost();

/ 1. Create an object from one of the basic classes.
$basicCar = new Suv();

// 2. Pass the object from the basic class as a parameter to the first feature class.
$carWithSunRoof = new SunRoof($basicCar);

// 3. Pass the object from the first feature class as a parameter to the second feature class.
$carWithSunRoofAndHighEndWheels = new HighEndWheels($carWithSunRoof);

// 4. Run the methods on the last object that was created.
echo $carWithSunRoofAndHighEndWheels -> description();
echo " costs ";
echo $carWithSunRoofAndHighEndWheels -> cost();

// And the result:

// Suv, sunroof, high end wheels costs 33500

//Summary: The usefulness of the decorator design pattern lies in the fact that we can add new optional classes to existing basic classes without having to change the codes of the latter, thereby helping us to avoid imposing additional responsibilities on classes that were already tested.

