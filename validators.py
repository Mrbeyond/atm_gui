import re

class Validators:
  def __init__(self):
    pass

  def passnames(data):
    """
      The name entitie to verified with regex
    """
    col = re.search("^[a-zA-Z]{3,}$", data)
    if(col == None):
      return False
    else:
      return col.group()
      # return True

  def passkeys(data):
    """
      Password verified with regex
    """
    key = re.search("^\w{7,}$", data)
    if(key == None):
      return False
    else:
      return key.group()
      
  def passamount(data):
    """
      Amount verifier with isnumeric
    """
    if(data.isnumeric()):
      return data
    else:
      return False

  def passAccountNum(data):
    """
      Amount verifier with isnumeric
    """
    if(data.isnumeric() and len(data) == 10):
      return data
    else:
      return False


