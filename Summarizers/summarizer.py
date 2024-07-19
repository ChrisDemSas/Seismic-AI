###################################################################
#
# Summarizer Class
#
###################################################################

import pandas as pd
from transformers import AutoTokenizer, AutoModelWithLMHead
from rouge import Rouge

class Summarizer:
    """Implementation of the Summarizer class: An object which summarizes articles.
    
    Attributes:
        summarizer: The type of summarizer: Bart, T5 or Pegasus.
        dataset: A pandas dataframe which contains the dataset for today. Must have the exact same headings as the one obtained by NewsScraper class.
        min_length: The minimum length for a single summary of an article.
        max_length: The maximum length for a single summary of an article.
    """
    
    def __init__(self, summarizer: str, dataset: pd.DataFrame, min_length = int, max_length = int) -> None:
        """Initialize the Summarizer class.
        
        Attributes:
            summarizer: The type of summarizer: Bart, T5 or Pegasus.
            dataset: A pandas dataframe which contains the dataset for today. Must have the exact same headings as the one obtained by NewsScraper class.
            min_length: The minimum length for a single summary of an article.
            max_length: The maximum length for a single summary of an article.
        """
        
        if summarizer == 'bart':
            self.summarizer = AutoModelWithLMHead.from_pretrained('facebook/bart-large-cnn', return_dict = True)
            self.tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-cnn')
        elif summarizer == 't5':
            self.summarizer = AutoModelWithLMHead.from_pretrained('T5-base', return_dict = True)
            self.tokenizer = AutoTokenizer.from_pretrained('T5-base')
        elif summarizer == 'pegasus':
            self.summarizer = AutoModelWithLMHead.from_pretrained('google/pegasus-large', return_dict = True)
            self.tokenizer = AutoTokenizer.from_pretrained('google/pegasus-large')

        self.dataset = dataset
        self.rouge = Rouge()
        self.rouge_results = []
        self.min_length = min_length
        self.max_length = max_length
    
    def _cleanup(self, text: str):
        """Take in a summarized text and return it wihtout the '>' or '<'. 
        
        Attributes:
            text: The text that needs to be processed.
        """

        final_text = ''
        indicator = False

        for i in text:
            if i == '>':
                indicator = False
            elif i == '<':
                indicator = True
            elif indicator:
                continue
            else:
                final_text += i

        return final_text
    
    def _summarize(self, content: str) -> dict:
        """Summarize the article in dataset and return a summarized article.

        Attributes:
            content: The contents of the article that is to be summarized.
        """

        inputs = self.tokenizer.encode("sumarize: " + content, return_tensors = 'pt', max_length = 1024, truncation = True)
        output = self.summarizer.generate(inputs, min_length = self.min_length, max_length = self.max_length)
        summary = self.tokenizer.decode(output[0])
    
        return self._cleanup(summary)
    
    def summarize(self, col_name: str) -> None:
        """Summarize the contents of a column.
        
        Attributes:
            col_name: The column whereby the summarization is to take place.
        """

        self.dataset[col_name].apply(self._summarize)
    
    def return_dataset(self) -> pd.DataFrame:
        """Return self.dataset."""

        return self.dataset
    


        

