def emailProcess():
    while True:
        email = input("Please enter your email address: ").strip()
        if email:
            
            email_username = email[0:email.index("@")]
            email_domain = email[email.index("@")+1:]
            print(f'Username is {email_username}, Domain is {email_domain}')
            break
        else:
            print("email is empty")
            continue
        
        


def main():
    emailProcess()
    

if __name__ == "__main__":
    main()