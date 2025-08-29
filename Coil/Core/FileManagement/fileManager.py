import fileScribe
import fileParser

def run():

    parentDir = "C:\\Users\\austi\\Projects\\Coil\\Testing\\Test001"
    file = "test001.py"
    functionLibrary, statementIndex = fileParser.buildFunctionIndex(file, parentDir)
    fileScribe.generateCoilFile(statementIndex, functionLibrary, file, parentDir)
    print(functionLibrary)

    parentDir = "C:\\Users\\austi\\Projects\\Coil\\Testing\\Test002"
    file = "test002.py"
    functionLibrary, statementIndex = fileParser.buildFunctionIndex(file, parentDir)
    fileScribe.generateCoilFile(statementIndex, functionLibrary, file, parentDir)
    print(functionLibrary)

if __name__ == "__main__":
    run()