# Map aka Apply-To-All

Map is one of the most common and useful higher-order functions. It takes a collection,
applies a function to every element in the collection, and returns a new collection
with the result of the function call.

It is a one-to-one mapping of a collection.

To avoid any clashes with Python's native `map` function, we'll call our function
`apply_to_all`.

The function signature is:

```python
def apply_to_all(fun: Callable, lst: list) -> list:
```

## Resources

[Map at Wikipedia](https://en.wikipedia.org/wiki/Map_(higher-order_function))
