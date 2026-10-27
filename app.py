import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

st.set_page_config(
    page_title="Molecule Explorer",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 Molecule Explorer")
st.write("Explore the properties of chemical molecules.")

smiles = st.text_input(
    "Enter a molecule in SMILES format:",
    "CCO"
)

if st.button("Analyze Molecule"):
    molecule = Chem.MolFromSmiles(smiles)

    if molecule is not None:
        st.success("Molecule analyzed successfully!")

        st.subheader("Molecular Information")

        st.write(
            "Molecular Formula:",
            Chem.rdMolDescriptors.CalcMolFormula(molecule)
        )

        st.write(
            "Molecular Weight:",
            round(Descriptors.MolWt(molecule), 2),
            "g/mol"
        )

        st.write(
            "Number of Atoms:",
            molecule.GetNumAtoms()
        )

        st.write(
            "Number of Bonds:",
            molecule.GetNumBonds()
        )

        st.write(
            "Hydrogen Bond Donors:",
            Lipinski.NumHDonors(molecule)
        )

        st.write(
            "Hydrogen Bond Acceptors:",
            Lipinski.NumHAcceptors(molecule)
        )

    else:
        st.error("Invalid SMILES. Please enter a valid molecule.")
