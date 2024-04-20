import logging

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        # Configure logging
        logging.basicConfig(level=logging.DEBUG, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger = logging.getLogger(__name__)

        # Log function call details
        logger.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)

        # Log results
        logger.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@logging_decorator
def calculate_area(width, height):
    return width * height

if __name__ == "__main__":    
    area = calculate_area(5, 10)
    print(f"The calculated area is: {area}")