from AI_lib import aifunction

def test_haversine():
    # Amsterdam to Berlin
    assert aifunction.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == 576.6625818456291