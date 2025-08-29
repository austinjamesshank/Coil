from strUtils import isEmpty, stringContains

# ========================
# === Function Parsing ===
# ========================

class Parsing:

    # === Public Methods ===

    @staticmethod
    def blockIsFunctionDef(block: str):
        return block.startswith("def ") and block.endswith(":")

    @staticmethod
    def statementIsFunctionCall(statement: str):
        return stringContains(statement, "(") and statement.endswith(")")
    
    # === Internal Methods ===

    @staticmethod
    def _getFunctionDefName(block: str):
        '''Gets the function name from a block definition.'''
        nameStart = block.find("def ") + 4
        return Parsing.__getFxnName(block, nameStart)
    
    @staticmethod
    def _getFunctionCallName(statement: str):
        '''Gets the function name from a function call statment.'''
        return Parsing.__getFxnName(statement, 0)
    
    @staticmethod
    def _getFunctionParams(block: str):
        paramStart = block.find("(") + 1
        paramEnd = block.find(")")
        paramString = block[paramStart:paramEnd].strip()
        if isEmpty(paramString):
            return []
        return [param.strip() for param in paramString.split(",")]

    # === Private Methods ===
    
    @staticmethod
    def __getFxnName(block: str, start: int):
        return block[start:block.find("(")].strip()

# ==========================
# === Library Management ===
# ==========================

class Access:

    # === Public Methods ===

    @staticmethod
    def storeFunctionDef(block: str, functionLibrary: dict):
        functionName, paramIdentifier = Access.__getFxnInfoFromBlock(block)
        Access.__addFunctionToLibrary(functionName, paramIdentifier, functionLibrary)

    @staticmethod
    def storeFunctionStatements(block: str, statements: list, functionLibrary: dict):
        functionName, paramIdentifier = Access.__getFxnInfoFromBlock(block)
        if not Access.__callInLibrary(functionName, paramIdentifier, functionLibrary):
            return
        functionLibrary[functionName][paramIdentifier][Access.CALL_STMTS] = statements

    @staticmethod
    def addFunctionStatement(functionName: str, paramIdentifier: str, statement: str, functionLibrary: dict):
        if not Access.__callInLibrary(functionName, paramIdentifier, functionLibrary):
            return
        functionLibrary[functionName][paramIdentifier][Access.CALL_STMTS].append(statement)

    @staticmethod
    def getFunctionStatments(functionName: str, paramIdentifier: str, functionLibrary: dict):
        if not Access.__callInLibrary(functionName, paramIdentifier, functionLibrary):
            return []
        return functionLibrary[functionName][paramIdentifier][Access.CALL_STMTS]

    @staticmethod
    def getStatementCode(statement: str, functionLibrary: dict):
        if not Parsing.statementIsFunctionCall(statement):
            return []
        
        functionName, paramIdentifier = Access.__getFxnInfoFromCall(statement)
        if not Access.__callInLibrary(functionName, paramIdentifier, functionLibrary):
            return []
        
        return functionLibrary[functionName][paramIdentifier][Access.CALL_STMTS]

    # TODO: not using this, but maybe helpful? idfk
    @staticmethod
    def statementInLibrary(statement: str, functionLibrary: dict):
        if not Parsing.statementIsFunctionCall(statement):
            return False
        functionName, paramIdentifier = Access.__getFxnInfoFromCall(statement)
        return Access.__callInLibrary(functionName, paramIdentifier, functionLibrary)
    
    # === Private Methods ===

    @staticmethod
    def __getFxnInfoFromBlock(block: str):
        functionName = Parsing._getFunctionDefName(block)
        functionParams = Parsing._getFunctionParams(block)
        paramIdentifier = Access.__getParamIdentifier(functionParams)
        return functionName, paramIdentifier
    
    @staticmethod
    def __getFxnInfoFromCall(block: str):
        functionName = Parsing._getFunctionCallName(block)
        functionParams = Parsing._getFunctionParams(block)
        paramIdentifier = Access.__getParamIdentifier(functionParams)
        return functionName, paramIdentifier

    @staticmethod
    def __addFunctionToLibrary(functionName: str, paramIdentifier: str, functionLibrary: dict):
        functionLibrary[functionName] = Access.__formUniqueFunctionInst(paramIdentifier, functionLibrary)

    @staticmethod
    def __formUniqueFunctionInst(paramIdentifier: str, functionLibrary: dict):
        return {
            paramIdentifier :  {
                Access.CALL_STMTS : []
            }
        }

    @staticmethod
    def __callInLibrary(functionName: str, paramIdentifier: str, functionLibrary: dict):
        return (functionName in functionLibrary) and (paramIdentifier in functionLibrary[functionName])
    
    @staticmethod
    def __getParamIdentifier(params: list):
        return len(params)  # TODO: needs to be more robust, for now just using count
    
    # === Constants ===
    CALL_STMTS = "statments"