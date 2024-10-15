# Tap Proxy Utility

The **Tap Proxy Utility** provides a simple mechanism for inspecting, modifying, and chaining operations on objects without breaking the flow of method chaining. This utility allows you to either apply a callback function to an object or dynamically call methods on it via a proxy object.

## Installation

Ensure you have Python 3.11 or later installed. You can add this utility to your project using [Poetry](https://python-poetry.org/) or manually copy the provided files into your project.

```bash
# Clone the repository
git clone https://github.com/PsyChaos/tap.git

# Navigate to the directory
cd tap

# Install the dependencies using Poetry (if applicable)
poetry install
```

## Usage

The `tap` function allows you to inspect or modify an object within a callback, or use a higher-order proxy to chain methods dynamically.

### Basic Usage

You can use `tap` in two primary ways:

1. **Using a callback:**

   When you provide a callback, `tap` will pass the object to the callback, allowing you to inspect or modify it.

   ```python
   from tap import tap

   def log_value(value):
       print(f"Current value: {value}")

   obj = {"a": 1}
   tap(obj, log_value)
   # Output: Current value: {'a': 1}
   ```

2. **Chaining methods via a proxy:**

   Without a callback, `tap` returns a `HigherOrderTapProxy` that allows you to chain methods dynamically on the object.

   ```python
   from tap import tap

   class SampleObject:
       def __init__(self):
           self.value = 1

       def increment(self):
           self.value += 1
           return self

       def double(self):
           self.value *= 2
           return self

   obj = SampleObject()
   result = tap(obj).increment().double()

   print(result.value)  # Output: 4
   ```

## Examples

### Using with Lists

```python
lst = [1, 2, 3]

tap(lst).append(4).reverse()

print(lst)  # Output: [4, 3, 2, 1]
```

### Using with Dictionaries

```python
d = {"a": 1}

tap(d).update({"b": 2})

print(d)  # Output: {'a': 1, 'b': 2}
```

### Using Nested Taps

You can even nest `tap` calls to modify and chain methods on objects within other objects.

```python
obj = SampleObject()
tap(tap(obj).increment()).double()

print(obj.value)  # Output: 4
```

## Test

Unit tests are provided using `pytest`. Run the following command to execute the tests:

```bash
pytest
```

Sample test cases are included to verify chaining, callback behavior, and error handling.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.