import Core.FunctionLibrary.functionLibrarian as fl
from Core.Compiler.const_pythonSyntax import StmtSep

def coil(statement: str, functionLibrary: dict):
    return __coilStatement(statement, functionLibrary)

def __coilStatement(statement: str, functionLibrary: dict):
    if not fl.Parsing.statementIsFunctionCall(statement):
        return statement
    
    callStatements = fl.Access.getStatementCode(statement, functionLibrary)
    if len(callStatements) == 0:
        return statement  # Not stored in library, just return the original call
    
    print(callStatements)
    coiledStatment = __coilStatements(callStatements, functionLibrary)
    return coiledStatment

def __coilStatements(statements: list, functionLibrary: dict):
    coiledStatements = []
    for statement in statements:
        coiledStatements.append(__coilStatement(statement, functionLibrary))
    return StmtSep.SEMI_COLON.join(coiledStatements)

if __name__ == "__main__":
    testFunctionLibrary = {}
    
    block = "def testFxn(a, b):"
    functionStatements = [
        "print(a)",
        "print(b)",
        "print('done')"
    ]

    fl.Access.storeFunctionDef(block, testFunctionLibrary)
    fl.Access.storeFunctionStatements(block, functionStatements, testFunctionLibrary)

    testStatement = "testFxn(1, 2)"
    print("Original Statement:")
    print(testStatement)
    print("\nCoiled Statement:")
    print(coil(testStatement, testFunctionLibrary))