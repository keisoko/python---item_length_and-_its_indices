# Item Length And Its Indices

## What Does It Do?

Python program to display item length and its indices

## How to use it?

Make sure to have both files in the same directory.<br>
The `isinstance` syntax in the `item_length(item)` function in `item_length_and_its_and_its_indices.py` requires Python 3.10.<br>
For Python below 3.10 the above function becomes this:

```python
def item_length(item):
    """Logs length of the given item"""
    if isinstance(item, (str, list, dict)):
        print(f"The length of the given item is {len(item)}\n")
```
To run excute `item_length_and_its_and_its_indices.py`
