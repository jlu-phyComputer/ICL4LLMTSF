from models import ICL4LLMTSF_Llama, ICL4LLMTSF_Gpt2, ICL4LLMTSF_Opt_1b


class Exp_Basic(object):
    def __init__(self, args):
        self.args = args
        self.model_dict = {
            'ICL4LLMTSF_Llama': ICL4LLMTSF_Llama,
            'ICL4LLMTSF_Gpt2': ICL4LLMTSF_Gpt2,
            'ICL4LLMTSF_Opt1b': ICL4LLMTSF_Opt_1b
        }
        self.model = self._build_model()

    def _build_model(self):
        raise NotImplementedError

    def _get_data(self):
        pass

    def vali(self):
        pass

    def train(self):
        pass

    def test(self):
        pass
