# -*- coding: utf-8 -*-

__author__ = 'Amit Botzer'

from report import *

class ReportBuilder():
    
    def build(self, conversation):

        # check who said more times - I love you
        #checked_strings = ["אוהב אותך"]
        #times_said_hist = conversation.how_much_times_said(checked_strings)

        # who sent more messages?
        number_of_messages_hist = conversation.get_number_of_messages()

        # get most frequent words:
        conv_most_frequent_words = conversation.get_conversation_most_frequent_words()

        # get participants most frequent words:
        # part_most_frequent_words = conversation.get_participants_most_frequent_words()

        # get day histogram:
        # days_hist = conversation.get_days_histogram()

        # get hour histogram:
        # hour_hist = conversation.get_hour_histogram()

        # who opened more sessions?
        # sessions_hist = conversation.get_sessions_histogram()

        # average reply time:
        # avg_reply_times_hist = conversation.get_avg_reply_times_histogram()

        # get message length histogram:
        # message_length_hist = conversation.get_message_length_histogram()

        # get average message length:
        # avg_message_length = conversation.get_avg_message_length()

        # get funniest joke:
        # funniest_jokes = conversation.get_funniest_jokes()

        # who talked first more times?
        return Report(number_of_messages_hist, conv_most_frequent_words)

    def show_histogram(hist):
        pass

