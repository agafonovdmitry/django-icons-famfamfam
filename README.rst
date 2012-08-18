============================
About Django Icons Famfamfam
============================

This package provides django staticfiles with famous famfamfam silk and
flag (png) icon sets combined together into one reuseable app.

All images were additionally optimized using optipng, pngcrush and
convert from imagemagick to produce minimal possible size with no loss.

Total image count: 1248. Optimization: 794 kB => 729 kB (~8% less).

Three template tags for easy usage are included via ``icons`` tag library.

Installation
------------

**Via PyPI**::

    pip install django-icons-famfamfam

**Directly from GitHub**::

    pip install git+git://github.com/agafonovdmitry/django-icons-famfamfam.git

Usage
-----

**Make sure these lines are in** ``INSTALLED_APPS`` **in** ``settings.py``::

    'django.contrib.staticfiles',
    'icons_famfamfam',

**In your templates**:

Add something like this to CSS::

    .icon { width:16px; height:16px; padding:2px; line-height:20px; }
    .bgicon { padding-left:20px; background-repeat:no-repeat; line-height:20px; }
    .listicon { /* ... */ }

Direct images usage::

    <img class="icon" src="{{ STATIC_URL }}icons/thumb_up.png" />
    
Or use special template tags bundled::

    {% load icons %}
    
    <p>{% icon 'webcam' styles='border:1px solid #ccc' classes='one two' %} See me on-line!</p>

    <p><a href="/login/" {% bgicon 'door_in' %}>Login</a></p>
    <h2 {% bgicon 'user' %}>Username</h2>
    <p>Please subscribe to our <span {% bgicon 'feed' classes="more" %}>RSS feed</span>.</p>

    <ul><li {% listicon 'bullet_picture' styles='font-weight:bold' %}>Item</li></ul>

See ``example_project`` folder at github which contains minimal django
project and provided for testing and demonstration purposes.


**Original author's README files with license information follows:**

------------

Silk icon set 1.3

Mark James
http://www.famfamfam.com/lab/icons/silk/

This work is licensed under a
Creative Commons Attribution 2.5 License.
[ http://creativecommons.org/licenses/by/2.5/ ]

This means you may use it for any purpose,
and make any changes you like.
All I ask is that you include a link back
to this page in your credits.

Are you using this icon set? Send me an email
(including a link or picture if available) to
mjames@gmail.com

Any other questions about this icon set please
contact mjames@gmail.com

------------

Flag icons - http://www.famfamfam.com

These icons are public domain, and as such are free for any use (attribution appreciated but not required).

Note that these flags are named using the ISO3166-1 alpha-2 country codes where appropriate. A list of codes can be found at http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2

If you find these icons useful, please donate via paypal to mjames@gmail.com (or click the donate button available at http://www.famfamfam.com/lab/icons/silk)

Contact: mjames@gmail.com
