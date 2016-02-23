.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
    
=================
Partner Directory
=================

This module was written to extend the functionality of a partner.
This module has the following functions:
    -   Creating a menu named "Partners Directory", where the structure menu is:
        
        1. Partners Directory
            1.1 Partners

                1.1.1 Corporate Partner
                
                1.1.2 Individual Partner
                
                1.1.3 All Contacts
                    
            1.2 Reporting

            1.3 Configuration
            
                1.3.1 Address
                
                    1.3.1.1 Countries
                    
                    1.3.1.2 States
                1.3.2 Bank
                
                    1.3.2.1 Bank Accounts
                    
                    1.3.2.2 Banks
                    
                    1.3.2.3 Bank Account Types
                    
    -   Removing field **Customer** and **Supplier** from view 
        and replace it with button **Set as supplier** and **Set as customer**.

    -   Creating a security group for all menus and buttons of "Partner Directory"

Configuration
=============

Every menu and button on this module has been created security group which can
be accessed on **Setting -> Users -> Users**

Installation
============

To install this module, you need to:

1.  Clone the branch 8.0 of the repository https://github.com/OCA/partner-contact
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list
4.  Go to menu *Setting -> Modules -> Local Modules*
5.  Search For *Partner Directory*
6.  Install the module

Usage
=====
.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/134/8.0


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/website/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed `feedback
<https://github.com/OCA/
partner-contact/issues/new?body=module:%20
partner_directory%0Aversion:%20
8.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
