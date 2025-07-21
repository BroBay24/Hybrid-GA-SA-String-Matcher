import streamlit as st
from app.ga import run_genetic_algorithm
from app.sa import run_simulated_annealing


st.title("Hybrid GA-SA String Matcher")

target = st.text_input("Target String", "HELLO WORLD").upper()
population_size = st.slider("Ukuran Populasi", 10, 500, 100)
mutation_rate = st.slider("Tingkat Mutasi", 0.0, 0.2, 0.01)
generations = st.slider("Jumlah Generasi Maks", 10, 2000, 1000)

if st.button("Jalankan"):
    output_area = st.empty()

    def callback(gen, best, fitness):
        output_area.markdown(f"**Generasi {gen}**: `{best}` (Fitness: {fitness})")

    best, gen = run_genetic_algorithm(target, population_size, mutation_rate, generations, callback)
    st.success(f"Target ditemukan pada generasi ke-{gen}: `{best}`")

    # Jalankan Simulated Annealing setelah GA
    sa_result, sa_fitness = run_simulated_annealing(best, target)
    st.info(f"🔧 Setelah Simulated Annealing: `{sa_result}` (Fitness: {sa_fitness})")
