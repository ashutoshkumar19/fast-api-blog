from passlib.context import CryptContext

hash_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash:
    def bcrypt(self: str):
        return hash_context.hash(self)

    def verify(self: str, hashed_password: str):
        return hash_context.verify(self, hashed_password)
