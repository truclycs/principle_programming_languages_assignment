<<<<<<< HEAD
# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u012c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\3\2\6\2C\n\2\r\2\16\2D\3\2\3\2\3")
        buf.write("\3\3\3\3\3\5\3L\n\3\3\3\3\3\3\4\3\4\3\4\7\4S\n\4\f\4\16")
        buf.write("\4V\13\4\3\5\3\5\3\5\3\5\5\5\\\n\5\3\6\3\6\3\6\3\6\5\6")
        buf.write("b\n\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7j\n\7\f\7\16\7m\13\7")
        buf.write("\3\b\3\b\3\b\3\b\5\bs\n\b\3\t\3\t\3\t\5\tx\n\t\3\n\3\n")
        buf.write("\3\13\3\13\5\13~\n\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u0088\n\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u0090\n\r")
        buf.write("\f\r\16\r\u0093\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16")
        buf.write("\u009b\n\16\f\16\16\16\u009e\13\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u00a5\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00ac")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00b4\n\21\f")
        buf.write("\21\16\21\u00b7\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7")
        buf.write("\22\u00bf\n\22\f\22\16\22\u00c2\13\22\3\23\3\23\3\23\5")
        buf.write("\23\u00c7\n\23\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u00cf")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\5\25\u00db\n\25\3\26\3\26\3\26\5\26\u00e0\n\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\7\27\u00e7\n\27\f\27\16\27\u00ea\13")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00f4")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00fd\n")
        buf.write("\31\3\32\3\32\6\32\u0101\n\32\r\32\16\32\u0102\3\32\3")
        buf.write("\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\5\36")
        buf.write("\u011b\n\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \7 \u0125")
        buf.write("\n \f \16 \u0128\13 \3 \3 \3 \2\6\30\32 \"!\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">\2\b\5\2\5\6\13\13\r\r\4\2\26\26\36\36\4\2\27\30\37 ")
        buf.write("\4\2\22\22\32\32\4\2\23\23\33\34\4\2\24\24\32\32\2\u0134")
        buf.write("\2B\3\2\2\2\4H\3\2\2\2\6O\3\2\2\2\bW\3\2\2\2\n]\3\2\2")
        buf.write("\2\ff\3\2\2\2\16n\3\2\2\2\20w\3\2\2\2\22y\3\2\2\2\24{")
        buf.write("\3\2\2\2\26\u0087\3\2\2\2\30\u0089\3\2\2\2\32\u0094\3")
        buf.write("\2\2\2\34\u00a4\3\2\2\2\36\u00ab\3\2\2\2 \u00ad\3\2\2")
        buf.write("\2\"\u00b8\3\2\2\2$\u00c6\3\2\2\2&\u00ce\3\2\2\2(\u00da")
        buf.write("\3\2\2\2*\u00dc\3\2\2\2,\u00e3\3\2\2\2.\u00f3\3\2\2\2")
        buf.write("\60\u00f5\3\2\2\2\62\u00fe\3\2\2\2\64\u0108\3\2\2\2\66")
        buf.write("\u0112\3\2\2\28\u0115\3\2\2\2:\u0118\3\2\2\2<\u011e\3")
        buf.write("\2\2\2>\u0121\3\2\2\2@C\5\4\3\2AC\5\n\6\2B@\3\2\2\2BA")
        buf.write("\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2EF\3\2\2\2FG\7\2")
        buf.write("\2\3G\3\3\2\2\2HK\5\22\n\2IL\5\b\5\2JL\5\6\4\2KI\3\2\2")
        buf.write("\2KJ\3\2\2\2LM\3\2\2\2MN\7\'\2\2N\5\3\2\2\2OT\5\b\5\2")
        buf.write("PQ\7(\2\2QS\5\b\5\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3")
        buf.write("\2\2\2U\7\3\2\2\2VT\3\2\2\2W[\7,\2\2XY\7!\2\2YZ\7)\2\2")
        buf.write("Z\\\7\"\2\2[X\3\2\2\2[\\\3\2\2\2\\\t\3\2\2\2]^\5\20\t")
        buf.write("\2^_\7,\2\2_a\7#\2\2`b\5\f\7\2a`\3\2\2\2ab\3\2\2\2bc\3")
        buf.write("\2\2\2cd\7$\2\2de\5> \2e\13\3\2\2\2fk\5\16\b\2gh\7(\2")
        buf.write("\2hj\5\16\b\2ig\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2")
        buf.write("l\r\3\2\2\2mk\3\2\2\2no\5\22\n\2or\7,\2\2pq\7!\2\2qs\7")
        buf.write("\"\2\2rp\3\2\2\2rs\3\2\2\2s\17\3\2\2\2tx\5\22\n\2ux\5")
        buf.write("\24\13\2vx\7\17\2\2wt\3\2\2\2wu\3\2\2\2wv\3\2\2\2x\21")
        buf.write("\3\2\2\2yz\t\2\2\2z\23\3\2\2\2{}\5\22\n\2|~\7,\2\2}|\3")
        buf.write("\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080\7!\2\2\u0080\u0081")
        buf.write("\7\"\2\2\u0081\25\3\2\2\2\u0082\u0083\5\30\r\2\u0083\u0084")
        buf.write("\7\31\2\2\u0084\u0085\5\26\f\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0088\5\30\r\2\u0087\u0082\3\2\2\2\u0087\u0086\3\2\2")
        buf.write("\2\u0088\27\3\2\2\2\u0089\u008a\b\r\1\2\u008a\u008b\5")
        buf.write("\32\16\2\u008b\u0091\3\2\2\2\u008c\u008d\f\4\2\2\u008d")
        buf.write("\u008e\7\25\2\2\u008e\u0090\5\32\16\2\u008f\u008c\3\2")
        buf.write("\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092")
        buf.write("\3\2\2\2\u0092\31\3\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095")
        buf.write("\b\16\1\2\u0095\u0096\5\34\17\2\u0096\u009c\3\2\2\2\u0097")
        buf.write("\u0098\f\4\2\2\u0098\u0099\7\35\2\2\u0099\u009b\5\34\17")
        buf.write("\2\u009a\u0097\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\33\3\2\2\2\u009e\u009c")
        buf.write("\3\2\2\2\u009f\u00a0\5\36\20\2\u00a0\u00a1\t\3\2\2\u00a1")
        buf.write("\u00a2\5\36\20\2\u00a2\u00a5\3\2\2\2\u00a3\u00a5\5\36")
        buf.write("\20\2\u00a4\u009f\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\35")
        buf.write("\3\2\2\2\u00a6\u00a7\5 \21\2\u00a7\u00a8\t\4\2\2\u00a8")
        buf.write("\u00a9\5 \21\2\u00a9\u00ac\3\2\2\2\u00aa\u00ac\5 \21\2")
        buf.write("\u00ab\u00a6\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\37\3\2")
        buf.write("\2\2\u00ad\u00ae\b\21\1\2\u00ae\u00af\5\"\22\2\u00af\u00b5")
        buf.write("\3\2\2\2\u00b0\u00b1\f\4\2\2\u00b1\u00b2\t\5\2\2\u00b2")
        buf.write("\u00b4\5\"\22\2\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3\2\2")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6!\3\2")
        buf.write("\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\b\22\1\2\u00b9\u00ba")
        buf.write("\5$\23\2\u00ba\u00c0\3\2\2\2\u00bb\u00bc\f\4\2\2\u00bc")
        buf.write("\u00bd\t\6\2\2\u00bd\u00bf\5$\23\2\u00be\u00bb\3\2\2\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1#\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4")
        buf.write("\t\7\2\2\u00c4\u00c7\5$\23\2\u00c5\u00c7\5&\24\2\u00c6")
        buf.write("\u00c3\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7%\3\2\2\2\u00c8")
        buf.write("\u00c9\5(\25\2\u00c9\u00ca\7!\2\2\u00ca\u00cb\5\26\f\2")
        buf.write("\u00cb\u00cc\7\"\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cf\5")
        buf.write("(\25\2\u00ce\u00c8\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\'")
        buf.write("\3\2\2\2\u00d0\u00db\7)\2\2\u00d1\u00db\7*\2\2\u00d2\u00db")
        buf.write("\7+\2\2\u00d3\u00db\7\60\2\2\u00d4\u00d5\7#\2\2\u00d5")
        buf.write("\u00d6\5\26\f\2\u00d6\u00d7\7$\2\2\u00d7\u00db\3\2\2\2")
        buf.write("\u00d8\u00db\5*\26\2\u00d9\u00db\7,\2\2\u00da\u00d0\3")
        buf.write("\2\2\2\u00da\u00d1\3\2\2\2\u00da\u00d2\3\2\2\2\u00da\u00d3")
        buf.write("\3\2\2\2\u00da\u00d4\3\2\2\2\u00da\u00d8\3\2\2\2\u00da")
        buf.write("\u00d9\3\2\2\2\u00db)\3\2\2\2\u00dc\u00dd\7,\2\2\u00dd")
        buf.write("\u00df\7#\2\2\u00de\u00e0\5,\27\2\u00df\u00de\3\2\2\2")
        buf.write("\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\7")
        buf.write("$\2\2\u00e2+\3\2\2\2\u00e3\u00e8\5\26\f\2\u00e4\u00e5")
        buf.write("\7(\2\2\u00e5\u00e7\5\26\f\2\u00e6\u00e4\3\2\2\2\u00e7")
        buf.write("\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9-\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00f4\5\60\31")
        buf.write("\2\u00ec\u00f4\5\64\33\2\u00ed\u00f4\5\62\32\2\u00ee\u00f4")
        buf.write("\5\66\34\2\u00ef\u00f4\58\35\2\u00f0\u00f4\5:\36\2\u00f1")
        buf.write("\u00f4\5<\37\2\u00f2\u00f4\5> \2\u00f3\u00eb\3\2\2\2\u00f3")
        buf.write("\u00ec\3\2\2\2\u00f3\u00ed\3\2\2\2\u00f3\u00ee\3\2\2\2")
        buf.write("\u00f3\u00ef\3\2\2\2\u00f3\u00f0\3\2\2\2\u00f3\u00f1\3")
        buf.write("\2\2\2\u00f3\u00f2\3\2\2\2\u00f4/\3\2\2\2\u00f5\u00f6")
        buf.write("\7\f\2\2\u00f6\u00f7\7#\2\2\u00f7\u00f8\5\26\f\2\u00f8")
        buf.write("\u00f9\7$\2\2\u00f9\u00fc\5.\30\2\u00fa\u00fb\7\t\2\2")
        buf.write("\u00fb\u00fd\5.\30\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\61\3\2\2\2\u00fe\u0100\7\20\2\2\u00ff\u0101")
        buf.write("\5.\30\2\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0105\7\21\2\2\u0105\u0106\5\26\f\2\u0106\u0107")
        buf.write("\7\'\2\2\u0107\63\3\2\2\2\u0108\u0109\7\n\2\2\u0109\u010a")
        buf.write("\7#\2\2\u010a\u010b\5\26\f\2\u010b\u010c\7\'\2\2\u010c")
        buf.write("\u010d\5\26\f\2\u010d\u010e\7\'\2\2\u010e\u010f\5\26\f")
        buf.write("\2\u010f\u0110\7$\2\2\u0110\u0111\5.\30\2\u0111\65\3\2")
        buf.write("\2\2\u0112\u0113\7\7\2\2\u0113\u0114\7\'\2\2\u0114\67")
        buf.write("\3\2\2\2\u0115\u0116\7\b\2\2\u0116\u0117\7\'\2\2\u0117")
        buf.write("9\3\2\2\2\u0118\u011a\7\16\2\2\u0119\u011b\5\26\f\2\u011a")
        buf.write("\u0119\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011d\7\'\2\2\u011d;\3\2\2\2\u011e\u011f\5\26\f")
        buf.write("\2\u011f\u0120\7\'\2\2\u0120=\3\2\2\2\u0121\u0126\7%\2")
        buf.write("\2\u0122\u0125\5\4\3\2\u0123\u0125\5.\30\2\u0124\u0122")
        buf.write("\3\2\2\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0129\u012a\7&\2\2\u012a?\3\2\2\2")
        buf.write("\36BDKT[akrw}\u0087\u0091\u009c\u00a4\u00ab\u00b5\u00c0")
        buf.write("\u00c6\u00ce\u00da\u00df\u00e8\u00f3\u00fc\u0102\u011a")
        buf.write("\u0124\u0126")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'string'", 
                     "'boolean'", "'break'", "'continue'", "'else'", "'for'", 
                     "'float'", "'if'", "'int'", "'return'", "'void'", "'do'", 
                     "'while'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", 
                     "'<='", "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", 
                     "'>'", "'>='", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "STRING", 
                      "BOOL", "BREAK", "CONTINUE", "ELSE", "FOR", "FLOAT", 
                      "IF", "INT", "RETURN", "VOID", "DO", "WHILE", "ADD", 
                      "MUL", "NOT", "OR", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQUAL", "GREATER", 
                      "GREATER_EQUAL", "LSB", "RSB", "LB", "RB", "LP", "RP", 
                      "SEMI", "COMMA", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRINGLIT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_var_decl = 1
    RULE_many_var = 2
    RULE_var = 3
    RULE_func_decl = 4
    RULE_para_list = 5
    RULE_para_decl = 6
    RULE_types = 7
    RULE_primitive_type = 8
    RULE_array_pointer_type = 9
    RULE_exp = 10
    RULE_exp1 = 11
    RULE_exp2 = 12
    RULE_exp3 = 13
    RULE_exp4 = 14
    RULE_exp5 = 15
    RULE_exp6 = 16
    RULE_exp7 = 17
    RULE_exp8 = 18
    RULE_operand = 19
    RULE_func_call = 20
    RULE_list_exp = 21
    RULE_stmt = 22
    RULE_if_stmt = 23
    RULE_while_stmt = 24
    RULE_for_stmt = 25
    RULE_break_stmt = 26
    RULE_continue_stmt = 27
    RULE_return_stmt = 28
    RULE_exp_stmt = 29
    RULE_block_stmt = 30

    ruleNames =  [ "program", "var_decl", "many_var", "var", "func_decl", 
                   "para_list", "para_decl", "types", "primitive_type", 
                   "array_pointer_type", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "operand", "func_call", 
                   "list_exp", "stmt", "if_stmt", "while_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "exp_stmt", 
                   "block_stmt" ]

    EOF = Token.EOF
    BLOCK_COMMENT=1
    LINE_COMMENT=2
    STRING=3
    BOOL=4
    BREAK=5
    CONTINUE=6
    ELSE=7
    FOR=8
    FLOAT=9
    IF=10
    INT=11
    RETURN=12
    VOID=13
    DO=14
    WHILE=15
    ADD=16
    MUL=17
    NOT=18
    OR=19
    NOT_EQUAL=20
    LESS=21
    LESS_EQUAL=22
    ASSIGN=23
    SUB=24
    DIV=25
    MOD=26
    AND=27
    EQUAL=28
    GREATER=29
    GREATER_EQUAL=30
    LSB=31
    RSB=32
    LB=33
    RB=34
    LP=35
    RP=36
    SEMI=37
    COMMA=38
    INTLIT=39
    FLOATLIT=40
    BOOLLIT=41
    ID=42
    WS=43
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45
    STRINGLIT=46
    ERROR_CHAR=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Func_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Func_declContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.var_decl()
                    pass

                elif la_ == 2:
                    self.state = 63
                    self.func_decl()
                    pass


                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT) | (1 << MCParser.VOID))) != 0)):
                    break

            self.state = 68
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def var(self):
            return self.getTypedRuleContext(MCParser.VarContext,0)


        def many_var(self):
            return self.getTypedRuleContext(MCParser.Many_varContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = MCParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.primitive_type()
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 71
                self.var()
                pass

            elif la_ == 2:
                self.state = 72
                self.many_var()
                pass


            self.state = 75
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VarContext)
            else:
                return self.getTypedRuleContext(MCParser.VarContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_many_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_var" ):
                return visitor.visitMany_var(self)
            else:
                return visitor.visitChildren(self)




    def many_var(self):

        localctx = MCParser.Many_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_many_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.var()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 78
                self.match(MCParser.COMMA)
                self.state = 79
                self.var()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = MCParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MCParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 86
                self.match(MCParser.LSB)
                self.state = 87
                self.match(MCParser.INTLIT)
                self.state = 88
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(MCParser.TypesContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def para_list(self):
            return self.getTypedRuleContext(MCParser.Para_listContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = MCParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.types()
            self.state = 92
            self.match(MCParser.ID)
            self.state = 93
            self.match(MCParser.LB)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT))) != 0):
                self.state = 94
                self.para_list()


            self.state = 97
            self.match(MCParser.RB)
            self.state = 98
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Para_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Para_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_para_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_list" ):
                return visitor.visitPara_list(self)
            else:
                return visitor.visitChildren(self)




    def para_list(self):

        localctx = MCParser.Para_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_para_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.para_decl()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 101
                self.match(MCParser.COMMA)
                self.state = 102
                self.para_decl()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_decl" ):
                return visitor.visitPara_decl(self)
            else:
                return visitor.visitChildren(self)




    def para_decl(self):

        localctx = MCParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.primitive_type()
            self.state = 109
            self.match(MCParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 110
                self.match(MCParser.LSB)
                self.state = 111
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def array_pointer_type(self):
            return self.getTypedRuleContext(MCParser.Array_pointer_typeContext,0)


        def VOID(self):
            return self.getToken(MCParser.VOID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MCParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_types)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.array_pointer_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(MCParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(MCParser.BOOL, 0)

        def INT(self):
            return self.getToken(MCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MCParser.STRING, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MCParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pointer_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_array_pointer_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pointer_type" ):
                return visitor.visitArray_pointer_type(self)
            else:
                return visitor.visitChildren(self)




    def array_pointer_type(self):

        localctx = MCParser.Array_pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_pointer_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.primitive_type()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID:
                self.state = 122
                self.match(MCParser.ID)


            self.state = 125
            self.match(MCParser.LSB)
            self.state = 126
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.exp1(0)
                self.state = 129
                self.match(MCParser.ASSIGN)
                self.state = 130
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 143
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 138
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 139
                    self.match(MCParser.OR)
                    self.state = 140
                    self.exp2(0) 
                self.state = 145
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 154
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 149
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 150
                    self.match(MCParser.AND)
                    self.state = 151
                    self.exp3() 
                self.state = 156
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp4Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp4Context,i)


        def EQUAL(self):
            return self.getToken(MCParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MCParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MCParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.exp4()
                self.state = 158
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT_EQUAL or _la==MCParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 159
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp5Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp5Context,i)


        def LESS(self):
            return self.getToken(MCParser.LESS, 0)

        def GREATER(self):
            return self.getToken(MCParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(MCParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MCParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MCParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.exp5(0)
                self.state = 165
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS) | (1 << MCParser.LESS_EQUAL) | (1 << MCParser.GREATER) | (1 << MCParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.exp5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.exp5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(MCParser.Exp5Context,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 174
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 175
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 176
                    self.exp6(0) 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 185
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 186
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 187
                    self.exp7() 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def exp8(self):
            return self.getTypedRuleContext(MCParser.Exp8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = MCParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.NOT, MCParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT or _la==MCParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 194
                self.exp7()
                pass
            elif token in [MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.exp8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MCParser.OperandContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = MCParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp8)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.operand()
                self.state = 199
                self.match(MCParser.LSB)
                self.state = 200
                self.exp()
                self.state = 201
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def func_call(self):
            return self.getTypedRuleContext(MCParser.Func_callContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_operand)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.match(MCParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(MCParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(MCParser.LB)
                self.state = 211
                self.exp()
                self.state = 212
                self.match(MCParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
                self.func_call()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.match(MCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def list_exp(self):
            return self.getTypedRuleContext(MCParser.List_expContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MCParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(MCParser.ID)
            self.state = 219
            self.match(MCParser.LB)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 220
                self.list_exp()


            self.state = 223
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_exp" ):
                return visitor.visitList_exp(self)
            else:
                return visitor.visitChildren(self)




    def list_exp(self):

        localctx = MCParser.List_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.exp()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 226
                self.match(MCParser.COMMA)
                self.state = 227
                self.exp()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(MCParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MCParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(MCParser.While_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MCParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MCParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MCParser.Return_stmtContext,0)


        def exp_stmt(self):
            return self.getTypedRuleContext(MCParser.Exp_stmtContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(MCParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.if_stmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.for_stmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.while_stmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.break_stmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 237
                self.continue_stmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 238
                self.return_stmt()
                pass
            elif token in [MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 239
                self.exp_stmt()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 240
                self.block_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MCParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MCParser.IF)
            self.state = 244
            self.match(MCParser.LB)
            self.state = 245
            self.exp()
            self.state = 246
            self.match(MCParser.RB)
            self.state = 247
            self.stmt()
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 248
                self.match(MCParser.ELSE)
                self.state = 249
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = MCParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(MCParser.DO)
            self.state = 254 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 253
                self.stmt()
                self.state = 256 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 258
            self.match(MCParser.WHILE)
            self.state = 259
            self.exp()
            self.state = 260
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MCParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MCParser.FOR)
            self.state = 263
            self.match(MCParser.LB)
            self.state = 264
            self.exp()
            self.state = 265
            self.match(MCParser.SEMI)
            self.state = 266
            self.exp()
            self.state = 267
            self.match(MCParser.SEMI)
            self.state = 268
            self.exp()
            self.state = 269
            self.match(MCParser.RB)
            self.state = 270
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MCParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(MCParser.BREAK)
            self.state = 273
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MCParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(MCParser.CONTINUE)
            self.state = 276
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MCParser.RETURN)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 279
                self.exp()


            self.state = 282
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_stmt" ):
                return visitor.visitExp_stmt(self)
            else:
                return visitor.visitChildren(self)




    def exp_stmt(self):

        localctx = MCParser.Exp_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.exp()
            self.state = 285
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Var_declContext)
            else:
                return self.getTypedRuleContext(MCParser.Var_declContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = MCParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(MCParser.LP)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.FLOAT) | (1 << MCParser.IF) | (1 << MCParser.INT) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 290
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.STRING, MCParser.BOOL, MCParser.FLOAT, MCParser.INT]:
                    self.state = 288
                    self.var_decl()
                    pass
                elif token in [MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.IF, MCParser.RETURN, MCParser.DO, MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.LP, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                    self.state = 289
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.exp1_sempred
        self._predicates[12] = self.exp2_sempred
        self._predicates[15] = self.exp5_sempred
        self._predicates[16] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




=======
# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0132\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\6\2F\n\2\r\2\16\2G")
        buf.write("\3\2\3\2\3\3\3\3\5\3N\n\3\3\4\3\4\3\4\5\4S\n\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\7\5Z\n\5\f\5\16\5]\13\5\3\6\3\6\3\6\3\6\5")
        buf.write("\6c\n\6\3\7\3\7\3\7\3\7\5\7i\n\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\5\bq\n\b\3\t\3\t\3\n\3\n\5\nw\n\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\7\13\177\n\13\f\13\16\13\u0082\13\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\7\f\u0089\n\f\f\f\16\f\u008c\13\f\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u0092\n\r\3\16\3\16\3\16\3\16\3\16\5")
        buf.write("\16\u0099\n\16\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00a1")
        buf.write("\n\17\f\17\16\17\u00a4\13\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\7\20\u00ac\n\20\f\20\16\20\u00af\13\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00b6\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u00bd\n\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23")
        buf.write("\u00c5\n\23\f\23\16\23\u00c8\13\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\7\24\u00d0\n\24\f\24\16\24\u00d3\13\24\3\25")
        buf.write("\3\25\3\25\5\25\u00d8\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00e0\n\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u00eb\n\30\3\31\3\31\3\31\5\31\u00f0\n")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\7\32\u00f7\n\32\f\32\16\32")
        buf.write("\u00fa\13\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5")
        buf.write("\33\u0104\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u010d\n\34\3\35\3\35\6\35\u0111\n\35\r\35\16\35\u0112")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\5!\u012b")
        buf.write("\n!\3!\3!\3\"\3\"\3\"\3\"\2\6\34\36$&#\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@B\2")
        buf.write("\t\5\2\5\6\13\13\r\r\4\2\26\26\36\36\4\2\27\30\37 \4\2")
        buf.write("\22\22\32\32\4\2\23\23\33\34\4\2\24\24\32\32\4\2)+\60")
        buf.write("\60\2\u0135\2E\3\2\2\2\4M\3\2\2\2\6O\3\2\2\2\bV\3\2\2")
        buf.write("\2\n^\3\2\2\2\fd\3\2\2\2\16p\3\2\2\2\20r\3\2\2\2\22t\3")
        buf.write("\2\2\2\24{\3\2\2\2\26\u0085\3\2\2\2\30\u008d\3\2\2\2\32")
        buf.write("\u0098\3\2\2\2\34\u009a\3\2\2\2\36\u00a5\3\2\2\2 \u00b5")
        buf.write("\3\2\2\2\"\u00bc\3\2\2\2$\u00be\3\2\2\2&\u00c9\3\2\2\2")
        buf.write("(\u00d7\3\2\2\2*\u00df\3\2\2\2,\u00e1\3\2\2\2.\u00ea\3")
        buf.write("\2\2\2\60\u00ec\3\2\2\2\62\u00f3\3\2\2\2\64\u0103\3\2")
        buf.write("\2\2\66\u0105\3\2\2\28\u010e\3\2\2\2:\u0118\3\2\2\2<\u0122")
        buf.write("\3\2\2\2>\u0125\3\2\2\2@\u0128\3\2\2\2B\u012e\3\2\2\2")
        buf.write("DF\5\4\3\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HI\3")
        buf.write("\2\2\2IJ\7\2\2\3J\3\3\2\2\2KN\5\6\4\2LN\5\f\7\2MK\3\2")
        buf.write("\2\2ML\3\2\2\2N\5\3\2\2\2OR\5\20\t\2PS\5\n\6\2QS\5\b\5")
        buf.write("\2RP\3\2\2\2RQ\3\2\2\2ST\3\2\2\2TU\7\'\2\2U\7\3\2\2\2")
        buf.write("V[\5\n\6\2WX\7(\2\2XZ\5\n\6\2YW\3\2\2\2Z]\3\2\2\2[Y\3")
        buf.write("\2\2\2[\\\3\2\2\2\\\t\3\2\2\2][\3\2\2\2^b\7,\2\2_`\7!")
        buf.write("\2\2`a\7)\2\2ac\7\"\2\2b_\3\2\2\2bc\3\2\2\2c\13\3\2\2")
        buf.write("\2de\5\16\b\2ef\7,\2\2fh\7#\2\2gi\5\26\f\2hg\3\2\2\2h")
        buf.write("i\3\2\2\2ij\3\2\2\2jk\7$\2\2kl\5\24\13\2l\r\3\2\2\2mq")
        buf.write("\5\20\t\2nq\5\22\n\2oq\7\17\2\2pm\3\2\2\2pn\3\2\2\2po")
        buf.write("\3\2\2\2q\17\3\2\2\2rs\t\2\2\2s\21\3\2\2\2tv\5\20\t\2")
        buf.write("uw\7,\2\2vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2xy\7!\2\2yz\7\"")
        buf.write("\2\2z\23\3\2\2\2{\u0080\7%\2\2|\177\5\6\4\2}\177\5\64")
        buf.write("\33\2~|\3\2\2\2~}\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2")
        buf.write("\2\2\u0080\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080")
        buf.write("\3\2\2\2\u0083\u0084\7&\2\2\u0084\25\3\2\2\2\u0085\u008a")
        buf.write("\5\30\r\2\u0086\u0087\7(\2\2\u0087\u0089\5\30\r\2\u0088")
        buf.write("\u0086\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2")
        buf.write("\u008a\u008b\3\2\2\2\u008b\27\3\2\2\2\u008c\u008a\3\2")
        buf.write("\2\2\u008d\u008e\5\20\t\2\u008e\u0091\7,\2\2\u008f\u0090")
        buf.write("\7!\2\2\u0090\u0092\7\"\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\31\3\2\2\2\u0093\u0094\5\34\17\2")
        buf.write("\u0094\u0095\7\31\2\2\u0095\u0096\5\32\16\2\u0096\u0099")
        buf.write("\3\2\2\2\u0097\u0099\5\34\17\2\u0098\u0093\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\33\3\2\2\2\u009a\u009b\b\17\1\2\u009b")
        buf.write("\u009c\5\36\20\2\u009c\u00a2\3\2\2\2\u009d\u009e\f\4\2")
        buf.write("\2\u009e\u009f\7\25\2\2\u009f\u00a1\5\36\20\2\u00a0\u009d")
        buf.write("\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\35\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5")
        buf.write("\u00a6\b\20\1\2\u00a6\u00a7\5 \21\2\u00a7\u00ad\3\2\2")
        buf.write("\2\u00a8\u00a9\f\4\2\2\u00a9\u00aa\7\35\2\2\u00aa\u00ac")
        buf.write("\5 \21\2\u00ab\u00a8\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\37\3\2\2\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00b0\u00b1\5\"\22\2\u00b1\u00b2\t\3\2")
        buf.write("\2\u00b2\u00b3\5\"\22\2\u00b3\u00b6\3\2\2\2\u00b4\u00b6")
        buf.write("\5\"\22\2\u00b5\u00b0\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("!\3\2\2\2\u00b7\u00b8\5$\23\2\u00b8\u00b9\t\4\2\2\u00b9")
        buf.write("\u00ba\5$\23\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd\5$\23\2")
        buf.write("\u00bc\u00b7\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd#\3\2\2")
        buf.write("\2\u00be\u00bf\b\23\1\2\u00bf\u00c0\5&\24\2\u00c0\u00c6")
        buf.write("\3\2\2\2\u00c1\u00c2\f\4\2\2\u00c2\u00c3\t\5\2\2\u00c3")
        buf.write("\u00c5\5&\24\2\u00c4\u00c1\3\2\2\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7%\3\2\2")
        buf.write("\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\b\24\1\2\u00ca\u00cb")
        buf.write("\5(\25\2\u00cb\u00d1\3\2\2\2\u00cc\u00cd\f\4\2\2\u00cd")
        buf.write("\u00ce\t\6\2\2\u00ce\u00d0\5(\25\2\u00cf\u00cc\3\2\2\2")
        buf.write("\u00d0\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3")
        buf.write("\2\2\2\u00d2\'\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d5")
        buf.write("\t\7\2\2\u00d5\u00d8\5(\25\2\u00d6\u00d8\5*\26\2\u00d7")
        buf.write("\u00d4\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8)\3\2\2\2\u00d9")
        buf.write("\u00da\5.\30\2\u00da\u00db\7!\2\2\u00db\u00dc\5\32\16")
        buf.write("\2\u00dc\u00dd\7\"\2\2\u00dd\u00e0\3\2\2\2\u00de\u00e0")
        buf.write("\5.\30\2\u00df\u00d9\3\2\2\2\u00df\u00de\3\2\2\2\u00e0")
        buf.write("+\3\2\2\2\u00e1\u00e2\t\b\2\2\u00e2-\3\2\2\2\u00e3\u00eb")
        buf.write("\5,\27\2\u00e4\u00e5\7#\2\2\u00e5\u00e6\5\32\16\2\u00e6")
        buf.write("\u00e7\7$\2\2\u00e7\u00eb\3\2\2\2\u00e8\u00eb\5\60\31")
        buf.write("\2\u00e9\u00eb\7,\2\2\u00ea\u00e3\3\2\2\2\u00ea\u00e4")
        buf.write("\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("/\3\2\2\2\u00ec\u00ed\7,\2\2\u00ed\u00ef\7#\2\2\u00ee")
        buf.write("\u00f0\5\62\32\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2\2")
        buf.write("\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\7$\2\2\u00f2\61\3\2")
        buf.write("\2\2\u00f3\u00f8\5\32\16\2\u00f4\u00f5\7(\2\2\u00f5\u00f7")
        buf.write("\5\32\16\2\u00f6\u00f4\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\63\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fb\u0104\5\66\34\2\u00fc\u0104\5:\36")
        buf.write("\2\u00fd\u0104\58\35\2\u00fe\u0104\5<\37\2\u00ff\u0104")
        buf.write("\5> \2\u0100\u0104\5@!\2\u0101\u0104\5B\"\2\u0102\u0104")
        buf.write("\5\24\13\2\u0103\u00fb\3\2\2\2\u0103\u00fc\3\2\2\2\u0103")
        buf.write("\u00fd\3\2\2\2\u0103\u00fe\3\2\2\2\u0103\u00ff\3\2\2\2")
        buf.write("\u0103\u0100\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0102\3")
        buf.write("\2\2\2\u0104\65\3\2\2\2\u0105\u0106\7\f\2\2\u0106\u0107")
        buf.write("\7#\2\2\u0107\u0108\5\32\16\2\u0108\u0109\7$\2\2\u0109")
        buf.write("\u010c\5\64\33\2\u010a\u010b\7\t\2\2\u010b\u010d\5\64")
        buf.write("\33\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\67")
        buf.write("\3\2\2\2\u010e\u0110\7\20\2\2\u010f\u0111\5\64\33\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0110\3\2\2\2")
        buf.write("\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\7")
        buf.write("\21\2\2\u0115\u0116\5\32\16\2\u0116\u0117\7\'\2\2\u0117")
        buf.write("9\3\2\2\2\u0118\u0119\7\n\2\2\u0119\u011a\7#\2\2\u011a")
        buf.write("\u011b\5\32\16\2\u011b\u011c\7\'\2\2\u011c\u011d\5\32")
        buf.write("\16\2\u011d\u011e\7\'\2\2\u011e\u011f\5\32\16\2\u011f")
        buf.write("\u0120\7$\2\2\u0120\u0121\5\64\33\2\u0121;\3\2\2\2\u0122")
        buf.write("\u0123\7\7\2\2\u0123\u0124\7\'\2\2\u0124=\3\2\2\2\u0125")
        buf.write("\u0126\7\b\2\2\u0126\u0127\7\'\2\2\u0127?\3\2\2\2\u0128")
        buf.write("\u012a\7\16\2\2\u0129\u012b\5\32\16\2\u012a\u0129\3\2")
        buf.write("\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d")
        buf.write("\7\'\2\2\u012dA\3\2\2\2\u012e\u012f\5\32\16\2\u012f\u0130")
        buf.write("\7\'\2\2\u0130C\3\2\2\2\36GMR[bhpv~\u0080\u008a\u0091")
        buf.write("\u0098\u00a2\u00ad\u00b5\u00bc\u00c6\u00d1\u00d7\u00df")
        buf.write("\u00ea\u00ef\u00f8\u0103\u010c\u0112\u012a")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'string'", 
                     "'boolean'", "'break'", "'continue'", "'else'", "'for'", 
                     "'float'", "'if'", "'int'", "'return'", "'void'", "'do'", 
                     "'while'", "'+'", "'*'", "'!'", "'||'", "'!='", "'<'", 
                     "'<='", "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", 
                     "'>'", "'>='", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BLOCK_COMMENT", "LINE_COMMENT", "STRING", 
                      "BOOL", "BREAK", "CONTINUE", "ELSE", "FOR", "FLOAT", 
                      "IF", "INT", "RETURN", "VOID", "DO", "WHILE", "ADD", 
                      "MUL", "NOT", "OR", "NOT_EQUAL", "LESS", "LESS_EQUAL", 
                      "ASSIGN", "SUB", "DIV", "MOD", "AND", "EQUAL", "GREATER", 
                      "GREATER_EQUAL", "LSB", "RSB", "LB", "RB", "LP", "RP", 
                      "SEMI", "COMMA", "INTLIT", "FLOATLIT", "BOOLLIT", 
                      "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRINGLIT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_many_declarations = 1
    RULE_variable_declaration = 2
    RULE_many_variables = 3
    RULE_variable = 4
    RULE_function_declaration = 5
    RULE_types = 6
    RULE_primitive_type = 7
    RULE_array_pointer_type = 8
    RULE_block_statement = 9
    RULE_parameter_list = 10
    RULE_parameter_declaration = 11
    RULE_expression = 12
    RULE_expression1 = 13
    RULE_expression2 = 14
    RULE_expression3 = 15
    RULE_expression4 = 16
    RULE_expression5 = 17
    RULE_expression6 = 18
    RULE_expression7 = 19
    RULE_expression8 = 20
    RULE_literal = 21
    RULE_operand = 22
    RULE_function_call = 23
    RULE_list_expression = 24
    RULE_statement = 25
    RULE_if_statement = 26
    RULE_while_statement = 27
    RULE_for_statement = 28
    RULE_break_statement = 29
    RULE_continue_statement = 30
    RULE_return_statement = 31
    RULE_expression_statement = 32

    ruleNames =  [ "program", "many_declarations", "variable_declaration", 
                   "many_variables", "variable", "function_declaration", 
                   "types", "primitive_type", "array_pointer_type", "block_statement", 
                   "parameter_list", "parameter_declaration", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "literal", "operand", "function_call", "list_expression", 
                   "statement", "if_statement", "while_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "expression_statement" ]

    EOF = Token.EOF
    BLOCK_COMMENT=1
    LINE_COMMENT=2
    STRING=3
    BOOL=4
    BREAK=5
    CONTINUE=6
    ELSE=7
    FOR=8
    FLOAT=9
    IF=10
    INT=11
    RETURN=12
    VOID=13
    DO=14
    WHILE=15
    ADD=16
    MUL=17
    NOT=18
    OR=19
    NOT_EQUAL=20
    LESS=21
    LESS_EQUAL=22
    ASSIGN=23
    SUB=24
    DIV=25
    MOD=26
    AND=27
    EQUAL=28
    GREATER=29
    GREATER_EQUAL=30
    LSB=31
    RSB=32
    LB=33
    RB=34
    LP=35
    RP=36
    SEMI=37
    COMMA=38
    INTLIT=39
    FLOATLIT=40
    BOOLLIT=41
    ID=42
    WS=43
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45
    STRINGLIT=46
    ERROR_CHAR=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def many_declarations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Many_declarationsContext)
            else:
                return self.getTypedRuleContext(MCParser.Many_declarationsContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.many_declarations()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT) | (1 << MCParser.VOID))) != 0)):
                    break

            self.state = 71
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(MCParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(MCParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_many_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_declarations" ):
                return visitor.visitMany_declarations(self)
            else:
                return visitor.visitChildren(self)




    def many_declarations(self):

        localctx = MCParser.Many_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_many_declarations)
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.function_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def variable(self):
            return self.getTypedRuleContext(MCParser.VariableContext,0)


        def many_variables(self):
            return self.getTypedRuleContext(MCParser.Many_variablesContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = MCParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.primitive_type()
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 78
                self.variable()
                pass

            elif la_ == 2:
                self.state = 79
                self.many_variables()
                pass


            self.state = 82
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Many_variablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VariableContext)
            else:
                return self.getTypedRuleContext(MCParser.VariableContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_many_variables

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMany_variables" ):
                return visitor.visitMany_variables(self)
            else:
                return visitor.visitChildren(self)




    def many_variables(self):

        localctx = MCParser.Many_variablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_many_variables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.variable()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 85
                self.match(MCParser.COMMA)
                self.state = 86
                self.variable()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = MCParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MCParser.ID)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 93
                self.match(MCParser.LSB)
                self.state = 94
                self.match(MCParser.INTLIT)
                self.state = 95
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(MCParser.TypesContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_statement(self):
            return self.getTypedRuleContext(MCParser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(MCParser.Parameter_listContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = MCParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.types()
            self.state = 99
            self.match(MCParser.ID)
            self.state = 100
            self.match(MCParser.LB)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT))) != 0):
                self.state = 101
                self.parameter_list()


            self.state = 104
            self.match(MCParser.RB)
            self.state = 105
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def array_pointer_type(self):
            return self.getTypedRuleContext(MCParser.Array_pointer_typeContext,0)


        def VOID(self):
            return self.getToken(MCParser.VOID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = MCParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_types)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.primitive_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.array_pointer_type()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(MCParser.VOID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(MCParser.BOOL, 0)

        def INT(self):
            return self.getToken(MCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MCParser.STRING, 0)

        def getRuleIndex(self):
            return MCParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MCParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.FLOAT) | (1 << MCParser.INT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pointer_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_array_pointer_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pointer_type" ):
                return visitor.visitArray_pointer_type(self)
            else:
                return visitor.visitChildren(self)




    def array_pointer_type(self):

        localctx = MCParser.Array_pointer_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_pointer_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.primitive_type()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID:
                self.state = 115
                self.match(MCParser.ID)


            self.state = 118
            self.match(MCParser.LSB)
            self.state = 119
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def variable_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Variable_declarationContext)
            else:
                return self.getTypedRuleContext(MCParser.Variable_declarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MCParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(MCParser.LP)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.STRING) | (1 << MCParser.BOOL) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.FLOAT) | (1 << MCParser.IF) | (1 << MCParser.INT) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 124
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.STRING, MCParser.BOOL, MCParser.FLOAT, MCParser.INT]:
                    self.state = 122
                    self.variable_declaration()
                    pass
                elif token in [MCParser.BREAK, MCParser.CONTINUE, MCParser.FOR, MCParser.IF, MCParser.RETURN, MCParser.DO, MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.LP, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                    self.state = 123
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Parameter_declarationContext)
            else:
                return self.getTypedRuleContext(MCParser.Parameter_declarationContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = MCParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.parameter_declaration()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 132
                self.match(MCParser.COMMA)
                self.state = 133
                self.parameter_declaration()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MCParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_parameter_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_declaration" ):
                return visitor.visitParameter_declaration(self)
            else:
                return visitor.visitChildren(self)




    def parameter_declaration(self):

        localctx = MCParser.Parameter_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.primitive_type()
            self.state = 140
            self.match(MCParser.ID)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 141
                self.match(MCParser.LSB)
                self.state = 142
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MCParser.Expression1Context,0)


        def ASSIGN(self):
            return self.getToken(MCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.expression1(0)
                self.state = 146
                self.match(MCParser.ASSIGN)
                self.state = 147
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MCParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MCParser.Expression1Context,0)


        def OR(self):
            return self.getToken(MCParser.OR, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 155
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 156
                    self.match(MCParser.OR)
                    self.state = 157
                    self.expression2(0) 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MCParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MCParser.Expression2Context,0)


        def AND(self):
            return self.getToken(MCParser.AND, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.expression3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 166
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 167
                    self.match(MCParser.AND)
                    self.state = 168
                    self.expression3() 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expression4Context)
            else:
                return self.getTypedRuleContext(MCParser.Expression4Context,i)


        def EQUAL(self):
            return self.getToken(MCParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MCParser.NOT_EQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)




    def expression3(self):

        localctx = MCParser.Expression3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression3)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expression4()
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT_EQUAL or _la==MCParser.EQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.expression4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.expression4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expression5Context)
            else:
                return self.getTypedRuleContext(MCParser.Expression5Context,i)


        def LESS(self):
            return self.getToken(MCParser.LESS, 0)

        def GREATER(self):
            return self.getToken(MCParser.GREATER, 0)

        def LESS_EQUAL(self):
            return self.getToken(MCParser.LESS_EQUAL, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MCParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)




    def expression4(self):

        localctx = MCParser.Expression4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expression4)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.expression5(0)
                self.state = 182
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS) | (1 << MCParser.LESS_EQUAL) | (1 << MCParser.GREATER) | (1 << MCParser.GREATER_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 183
                self.expression5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.expression5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MCParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MCParser.Expression5Context,0)


        def ADD(self):
            return self.getToken(MCParser.ADD, 0)

        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.expression6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 191
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 192
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD or _la==MCParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 193
                    self.expression6(0) 
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MCParser.Expression7Context,0)


        def expression6(self):
            return self.getTypedRuleContext(MCParser.Expression6Context,0)


        def DIV(self):
            return self.getToken(MCParser.DIV, 0)

        def MUL(self):
            return self.getToken(MCParser.MUL, 0)

        def MOD(self):
            return self.getToken(MCParser.MOD, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)



    def expression6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expression6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expression7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 207
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expression6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression6)
                    self.state = 202
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 203
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL) | (1 << MCParser.DIV) | (1 << MCParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 204
                    self.expression7() 
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MCParser.Expression7Context,0)


        def SUB(self):
            return self.getToken(MCParser.SUB, 0)

        def NOT(self):
            return self.getToken(MCParser.NOT, 0)

        def expression8(self):
            return self.getTypedRuleContext(MCParser.Expression8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = MCParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.NOT, MCParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT or _la==MCParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 211
                self.expression7()
                pass
            elif token in [MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.expression8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MCParser.OperandContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = MCParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression8)
        try:
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.operand()
                self.state = 216
                self.match(MCParser.LSB)
                self.state = 217
                self.expression()
                self.state = 218
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MCParser.LiteralContext,0)


        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def function_call(self):
            return self.getTypedRuleContext(MCParser.Function_callContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operand)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MCParser.LB)
                self.state = 227
                self.expression()
                self.state = 228
                self.match(MCParser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.match(MCParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MCParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MCParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MCParser.ID)
            self.state = 235
            self.match(MCParser.LB)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 236
                self.list_expression()


            self.state = 239
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MCParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.expression()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 242
                self.match(MCParser.COMMA)
                self.state = 243
                self.expression()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_statement(self):
            return self.getTypedRuleContext(MCParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MCParser.For_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(MCParser.While_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MCParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MCParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MCParser.Return_statementContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(MCParser.Expression_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(MCParser.Block_statementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_statement)
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.if_statement()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.for_statement()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.while_statement()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 252
                self.break_statement()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 253
                self.continue_statement()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 254
                self.return_statement()
                pass
            elif token in [MCParser.NOT, MCParser.SUB, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.ID, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 255
                self.expression_statement()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 256
                self.block_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MCParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MCParser.IF)
            self.state = 260
            self.match(MCParser.LB)
            self.state = 261
            self.expression()
            self.state = 262
            self.match(MCParser.RB)
            self.state = 263
            self.statement()
            self.state = 266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 264
                self.match(MCParser.ELSE)
                self.state = 265
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = MCParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MCParser.DO)
            self.state = 270 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.statement()
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.DO) | (1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 274
            self.match(MCParser.WHILE)
            self.state = 275
            self.expression()
            self.state = 276
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MCParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MCParser.FOR)
            self.state = 279
            self.match(MCParser.LB)
            self.state = 280
            self.expression()
            self.state = 281
            self.match(MCParser.SEMI)
            self.state = 282
            self.expression()
            self.state = 283
            self.match(MCParser.SEMI)
            self.state = 284
            self.expression()
            self.state = 285
            self.match(MCParser.RB)
            self.state = 286
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MCParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(MCParser.BREAK)
            self.state = 289
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MCParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(MCParser.CONTINUE)
            self.state = 292
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MCParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(MCParser.RETURN)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.NOT) | (1 << MCParser.SUB) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.ID) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 295
                self.expression()


            self.state = 298
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expression_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = MCParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expression_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.expression()
            self.state = 301
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expression1_sempred
        self._predicates[14] = self.expression2_sempred
        self._predicates[17] = self.expression5_sempred
        self._predicates[18] = self.expression6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression6_sempred(self, localctx:Expression6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




>>>>>>> 626ac39fdc3ced81c59e12b9bf8cc445495487e9
