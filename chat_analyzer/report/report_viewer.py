# -*- coding: utf-8 -*-

__author__ = 'Amit Botzer'

from chat_analyzer.parser.parser import *
from chat_analyzer.report.report_builder import *
import matplotlib.pyplot as plt
from chat_analyzer.configuration import configuration_adapter

class ReportViewer:

    def __init__(self, report_builder):
        self.report_builder = report_builder

    def view(self):
        conversation = parse()
        conf_adapter = ConfigurationAdapter()
        report = self.report_builder.build(conversation)
        # self.plot_pie_chart(report.number_of_messages_hist.keys(), report.number_of_messages_hist.values())
        self.write_dictionaries_to_file(report.conv_most_frequent_words,
                                        conf_adapter.get_by_key("FREQUENT_WORDS_FILE_PATH"))

    def write_dictionaries_to_file(self, dict, file_path):
        os.remove(file_path)
        with open(file_path, 'w') as f:
            for key in dict.keys():
                inner_dict = dict[key]
                f.write(key + '\n')
                for hebrew_word, coutner in inner_dict.iteritems():
                    f.write(hebrew_word.encode('utf8') + ' - ' + str(coutner) + '\n')

    def plot_pie_chart(self, labels, sizes):
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()

if __name__ == '__main__':
    report_builder = ReportBuilder()
    report_viewer = ReportViewer(report_builder)
    report_viewer.view()