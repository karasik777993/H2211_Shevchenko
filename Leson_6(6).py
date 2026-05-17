import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
try:
 warnings.warn("Warning, modul not import", ImportWarning)
except:
    print("Warning, processed")