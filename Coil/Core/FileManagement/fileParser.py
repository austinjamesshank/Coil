import os
from const_fileManagement import MAIN_BLOCK
import functionLibrarian as fxnBookworm 
from strUtils import stringContains, isEmpty

def buildFunctionIndex(file, parentDir):
    
    functionLibrary = {}
    statementIndex = readFile(file, parentDir, functionLibrary)
        
    return functionLibrary, statementIndex

def readFile(inputFile: str, parentDir: str, functionLibrary: dict):

    inputPath = os.path.join(parentDir, inputFile)

    statementIndex = []
    functionLibrary = {}

    blockStack = []

    with open(inputPath, "r") as pyFile:
        
        currentBlock = MAIN_BLOCK
        blockStack.append(currentBlock)
        previousIndent =  0
        statementIndex.append(_makeBlockData(MAIN_BLOCK, 0))
        
        for line in pyFile:
            cleanLine = line.strip()
            if isEmpty(cleanLine):
                continue  # Empty lines are stripped for storage
            
            lineStatements = _getStatements(cleanLine)
            if len(lineStatements) == 0:
                continue
            
            currentIndent = _getIndentLevel(line)
            newBlock = _parseStatements(lineStatements, currentBlock, currentIndent, previousIndent, statementIndex, functionLibrary)
            
            if currentIndent > previousIndent:
                blockStack.append(newBlock)
            elif currentIndent < previousIndent:
                currentBlock = blockStack.pop()

    return statementIndex

def _getIndentLevel(line: str):
    indent = 0
    for char in line:
        if char == " ":
            indent += 1
        elif char == "\t":
            indent += 4
        else:
            break
    return indent // 4

def _parseStatements(statements: list, currentBlock: str, currentIndent: int, previousIndent: int, statementIndex: list, functionLibrary: dict):

    if _hasBlockHeader(statements[0]):
        block = statements[0]

        if fxnBookworm.Parsing.blockIsFunctionDef(block):
            fxnBookworm.Access.storeFunctionDef(block, functionLibrary)

        # For a block header with nothing following, we'll be opening a new block
        if len(statements) == 1:
            blockData = _makeBlockData(block, currentIndent+1)
            statementIndex.append(blockData)
            return block
        # Otherwise the logic on this line is contained, we can return the previous block and continue
        else:
            blockData = _makeBlockData(block, currentIndent)
            for blockStatement in statements[1:]:
                blockData["statements"].append(blockStatement)
            statementIndex.append(blockData)
            return currentBlock

    for statement in statements:
        statementIndex[-1]["statements"].append(statement)

    return currentBlock

def _makeBlockData(block: str, indentLevel: int):
    return {"blockStatement" : block, "statements" : [], "indentLevel" : indentLevel }

# --- Statement Parsing Functions ---

def _getStatements(line: str):  
    if _hasBlockHeader(line):
        return _getBlockHeaderStatements(line) 
    return _getLineStatements(line)

def _hasBlockHeader(line: str):
    # TODO: needs to take into account strings and objects (like dicts)
    return (stringContains(line, ":"))

def _getBlockHeaderStatements(line: str):
    blockSplit = line.split(":")
    if len(blockSplit) == 1:
        return [line]
    blockHeader = blockSplit[0] + ":"
    blockStatements = blockSplit[1].split(";")
    outputStatements = [blockHeader]
    for statement in blockStatements:
        statement = statement.strip()
        if isEmpty(statement):
            continue
        outputStatements.append(statement)
    return outputStatements

def _getLineStatements(line: str):
    if not stringContains(line, ";"):
        return [line]
    lineStatements = line.split(";")  # TODO: needs to take into account comment blocks
    outputStatements = []
    for statement in lineStatements:
        statement = statement.strip()
        if isEmpty(statement):
            continue
        outputStatements.append(statement)
    return outputStatements

# TODO
def _statementIsComment(line: str):
    return False

# TODO
def _stripComments(line: str):
    return line