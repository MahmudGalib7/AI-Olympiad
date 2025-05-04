def func(positional, *args, keyword_only=..., **kwargs):
    """
    Function with different types of arguments.
    
    Args:
        positional: A positional argument.
        *args: Variable length positional arguments.
        keyword_only: A keyword-only argument.
        **kwargs: Variable length keyword arguments.
    
    Returns:
        None
    """
    print(f"Positional argument: {positional}")
    print(f"Variable length positional arguments: {args}")
    print(f"Keyword-only argument: {keyword_only}")
    print(f"Variable length keyword arguments: {kwargs}")

# Example usage
if __name__ == "__main__":
    func(1, 2, 3, keyword_only=4, a=5, b=6)