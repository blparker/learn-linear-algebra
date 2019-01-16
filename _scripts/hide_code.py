from nbconvert.preprocessors import *
from traitlets.log import get_logger

class HideCodePreprocessor(Preprocessor):
    def preprocess_cell(self, cell, resources, index):
        try:
            if cell.metadata['hideCode'] and cell.cell_type != 'markdown':
                cell.source = ''
        except:
            pass

        # try:
        #     if cell.metadata['hidePrompt']:
        #         cell.execution_count = None
        #         cell.output.execution_count = None
        # except:
        #     pass

        return cell, resources

    def preprocess(self, nb, resources):
        super().preprocess(nb, resources)

        #print(json.dumps(nb.cells))
        # Filter out empty code cells
        nb.cells = [cell for cell in nb.cells if not self.empty_code_cell(cell)]

        return nb, resources

    def empty_code_cell(self, cell):
        if cell.get('cell_type', '') != 'code':
            return False
        return not cell.source and not len(cell.get('outputs', []))

