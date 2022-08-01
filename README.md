                                                              0x00. AirBnB clone - The console
1. Project description:

                        The goal of the project is to deploy on your server a simple copy of the AirBnB website.
                        https://www.youtube.com/playlist?list=PLlLHfkTcnvmPOp6jv_89tRpJUMFrP-Wbi
                        https://www.youtube.com/watch?v=QTwmCB_AWqI
                        https://www.youtube.com/watch?v=jeJwRB33YNg
                        https://www.youtube.com/watch?v=ZwCD8cNZk9U
                        https://www.youtube.com/watch?v=LrQhULlFJdU


2. What’s a command interpreter?

                                  What’s a command interpreter?
                                  Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the                                       objects of our project:

                                                            Create a new object (ex: a new User or a new Place)
                                                            Retrieve an object from a file, a database etc…
                                                            Do operations on objects (count, compute stats, etc…)
                                                            Update attributes of an object
                                                            Destroy an object

3. Execution

                                  Your shell should work like this in interactive mode:

                                  $ ./console.py
                                  (hbnb) help

                                  Documented commands (type help <topic>):
                                  ========================================
                                  EOF  help  quit

                                  (hbnb) 
                                  (hbnb) 
                                  (hbnb) quit
                                  $
                                  
                                  
                                  
                                  But also in non-interactive mode: (like the Shell project in C)

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
                                  All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
