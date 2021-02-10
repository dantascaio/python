import numpy as np
import nltk


class TFIDF:

    def term_frequency(self, term, sentence):
        # please use nltk.word_tokenize
        lista_palavras = nltk.word_tokenize(sentence)

        quantidade_termo_solicitado = self.contar_termos(term, lista_palavras)
        print(f'termo: {term}')
        print(f'quantidade_termo: {quantidade_termo_solicitado}')

        # buscar termo mais frequente
        termo_mais_frequente = 0

        for palavra in lista_palavras:
            quantidade_ocorrencias = self.contar_termos(palavra, lista_palavras)
            if quantidade_ocorrencias > termo_mais_frequente:
                termo_mais_frequente = quantidade_ocorrencias
        print(f'termo buscado {term} qtd {quantidade_termo_solicitado}')
        print(f'termo mais encontrado qtd {termo_mais_frequente}')
        print(f'frase inserida{sentence}')

        if quantidade_termo_solicitado > 0:
            tf = 0.5 + 0.5 * (quantidade_termo_solicitado / termo_mais_frequente)
        else:
            tf = 0
        print(f'tf: {tf}')
        return tf

    def inverse_document_frequency(self, term, corpus):
        # please use nltk.word_tokenize
        contador_sentecas = len(corpus)
        quantidade_setencas_com_termo = 0
        for sentence in corpus:
            print(f'Sentence: {sentence}')
            if self.contar_termos(term, nltk.word_tokenize(sentence)) > 0:
                quantidade_setencas_com_termo += 1
        idf = np.log(contador_sentecas / quantidade_setencas_com_termo)
        print(f'term: {term}')
        print(f'Corpus: {corpus}')
        print(f'Idf: {idf}')
        return idf

    def tfidf(self, term, sentence, corpus):
        tfidf = self.term_frequency(term, sentence) * self.inverse_document_frequency(term, corpus)
        return tfidf

    def contar_termos(self, term, lista_palavras):
        contador_palavra = 0
        for j in range(0, len(lista_palavras)):
            if term == lista_palavras[j]:
                contador_palavra += 1
            j += 1
            # print(f'palavra: {term}')
            # print(f'contador: {contador_palavra}')
        return contador_palavra
