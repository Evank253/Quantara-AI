Quantara adapter stub: replace with real Quantara SDK calls
def run_quantara_sim(sim_inputs: dict):
    # deterministic stubbed simulation run
    run_id = "quantara-stub-001"
    outputs = {"status":"ok","result":{"value":42},"precision_bits":64}
    provenance = {"run_id": run_id, "inputs": sim_inputs}
    return run_id, outputs, provenance
