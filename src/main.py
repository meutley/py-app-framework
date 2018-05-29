import application

try:
    application = application.Application("first-py")
    application.run()
except Exception as ex:
    print("An error occurred: {0}".format(str(ex)))