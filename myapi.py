import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key("IH40CcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk")

    def sentiment_analysis(self,text):
        response=paralleldots.sentiment(text)
        return response

