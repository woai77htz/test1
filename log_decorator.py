
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('log')

# 定义装饰器

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.debug(f"装饰器：{log_decorator.__name__} --> 传入函数：{wrapper.__name__}")
        return func(*args,**kwargs)
    return wrapper