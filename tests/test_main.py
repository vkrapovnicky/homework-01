from homework.main import calculate_hashes

def test_calculate_hashes():
    assert (calculate_hashes("hse")) == ('ff85fdbd9ba2a43896908930c9048fd5', 'dccdacc87520c09e583c4138aa9301c90f430bf36b479f573d73e6404bae7cdd')