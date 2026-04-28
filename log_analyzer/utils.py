def validate_file(filename):
    if not filename.endswith(".log"):
        raise ValueError("File must be a .log file")
    return filename