import socket
import constants

#The code that takes care of the socket timeout:
def setblocking():
    """
    This function makes sure that the socket will timeout after the defined timeout time.
    It will only be used to replace the built-in socket.settimeout() function.
    Input: None.
    Output: None.
    """
    setblocking_func = socket.socket.setblocking
 
    def wrapper(self, flag):
        if flag:
            # prohibit timeout reset
            timeout = socket.getdefaulttimeout()
            if timeout:
                self.settimeout(timeout)
            else:
                setblocking_func(self, flag)
        else:
            setblocking_func(self, flag)
 
    wrapper.__doc__ = setblocking_func.__doc__
    wrapper.__name__ = setblocking_func.__name__
    return wrapper
 
 
socket.socket.setblocking = setblocking() #Makes the code above active for the socket
socket.setdefaulttimeout(constants.SOCKET_TIMEOUT) #Sets default timeout for all sockets.