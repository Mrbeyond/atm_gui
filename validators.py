import re

class Validators:
  def __init__(self):
    pass

  def names(self, data):
    """
      The name entitie to verified with regex
    """
    col = re.search("^[a-zA-Z]{3,}$", data)
    if(col == None):
      return False
    else:
      return col.group()

  def passkeys(self, data):
    """
      Password verified with regex
    """
    key = re.search("^\w{7,}$", data)
    if(key == None):
      return False
    else:
      return key.group()
