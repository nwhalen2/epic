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
                136 : 'capsula'
            },
            'application' : {
                136 : 'aplicacion'
            },
            'patch' : {
                136 : 'parche'
            },
            'puff' : {
                136 : 'inhalacion'
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
            'capsula' : {
                42 : 'capsule'
            },
            'aplicacion' : {
                42 : 'application'
            },
            'parche' : {
                42 : 'patch'
            },
            'inhalacion' : {
                42 : 'puff'
            }
        }
    },
    'method' : {
        42 : {
            'by mouth' : {
                136 : 'por vaa oral'
            },
            'topically' : {
                136 : 'por via topica'
            },
            'into affected notril(s)' : {
                136 : 'en los orificios nasales afectados'
            },
            'as instructed' : {
                136 : 'segun las instrucciones'
            },
            'into one nostril' : {
                136 : 'en un orificio nasal'
            },
            'as directed' : {
                136 : 'como se indica'
            },
            'blood sugar' : {
                136 : 'el nivel de azucar en las sangre'
            },
            'into affected eye(s)' : {
                136 : 'en los ojos afectados'
            }
        },
        136 : {
            'por via oral' : {
                42 : 'by mouth'
            },
            'por via topica' : {
                42 : 'topically'
            },
            'en los orificios nasales afectados' : {
                42 : 'into affected nostril(s)'
            },
            'segun las instrucciones' : {
                42 : 'as instructed'
            },
            'en un orificio nasal' : {
                42 : 'into one nostril'
            },
            'como se indica' : {
                42 : 'as directed'
            },
            'el nivel de azucar en las sangre' : {
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
			# special case
			'each day' : {
				136 : 'al dia'
			},
			# special case
			'a day' : {
				136 : 'al dia'
			},
			# special case, 'for' when followed by a frequency
			'for -f' : {
				136 : 'por'
			},
			'day' : {
				136 : 'dia'
			},
			'days' : {
				136 : 'dias'
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
			# special case
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
			# special case
			'al dia' : {
				#42 : {'each day', 'a day'}
                42 : 'each day'
			},
			'por' : {
				42 : 'for'
			},
			'durante' : {
				42 : 'for'
			},
			'dia' : {
				42 : 'day'
			},	
			'dias' : {
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
			# special case
			'una vez' : {
				42 : 'once'
			},
			'hasta' : {
				42 : 'up to'
			}
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
                136 : 'para la presion arterial'
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
            'para la presion arterial' : {
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

    return json.dumps(dictionary)


if __name__ == '__main__':
    get_json()
