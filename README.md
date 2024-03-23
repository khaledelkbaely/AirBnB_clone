# AirBnB clone (our own version)

In this project, we are cloning [AirBnB](https://www.airbnb.com/) website with its basic functions and usage.
We use python as the main programming language for developing.
In terms of storage system in this project, we use two formats: JSON file and MySQL DBMS, firstly, we use JSON and later on we will use MySQL for store website data efficiently.
Our main purpose is to be able to build the core of AirBnB from scratch making use of OOP princples using python. 

## Description

Our project is consisting from mutliple parts and systems integrated together to have the work done, so let us get through each one of them:    

**1.. The console**
- creating our data model
- managing (create, update, destroy, etc) objects via a console command interpreter
- storing and persisting objects to a file (JSON file)      
![first-img](./imgs/first.png)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

