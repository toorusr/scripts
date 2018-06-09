# Struc.tur
> A simple script to easily create a lot of folders and quickly initialize a folder structure.

## Features
- Create folder structures easily
- Avoid clicking fivethousend times
- Simple config syntax

## Get started
###### Setup
1. Make sure you have [python3.x](https://www.python.org/downloads/) installed
2. Download the [script](https://raw.githubusercontent.com/toorusr/scripts/master/struc.tur/struct) (struct)

###### Creating a blank config
1. Navigate to the folder where you want your folder structure
2. Create a file named `struc.tur`
3. Open the struc.tur file using your favourite editor
4. To initialize the struc.tur as a config type or paste into the first line the string: `[struc.tur]`
5. Now we have a blank valid config file

###### Configure the config
Currently there are two functions which you can use in the config file

Function | Description | Example
---------|-------------|---------
ec [string] | Print something to the console | ec Hello
mk [path] | Create dictionary | mk nice-folder

To use these functions you first must specify where to create all that stuff. You can do that by adding the path under the first line. For example `./` as a relative path for the folder where the config is.

The struc.tur file schould look like this then:
```
[struc.tur]
./
```

In the next step you have to tell the script where to start and where to end with your commands. You can do that by adding a `start` string and an `end` string. At this point the struct.tur file should be ready to handle your functions.

```
[struc.tur]
./
start
// here will your commands go
end
```

###### Execute the struct
To run the struct script and let it create your folder structure do the following steps:
1. Move the previously downloaded struct script into the directory where your struc.tur lays.
2. Open your terminal
3. Run the script by typing/copying `python3 struct` into the terminal
4. The script should run  

###### Create your first folders
A basic example for a usecase of this script could be that you want to create a overseeable folder structure for your photo archiv.

Here is the struc.tur config for such case:
```
[struc.tur]
./
start
mk photo_archiv
mk photo_archiv/2017
mk photo_archiv/2017/holiday
mk photo_archiv/2017/party
mk photo_archiv/2017/selfies
mk photo_archiv/2017/memes
mk photo_archiv/2018
mk photo_archiv/2018/holiday
mk photo_archiv/2018/party
mk photo_archiv/2018/selfies
mk photo_archiv/2018/memes
end
```
