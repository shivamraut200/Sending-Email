import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()


try:

    newid = input("Enter Senders Email id : ")
    password = input("Enter senders password : ")
        
    s.login(newid,password)
        
    receiver_id = input("Enter receivers Email id : ")
    Subject = input("Enter Subject of your Email : ")
    Body = input("Enter body of your Email : ")
    message = 'Subject: {}\n\n{}'.format(Subject, Body)
        

    s.sendmail(newid,receiver_id,message)

    print("Message sent")
    s.quit()
except smtplib.SMTPAuthenticationError:    
    print("""
Your Email is not sent

because Your Authentication is not done yet
change your account setting that to enable for less secure apps

to change your account setting below is link
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbTFUYXZDWlU1YUJUN1BKWFpwUlZmV2x5MEdIUXxBQ3Jtc0tsS1JRWHhCM2lBTmwtVHRpVVJpZGtNTHY5cUVlWkl5akU0Y2RFMkZ3VVB5bkNMWmZ3Qm9hSmVWQWZSSGJkTnE1Z2hpOFA3bEMydlZqakI5b2xsWU1ranZUMHZNWmFSWm5TczhuVkJSUWRMZHZOMmlOUQ&q=https%3A%2F%2Fmyaccount.google.com%2Flesssecureapps
""")
    

except:    
    print("Email not sent")

