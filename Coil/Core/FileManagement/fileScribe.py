import os
from Core.FileManagement.const_fileManagement import MAIN_BLOCK
import Core.Coil.empress as empress

def generateCoilFile(statementIndex: list, functionLibrary: dict, inputFile: str, parentDir: str):
    outputFile = inputFile.rstrip(".py") + ".coil.py"
    outputPath = os.path.join(parentDir, outputFile)
    writeFile(outputPath, statementIndex, functionLibrary)

def writeFile(outputPath: str, statementIndex: list[dict], functionLibrary: dict = {}):
    with open(outputPath, "w") as coilFile:
        for block in statementIndex:
            _handleBlock(block, coilFile, functionLibrary)

def _handleBlock(block: str, coilFile, functionLibrary: dict):
    blockStatement = block["blockStatement"]
    if blockStatement == MAIN_BLOCK:
        _writeStatements(block["statements"], 0, coilFile, functionLibrary)
    else:
        indentLevel = block["indentLevel"]
        _writeStatement(blockStatement, indentLevel, coilFile, functionLibrary)
        _writeStatements(block["statements"], indentLevel + 1, coilFile, functionLibrary)

def _writeStatements(statements: list, indentLevel: int, coilFile, functionLibrary: dict):
    for statement in statements:
        _writeStatement(statement, indentLevel, coilFile, functionLibrary)

def _writeStatement(statement: str, indentLevel: int, coilFile, functionLibrary: dict):
    coiledStatement = empress.coil(statement, functionLibrary)
    coilFile.write(_fmtIndent(indentLevel) + coiledStatement + "\n")

def _fmtIndent(indentLevel: int):
    return "\t" * indentLevel