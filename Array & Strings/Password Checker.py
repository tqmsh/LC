from re import search
class Solution: 
    def validatePassword(self, password, username):
        message = ""
        if len(password) < 8: message += 'Password must be at least 8 characters long.\n'
        if len(password) > 20: message += 'Password must be no more than 20 characters long.\n'
        # re search 模版
        if not search(r'[A-Z]', password): message += 'Password must contain at least one uppercase letter.\n' 
        if not search(r'[a-z]', password): message += 'Password must contain at least one lowercase letter.\n'
        if not search(r'\d', password): message += 'Password must contain at least one digit.\n'
        if not search(r'[!@#$%^&*(),.?":{}|<>]', password): message += 'Password must contain at least one special character.\n'
        if username and username in password: message += 'Password must not contain the username.\n'
        if message == '': message = "Password is valid."
        return message 

    
def main():
    username = 'johnDoe'
    password = 'Passw0d'
    print(Solution().validatePassword(password, username) )
if __name__ == "__main__":
    main()