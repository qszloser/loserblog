# encoding: utf-8
"""
@author: qsz
@contact: qsz2961914151@gmail.com
@time: 2020/12/21 下午3:31
@file: configs.py
@desc: 
"""
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

DEFAULT_CONFIG = {
    'width': '100%',
    'height': 800,
    'toolbar': ["undo", "redo",
                "|",
                "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase",
                "|",
                "h1", "h2", "h3", "h5", "h6",
                "|",
                "list-ul", "list-ol", "hr",
                "|",
                "image", "code", "code-block", "table", "datetime", "pagebreak", "goto-line",
                "|",
                "||",
                "help", "watch", ],
    'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                             "PNG", "bmp", "BMP", "webp", "WEBP"],
    'image_folder': 'editor',
    'theme': 'default',  # dark / default
    'preview_theme': 'default',  # dark / default
    'editor_theme': 'default',  # pastel-on-dark / default
    'toolbar_autofixed': True,
    'search_replace': True,
    'emoji': True,
    'tex': True,
    'task_list': False,
    'flow_chart': True,
    'sequence': True,
    'language': 'zh',  # zh / en
    'watch': True,  # Live preview
    'lineWrapping': False,  # lineWrapping
    'lineNumbers': False  # lineNumbers
}


class MDConfig(dict):

    def __init__(self, config_name='default'):
        self.update(DEFAULT_CONFIG)
        self.set_configs(config_name)

    def set_configs(self, config_name='default'):
        """
        set config item
        :param config_name:
        :return:
        """
        # Try to get valid config from settings.
        configs = getattr(settings, 'MDEDITOR_CONFIGS', None)
        if configs:
            if isinstance(configs, dict):
                # Make sure the config_name exists.
                if config_name in configs:
                    config = configs[config_name]
                    # Make sure the configuration is a dictionary.
                    if not isinstance(config, dict):
                        raise ImproperlyConfigured('MDEDITOR_CONFIGS["%s"] \
                                        setting must be a dictionary type.' %
                                                   config_name)
                    # Override defaults with settings config.
                    self.update(config)
                else:
                    raise ImproperlyConfigured("No configuration named '%s' \
                                    found in your CKEDITOR_CONFIGS setting." %
                                               config_name)
            else:
                raise ImproperlyConfigured('MDEDITOR_CONFIGS setting must be a\
                                dictionary type.')