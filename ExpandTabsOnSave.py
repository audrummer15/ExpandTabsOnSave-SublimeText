"""ExpandTabsOnSave SublimeText plugin."""
import os

import sublime
import sublime_plugin


class ExpandTabsOnSave(sublime_plugin.EventListener):
    """Expant tabs on file save."""

    def on_pre_save(self, view):
        """Run ST's 'expand_tabs' command when saving a file."""
        if view.settings().get('expand_tabs_on_save') == 1:
            view.window().run_command('expand_tabs')
