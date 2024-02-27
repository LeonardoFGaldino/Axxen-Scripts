import tkinter as tk
from tkinter import filedialog
import pandas as pd
from cnpj_info_logic import CNPJInfoLogic
import threading
import logging

class CNPJInfoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CNPJ Info Retriever")

        self.label = tk.Label(root, text="Selecione a Planilha Excel:")
        self.label.pack(pady=10)


        self.button = tk.Button(root, text="Selecionar", command=self.start_processing_thread)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def start_processing_thread(self):
            # Cria uma nova thread para processar os dados e evitar travamentos na interface
        processing_thread = threading.Thread(target=self.process_excel_data)
        processing_thread.start()

    def process_excel_data(self):
        logger = logging.getLogger()
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        logger.warning(file_path)
        if file_path:
            logger.warning('Abrindo arquivo')
            df_excel = pd.read_excel(file_path, dtype=str)
            logger.warning('Processando dados')
            results = CNPJInfoLogic.process_data(df_excel)

            self.root.after(0, self.update_gui, results)  # Atualiza a GUI após o processamento

    def update_gui(self, results):
        self.result_label.config(text=f"Resultados: {results}")
        self.export_results_to_excel(results)

    def export_results_to_excel(self, results):
        if results is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

            if save_path:
                results.to_excel(save_path, index=False)
                self.result_label.config(text=f"Resultados exportados para {save_path}")
            else:
                self.result_label.config(text="Exportação cancelada.")
        else:
            self.result_label.config(text="Nenhum resultado para exportar.")


root = tk.Tk()
app = CNPJInfoGUI(root)
root.mainloop()
