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

import json

dictionary = {
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
            }
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
            }
        }
    },
    'method' : {
        42 : {
            'by mouth' : {
                136 : 'por vía oral'
            },
            'topically' : {
                136 : 'por vía tópica'
            },
            'into affected notril(s)' : {
                136 : 'en los orificios nasales afectados'
            },
            'as instructed' : {
                136 : 'según las instrucciones'
            },
            'into one nostril' : {
                136 : 'en un orificio nasal'
            },
            'as directed' : {
                136 : 'como se indica'
            },
            'blood sugar' : {
                136 : 'el nivel de azúcar en las sangre'
            },
            'into affected eye(s)' : {
                136 : 'en los ojos afectados'
            }
        },
        136 : {
            'por vía oral' : {
                42 : 'by mouth'
            },
            'por vía tópica' : {
                42 : 'topically'
            },
            'en los orificios nasales afectados' : {
                42 : 'into affected nostril(s)'
            },
            'según las instrucciones' : {
                42 : 'as instructed'
            },
            'en un orificio nasal' : {
                42 : 'into one nostril'
            },
            'como se indica' : {
                42 : 'as directed'
            },
            'el nivel de azúcar en las sangre' : {
                42 : 'blood sugar'
            },
            'en los ojos afectados' : {
                42 : 'into affected eye(s)'
            }
        }
    },
    'frequency' : {
		42: {
			'every' : {
				136 : 'cada'
			},
			'hour' : {
				136 : 'hora'
			},
			'hours' : {
				136 : 'horas'
			},
			'time' : {
				136 : 'vez'
			},
			'times' : {
				136 : 'veces'
			},
			'each day' : {
				136 : 'al día'
			},
			'a day' : {
				136 : 'al día'
			},
			# special case, 'for' when followed by a frequency
			'for -f' : {
				136 : 'por'
			},
			'day' : {
				136 : 'día'
			},
			'days' : {
				136 : 'días'
			},
			'daily' : {
				136 : 'diariamente'
			},
			'night' : {
				136 : 'noche'
			},
			'nights' : {
				136 : 'noches'
			},
			'once' : {
				136 : 'una vez'
			},
			'up to' : {
				136 : 'hasta'
			}
		},
		136 : {
			'cada' : {
				42 : 'every'
			},
			'hora' : {
				42 : 'hour'
			},
			'horas' : {
				42 : 'hours'
			},
			'vez' : {
				42 : 'time'
			},
			'veces' : {
				42 : 'times'
			},
			'al día' : {
                42 : 'each day'
			},
			'por' : {
				42 : 'for'
			},
			'durante' : {
				42 : 'for'
			},
			'día' : {
				42 : 'day'
			},	
			'días' : {
				42 : 'days'
			},
			'diariamente' : {
				42 : 'daily'
			},
			'noche' : {
				42 : 'night'
			},
			'noches' : {
				42 : 'nights'
			},
			'una vez' : {
				42 : 'once'
			},
			'hasta' : {
				42 : 'up to'
			}
		} 
    },
    'number': {
        42 : {
            'one' : {
                136 : 'uno'
            },
            'two' : {
                136 : 'dos'
            },
            'three' : {
                136 : 'tres'
            },
            'four' : {
                136 : 'quatro'
            },
            'five' : {
                    136 : 'cinco'
            },
            'six' : {
                136 : 'seis'
            },
            'seven' : {
                136 : 'siete'
            },
            'eight' : {
                136 : 'ocho'
            },
            'nine' : {
                136 : 'nueve'
            },
            'ten' : {
                136 : 'diez'
            },
        },
        136 : {
            'uno' : {
                42 : 'one'
            },
            'dos' : {
                42 : 'two'
            },
            'tres' : {
                42 : 'three'
            },
            'quatro' : {
                42 : 'four'
            },
            'cinco' : {
                42 : 'five'
            },
            'seis' : {
                42 : 'six'
            },
            'siete' : {
                42 : 'seven'
            },
            'ocho' : {
                42 : 'eight'
            },
            'nueve' : {
                42 : 'nine'
            },
            'diez' : {
                42 : 'ten'
            },
        }
    },
    'extra' : {
         42 : {
            'mg' : {
                136 : 'mg'
            },
            'total' : {
                136 : 'en total'
            },
            'mL' : {
                136 : 'mL'
            },
            'for pain' : {
                136 : 'para el dolor'
            },
            'with meals' : {
                136 : 'con comida'
            },
            'if needed' : {
                136 : 'si necesario'
            },
            'at bed time' : {
                136 : 'al acostarse'
            },
            'for mild pain' : {
                136 : 'para el dolor leve'
            },
            'for moderate pain' : {
                136 : 'para el dolor moderado'
            },
            'do not crush or chew' : {
                136 : 'no triture ni mastique'
            },
            'for wheezing' : {
                136 : 'para sibilancias'
            },
            'for cough' : {
                136 : 'para la tos'
            },
            'for blood pressure' : {
                136 : 'para la presión arterial'
            },
            'at the same time' : {
                136 : 'a la misma hora'
            },
            'for cholesterol' : {
                136 : 'para el colesterol'
            }
        },
        136 : {
            'mg' : {
                42 : 'mg'
            },
            'en total' : {
                42 : 'total'
            },
            'mL' : {
                42 : 'mL'
            },
            'para el dolor' : {
                42 : 'for pain'
            },
            'con comida' : {
                42 : 'with meals'
            },
            'si necesario' : {
                42 : 'if needed'
            },
            'al acostarse' : {
                42 : 'at bed time'
            },
            'para el dolor leve' : {
                42 : 'for mild pain'
            },
            'para el dolor moderado' : {
                42 : 'for moderate pain'
            },
            'no triture ni mastique' : {
                42 : 'do not crush or chew'
            },
            'para sibilancias' : {
                42 : 'for wheezing'
            },
            'para la tos' : {
                42 : 'for cough'
            },
            'para la presión arterial' : {
                42 : 'for blood pressure'
            },
            'a la misma hora' : {
                42 : 'at the same time'
            },
            'para el colesterol' : {
                42 : 'for cholesterol'
            }
        }
    }
}


def get_json():

    with open("translation_dict.json", "w") as fh:
        json.dump(dictionary, fh, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    get_json()
