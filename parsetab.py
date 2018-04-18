
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'PROGRAMAAND ARCO BOOLEAN BORRAR CIRCULO COMMA DEFINE DEFINIRCOLOR DEFINIRPOSICION DEFINIRX DEFINIRY DERECHA DERECHO DIVI DRAW DRAWI ELSE END EQUAL FALSE FCTE FLOAT FOR GLOBAL GREATEREQTH GREATERTH GROSOR ICTE ID IF INT IZQUIERDA LBRA LESSEQTH LESSTH LPAR MAIN MINUS MOSTRAR MULT NEW NOT NOTEQ OCULTAR OR PLUS POINT PRINT RBRA RETURN REVERSA RPAR SCTE SEQUAL STRING TRUE VELOCIDAD VOID WHILEempty : \n    PROGRAMA : PROGRAMAZ PROGRAMAB PRINCIPAL\n  PROGRAMAB  : FUNCION PROGRAMAB\n                | empty\n  PROGRAMAZ  : GLOBALES\n                | empty\n  GLOBALES : GLOBAL GLOBALEZ END\n  GLOBALEZ : VART GLOBALEZ\n              | empty\n  VART : DRAW ID addVariable EQUAL NEW DRAWI LPAR RPAR\n          | DATA_TIPOS ID addVariable\n        | ARR ID addVariable\n  ESTATUTO : EXPRE genQuad5\n              | CONDICION\n              | CICLO\n              | ACCION\n              | VART\n              | LLAMADA_FUNCION\n              | IMPRIMIR\n  BLOQUE : ESTATUTO BLOQUE\n            | empty\n  DATA_TIPOS : INT addDataType\n                | BOOLEAN addDataType\n                | STRING addDataType\n                | FLOAT addDataType\n                | VOID addDataType\n  ASOP : PLUS\n          | MINUS\n  MDOP : MULT\n          | DIVI\n  ARR : DATA_TIPOS LBRA ICTE RBRA\n  LLAMADA_FUNCION : ID LPAR LLAMADA_FUNCIONP RPAR\n  LLAMADA_FUNCIONP : EXPRE LLAMADA_FUNCIONZ LLAMADA_FUNCIONP\n                      | empty\n  LLAMADA_FUNCIONZ : COMMA\n                      | empty\n  PRINCIPAL : MAIN changeScope LPAR RPAR BLOQUE END\n  CICLO  : WHILEF\n            | FORZ\n  WHILEF : WHILE LPAR EXPRE RPAR BLOQUE END\n  FORZ : FOR LPAR ICTE COMMA ICTE COMMA ICTE RPAR BLOQUE END\n  CONDICION : IF LPAR EXPRE RPAR BLOQUE CONDICIONP END\n  CONDICIONP : ELSE BLOQUE\n                | empty\n  RELOP  : LESSTH \n            | GREATERTH\n            | SEQUAL\n            | NOTEQ\n            | LESSEQTH\n            | GREATEREQTH\n  EXPRE : EXT EXPREZ\n  EXPREZ : EQUAL operatorPush EXT\n            | empty\n  EXT  : EXP EXT_W_RELOP\n  EXT_W_RELOP  : RELOP EXT\n        | empty\n  EXP : TERMINO genQuad2 EXP_W_SIGN\n  EXP_W_SIGN : ASOP operatorPush EXP\n                | empty\n  TERMINO : FAC genQuad1 TERMINO_W_SIGN\n  TERMINO_W_SIGN : MDOP operatorPush TERMINO\n                    | empty\n  VAR_CTE  : ICTE\n              | FCTE\n  IMPRIMIR : PRINT LBRA IMPRIMIRZ RBRA\n  IMPRIMIRZ  : EXPRE \n                | SCTE\n  FAC  : pushExp LPAR EXPRE RPAR popExp\n          | VAR_CTE operandPush\n          | LBRA EXPRE RPAR\n          | ID operandPush FACT\n  FACT : LBRA EXPRE RBRA\n          | LPAR EXPRE RPAR\n          | empty\n  FUNCION : DEFINE DATA_TIPOS ID changeScope VAR_FUN BLOQUE RETURN EXPRE END restoreScope\n  ACCION : ID POINT DIBUJA LPAR VAR_CTE RPAR\n   VAR_FUN : LPAR VAR_FUNP RPAR\n  VAR_FUNP : DATA_TIPOS ID VAR_FUNZ\n              | empty\n  VAR_FUNZ : COMMA VAR_FUNP\n              | empty\n  DIBUJA : DEFINIRPOSICION\n            | DEFINIRCOLOR\n            | DERECHO\n            | REVERSA\n            | IZQUIERDA\n            | DERECHA\n            | VELOCIDAD\n            | BORRAR\n            | MOSTRAR\n            | OCULTAR\n            | CIRCULO\n            | DEFINIRX\n            | DEFINIRY\n            | ARCO\n            | GROSOR\n  restoreScope  :   empty\n    changeScope  :   empty\n     addDataType :  empty\n    addVariable  :   empty \n    operandPush  :   empty   \n    operatorPush   :   empty \n    pushExp   :   empty \n    popExp   :    empty \n    genQuad0   :    empty \n    genQuad1  :    empty   \n    genQuad2  :    empty \n    genQuad5   :    empty \n    '
    
_lr_action_items = {'LPAR':([23,32,33,37,38,39,41,43,44,46,49,51,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,104,105,106,108,109,110,112,113,114,115,116,118,119,121,122,123,127,129,130,131,132,133,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,159,160,161,162,163,169,170,171,173,174,175,176,177,178,182,183,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,-1,-98,45,-1,-100,-11,-12,50,-1,-1,-15,-1,-1,-1,-18,-1,-1,103,-1,106,-103,-38,-17,-39,-14,-63,-19,-1,110,113,-1,-16,116,-64,120,-13,-108,-51,-53,-1,-49,-1,-47,-48,-54,-50,-46,-45,-56,-1,-103,-1,-1,-107,-1,-69,-101,-1,154,-1,-1,-106,-1,-77,-1,-1,-102,-55,-70,-1,-57,-27,-28,-59,-1,-103,-87,-95,-92,-88,-85,-91,-82,-90,-86,179,-84,-94,-93,-89,-96,-83,-1,-1,-74,-71,-30,-1,-29,-62,-60,-10,-52,-65,-1,-1,-32,-1,-35,-36,-1,-1,-1,-58,-68,-104,-73,-72,-61,-76,-1,-40,-42,-1,-41,]),'RETURN':([32,33,41,43,44,51,53,54,55,56,58,60,62,64,65,66,67,68,69,70,72,73,75,76,78,82,84,85,86,87,93,97,101,102,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,169,170,171,174,175,188,189,190,193,194,196,201,205,207,211,],[-1,-1,-100,-11,-12,-1,-15,-1,-1,-1,-18,-1,-1,-21,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,119,-13,-108,-51,-53,-54,-56,-1,-20,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,-58,-68,-104,-73,-72,-61,-76,-40,-42,-41,]),'SEQUAL':([56,62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[91,-1,-63,-1,-1,-1,-64,-1,-1,-107,-69,-101,-1,-1,-106,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'NOTEQ':([56,62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[92,-1,-63,-1,-1,-1,-64,-1,-1,-107,-69,-101,-1,-1,-106,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'VOID':([2,9,10,32,33,41,43,44,49,50,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,166,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[11,11,11,-1,-1,-100,-11,-12,11,11,11,-15,-1,-1,-1,-18,11,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,11,-10,-52,-65,-1,-32,11,11,-58,-68,-104,-73,-72,-61,-76,11,-40,-42,11,-41,]),'GLOBAL':([0,],[2,]),'EQUAL':([29,40,41,55,56,62,69,72,73,75,78,93,97,101,104,105,108,109,112,114,115,123,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[-1,47,-100,88,-1,-1,-63,-1,-1,-1,-64,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-55,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'RPAR':([45,50,55,56,62,69,72,75,78,80,81,86,87,93,97,99,101,104,105,108,109,110,112,114,115,117,120,123,127,130,133,134,135,136,137,156,157,158,162,163,164,165,166,167,170,174,176,177,178,180,185,188,189,190,191,192,193,194,196,206,],[49,-1,-1,-1,-1,-63,-1,-1,-64,118,-79,-51,-53,-54,-56,127,-1,-1,-107,-69,-101,-1,-1,-1,-106,-1,169,-55,-70,-57,-59,174,175,-1,-34,-74,-71,182,-62,-60,184,-78,-1,-81,-52,-1,-1,-35,-36,193,-80,-58,-68,-104,-33,201,-73,-72,-61,209,]),'IZQUIERDA':([111,],[146,]),'WHILE':([32,33,41,43,44,49,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,-100,-11,-12,77,77,-15,-1,-1,-1,-18,77,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,77,77,-58,-68,-104,-73,-72,-61,-76,77,-40,-42,77,-41,]),'GREATERTH':([56,62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[95,-1,-63,-1,-1,-1,-64,-1,-1,-107,-69,-101,-1,-1,-106,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'PRINT':([32,33,41,43,44,49,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,-100,-11,-12,57,57,-15,-1,-1,-1,-18,57,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,57,57,-58,-68,-104,-73,-72,-61,-76,57,-40,-42,57,-41,]),'NEW':([47,],[52,]),'BORRAR':([111,],[151,]),'ARCO':([111,],[139,]),'GROSOR':([111,],[152,]),'MINUS':([62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,156,157,162,163,174,189,190,193,194,196,],[-1,-63,-1,-1,-1,-64,-1,132,-107,-69,-101,-1,-1,-106,-70,-74,-71,-62,-60,-1,-68,-104,-73,-72,-61,]),'DRAWI':([52,],[83,]),'LBRA':([11,15,16,18,19,20,26,27,30,32,33,34,35,36,41,43,44,49,51,53,54,55,56,57,58,59,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,104,105,106,108,109,110,112,113,114,115,116,118,119,121,122,123,127,129,130,131,132,133,136,154,155,156,157,159,160,161,162,163,169,170,171,173,174,175,176,177,178,182,183,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,31,-1,-1,-1,-26,-99,-24,-1,-1,-22,-25,-23,-100,-11,-12,59,59,-15,-1,-1,-1,98,-18,59,59,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-1,-49,59,-47,-48,-54,-50,-46,-45,-56,59,-1,-1,-107,59,-69,-101,59,155,59,-1,-106,59,-77,59,59,-102,-55,-70,-1,-57,-27,-28,-59,-1,59,59,-74,-71,-30,-1,-29,-62,-60,-10,-52,-65,59,-1,-32,59,-35,-36,59,59,59,-58,-68,-104,-73,-72,-61,-76,59,-40,-42,59,-41,]),'POINT':([73,],[111,]),'DEFINE':([0,1,4,5,6,28,186,198,199,],[-1,9,-5,-6,9,-7,-1,-97,-75,]),'MOSTRAR':([111,],[145,]),'RBRA':([42,55,56,62,69,72,75,78,86,87,93,97,101,104,105,108,109,112,114,115,123,124,125,126,127,130,133,156,157,162,163,170,174,181,188,189,190,193,194,196,],[48,-1,-1,-1,-63,-1,-1,-64,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-55,-66,171,-67,-70,-57,-59,-74,-71,-62,-60,-52,-1,194,-58,-68,-104,-73,-72,-61,]),'COMMA':([55,56,62,69,72,75,78,86,87,93,97,101,104,105,108,109,112,114,115,117,123,127,128,130,133,136,156,157,162,163,170,174,187,188,189,190,193,194,196,],[-1,-1,-1,-63,-1,-1,-64,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,166,-55,-70,172,-57,-59,177,-74,-71,-62,-60,-52,-1,200,-58,-68,-104,-73,-72,-61,]),'MULT':([69,72,73,75,78,101,108,109,112,114,115,127,156,157,174,189,190,193,194,],[-63,-1,-1,-1,-64,-1,-69,-101,-1,161,-106,-70,-74,-71,-1,-68,-104,-73,-72,]),'DEFINIRY':([111,],[149,]),'GREATEREQTH':([56,62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[94,-1,-63,-1,-1,-1,-64,-1,-1,-107,-69,-101,-1,-1,-106,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'PLUS':([62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,156,157,162,163,174,189,190,193,194,196,],[-1,-63,-1,-1,-1,-64,-1,131,-107,-69,-101,-1,-1,-106,-70,-74,-71,-62,-60,-1,-68,-104,-73,-72,-61,]),'DEFINIRPOSICION':([111,],[144,]),'DEFINIRCOLOR':([111,],[153,]),'$end':([3,22,107,],[0,-2,-37,]),'DERECHO':([111,],[148,]),'DRAW':([2,10,32,33,41,43,44,49,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[14,14,-1,-1,-100,-11,-12,14,14,-15,-1,-1,-1,-18,14,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,14,14,-58,-68,-104,-73,-72,-61,-76,14,-40,-42,14,-41,]),'END':([2,10,12,13,25,32,33,41,43,44,49,53,54,55,56,58,60,62,64,65,66,67,68,69,70,71,72,73,75,76,78,84,85,86,87,93,97,101,102,104,105,108,109,112,114,115,123,127,130,133,156,157,162,163,168,169,170,171,174,175,182,184,188,189,190,193,194,195,196,197,201,202,203,204,205,207,208,209,210,211,],[-1,-1,28,-9,-8,-1,-1,-100,-11,-12,-1,-15,-1,-1,-1,-18,-1,-1,-21,-38,-17,-39,-14,-63,-19,107,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-20,-1,-107,-69,-101,-1,-1,-106,-55,-70,-57,-59,-74,-71,-62,-60,186,-10,-52,-65,-1,-32,-1,-1,-58,-68,-104,-73,-72,-1,-61,205,-76,207,-1,-44,-40,-42,-43,-1,211,-41,]),'STRING':([2,9,10,32,33,41,43,44,49,50,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,166,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[15,15,15,-1,-1,-100,-11,-12,15,15,15,-15,-1,-1,-1,-18,15,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,15,-10,-52,-65,-1,-32,15,15,-58,-68,-104,-73,-72,-61,-76,15,-40,-42,15,-41,]),'FOR':([32,33,41,43,44,49,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,-100,-11,-12,61,61,-15,-1,-1,-1,-18,61,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,61,61,-58,-68,-104,-73,-72,-61,-76,61,-40,-42,61,-41,]),'REVERSA':([111,],[142,]),'OCULTAR':([111,],[143,]),'DEFINIRX':([111,],[150,]),'ELSE':([32,33,41,43,44,53,54,55,56,58,60,62,64,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,102,104,105,108,109,112,114,115,123,127,130,133,156,157,162,163,169,170,171,174,175,182,188,189,190,193,194,195,196,201,205,207,211,],[-1,-1,-100,-11,-12,-15,-1,-1,-1,-18,-1,-1,-21,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-20,-1,-107,-69,-101,-1,-1,-106,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,-1,-58,-68,-104,-73,-72,203,-61,-76,-40,-42,-41,]),'ICTE':([31,32,33,41,43,44,49,51,53,54,55,56,58,59,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,103,104,105,106,108,109,110,112,113,114,115,116,118,119,121,122,123,127,129,130,131,132,133,136,154,155,156,157,159,160,161,162,163,169,170,171,172,173,174,175,176,177,178,179,182,183,184,188,189,190,193,194,196,200,201,203,205,207,209,211,],[42,-1,-1,-100,-11,-12,69,69,-15,-1,-1,-1,-18,69,69,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-1,-49,69,-47,-48,-54,-50,-46,-45,-56,69,-1,128,-1,-107,69,-69,-101,69,-1,69,-1,-106,69,-77,69,69,-102,-55,-70,-1,-57,-27,-28,-59,-1,69,69,-74,-71,-30,-1,-29,-62,-60,-10,-52,-65,187,69,-1,-32,69,-35,-36,69,69,69,69,-58,-68,-104,-73,-72,-61,206,-76,69,-40,-42,69,-41,]),'LESSTH':([56,62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[96,-1,-63,-1,-1,-1,-64,-1,-1,-107,-69,-101,-1,-1,-106,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'DERECHA':([111,],[138,]),'ID':([11,14,15,16,17,18,19,20,24,26,27,30,32,33,34,35,36,41,43,44,48,49,51,53,54,55,56,58,59,60,62,65,66,67,68,69,70,72,73,75,76,78,79,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,104,105,106,108,109,110,112,113,114,115,116,118,119,121,122,123,127,129,130,131,132,133,136,154,155,156,157,159,160,161,162,163,169,170,171,173,174,175,176,177,178,182,183,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,29,-1,32,33,-1,-1,-1,39,-26,-99,-24,-1,-1,-22,-25,-23,-100,-11,-12,-31,73,73,-15,-1,-1,-1,-18,101,73,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,117,-13,-108,-51,-53,-1,-49,101,-47,-48,-54,-50,-46,-45,-56,101,-1,-1,-107,101,-69,-101,101,-1,101,-1,-106,101,-77,101,101,-102,-55,-70,-1,-57,-27,-28,-59,-1,101,101,-74,-71,-30,-1,-29,-62,-60,-10,-52,-65,101,-1,-32,101,-35,-36,73,101,73,-58,-68,-104,-73,-72,-61,-76,73,-40,-42,73,-41,]),'IF':([32,33,41,43,44,49,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,-100,-11,-12,74,74,-15,-1,-1,-1,-18,74,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,-10,-52,-65,-1,-32,74,74,-58,-68,-104,-73,-72,-61,-76,74,-40,-42,74,-41,]),'LESSEQTH':([56,62,69,72,73,75,78,101,104,105,108,109,112,114,115,127,130,133,156,157,162,163,174,188,189,190,193,194,196,],[89,-1,-63,-1,-1,-1,-64,-1,-1,-107,-69,-101,-1,-1,-106,-70,-57,-59,-74,-71,-62,-60,-1,-58,-68,-104,-73,-72,-61,]),'VELOCIDAD':([111,],[141,]),'INT':([2,9,10,32,33,41,43,44,49,50,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,166,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[18,18,18,-1,-1,-100,-11,-12,18,18,18,-15,-1,-1,-1,-18,18,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,18,-10,-52,-65,-1,-32,18,18,-58,-68,-104,-73,-72,-61,-76,18,-40,-42,18,-41,]),'FLOAT':([2,9,10,32,33,41,43,44,49,50,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,166,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[19,19,19,-1,-1,-100,-11,-12,19,19,19,-15,-1,-1,-1,-18,19,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,19,-10,-52,-65,-1,-32,19,19,-58,-68,-104,-73,-72,-61,-76,19,-40,-42,19,-41,]),'SCTE':([98,],[126,]),'BOOLEAN':([2,9,10,32,33,41,43,44,49,50,51,53,54,55,56,58,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,93,97,101,104,105,108,109,112,114,115,118,123,127,130,133,156,157,162,163,166,169,170,171,174,175,182,184,188,189,190,193,194,196,201,203,205,207,209,211,],[20,20,20,-1,-1,-100,-11,-12,20,20,20,-15,-1,-1,-1,-18,20,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-54,-56,-1,-1,-107,-69,-101,-1,-1,-106,-77,-55,-70,-57,-59,-74,-71,-62,-60,20,-10,-52,-65,-1,-32,20,20,-58,-68,-104,-73,-72,-61,-76,20,-40,-42,20,-41,]),'FCTE':([32,33,41,43,44,49,51,53,54,55,56,58,59,60,62,65,66,67,68,69,70,72,73,75,76,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,104,105,106,108,109,110,112,113,114,115,116,118,119,121,122,123,127,129,130,131,132,133,136,154,155,156,157,159,160,161,162,163,169,170,171,173,174,175,176,177,178,179,182,183,184,188,189,190,193,194,196,201,203,205,207,209,211,],[-1,-1,-100,-11,-12,78,78,-15,-1,-1,-1,-18,78,78,-1,-38,-17,-39,-14,-63,-19,-1,-1,-1,-16,-64,-13,-108,-51,-53,-1,-49,78,-47,-48,-54,-50,-46,-45,-56,78,-1,-1,-107,78,-69,-101,78,-1,78,-1,-106,78,-77,78,78,-102,-55,-70,-1,-57,-27,-28,-59,-1,78,78,-74,-71,-30,-1,-29,-62,-60,-10,-52,-65,78,-1,-32,78,-35,-36,78,78,78,78,-58,-68,-104,-73,-72,-61,-76,78,-40,-42,78,-41,]),'DIVI':([69,72,73,75,78,101,108,109,112,114,115,127,156,157,174,189,190,193,194,],[-63,-1,-1,-1,-64,-1,-69,-101,-1,159,-106,-70,-74,-71,-1,-68,-104,-73,-72,]),'MAIN':([0,1,4,5,6,7,8,21,28,186,198,199,],[-1,-1,-5,-6,-1,23,-4,-3,-7,-1,-97,-75,]),'CIRCULO':([111,],[140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'operatorPush':([88,129,160,],[121,173,183,]),'VART':([2,10,49,51,60,182,184,203,209,],[10,10,66,66,66,66,66,66,66,]),'CICLO':([49,51,60,182,184,203,209,],[53,53,53,53,53,53,53,]),'EXPRE':([49,51,59,60,98,106,110,113,116,119,154,155,176,182,184,203,209,],[54,54,99,54,124,134,136,158,164,168,180,181,136,54,54,54,54,]),'popExp':([174,],[189,]),'LLAMADA_FUNCIONP':([110,176,],[135,191,]),'IMPRIMIRZ':([98,],[125,]),'VAR_CTE':([49,51,59,60,90,98,106,110,113,116,119,121,154,155,173,176,179,182,183,184,203,209,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,192,72,72,72,72,72,]),'EXT':([49,51,59,60,90,98,106,110,113,116,119,121,154,155,176,182,184,203,209,],[55,55,55,55,123,55,55,55,55,55,55,170,55,55,55,55,55,55,55,]),'EXP':([49,51,59,60,90,98,106,110,113,116,119,121,154,155,173,176,182,184,203,209,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,188,56,56,56,56,56,]),'restoreScope':([186,],[199,]),'EXPREZ':([55,],[86,]),'RELOP':([56,],[90,]),'LLAMADA_FUNCION':([49,51,60,182,184,203,209,],[58,58,58,58,58,58,58,]),'genQuad2':([62,],[104,]),'genQuad5':([54,],[84,]),'VAR_FUNZ':([117,],[165,]),'MDOP':([114,],[160,]),'ASOP':([104,],[129,]),'addDataType':([11,15,18,19,20,],[26,30,34,35,36,]),'ESTATUTO':([49,51,60,182,184,203,209,],[60,60,60,60,60,60,60,]),'operandPush':([72,73,101,],[108,112,112,]),'VAR_FUNP':([50,166,],[80,185,]),'EXP_W_SIGN':([104,],[130,]),'GLOBALEZ':([2,10,],[12,25,]),'TERMINO':([49,51,59,60,90,98,106,110,113,116,119,121,154,155,173,176,182,183,184,203,209,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,196,62,62,62,]),'pushExp':([49,51,59,60,90,98,106,110,113,116,119,121,154,155,173,176,182,183,184,203,209,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'FAC':([49,51,59,60,90,98,106,110,113,116,119,121,154,155,173,176,182,183,184,203,209,],[75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'VAR_FUN':([46,],[51,]),'GLOBALES':([0,],[4,]),'empty':([0,1,2,6,10,11,15,18,19,20,23,29,32,33,39,49,50,51,54,55,56,59,60,62,72,73,75,88,90,98,101,104,106,110,112,113,114,116,117,119,121,129,136,154,155,160,166,173,174,176,182,183,184,186,195,203,209,],[5,8,13,8,13,27,27,27,27,27,37,41,41,41,37,64,81,64,85,87,97,100,64,105,109,109,115,122,100,100,109,133,100,137,156,100,162,100,167,100,100,122,178,100,100,122,81,100,190,137,64,100,64,198,204,64,64,]),'changeScope':([23,39,],[38,46,]),'LLAMADA_FUNCIONZ':([136,],[176,]),'genQuad1':([75,],[114,]),'WHILEF':([49,51,60,182,184,203,209,],[65,65,65,65,65,65,65,]),'DATA_TIPOS':([2,9,10,49,50,51,60,166,182,184,203,209,],[16,24,16,16,79,16,16,79,16,16,16,16,]),'addVariable':([29,32,33,],[40,43,44,]),'FORZ':([49,51,60,182,184,203,209,],[67,67,67,67,67,67,67,]),'CONDICION':([49,51,60,182,184,203,209,],[68,68,68,68,68,68,68,]),'CONDICIONP':([195,],[202,]),'IMPRIMIR':([49,51,60,182,184,203,209,],[70,70,70,70,70,70,70,]),'BLOQUE':([49,51,60,182,184,203,209,],[71,82,102,195,197,208,210,]),'TERMINO_W_SIGN':([114,],[163,]),'FUNCION':([1,6,],[6,6,]),'ARR':([2,10,49,51,60,182,184,203,209,],[17,17,17,17,17,17,17,17,17,]),'PROGRAMAZ':([0,],[1,]),'ACCION':([49,51,60,182,184,203,209,],[76,76,76,76,76,76,76,]),'EXT_W_RELOP':([56,],[93,]),'DIBUJA':([111,],[147,]),'PROGRAMA':([0,],[3,]),'PROGRAMAB':([1,6,],[7,21,]),'FACT':([112,],[157,]),'PRINCIPAL':([7,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','Andor.py',34),
  ('PROGRAMA -> PROGRAMAZ PROGRAMAB PRINCIPAL','PROGRAMA',3,'p_PROGRAMA','Andor.py',39),
  ('PROGRAMAB -> FUNCION PROGRAMAB','PROGRAMAB',2,'p_PROGRAMAB','Andor.py',43),
  ('PROGRAMAB -> empty','PROGRAMAB',1,'p_PROGRAMAB','Andor.py',44),
  ('PROGRAMAZ -> GLOBALES','PROGRAMAZ',1,'p_PROGRAMAZ','Andor.py',48),
  ('PROGRAMAZ -> empty','PROGRAMAZ',1,'p_PROGRAMAZ','Andor.py',49),
  ('GLOBALES -> GLOBAL GLOBALEZ END','GLOBALES',3,'p_GLOBALES','Andor.py',53),
  ('GLOBALEZ -> VART GLOBALEZ','GLOBALEZ',2,'p_GLOBALEZ','Andor.py',56),
  ('GLOBALEZ -> empty','GLOBALEZ',1,'p_GLOBALEZ','Andor.py',57),
  ('VART -> DRAW ID addVariable EQUAL NEW DRAWI LPAR RPAR','VART',8,'p_VART','Andor.py',61),
  ('VART -> DATA_TIPOS ID addVariable','VART',3,'p_VART','Andor.py',62),
  ('VART -> ARR ID addVariable','VART',3,'p_VART','Andor.py',63),
  ('ESTATUTO -> EXPRE genQuad5','ESTATUTO',2,'p_ESTATUTO','Andor.py',67),
  ('ESTATUTO -> CONDICION','ESTATUTO',1,'p_ESTATUTO','Andor.py',68),
  ('ESTATUTO -> CICLO','ESTATUTO',1,'p_ESTATUTO','Andor.py',69),
  ('ESTATUTO -> ACCION','ESTATUTO',1,'p_ESTATUTO','Andor.py',70),
  ('ESTATUTO -> VART','ESTATUTO',1,'p_ESTATUTO','Andor.py',71),
  ('ESTATUTO -> LLAMADA_FUNCION','ESTATUTO',1,'p_ESTATUTO','Andor.py',72),
  ('ESTATUTO -> IMPRIMIR','ESTATUTO',1,'p_ESTATUTO','Andor.py',73),
  ('BLOQUE -> ESTATUTO BLOQUE','BLOQUE',2,'p_BLOQUE','Andor.py',77),
  ('BLOQUE -> empty','BLOQUE',1,'p_BLOQUE','Andor.py',78),
  ('DATA_TIPOS -> INT addDataType','DATA_TIPOS',2,'p_DATA_TIPOS','Andor.py',82),
  ('DATA_TIPOS -> BOOLEAN addDataType','DATA_TIPOS',2,'p_DATA_TIPOS','Andor.py',83),
  ('DATA_TIPOS -> STRING addDataType','DATA_TIPOS',2,'p_DATA_TIPOS','Andor.py',84),
  ('DATA_TIPOS -> FLOAT addDataType','DATA_TIPOS',2,'p_DATA_TIPOS','Andor.py',85),
  ('DATA_TIPOS -> VOID addDataType','DATA_TIPOS',2,'p_DATA_TIPOS','Andor.py',86),
  ('ASOP -> PLUS','ASOP',1,'p_ASOP','Andor.py',91),
  ('ASOP -> MINUS','ASOP',1,'p_ASOP','Andor.py',92),
  ('MDOP -> MULT','MDOP',1,'p_MDOP','Andor.py',97),
  ('MDOP -> DIVI','MDOP',1,'p_MDOP','Andor.py',98),
  ('ARR -> DATA_TIPOS LBRA ICTE RBRA','ARR',4,'p_ARR','Andor.py',103),
  ('LLAMADA_FUNCION -> ID LPAR LLAMADA_FUNCIONP RPAR','LLAMADA_FUNCION',4,'p_LLAMADA_FUNCION','Andor.py',108),
  ('LLAMADA_FUNCIONP -> EXPRE LLAMADA_FUNCIONZ LLAMADA_FUNCIONP','LLAMADA_FUNCIONP',3,'p_LLAMADA_FUNCIONP','Andor.py',112),
  ('LLAMADA_FUNCIONP -> empty','LLAMADA_FUNCIONP',1,'p_LLAMADA_FUNCIONP','Andor.py',113),
  ('LLAMADA_FUNCIONZ -> COMMA','LLAMADA_FUNCIONZ',1,'p_LLAMADA_FUNCIONZ','Andor.py',117),
  ('LLAMADA_FUNCIONZ -> empty','LLAMADA_FUNCIONZ',1,'p_LLAMADA_FUNCIONZ','Andor.py',118),
  ('PRINCIPAL -> MAIN changeScope LPAR RPAR BLOQUE END','PRINCIPAL',6,'p_PRINCIPAL','Andor.py',122),
  ('CICLO -> WHILEF','CICLO',1,'p_CICLO','Andor.py',127),
  ('CICLO -> FORZ','CICLO',1,'p_CICLO','Andor.py',128),
  ('WHILEF -> WHILE LPAR EXPRE RPAR BLOQUE END','WHILEF',6,'p_WHILEF','Andor.py',132),
  ('FORZ -> FOR LPAR ICTE COMMA ICTE COMMA ICTE RPAR BLOQUE END','FORZ',10,'p_FORZ','Andor.py',136),
  ('CONDICION -> IF LPAR EXPRE RPAR BLOQUE CONDICIONP END','CONDICION',7,'p_CONDICION','Andor.py',140),
  ('CONDICIONP -> ELSE BLOQUE','CONDICIONP',2,'p_CONDICIONP','Andor.py',143),
  ('CONDICIONP -> empty','CONDICIONP',1,'p_CONDICIONP','Andor.py',144),
  ('RELOP -> LESSTH','RELOP',1,'p_RELOP','Andor.py',148),
  ('RELOP -> GREATERTH','RELOP',1,'p_RELOP','Andor.py',149),
  ('RELOP -> SEQUAL','RELOP',1,'p_RELOP','Andor.py',150),
  ('RELOP -> NOTEQ','RELOP',1,'p_RELOP','Andor.py',151),
  ('RELOP -> LESSEQTH','RELOP',1,'p_RELOP','Andor.py',152),
  ('RELOP -> GREATEREQTH','RELOP',1,'p_RELOP','Andor.py',153),
  ('EXPRE -> EXT EXPREZ','EXPRE',2,'p_EXPRE','Andor.py',157),
  ('EXPREZ -> EQUAL operatorPush EXT','EXPREZ',3,'p_EXPREZ','Andor.py',160),
  ('EXPREZ -> empty','EXPREZ',1,'p_EXPREZ','Andor.py',161),
  ('EXT -> EXP EXT_W_RELOP','EXT',2,'p_EXT','Andor.py',164),
  ('EXT_W_RELOP -> RELOP EXT','EXT_W_RELOP',2,'p_EXT_W_RELOP','Andor.py',167),
  ('EXT_W_RELOP -> empty','EXT_W_RELOP',1,'p_EXT_W_RELOP','Andor.py',168),
  ('EXP -> TERMINO genQuad2 EXP_W_SIGN','EXP',3,'p_EXP','Andor.py',172),
  ('EXP_W_SIGN -> ASOP operatorPush EXP','EXP_W_SIGN',3,'p_EXP_W_SIGN','Andor.py',176),
  ('EXP_W_SIGN -> empty','EXP_W_SIGN',1,'p_EXP_W_SIGN','Andor.py',177),
  ('TERMINO -> FAC genQuad1 TERMINO_W_SIGN','TERMINO',3,'p_TERMINO','Andor.py',181),
  ('TERMINO_W_SIGN -> MDOP operatorPush TERMINO','TERMINO_W_SIGN',3,'p_TERMINO_W_SIGN','Andor.py',185),
  ('TERMINO_W_SIGN -> empty','TERMINO_W_SIGN',1,'p_TERMINO_W_SIGN','Andor.py',186),
  ('VAR_CTE -> ICTE','VAR_CTE',1,'p_VAR_CTE','Andor.py',190),
  ('VAR_CTE -> FCTE','VAR_CTE',1,'p_VAR_CTE','Andor.py',191),
  ('IMPRIMIR -> PRINT LBRA IMPRIMIRZ RBRA','IMPRIMIR',4,'p_IMPRIMIR','Andor.py',196),
  ('IMPRIMIRZ -> EXPRE','IMPRIMIRZ',1,'p_IMPRIMIRZ','Andor.py',200),
  ('IMPRIMIRZ -> SCTE','IMPRIMIRZ',1,'p_IMPRIMIRZ','Andor.py',201),
  ('FAC -> pushExp LPAR EXPRE RPAR popExp','FAC',5,'p_FAC','Andor.py',205),
  ('FAC -> VAR_CTE operandPush','FAC',2,'p_FAC','Andor.py',206),
  ('FAC -> LBRA EXPRE RPAR','FAC',3,'p_FAC','Andor.py',207),
  ('FAC -> ID operandPush FACT','FAC',3,'p_FAC','Andor.py',208),
  ('FACT -> LBRA EXPRE RBRA','FACT',3,'p_FACT','Andor.py',212),
  ('FACT -> LPAR EXPRE RPAR','FACT',3,'p_FACT','Andor.py',213),
  ('FACT -> empty','FACT',1,'p_FACT','Andor.py',214),
  ('FUNCION -> DEFINE DATA_TIPOS ID changeScope VAR_FUN BLOQUE RETURN EXPRE END restoreScope','FUNCION',10,'p_FUNCION','Andor.py',218),
  ('ACCION -> ID POINT DIBUJA LPAR VAR_CTE RPAR','ACCION',6,'p_ACCION','Andor.py',223),
  ('VAR_FUN -> LPAR VAR_FUNP RPAR','VAR_FUN',3,'p_VAR_FUN','Andor.py',227),
  ('VAR_FUNP -> DATA_TIPOS ID VAR_FUNZ','VAR_FUNP',3,'p_VAR_FUNP','Andor.py',231),
  ('VAR_FUNP -> empty','VAR_FUNP',1,'p_VAR_FUNP','Andor.py',232),
  ('VAR_FUNZ -> COMMA VAR_FUNP','VAR_FUNZ',2,'p_VAR_FUNZ','Andor.py',236),
  ('VAR_FUNZ -> empty','VAR_FUNZ',1,'p_VAR_FUNZ','Andor.py',237),
  ('DIBUJA -> DEFINIRPOSICION','DIBUJA',1,'p_DIBUJA','Andor.py',241),
  ('DIBUJA -> DEFINIRCOLOR','DIBUJA',1,'p_DIBUJA','Andor.py',242),
  ('DIBUJA -> DERECHO','DIBUJA',1,'p_DIBUJA','Andor.py',243),
  ('DIBUJA -> REVERSA','DIBUJA',1,'p_DIBUJA','Andor.py',244),
  ('DIBUJA -> IZQUIERDA','DIBUJA',1,'p_DIBUJA','Andor.py',245),
  ('DIBUJA -> DERECHA','DIBUJA',1,'p_DIBUJA','Andor.py',246),
  ('DIBUJA -> VELOCIDAD','DIBUJA',1,'p_DIBUJA','Andor.py',247),
  ('DIBUJA -> BORRAR','DIBUJA',1,'p_DIBUJA','Andor.py',248),
  ('DIBUJA -> MOSTRAR','DIBUJA',1,'p_DIBUJA','Andor.py',249),
  ('DIBUJA -> OCULTAR','DIBUJA',1,'p_DIBUJA','Andor.py',250),
  ('DIBUJA -> CIRCULO','DIBUJA',1,'p_DIBUJA','Andor.py',251),
  ('DIBUJA -> DEFINIRX','DIBUJA',1,'p_DIBUJA','Andor.py',252),
  ('DIBUJA -> DEFINIRY','DIBUJA',1,'p_DIBUJA','Andor.py',253),
  ('DIBUJA -> ARCO','DIBUJA',1,'p_DIBUJA','Andor.py',254),
  ('DIBUJA -> GROSOR','DIBUJA',1,'p_DIBUJA','Andor.py',255),
  ('restoreScope -> empty','restoreScope',1,'p_restoreScope','Andor.py',268),
  ('changeScope -> empty','changeScope',1,'p_changeScope','Andor.py',273),
  ('addDataType -> empty','addDataType',1,'p_addDataType','Andor.py',278),
  ('addVariable -> empty','addVariable',1,'p_addVariable','Andor.py',282),
  ('operandPush -> empty','operandPush',1,'p_operandPush','Andor.py',288),
  ('operatorPush -> empty','operatorPush',1,'p_operatorPush','Andor.py',293),
  ('pushExp -> empty','pushExp',1,'p_pushExp','Andor.py',299),
  ('popExp -> empty','popExp',1,'p_popExp','Andor.py',304),
  ('genQuad0 -> empty','genQuad0',1,'p_genQuad0','Andor.py',309),
  ('genQuad1 -> empty','genQuad1',1,'p_genQuad1','Andor.py',313),
  ('genQuad2 -> empty','genQuad2',1,'p_genQuad2','Andor.py',318),
  ('genQuad5 -> empty','genQuad5',1,'p_genQuad5','Andor.py',323),
]
