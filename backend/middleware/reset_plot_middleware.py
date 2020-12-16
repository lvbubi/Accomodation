import matplotlib.pyplot as plt


class middleware():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.userName = 'Tony'
        self.password = 'IamIronMan'

    def __call__(self, environ, start_response):
        # try:
        #     plt.cla()
        #     plt.clf()
        # except:
        #     print('plt was empty')
        return self.app(environ, start_response)
