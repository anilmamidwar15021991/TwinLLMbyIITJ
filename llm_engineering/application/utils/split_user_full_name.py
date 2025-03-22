from llm_engineering.domain.exceptions import ImproperlyConfigured


def split_user_full_name(user: str|None )-> tuple [str, str]:
    if user is None:
        raise ImproperlyConfigured('User name is empty')
    

    name_tokens= user.split(" ")
    if len(name_tokens)==0 :
        raise ImproperlyConfigured('User name is empty')
    elif len
