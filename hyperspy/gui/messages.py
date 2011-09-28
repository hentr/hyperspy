# -*- coding: utf-8 -*-
# Copyright 2007-2011 The Hyperspy developers
#
# This file is part of  Hyperspy.
#
#  Hyperspy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
#  Hyperspy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with  Hyperspy.  If not, see <http://www.gnu.org/licenses/>.

import enthought.traits.api as t
import enthought.traits.ui.api as tui
from enthought.traits.ui.menu import OKButton
    
information_view = tui.View(tui.Item('text', show_label = False, 
                            style = 'readonly', springy = True, width = 300,), 
                            kind = 'modal', buttons = [OKButton,] )
class Message(t.HasTraits):
    text = t.Str
    def __init__(self, text):
        self.text = text
    traits_view = information_view
    
class Options(t.HasTraits):
    options = t.Enum(('a'))
    def __init__(self, options = ['a', 'b', 'c']):
        self.options = options
    
class MessageWithOptions(Message, Options):
    def __init__(self, text, options):
        Message.__init__(self, text)
        Options.__init__(self, options)

                                
def information(text):
    message = Message(text)
    message.text = text
    message.edit_traits()
    
def options(options_):
    class Options(t.HasTraits):
        options = t.Enum(options_)
    return Options
    
