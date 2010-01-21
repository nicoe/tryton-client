#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from interface import ParserView


class ViewGraph(ParserView):

    def __init__(self, window, screen, widget, children=None,
            buttons=None, toolbar=None, notebooks=None, cursor_widget=None):
        super(ViewGraph, self).__init__(window, screen, widget, children,
                buttons, toolbar, notebooks, cursor_widget)
        self.view_type = 'graph'
        self.model_add_new = False
        self.widgets = children

    def __getitem__(self, name):
        return None

    def destroy(self):
        self.widget.destroy()
        for widget in self.widgets.keys():
            self.widgets[widget].destroy()
            del self.widgets[widget]
        del self.widget
        del self.screen
        del self.buttons

    def cancel(self):
        pass

    def set_value(self):
        pass

    def sel_ids_get(self):
        return []

    def reset(self):
        pass

    def signal_record_changed(self, *args):
        self.display()

    def display(self):
        for widget in self.widgets.itervalues():
            widget.display(self.screen.models)
        return True

    def set_cursor(self, new=False, reset_view=True):
        pass
