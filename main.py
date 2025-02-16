import streamlit as st
from generator import RedacaoGenerator
from styles import apply_custom_styles, add_footer
from export_utils import export_estrutura

def main():
    # Aplicar estilos customizados
    apply_custom_styles()

    st.title("Scriptor")
    st.markdown("""
    ### Gere estruturas para sua redação do ENEM e vestibulares
    Este gerador fornece máscaras de redação com espaços para você preencher com seu próprio conteúdo.
    Clique nos botões para gerar diferentes estruturas para cada parte da sua redação.
    """)

    # Inicializar estado da sessão se não existir
    if 'redacao' not in st.session_state:
        st.session_state.redacao = {
            'introducao': '',
            'desenvolvimento1': '',
            'desenvolvimento2': '',
            'conclusao': ''
        }

    # Container principal para melhor espaçamento
    with st.container():
        # Botão para gerar redação completa
        if st.button("🔄 Gerar Estrutura Completa"):
            st.session_state.redacao = RedacaoGenerator.gerar_redacao_completa()
            st.rerun()

        # Seção de Introdução
        st.markdown("### Introdução")
        col1, col2 = st.columns([4, 1])
        with col1:
            st.text_area("", st.session_state.redacao['introducao'], height=150, key='intro_text', 
                        help="Preencha os campos indicados entre chaves { } com seu próprio conteúdo", label_visibility="collapsed")
        with col2:
            if st.button("🔄 Gerar", key='btn_intro'):
                st.session_state.redacao['introducao'] = RedacaoGenerator.gerar_introducao()
                st.rerun()

        # Primeiro Desenvolvimento
        st.markdown("### Desenvolvimento 1")
        col1, col2 = st.columns([4, 1])
        with col1:
            st.text_area("", st.session_state.redacao['desenvolvimento1'], height=150, key='dev1_text',
                        help="Preencha os campos indicados entre chaves { } com seu próprio conteúdo", label_visibility="collapsed")
        with col2:
            if st.button("🔄 Gerar", key='btn_dev1'):
                st.session_state.redacao['desenvolvimento1'] = RedacaoGenerator.gerar_desenvolvimento1()
                st.rerun()

        # Segundo Desenvolvimento
        st.markdown("### Desenvolvimento 2")
        col1, col2 = st.columns([4, 1])
        with col1:
            st.text_area("", st.session_state.redacao['desenvolvimento2'], height=150, key='dev2_text',
                        help="Preencha os campos indicados entre chaves { } com seu próprio conteúdo", label_visibility="collapsed")
        with col2:
            if st.button("🔄 Gerar", key='btn_dev2'):
                st.session_state.redacao['desenvolvimento2'] = RedacaoGenerator.gerar_desenvolvimento2()
                st.rerun()

        # Conclusão
        st.markdown("### Conclusão")
        col1, col2 = st.columns([4, 1])
        with col1:
            st.text_area("", st.session_state.redacao['conclusao'], height=150, key='concl_text',
                        help="Preencha os campos indicados entre chaves { } com seu próprio conteúdo", label_visibility="collapsed")
        with col2:
            if st.button("🔄 Gerar", key='btn_concl'):
                st.session_state.redacao['conclusao'] = RedacaoGenerator.gerar_conclusao()
                st.rerun()

        # Exportar
        st.markdown("### Exportar")
        formato = st.selectbox(
            "Formato de exportação",
            ["Texto (.txt)", "Word (.docx)", "PDF (.pdf)"],
            label_visibility="collapsed"
        )
        if st.button("📥 Exportar Estrutura"):
            texto_completo = '\n\n'.join([
                st.session_state.redacao['introducao'],
                st.session_state.redacao['desenvolvimento1'],
                st.session_state.redacao['desenvolvimento2'],
                st.session_state.redacao['conclusao']
            ])
            export_estrutura(texto_completo, formato)

        # Instruções de uso
        with st.expander("📝 Como usar este gerador"):
            st.markdown("""
            1. Use os botões 🔄 para gerar diferentes estruturas para cada parte da redação
            2. Os campos entre chaves { } indicam onde você deve inserir seu próprio conteúdo
            3. Você pode gerar múltiplas vezes até encontrar uma estrutura que melhor se adeque ao seu tema
            4. Exporte a estrutura no formato desejado (.txt, .docx ou .pdf)
            """)

        # Adicionar rodapé
        add_footer()

if __name__ == "__main__":
    main()