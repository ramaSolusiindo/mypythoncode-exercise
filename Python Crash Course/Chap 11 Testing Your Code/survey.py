class AnonymousSurvey:
    """ Collect anonymous answer to a survey question. """
    def __init__(self, question):
        """Store a question, and prepare to store response. """
        self.question = question
        self.response = []

    def show_question(self):
        """ Show the survey question """
        print(self.question)

    def store_response(self, new_response):
        """ Store a single response to the survey. """
        self.response.append(new_response)

    def show_result(self):
        """ Show all the responses that have been given. """
        print("Survey results:")
        for response in self.response:
            print(f"- {response}")

