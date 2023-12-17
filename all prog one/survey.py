#!/usr/bin/env python
# coding: utf-8

# In[5]:


#class test
class anonymousSurvey():
    """collect anonymoous answers to a survey question."""
    def __init__(self,question):
        """store questions and prepare to store responses"""
        self.question = question
        self.response = []
    def show_question(self):
        """show the survey question"""
        print(question)
    def store_response(self,new_response):
        """store a singe response to a survye"""
        self.response.append(new_response)
    def show_result(self):
        """show all response that have been given"""
        print("survey result")
        for response in responses:
            print('-' + response)


# In[ ]:





# In[ ]:




