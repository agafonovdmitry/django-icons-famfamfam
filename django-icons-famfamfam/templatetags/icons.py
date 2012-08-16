# -*- coding: utf-8 -*-

"""
Icon inclusion tags for your templates.

Add this to CSS:
.icon { padding-left: 20px; background-repeat: no-repeat;}
Note: use at least 20px line-height for best experiences.

Add this to your template before use:
{% load icons %}

This is a rewritten version of http://djangosnippets.org/snippets/2182/
originally posted by Hangya.
"""

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def icon(icon_name):
    """
    Adds icon for element as a backgroung image.

    Example usage:
    <a href="/login/" {% icon 'door_in' %}>Login</a>
    <h2 {% icon 'user' %}>{{ user.username }}</h2>
    <p>Please subscribe to our <span {% icon 'feed' %}>RSS feed</span>.</p>
    """

    return (
        'class="icon" style="background-image:url(' +
        settings.STATIC_URL + '/icons/' + icon_name + '.png);"'
    )


@register.simple_tag
def listicon(icon_name):
    """
    Adds list-style icon for element.

    Example usage:
    <ul><li {% listicon 'bullet_picture' %}>Item</li></ul>
    """

    return (
        'style="list-style-image:url(' + settings.STATIC_URL +
        '/icons/' + icon_name + '.png);"'
    )
