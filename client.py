import socket

HANGMANPICS = ['''
    +-----+
    |     |
    |
    |
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |     |
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|\ 
    |
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|\ 
    |    / 
    |
    ======= ''','''
    +-----+
    |     |
    |     0
    |    /|\ 
    |    / \ 
    |
    ======= ''' ,'''
    +-----+
    |     |
    |     0
    |    /|\ 
    |    / \ 
    |     DEAD
    ======= ''']

def client_program():
    host = '127.0.0.1'  # as both code is running on same pc
    port = 8082  # socket server port number

    clientsocket = socket.socket()  # instantiate
    clientsocket.connect((host, port))  # connect to the server

    login = input("Already logged in to the game (y or n) ?:")
    if login == 'y' or login == 'Y':
        Username = input(" username: ")  # take input
        password = input(" password: ")  # take input
        sendinfString = Username + "|" + password
        while Username.lower().strip() != 'bye' and password.lower().strip() != 'bye':

            clientsocket.send(bytes(sendinfString,'utf-8'))

            data = clientsocket.recv(1024)
            print('Received from server: ' + str(data, 'utf-8'))  # show in terminal
            if str(data, 'utf-8') == str("Login Successfull!"):
                pass
            else:
                clientsocket.close()
                client_program()
    elif login == 'n' or login == 'N':
        username = input(" username: ")   #take input
        exist(username,clientsocket)
    else:
        pass
def exist(username,clientsocket):

    while username.lower().strip() != 'bye':
        clientsocket.send(bytes(username,'utf-8'))  # send message
        data = clientsocket.recv(1024)  # receive response
        print('Received from server: ' + str(data,'utf-8'))  # show in terminal
        if str(data,'utf-8') == str("Already exists,please try another username:"):
            username = input(" username: ")
            exist(username,clientsocket)
        else:
            password = input(" password: ")  # again take input
            clientsocket.send(bytes(password, 'utf-8'))  # send message
            while password.lower().strip() != 'bye':
                data = clientsocket.recv(1024)  # receive response
                strData = str(data, 'utf-8')

                if str(data,'utf-8') == str("firstUser"):
                    size = input("How many players you get?:")
                    clientsocket.send(bytes(size,'utf-8'))
                elif str(data, 'utf-8') == str("Login Successfull!"):
                    print("Logged In!")
                    clientsocket.send(bytes("OK", 'utf-8'))
                elif strData.isdigit():
                    print(HANGMANPICS[int(strData)])
                elif str(data,'utf-8') == str("Your Turn"):
                    guess =input("its your turn Enter your guess:")
                    clientsocket.send(bytes(guess,'utf-8'))
                else:
                    print('Received from server: ' + str(data, 'utf-8'))  # show in terminal

    while password.lower().strip() != 'bye':
        clientsocket.send(bytes(password,'utf-8'))  # send message
        data = clientsocket.recv(1024)  # receive response
        print('Received from server: ' + str(data, 'utf-8'))
        if str(data, 'utf-8') == str("Login Successfull!"):
            pass
        else:
           pass

    clientsocket.close()  # close the connection


if __name__ == "__main__":
    client_program()