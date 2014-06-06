# dgr-python-tool

A tool for data garage usage using python

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

###Set URL


- Argument
    * URL :

```python
setURL("http://www.datagarage.io/api/5365dee31bc6e9d9463a0057")
```


#Set DataID


- Argument
    * dataID :

```python
setURL("5365dee31bc6e9d9463a0057")
```

#Set Selector


- Argument
    * condition

```python
setSelector([["鄉鎮市區", "=", "文山區"], ["土地區段位置或建物區門牌","=","/辛亥路/"], ["交易年月", ">=", 10300]])
```

#Set Sort


- Arguments
    * fields
    * acs

```python
setSort('車位總價元', acs = True)
```

#Set skip


- Argument
    * skipNum

```python
setSkip(5)
```

#Set limits


- Argument
    * limitNum

```python
setLimit(10)
```

#Get raw data


- Argument
    * returnList

- Return : list or string (depends on argument returnList)

```python
getRawData(True)
```

#Get filtered data


- Argument
    * returnList

- Return : list or string (depends on argument returnList)

```python
getFilteredData(True)
```


#Reset filter

```python
resetFilter()
```

## License

MIT
