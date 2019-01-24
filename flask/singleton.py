class Log:
    """
    Singleton provides you with a mechanism to have one, and only one, 
    object of a given type and provides a global point of access. Hence,
    Singletons are typically used in cases such as logging or database 
    operations, printer spoolers, and many others, where there is a
    need to have only one instance that is available across the application 
    to avoid conflicting requests on the same resource. 
    For example, we may want to use one database object to
    perform operations on the DB to maintain data consistency or one 
    object of the logging class across multiple services to dump log 
    messages in a particular log file sequentially.
    In brief, the intentions of the Singleton design pattern are as follows:
    Ensuring that one and only one object of the class gets created
    Providing an access point for an object that is global to the program
    Controlling concurrent access to resources that are shared
    """
    def __new__(cls):
        if not hasattr(cls, '_mi_instancia_existe'):
            cls._mi_instancia_existe = super(Log, cls).__new__(cls)
            cls.__file = None
            cls.__file_is_open = False
        return cls._mi_instancia_existe

    def init(self, logname, mode="a"):
        if self.__file_is_open is False:
            self.__file = open(logname, mode=mode, encoding="utf-8")
            self.__file_is_open = True

    def write(self, log):
        return self.__file.write(log+"\n")

    def __del__(self):
        if self.__file_is_open is True:
            self.__file.close()
            self.__file_is_open = False

    def __repr__(self):
        return self.__file.name


l1 = Log()
l1.init("black.log")
l2 = Log()
l2.init("ss.log")
print(l1.write("L1"))
print(l2.write("L2"))
print(l1 is l2)
print(l1 == l2)
print(type(l1))
print(type(l2))
print(id(l1))
print(id(l2))
print(hash(l1))
print(hash(l2))
print(l1, l2)
