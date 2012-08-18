# -*- coding: utf-8 -*-

"""
Icon inclusion tags for your templates.

Add something like this to CSS:

.icon { width:16px; height:16px; padding:2px; line-height:20px; }
.bgicon { padding-left:20px; background-repeat:no-repeat; line-height:20px; }
.listicon { /* ... */ }

Add this to your template before use:

{% load icons %}

This is a rewritten version of http://djangosnippets.org/snippets/2182/
originally posted by Hangya.
"""

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def icon(icon_name, *args, **kwargs):
    """
    Adds icon as inline image.

    Example usage:
    <p>{% icon 'webcam' styles='border:1px solid #ccc' classes='one two' %} See me on-line!</p>
    """

    classes = ' ' + kwargs['classes'] if 'classes' in kwargs else ''
    styles = ' style="' + kwargs['styles'] + ';"' if 'styles' in kwargs else ''

    return (
        '<img class="icon' + classes + '" src="' +
        settings.STATIC_URL + 'icons/' + icon_name + '.png"' +
        styles + ' />'
    )


@register.simple_tag
def bgicon(icon_name, *args, **kwargs):
    """
    Adds icon for element as a backgroung image.

    Example usage:
    <p><a href="/login/" {% bgicon 'door_in' %}>Login</a></p>
    <h2 {% bgicon 'user' %}>Username</h2>
    <p>Please subscribe to our <span {% bgicon 'feed' classes="more" %}>RSS feed</span>.</p>
    """

    classes = ' ' + kwargs['classes'] if 'classes' in kwargs else ''
    styles = ';' + kwargs['styles'] if 'styles' in kwargs else ''

    return (
        'class="bgicon' + classes +
        '" style="background-image:url(' +
        settings.STATIC_URL + 'icons/' + icon_name + '.png)' +
        styles + ';"'
    )


@register.simple_tag
def listicon(icon_name, *args, **kwargs):
    """
    Adds list-style icon for element.

    Example usage:
    <ul><li {% listicon 'bullet_picture' styles='font-weight:bold' %}>Item</li></ul>
    """

    classes = ' ' + kwargs['classes'] if 'classes' in kwargs else ''
    styles = ';' + kwargs['styles'] if 'styles' in kwargs else ''

    return (
        'class="listicon' + classes +
        '" style="list-style-image:url(' +
        settings.STATIC_URL + 'icons/' + icon_name + '.png)' +
        styles + ';"'
    )
