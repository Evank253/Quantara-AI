from services.quantara import adapter


def test_quantara_stub():
    run_id, outputs, prov = adapter.run_quantara_sim({"param": 1})
    assert run_id.startswith("quantara")
    assert outputs.get("status") == "ok"
    assert "precision_bits" in outputs
