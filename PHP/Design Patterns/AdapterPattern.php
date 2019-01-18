<?php

/* 

The Adapter design pattern as the name suggests is like real life adapter that converts one thing into some other one. Similarly, it can help us wrap functionality of some object into adapter providing us with consistent methods/API to work with. Understanding through an example is always the best way to learn.


Suppose you have developed a website where client has asked you to allow users to post status updates on the Facebook. In order to to that, we use Facebook PHP client library which looks something like this:

*/


class Facebook {    
    public function getUserToken($userId) {
        // code to get user token
    }

    public function postUpdate($message) {
        // code to post status update
    }
}

/*
And then you use it to post updates on Facebook:
*/

$statusUpdate = new Facebook;
$statusUpdate->getUserToken($someUserId);
$statusUpdate->postUpdate('some message');

/*
Now let's assume suddenly client requires that instead of Facebook, he wants users to post updates on Twitter and Twitter's PHP client library looks like this:
*/
class Twitter {    
    public function checkUserToken($userId) {
        // code to get user token
    }

    public function setStatusUpdate($message) {
        // code to post status update
    }
}

/*
And here is the problem. We can see that Twitter's library has different method names which means we will have to modify code everywhere where we are using status updates. At this point, as developer, we should also not overrule the fact that client may again ask to use Facebook again or may be some other service to allow users to post status update but we don't want to change our code again and again.

So how do we make sure that:

We should be able to add any new service easily when client asks
We should be able to not modify code again and again, same code should post status updates without modifying it
This is where Adapter pattern comes out to be as life saver. In order to implement that, 

we first set interface that all status update service should follow so let's create one:

*/

interface iStatusUpdate {
    function getUserToken($userId);
    function postUpdate($message);
}

// Now we create our Twitter adapter class:

class TwitterAdapter implements iStatusUpdate {

    protected $twitter;

    public function __construct(Twitter $twitter){
        $this->twitter = $twitter;
    }

    public function getUserToken($userId) {
        $this->twitter->checkUserToken($userId);
    }

    public function postUpdate($message) {
        $this->twitter->setStatusUpdate($message);
    }
}

/*
Notice how we have passed Twitter object via the constructor. Of course we could have used setter or interface injection as well.

We can see that we now have same method names for Facebook and Twitter which means we won't have to modify much code in our codebase where we need to post status updates for users. Now all we need to do is to use our new adapter class providing it with actual Twitter object:
*/


$statusUpdate = new TwitterAdapter(new Twitter);
$statusUpdate->getUserToken($someUserId);
$statusUpdate->postUpdate('some message');

/*
As can be we have added a line or couple but most of status update code remains same, thanks to adapter pattern. We as developers should foresee such changes client may require in which case we would have created adapter class even for our first Facebook service and then we didn't need to modify even a single line of code.

Okay, client asks some other service to use, no problem:
*/

class SomeOtherServiceAdapter implements iStatusUpdate {

    protected $otherService;

    public function __construct(SomeOtherService $otherService){
        $this->otherService = $otherService;
    }

    public function getUserToken($userId) {
        $this->otherService->authenticate($userId);
    }

    public function postUpdate($message) {
        $this->otherService->postMessage($message);
    }
}

$statusUpdate = new SomeOtherServiceAdapter(new SomeOtherService);
$statusUpdate->getUserToken($someUserId);
$statusUpdate->postUpdate('some message');

?>