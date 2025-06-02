## Doxygen Documentation

This project uses Doxygen to automatically generate API documentation from comments left in source code. The generated documentation will appear in the `docs/html` directory and can be run on a live server.

### How to Build Documentation

To build the documentation:

1. Make sure you have Doxygen installed
   ```
   which doxygen
   ```

2. Create a `mainpage.dox` file for homepage information

3. Auto-generate a configuration file
   ```
   doxygen -g
   ```
This creates a Doxyfile in the current directory. Make sure to correctly set the `INPUT` field
    ```
    INPUT           = ../src mainpage.dox
    ```

4. Generate the documentation. Make sure you are in the correct directory
   ```
   doxygen
   ```

5. Open the documentation
   ```
   open ../docs/html/index.html
   ```

When new changes are made to the source code, Steps 4-5 will need to be run again.

## Documentation Style Guide

When adding documentation comments to code, please follow these guidelines:

- Use `"""` docstring comments for Doxygen documentation
- Within a docstring, comments should be preceded by a `!` to enable Doxygen extraction 
- Document all public classes, methods, and functions
- Use @brief for short descriptions
- Use @param to document parameters
- Use @return to document return values
- Use @see to reference related items
- Document code examples with @code and @endcode

Example:

```python
def hello_world(first_name, last_name):
    """!@brief A brief description of the function
    
    A more detailed description if needed

    @param first_name   The user's first name.
    @param last_nume    The user's last name.
    @return A greeting for the user
    """
    return f"Hello {first_name} {last_name}!"
```

For more information on Doxygen comment syntax, see [Doxygen documentation](https://www.doxygen.nl/manual/docblocks.html) or [this Python guide](https://www.woolseyworkshop.com/2020/06/25/documenting-python-programs-with-doxygen/). -->