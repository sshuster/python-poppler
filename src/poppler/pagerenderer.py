# poppler-python: python binding to the poppler-cpp pdf lib
# Copyright (C) 2020, Charles Brunet <charles@cbrunet.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from poppler import _page_renderer
from poppler import Rotation
from poppler.image import Image


class PageRenderer(object):

    LineMode = _page_renderer.line_mode_enum
    RenderHint = _page_renderer.render_hint

    def __init__(self):
        self._renderer = _page_renderer.page_renderer()

    @property
    def image_format(self):
        return self._renderer.image_format()

    @image_format.setter
    def image_format(self, format):
        self._renderer.set_image_format(format)

    @property
    def line_mode(self):
        return self._renderer.line_mode()

    @line_mode.setter
    def line_mode(self, mode):
        self._renderer.set_line_mode(mode)

    @property
    def paper_color(self):
        return self._renderer.paper_color()

    @paper_color.setter
    def paper_color(self, color):
        self._renderer.set_paper_color(color)

    @property
    def render_hints(self):
        return self._renderer.render_hints()

    @render_hints.setter
    def render_hints(self, hints):
        self._renderer.set_render_hints(hints)

    def render_page(
        self,
        page,
        xres=72.0,
        yres=72.0,
        x=-1,
        y=-1,
        w=-1,
        h=-1,
        rotate=Rotation.rotate_0,
    ):
        img = self._renderer.render_page(page._page, xres, yres, x, y, w, h, rotate)
        return Image.from_object(img)

    def set_render_hint(self, hint, on=True):
        self._renderer.set_render_hint(hint, on)

    @staticmethod
    def can_render():
        return _page_renderer.can_render()