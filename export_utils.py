import streamlit as st
from docx import Document
from fpdf import FPDF

def export_estrutura(texto, formato):
    """
    Exporta a estrutura no formato especificado
    """
    try:
        if formato == "Texto (.txt)":
            st.download_button(
                label="📥 Baixar arquivo .txt",
                data=texto,
                file_name="estrutura_redacao.txt",
                mime="text/plain"
            )

        elif formato == "Word (.docx)":
            doc = Document()
            doc.add_paragraph(texto)
            doc_bytes = doc.save("estrutura_redacao.docx")

            with open("estrutura_redacao.docx", "rb") as file:
                st.download_button(
                    label="📥 Baixar arquivo .docx",
                    data=file,
                    file_name="estrutura_redacao.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

        elif formato == "PDF (.pdf)":
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=texto)

            st.download_button(
                label="📥 Baixar arquivo .pdf",
                data=pdf.output(dest="S").encode("latin-1"),
                file_name="estrutura_redacao.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"Erro ao exportar o arquivo: {str(e)}")