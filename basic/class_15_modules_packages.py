def demo():
  '''
  A module is a piece of software that has a specific functionality. A Python module is a file that contains Python code.

  Advantages:
  1. reusibilty: reuse the module in different systems, which save more time rather than rewrite everything
  2. trouble shootting: if something goes wrong, we can narrow down the issue in that module only
  3. make code more organized, easier to maintain, fix, extend more feature
  '''

  '''
  1. importing module
  import <module_name>

  after importing the module, everything in that module can be used

  import pricing
  pricing.get_net_price() 
  '''


  '''
  import <module_name> as new_name
  
  import pricing as selling_price
  selling_price.get_net_price() 
  '''


  '''
  from <module_name> import <name>
  If you want to reference objects in a module without prefixing the module name, you can explicitly import them
  
  from pricing import get_net_price
  '''

  '''
  from <module_name> import <name> as <new_name>: rename the imported objects

  from pricing import get_net_price as calculate_net_price
  '''

  '''
  from <module_name> import * : import all objects from a module

  from pricing import *
  '''


  '''
  __name__
  The __name__ is a special variable in Python. It’s special because Python assigns a different value to it depending on how its containing script executes.


  1. module A is imported
    __name__ is the module name of A
  2. module A is not imported, but excuted directly
    __name__ is "__main__"
  '''


  '''
  Packages

  Packages allow you to organize modules in the hierarchical structure.

  The way Python organizes packages and modules like the Operating System structures the folders and files.

  To create a package, you create a new folder and place the relevant modules in that folder.

  To instruct Python to treat a folder containing files as a package, you need to create a __init__.py file in the folder.
  
  '''

  '''
  Initializing a package
  
  By convention, when you import a package, Python will execute the __init__.py in that package.

  Therefore, you can place the code in the __init__.py file to initialize package-level data.
  '''

  '''
  __all__
  If the __init__.py file exists, it'll load all modules specified in a special list called __all__ in the file.

  For example, you can place the order and delivery modules in the __all__ list like this:

  # __init__.py

  __all__ = [
      'order',
      'delivery'
  ]
  '''