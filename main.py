from linkedin_login.login import LoginLinkedin

if __name__ == '__main__':
    linkedin = LoginLinkedin('anathaissenger@hotmail.com', 'ana3519424')
    linkedin.driver_open()
    linkedin.user_action()
    linkedin.password_action()
    linkedin.submit_action()

