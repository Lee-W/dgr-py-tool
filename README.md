# dgr-java-tool

A tool for data garage usage using java

## Sample


```json
[{
    
    "Format": "48",
    "Valuie": "12.3E+3",
    "B Fmt": "##0.0E+0",
    "VBA Fmt": "123.5E+2",
    "Fmt": "##0.0E+0",
    "Macro": "12.3E+3"
}, {
    
    "Format": "49",
    "Valuie": "12345.6789",
    "B Fmt": "@",
    "VBA Fmt": "12345.6789",
    "Fmt": "@",
    "Macro": "12345.6789"
}]
```

## Example


## Methods

#### Fetch all data

- Argument
    * Data id (String)

- Return: Json

```python
fetchAll('52e12d31203b41ab5d14964b')
```

#### Fetch custom data


- Arguments
    * Data id (String) : 
        

    * data (Object) : 
        - limit: You can limit the data set you are pulling from remote, should be a number
        - fields: Select the fields you want to get, should be a string seperate by comma (for example: `Format, Valuie, ...`)
        - skip: You could also skip the record you don't want( for example: `skip: 2`, that means the data will start from the 3)
        - selector : You can also select the data using greater, lesser, or equal ( for exmaple: `B Fmt=General`)

- Return: Json

```python
fetchCustom('52e12d31203b41ab5d14964b', {'limit': '3'})
```


## License

MIT [@chilijung](http://github.com/chilijung)
