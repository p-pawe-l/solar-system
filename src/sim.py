
from objects import *

import plotly.graph_objects as go

# --- Simulation settings ---
DT: float = 6 * 60 * 60           # physics step [s] (~350 steps per Mercury orbit)
SIM_TIME: float = SATURN_ORBITAL_PERIOD  # ~30 years, takes ~15 s to compute
FRAME_EVERY: float = 5 * DAY      # one animation frame every 5 days
STEPS_PER_FRAME: int = int(FRAME_EVERY / DT)
N_FRAMES: int = int(SIM_TIME / FRAME_EVERY)

bodies: list[SolarSystemObject] = [
    sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
]


def step(dt: float) -> None:
    """One time step using the methods from SolarSystemObject."""
    # update_forces() computes the force from a single other body, so the
    # total force on each body is the sum over all other bodies.
    for body in bodies:
        total_force = np.zeros(3)
        for other in bodies:
            if other is body:
                continue
            body.update_forces(other)
            total_force = total_force + body.get_force()
        body.forces = total_force

    for body in bodies:
        body.update_velocity(dt)
        body.update_position(dt)


def run_simulation() -> np.ndarray:
    """Returns positions in AU, shape (N_FRAMES, n_bodies, 3)."""
    history = np.zeros((N_FRAMES, len(bodies), 3))
    for f in range(N_FRAMES):
        for b, body in enumerate(bodies):
            history[f, b] = body.get_pos() / AU
        for _ in range(STEPS_PER_FRAME):
            step(DT)
        if f % 100 == 0:
            print(f"\rSimulating... {100 * f / N_FRAMES:3.0f}%", end="", flush=True)
    print("\rSimulating... done")
    return history


# --- GUI ---
COLORS: dict[str, str] = {
    "Sun": "#ffc83c", "Mercury": "#a9a9a9", "Venus": "#84671c", "Earth": "#4f8fe0",
    "Mars": "#d0603a", "Jupiter": "#d8b48a", "Saturn": "#e6d48f", "Uranus": "#9fd8e0",
    "Neptune": "#4a6fe3",
}
SIZES: dict[str, int] = {  # not to scale, real radii are invisible
    "Sun": 16, "Mercury": 5, "Venus": 7, "Earth": 7, "Mars": 6,
    "Jupiter": 12, "Saturn": 11, "Uranus": 9, "Neptune": 9,
}
ZOOM_LEVELS: dict[str, float] = {  # axis half-width [AU]
    "Inner planets": 1.8, "Up to Jupiter": 6.0, "Up to Saturn": 11.0, "All planets": 32.0,
}


def zoom(lim: float) -> dict:
    return {"scene.xaxis.range": [-lim, lim], "scene.yaxis.range": [-lim, lim],
            "scene.zaxis.range": [-lim / 3, lim / 3]}


def build_figure(history: np.ndarray) -> go.Figure:
    names = [body.get_name() for body in bodies]
    colors = [COLORS.get(n, "white") for n in names]
    sizes = [SIZES.get(n, 5) for n in names]
    planets = [i for i, n in enumerate(names) if n != "Sun"]

    def bodies_trace(f: int) -> go.Scatter3d:
        p = history[f]
        return go.Scatter3d(
            x=p[:, 0], y=p[:, 1], z=p[:, 2],
            mode="markers+text", text=names, textposition="top center",
            textfont=dict(color="white", size=11),
            marker=dict(size=sizes, color=colors, line=dict(width=0)),
            hovertemplate="%{text}<br>x=%{x:.4f} AU<br>y=%{y:.4f} AU<br>z=%{z:.4f} AU<extra></extra>",
            showlegend=False,
        )

    # Whole simulated path of each planet, drawn once (static). Growing trails
    # for 8 planets over 30 years would make the plot far too heavy.
    paths = [
        go.Scatter3d(
            x=history[:, i, 0], y=history[:, i, 1], z=history[:, i, 2], mode="lines",
            line=dict(color=colors[i], width=2), opacity=0.45, name=names[i], hoverinfo="skip",
        )
        for i in planets
    ]

    def title(f: int) -> str:
        return f"Solar System · t = {f * FRAME_EVERY / DAY:7.0f} days ({f * FRAME_EVERY / YEAR:5.2f} years)"

    # Faint ecliptic plane (z = 0) to show the planets' inclination.
    lim = max(ZOOM_LEVELS.values())
    plane = go.Surface(
        x=[[-lim, lim], [-lim, lim]], y=[[-lim, -lim], [lim, lim]], z=[[0, 0], [0, 0]],
        showscale=False, opacity=0.08, colorscale=[[0, "white"], [1, "white"]],
        hoverinfo="skip", name="Ecliptic",
    )

    # Trace 0 (bodies) is animated, the paths and plane are static.
    fig = go.Figure(
        data=[bodies_trace(0), *paths, plane],
        frames=[
            go.Frame(name=str(f), data=[bodies_trace(f)], traces=[0],
                     layout=go.Layout(title=title(f)))
            for f in range(N_FRAMES)
        ],
    )

    start = ZOOM_LEVELS["Inner planets"]
    axis = dict(backgroundcolor="rgb(5,5,20)", gridcolor="rgb(40,40,60)", color="rgb(150,150,170)")
    play = dict(frame=dict(duration=40, redraw=True), fromcurrent=True, transition=dict(duration=0))
    fig.update_layout(
        title=title(0),
        template="plotly_dark",
        legend=dict(title="Paths (click to toggle)"),
        scene=dict(
            xaxis=dict(axis, title="x [AU]", range=[-start, start]),
            yaxis=dict(axis, title="y [AU]", range=[-start, start]),
            zaxis=dict(axis, title="z [AU]", range=[-start / 3, start / 3]),
            aspectmode="manual", aspectratio=dict(x=1, y=1, z=1 / 3),
            camera=dict(eye=dict(x=1.1, y=-1.1, z=0.7)),
        ),
        updatemenus=[
            dict(
                type="buttons", direction="right", x=0.02, y=0.06, xanchor="left", yanchor="bottom",
                buttons=[
                    dict(label="▶ Play", method="animate", args=[None, play]),
                    dict(label="⏸ Pause", method="animate",
                         args=[[None], dict(frame=dict(duration=0), mode="immediate")]),
                ],
            ),
            dict(  # the outer planets are ~80x farther out than Mercury
                type="buttons", direction="right", x=0.02, y=1.0, xanchor="left", yanchor="top",
                buttons=[dict(label=label, method="relayout", args=[zoom(lim)])
                         for label, lim in ZOOM_LEVELS.items()],
            ),
        ],
        sliders=[dict(
            x=0.2, len=0.78, y=0.06, currentvalue=dict(prefix="Day "),
            steps=[dict(method="animate", label=f"{f * FRAME_EVERY / DAY:.0f}",
                        args=[[str(f)], dict(mode="immediate", frame=dict(duration=0, redraw=True))])
                   for f in range(0, N_FRAMES, 10)],
        )],
    )
    return fig


if __name__ == "__main__":
    history = run_simulation()
    fig = build_figure(history)
    fig.show()
