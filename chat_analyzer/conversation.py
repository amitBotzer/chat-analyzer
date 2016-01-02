# -*- coding: utf-8 -*-

__author__ = 'Amit Botzer'

import operator

class Conversation:

    def __init__(self, messages, participants):
        self.messages = messages
        self.participants = participants

    def get_number_of_messages(self):
        res = {}
        for participant in self.participants:
            number_of_participant_messages = self.get_participant_number_of_messages(participant)
            res[participant] = number_of_participant_messages
        return res

    def get_participant_number_of_messages(self, participant):
        messages = [message for message in self.messages if message.sender == participant]
        return len(messages)


    def get_conversation_most_frequent_words(self):
        res = {}
        for participant in self.participants:
            participant_dict = self.get_participant_word_frequency(participant)
            res[participant] = self.get_highest_entries(participant_dict, 50)
        return res

    def get_participant_word_frequency(self, participant):
        participant_dict = {}
        for message in [message for message in self.messages if message.sender == participant]:
            splits = message.text.split()
            for word in splits:
                if word not in participant_dict.keys():
                    participant_dict[word] = 1
                else:
                    participant_dict[word] += 1
        return participant_dict

    # gets a dictionary and returns the x entries with the highest value
    def get_highest_entries(self, my_dict, x):
        return dict(sorted(my_dict.iteritems(), key=operator.itemgetter(1), reverse=True)[:x])

    # def get_conversation_length(self):
    #     return len(self.messages)
    #
    # def how_much_times_said(self, participant, phrase_str):
    #     messages = [message in self.messages if message.sender == participant and phrase_str in message.text]
    #     return len(messages)
    #
    # def who_say_more(self, phrase_str):
    #
    #     counters = []
    #     for participant in self.participants:
    #         counters.append(self.how_much_time_said(participant, phrase_str))
    #
    #     max_said = max([counter[1] for counter in counters])
    #     said_more_index = [i for i, j in enumerate(counters) if j == max_said]
    #     return self.participants[said_more_index]