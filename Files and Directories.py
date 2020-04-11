from pathlib import Path

# Absolute path
# example of absolute Path c:\User\PycharmProject\Hello
# Relative path

# check either a directory exist or not....
# path = Path("ecommerece")
# print(path.exists())
#
#  we cane also make new directory
path1 = Path("email")
path1.mkdir()

# remove a directory
path1 = Path("email")
path1.rmdir()

