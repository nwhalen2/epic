###############################################################################
# 
# translation_dict.py
#
# Authors: Epic Systems Preternship Team
# Date:    April 18, 2021
#
# A python dictionary that translates from English to other languages. The 
# first integer represents the source language. The child integers represent
# the target languages.
#
# Language Codes:
#  - 41:  Dutch
#  - 42:  English
#  - 47:  French
#  - 136: Spanish
#
###############################################################################

{
    'command' : {
        42 : {
            'take' : {
                136 : 'tome'
            },
            'apply' : {
                136 : 'aplique'
            },
            'inhale' : {
                136 : 'inhale'
            },
            'administer' : {
                136 : 'administre'
            },
            'use' : {
                136 : 'utilice'
            }
        },
        136: {
            'tome' : {
                42 : 'take'
            },
            'aplique' : {
                42 : 'apply'
            },
            'inhale' : {
                42 : 'inhale'
            },
            'administre' : {
                42 : 'administer'
            },
            'utilice' : {
                42 : 'use'
            }
        }
    },
    'dosage' : {
        42 : {
            'tablet' : {
                136 : 'tableta'
            },
            'tablets' : {
                136 : 'tabletas'
            },
            'puffs' : {
                136 : 'inhalaciones'
            },
            'capsule' : {
                136 : 'cápsula'
            },
            'application' : {
                136 : 'aplicación'
            },
            'patch' : {
                136 : 'parche'
            },
            'puff' : {
                136 : 'inhalación'
            },
        }, 
        136 : {
            'tableta' : {
                42 : 'tablet'
            },
            'tabletas' : {
                42 : 'tablets'
            },
            'inhalaciones' : {
                42 : 'puffs'
            },
            'cápsula' : {
                42 : 'capsule'
            },
            'aplicación' : {
                42 : 'application'
            },
            'parche' : {
                42 : 'patch'
            },
            'inhalación' : {
                42 : 'puff'
            },
        },
    },
    'method' : {

    },
    'frequency' : {

    },
    'extra' : {

    }
}
