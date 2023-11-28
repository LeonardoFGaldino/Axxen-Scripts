{ 
   "tipo documento Declaração de Compensação":  {
        "tipo de crédito PIS/PASEP": {
            "6.2": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){0}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){1}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'valor_utili_dcomp': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){2}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){3}([\d\.]*\,\d{2})',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
            
            "6.3": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){0}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){1}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'valor_utili_dcomp': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){2}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){3}([\d\.]*\,\d{2})',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
            
            "6.5": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
                
            },
            
            "6.6": {   
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
                
            },
            
            "6.7": {   
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
                
            },
            
            "6.8": {      
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
                
            },
            
            "6.8/2018": { 
                  
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',  # Não possui no modelo
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
        
            },
            
            "6.8a": {   
                
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d[ab])',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
                
            },
            
            "6.9": {    
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
                
            },
            
            "8.1": { 
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'     
            }  
        }  
    }
}

{
    "tipo documento Declaração de Compensação":  {
        "tipo de crédito COFINS": {
            
            "6.2": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'(?<=Valor Utilizado nesta DCOMP)\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
                
            },
              
            "6.3": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'(?<=Valor Utilizado nesta DCOMP)\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            
            },
            
            "6.5": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'               
            },
            
            "6.6": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'    
            },
            
            "6.7": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "6.8": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "6.8a": {   
    
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d[ab])',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "6.9.1": {   
    
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'   
            },
            

            
            "6.9.2": { 
                
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
            },
            
            "8.1": { 
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
                
            }  
        }  
    }
}
    
##################################################################################################################################################
  
{     
    "tipo documento Declaração de Compensação":  {
        "tipo de crédito PAGEMENTO INDEVIDO": {
            
            "6.2": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){0}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){1}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'valor_utili_dcomp': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){2}([\d\.]*\,\d{2})(?:\n[\d\.]*\,\d{2})',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*(?:[\d\.]*\,\d{2}\n){3}([\d\.]*\,\d{2})',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },

            "6.9b": {
                
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d[ab])',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'Crédito (?:Original|Atualizado)?\s?na Data da Transmissão\n([\d\.]*\,\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "8.1": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
    
            "8.2": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
        }  
    }  
}

{                      
    "tipo documento Declaração de Compensação":  {
        "tipo de crédito OUTRO CRÉDITO": {
              
            "6.9b": {
                
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d[ab])',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'Crédito (?:Original|Atualizado)?\s?na Data da Transmissão\n([\d\.]*\,\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
            },
            
            "8.1": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'(?<=N[°º] do PER/DCOMP Inicial)[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(?:\n([\s\S]*?))\n',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'   
            },
        }  
    }  
}

{
          
    "tipo documento Declaração de Compensação":  {
        "tipo de crédito SALDO NEGATIVO DE CSLL": {
             
            "6.9b": {
                
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d[ab])',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'Crédito (?:Original|Atualizado)?\s?na Data da Transmissão\n([\d\.]*\,\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
            },
        }  
    }  
}
    
##################################################################################################################################################    

{                
    "tipo documento Pedido de Cancelamento":  {
        "tipo de crédito PIS/PASEP": {
            
            "6.8": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
        }  
    }  
}

{
            
    "tipo documento  Pedido de Cancelamento":{
        "tipo de crédito COFINS": {
                   
            "6.8": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'   
            },
        }  
    }  
}
       
##################################################################################################################################################       

{          
    "tipo documento Pedido de Ressarcimento":  {
        "tipo de crédito PIS/PASEP": {
                  
            "6.2": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi':  r'\n([\d.,]+)\nTotal\n',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
            
            "6.5": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'   
            },
            
            "6.6": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },

            "6.9": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
            
            "8.1": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
        }  
    }  
}    
    
{           
    "tipo documento Pedido de Ressarcimento":  {
        "tipo de crédito COFINS": {
              
            "6.2": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi':  r'\n([\d.,]+)\nTotal\n',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'    
            },
            
            "6.5": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "6.6": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "6.9": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
            
            "8.1": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)\n([^\d]*\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
        }  
    }  
}
    
    ##################################################################################################################################################      

{        
    "tipo documento Pedido de Restituição":  {
        "tipo de crédito PAGAMENTO INDEVIDO": {
              
            "6.0": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'  
            },
            
            "6.9b": {
                
                'versao': r'(?<=PER/DCOMP)[\s\t]*(\d.\d[ab])',
                'data_criacao': r'(?<=Data de Criação: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})', 
                'tipo_documento': r'(?<=Tipo de Documento: )[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito: )[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador: )[\s\t]*(SIM|NÃO)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial: )[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte: )[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária: )[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP:)[\s\t](SIM|NÃO)',
                'numero_perdcomp_ini': r'(?<=N° do PER/DCOMP Inicial: )[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida: )[\s\t]*(SIM|NÃO*)',
                'valor_credi': r'(?<=Valor do Crédito)[\s]*([\d\,\.]*)',
                'credi_data_trans': r'Crédito (?:Original|Atualizado)?\s?na Data da Transmissão\n([\d\.]*\,\d\d)',
                'valor_utili_dcomp': r'Valor Utilizado nesta (?:DCOMP|Declaração de Compensação)?\s([\d\.]{,},\d\d)',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ Detentor do Crédito: )[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida: )[\s]*(SIM|NÃO)',
                'grupo_tribu': r'(?<=Grupo de Tributo: )[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração: )[\s]*([^\n]*)',
                'periodicidade': r'(?<=Periodicidade: )[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota: )[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)' 
            },
        }  
    }  
}

##################################################################################################################################################
 
{ 
        
    "tipo documento Pedido de Restituição":  {
        "tipo de crédito CONTRIBUIÇÃO PREFIDENCIÁRIA": {
              
            "6.0": {
                
                'versao': r'(?<=PERDCOMP)[\s\t]*(\d.\d)',
                'data_criacao': r'(?<=Data de Criação)\:?[\s]*(\d{2}\/\d{2}\/\d{4})',
                'data_transmi': r'(?<=Data de Transmissão)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'tipo_documento': r'(?<=Tipo de Documento)[\s\t]*([^\n]*)',
                'tipo_de_credito': r'(?<=Tipo de Crédito)[\s\t]*([^\n]*)',
                'perdcomp_retificador': r'(?<=PER/DCOMP Retificador)[\s\t]*(Sim|Não)',
                'credito_oriundo': r'(?<=Crédito Oriundo de Ação Judicial)[\s]*([^\n]*)',
                'quali_contribuinte': r'(?<=Qualificação do Contribuinte)[\s]*([^\n]*)',
                'pessoa_extinta': r'(?<=Pessoa Jurídica Extinta por Liquidação Voluntária)[\s]*([^\n]*)',
                'indo_outro_perdcomp': r'(?<=Informado em Outro PER/DCOMP)[\s\t](Sim|Não)',
                'numero_perdcomp_ini': r'[\s\t]*(\d{5}\.\d{5}\.\d{6}\.\d{1}\.\d{1}\.\d{2}\-\d{4})',
                'credito_suce': r'(?<=Crédito de Sucedida)[\s\t]*(Sim|Não*)',
                'valor_credi': r'(?<=\nValor do Pedido de Ressarcimento)\s([\d\.]*\,\d{2})',
                'credi_data_trans': r'(?<=Crédito na Data de Transmissão)\s([\d\.]{,},\d\d)',
                'valor_utili_dcomp': r'\n([\d.,]+)\nValor Utilizado nesta DCOMP\n',
                'saldo_credi': r'(?<=Saldo do Crédito)[\s]*([\d\.]{,},\d\d)',
                'cnpj_detentor': r'(?<=CNPJ do Detentor do Débito)[\s]*([^\n]*)',
                'debi_suce': r'(?<=Débito de Sucedida)[\s]*(Sim|Não)',
                'grupo_tribu': r'(?<=Grupo de Tributo)[\s]*([^\n]*)',
                'periodo_apura': r'(?<=Período de Apuração)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'periodicidade': r'(?<=Período de Apuração)[\s]*(Anual|Mensal|Trimestral|Decendial)',
                'data_venci_triquota': r'(?<=Data de Vencimento do Tributo/Quota)[\s]*(\d{2}\/\d{2}\/\d{4})',
                'principal': r'(?<=\nPrincipal)\s([\d\.]*\,\d{2})',
                'multa': r'(?<=\nMulta)\s([\d\.]*\,\d{2})',
                'juros': r'(?<=\nJuros)\s([\d\.]*\,\d{2})',
                'total': r'(?<=\nTotal)\s([\d\.]*\,\d{2})',
                'valor': r'VALOR TOTAL\s*([\d.,]+)'
            },
        }
    }
}  
    
    
    
    
    
    
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

