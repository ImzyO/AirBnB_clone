                                                      0x00. AirBnB clone - The console
                                                      The goal of the project is to deploy on your server a simple copy of the AirBnB website.
                                                      It does not contain all features
                                                      
It contains:  
                A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
                A website (the front-end) that shows the final product to everybody: static and dynamic
                A database or files that store data (data = objects)
                An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)
                
What’s a command interpreter?
                                Do you remember the Shell? It’s exactly the same but limited to a specific use-case
                                
How to start a command interpreter?  
                                         1. Your shell should work like this in interactive mode:

                                          $ ./console.py
                                          (hbnb) help

                                          Documented commands (type help <topic>):
                                          ========================================
                                          EOF  help  quit

                                          (hbnb) 
                                          (hbnb) 
                                          (hbnb) quit
                                          $
                                          
                                          
                                        2.  But also in non-interactive mode: (like the Shell project in C)

                                          $ echo "help" | ./console.py
                                          (hbnb)

                                          Documented commands (type help <topic>):
                                          ========================================
                                          EOF  help  quit
                                          (hbnb) 
                                          $
                                          $ cat test_help
                                          help
                                          $
                                          $ cat test_help | ./console.py
                                          (hbnb)

                                          Documented commands (type help <topic>):
                                          ========================================
                                          EOF  help  quit
                                          (hbnb) 
                                          $
                                          
Why we use it ?

                      Create a new object (ex: a new User or a new Place)
                      Retrieve an object from a file, a database etc…
                      Do operations on objects (count, compute stats, etc…)
                      Update attributes of an object
                      Destroy an object
