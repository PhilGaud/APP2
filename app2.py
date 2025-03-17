import streamlit as st

def calculate_compound_interest(principal, rate, years):
    return principal * (1 + rate / 100) ** years

def main():
    st.title("📈 Application Financière Simple")
    
    st.sidebar.header("Paramètres de l'Investissement")
    principal = st.sidebar.number_input("Montant initial (€)", min_value=0.0, value=1000.0, step=100.0)
    rate = st.sidebar.number_input("Taux d'intérêt annuel (%)", min_value=0.0, value=5.0, step=0.1)
    years = st.sidebar.number_input("Durée de l'investissement (années)", min_value=1, value=10, step=1)
    
    if st.sidebar.button("Calculer"):
        future_value = calculate_compound_interest(principal, rate, years)
        st.success(f"💰 Valeur future de l'investissement : {future_value:.2f} €")
    
    st.write("### Explication de l'intérêt composé")
    st.write("L'intérêt composé est calculé en appliquant un taux d'intérêt non seulement au capital initial, mais aussi aux intérêts accumulés.")

if __name__ == "__main__":
    main()