#crate acount
#different acounts types
#make a acount for kids to connect to their parents acount
while True:
  print('welcome to reality bank the bank that helps your financial suecce become a reality')
  print('Sign up')
  print('Log in')
# if they can log in to an alrdy existing acount
# if they want they can make a new acount
  account = input('')
  if account == 'Sign up' or account == 'sign up':
      print('First name:')
      first_name = input('')
      print('Last name:')
      last_name = input('')
      print('email:')
      email = input('')
      print('Age:')
      age = input('')
  if age < "18":
    print("you can't create an acount on your own but you can create a personal acount under your parent or gardian acount")
    print('Please navigate back to the log in page with your parent or gardian to make a joint acount under their name')
  
    print('1.back to log in page')
    back = input('')
  if age > "18" or age == "18":
    print('username:')
  username = input('')
  print('password:')
  password = input('')
  print('confirm password:')
  confirm_password = input('')
    
  if password == confirm_password:
    print('Welcome to your reality bank account' + first_name + last_name)
    print("Please navigate back to the log in page to log in to your account")
    
  else:
    print('passwords do not match')
  
if account == 'Log in' or account == 'log in':
  print('username:')
  username = input('')
  print('password:')
  password = input('')