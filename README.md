# Opening, reading, writing files and error handling

Topics covered:
- open()
- try and except
- with & finally
- exceptions and error handling
 
 
   ````
  (...)All that can go wrong,
   will go wrong(...) - Mr. Murphy
  ````

## Error handling
Mean assuming things will break, and handling your errors
when they do. Providing adequate feedback while
failing with grace.

When you handle your errors your code can continue to run 
(which is a good thing).

## Definitions

### try:/ except:
These blocks of code are used in conjunction to error handling
````
try:
    block of code
    block of code
    except <exception> as <placeholder>:
    block of code
    block of code
    print('Check file name &/or path - File cannot be found')
    print(<placeholder>)

````
### Exceptions
These occur when an error occurs  