import os

def getFileNames():
    """
    Returns the current foldername and files contained

    Parameters: none

    Returns: folder_name (string), file_names (string)
    """
    # TODO: folder_name not hard-coded
    folder_name = 'papers'
    # TODO: compatibility for other systems
    file_names = os.listdir(foldername)
    return folder_name, file_names
