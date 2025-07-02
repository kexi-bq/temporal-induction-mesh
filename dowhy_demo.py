
import pandas as pd
import numpy as np
from tim_core import compute_influence_matrix
from dowhy import CausalModel

# Fake data
np.random.seed(0)
df = pd.DataFrame({
    "cause": np.random.binomial(1, 0.5, 100),
    "feature": np.random.normal(0, 1, 100),
})
df["effect"] = df["cause"] * df["feature"] + np.random.normal(0, 0.1, 100)

# Causal analysis
model = CausalModel(data=df, treatment="cause", outcome="effect",
                    common_causes=["feature"])
identified_estimand = model.identify_effect()
estimate = model.estimate_effect(identified_estimand,
                                 method_name="backdoor.linear_regression")
print(estimate)
refutation = model.refute_estimate(identified_estimand, estimate,
                                   method_name="placebo_treatment_refuter")
print(refutation)
