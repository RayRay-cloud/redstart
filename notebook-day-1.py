import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la


    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    L'énoncé indique les deux constantes correspondant à la masse et à la longueur du booster. La constante gravitationelle aussi.
    """)
    return


@app.cell
def _():
    g=1
    M=1.0
    l=2.0
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En projetant la force appliquée par le réacteur sur le booster selon le même schéma fourni, et en considérant un repère cartésien tel que x l'horizontale et y la verticale, on obtient les projections suivantes:
    """)
    return


@app.cell
def _(np):
    theta=0;
    phi=0;
    f=0;
    fx=-f*np.sin(theta+phi)
    fy=f*np.cos(theta+phi)
    return fx, fy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    En utilisant la deuxième loi de Newton, nous projetons les forces appliquées. Ici les forces considérées sont : le poids P et la force appliquée par le réacteur sur le booster F. Dans ce qui suit, ax représente l'accélération suivant l'axe X et ay représente l'accélération suivant l'axe Y.

    Les équations sont les suivantes :

    \[
    \ddot{x} = \frac{f_x}{M}, \quad \ddot{y} = \frac{f_y - M g}{M}
    \]
    où $f_x = -f \sin(\theta + \phi)$, $f_y = f \cos(\theta + \phi)$
    """)
    return


@app.cell
def _(M, fx, fy, g):


    # Initialize accelerations to 0
    ax = 0.0  # ẍ (horizontal acceleration)
    ay = 0.0  # ÿ (vertical acceleration)

    # Newton's second law F = ma
    # Horizontal: M·ẍ = fx
    ax = fx / M                      #  # ẍ = -f·sin(θ + ϕ)

    # Vertical: M·ÿ = fy - Mg
    ay = (fy - M * g) / M           # ÿ = f·cos(θ + ϕ) - g


    # Vertical: M·ÿ = fy - Mg
    ay = (fy - M * g) / M           # ÿ = f·cos(θ + ϕ) - g
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The booster is a uniform rod. The center of mass (x, y) is exactly at the middle, so the rod extends ℓ/2 above and ℓ/2 below the center. Total length = ℓ.
    """)
    return


@app.cell
def _(M, l):
    J = (1/12) * M * l**2
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Applying the angular momentum theorem about the center of mass, the torque exerted by the reactor force is:

    $$\tau = -\frac{\ell}{2} \cdot f \sin\phi$$

    where $\frac{\ell}{2}$ is the distance between the center of mass and the base of the booster (the point where the force is applied).

    The fundamental rotation law gives $J\ddot{\theta} = \tau$, so:

    $$\ddot{\theta} = -\frac{\ell}{2J} f \sin\phi$$

    If we consider that $\omega = \dot{\theta}$, the equation becomes:

    $$\dot{\theta} = \omega, \quad \dot{\omega} = -\frac{\ell}{2J} f \sin\phi$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The dimension is \( n = 6 \).

    The state is:
    $$
    s = [x, v_x, y, v_y, \theta, \omega]
    $$

    where \( \omega \) is the derivative of \( \theta \), i.e.:
    $$
    \omega = \dot{\theta}
    $$

    The system dynamics are:
    $$
    F(s, f, \phi) = [v_x, a_x, v_y, a_y, \omega, \dot{\omega}]
    $$

    where the forces are defined as:
    $$
    f_x = -f \sin(\theta + \phi), \quad f_y = f \cos(\theta + \phi)
    $$

    Thus,
    $$
    F(s, f, \phi) =
    \begin{bmatrix}
    v_x \\
    \frac{f_x}{M} \\
    v_y \\
    \frac{f_y - Mg}{M} \\
    \omega \\
    -\frac{l}{2J} f \sin(\phi)
    \end{bmatrix}
    $$

    and again:
    $$
    f_x = -f \sin(\theta + \phi), \quad f_y = f \cos(\theta + \phi)
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    $F$ encodes the right-hand side of the ODE:

    $$\dot{s} = F(s,\ f,\ \phi)$$

    Expanding $\dot{s}$ component by component:

    $$\dot{s} = \frac{d}{dt}\begin{pmatrix} x \\ v_x \\ y \\ v_y \\ \theta \\ \omega \end{pmatrix} = \begin{pmatrix} \dot{x} \\ \dot{v}_x \\ \dot{y} \\ \dot{v}_y \\ \dot{\theta} \\ \dot{\omega} \end{pmatrix} = F(s,\ f,\ \phi) = \begin{pmatrix} v_x \\[4pt] -\dfrac{f}{M}\sin(\theta + \phi) \\[8pt] v_y \\[4pt] \dfrac{f\cos(\theta+\phi)}{M} - g \\[8pt] \omega \\[4pt] -\dfrac{l}{2J}\,f\sin(\phi) \end{pmatrix}$$

    The first and third rows follow directly from the definitions $v_x = \dot{x}$ and $v_y = \dot{y}$. The second and fourth rows are Newton's second law $\dot{v} = F/M$, with thrust decomposed into horizontal and vertical components and gravity subtracted vertically. The fifth row follows from $\omega = \dot{\theta}$. The sixth is the rotational equivalent of Newton's second law, $\dot{\omega} = \tau / J$.

    $F$ returns exactly this vector, and `solve_ivp` integrates $\dot{s} = F(s, f, \phi)$ forward step by step to build the full trajectory.

    - **`dense_output=True`**  :instead of returning values only at discrete grid points, this produces a **continuous interpolating function** `sol.sol(t)`.
    - **`max_step=0.01`** :caps the integration step size at 10 ms.
    The function returns `sol.sol`, a callable `t → [x, vx, y, vy, theta, omega]` that gives the full state of the rocket at any moment.

    ---
    """)
    return


@app.cell
def _(J, M, g, l, np, sci):
    def redstart_solve(t_span, y0, f_phi):
        def rhs(t, y):
            x, vx, y_pos, vy, theta, omega = y
            f, phi = f_phi(t, y)
            fx = -f * np.sin(theta + phi)
            fy = f * np.cos(theta + phi)
            ax = fx / M
            ay = (fy - M * g) / M
            torque = - (l / 2) * f * np.sin(phi)
            alpha = torque / J
            return [vx, ax, vy, ay, omega, alpha]
        sol = sci.solve_ivp(rhs, t_span, y0, dense_output=True)
        return sol.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell
def _(l, np, plt, redstart_solve):
    t_span = [0.0, 5.0]

    y0 = [0, 0, 10, 0, 0, 0]

    def f_phi(t, y):
        return np.array([0.0, 0.0])

    sol = redstart_solve(t_span, y0, f_phi)

    t = np.linspace(0, 5, 1000)

    Y = sol(t)

    plt.figure(figsize=(8,5))

    plt.plot(t, Y[2], label=r"$y(t)$")
    plt.axhline(l, color="red", linestyle="--", label=r"$y=\ell$")
    plt.axvline(4, color="green", linestyle="--", label=r"$t=4$")

    plt.xlabel("time")
    plt.ylabel("height")
    plt.title("Free Fall Verification")
    plt.grid(True)
    plt.legend()

    plt.gcf()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Controlled Landing — Redstart Booster

    ## Initial Conditions

    $$x(0) = 0, \quad \dot{x}(0) = 0, \quad \theta(0) = 0, \quad \dot{\theta}(0) = 0$$
    $$y(0) = 10 \text{ m}, \quad \dot{y}(0) = -2 \text{ m/s}$$

    ## Goal

    Find $f(t)$ such that at $t = 5$ s:

    $$y(5) = \frac{\ell}{2} = 1 \text{ m} \quad \text{(booster at ground level)}, \qquad \dot{y}(5) = 0 \text{ m/s} \quad \text{(booster at rest)}$$

    ---

    ## Simplification

    Since $\theta = 0$ and $\phi = 0$ throughout, the horizontal and angular motion stay zero. Only the vertical axis matters.

    Newton's second law gives:

    $$M\ddot{y} = f - Mg \quad \Rightarrow \quad \ddot{y} = \frac{f}{M} - g$$

    ---

    ## Method: Inverse Trajectory Planning

    **Idea:** freely choose a smooth $y(t)$ that satisfies all 4 boundary conditions, then compute the force $f(t)$ that produces it.

    We pick a **cubic polynomial** (4 unknowns for 4 conditions):

    $$y(t) = at^3 + bt^2 + ct + d$$

    Its derivatives are:

    $$\dot{y}(t) = 3at^2 + 2bt + c$$

    $$\ddot{y}(t) = 6at + 2b$$

    ### Finding the Coefficients

    **$d$ and $c$ are found directly** from the initial conditions at $t=0$:

    $$y(0) = d = 10 \quad \Rightarrow \quad d = 10$$

    $$\dot{y}(0) = c = -2 \quad \Rightarrow \quad c = -2$$

    **$a$ and $b$ require solving a 2×2 system** using the conditions at $t=5$:

    $$y(5) = 125a + 25b + 5(-2) + 10 = 1 \quad \Rightarrow \quad 125a + 25b = 1$$

    $$\dot{y}(5) = 75a + 10b + (-2) = 0 \quad \Rightarrow \quad 75a + 10b = 2$$

    $$\begin{pmatrix} 125 & 25 \\ 75 & 10 \end{pmatrix} \begin{pmatrix} a \\ b \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \quad \Rightarrow \quad \text{solved with } \texttt{np.linalg.solve}$$

    ### Reactor Force

    Once $y(t)$ is known, $\ddot{y}(t) = 6at + 2b$ is also known, so:

    $$\boxed{f(t) = M\bigl(\ddot{y}(t) + g\bigr)}$$

    $f(t)$ is a **linear function of $t$** — simple and physically realizable (positive throughout).

    ---

    ## Simulation Results

    | Variable | $t = 0$ | $t = 5$ |
    |----------|---------|---------|
    | $y(t)$ | $10$ m | $1$ m |
    | $\dot{y}(t)$ | $-2$ m/s | $0$ m/s |
    | $x(t)$, $\dot{x}(t)$, $\theta(t)$ | $0$ | $0$ (unchanged) |
    | $f(t)$ | — | $\geq 0$ everywhere |
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    def controlled_landing():
        d = 10
        c = -2
        A = np.array([[125, 25],
                      [75,  10]])
        b_vec = np.array([1 - 5*c - d, -c])
        a, b = np.linalg.solve(A, b_vec)

        def f_control(t):
            yddot = 6*a*t + 2*b
            return M * (yddot + g)

        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]  # x=0, vx=0, y=10, vy=-2, theta=0, omega=0

        def f_phi(t, y):
            return np.array([f_control(t), 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(0, 5, 1000)
        Y = sol(t)

        # x(t)
        plt.subplot(2, 3, 1)
        plt.plot(t, Y[0], label=r"$x(t)$")
        plt.axhline(0, color="grey", ls="--", label=r"$x=0$")
        plt.title("Position horizontale x(t)")
        plt.xlabel("temps $t$")
        plt.grid(True)
        plt.legend()

        # vx(t)
        plt.subplot(2, 3, 2)
        plt.plot(t, Y[1], label=r"$\dot{x}(t)$", color="orange")
        plt.axhline(0, color="grey", ls="--")
        plt.title("Vitesse horizontale vx(t)")
        plt.xlabel("temps $t$")
        plt.grid(True)
        plt.legend()

        # y(t)
        plt.subplot(2, 3, 3)
        plt.plot(t, Y[2], label=r"$y(t)$", color="blue")
        plt.axhline(l/2, color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Position verticale y(t)")
        plt.xlabel("temps $t$")
        plt.grid(True)
        plt.legend()

        # vy(t)
        plt.subplot(2, 3, 4)
        plt.plot(t, Y[3], label=r"$\dot{y}(t)$", color="green")
        plt.axhline(0, color="grey", ls="--", label=r"$\dot{y}=0$")
        plt.title("Vitesse verticale vy(t)")
        plt.xlabel("temps $t$")
        plt.grid(True)
        plt.legend()

        # theta(t)
        plt.subplot(2, 3, 5)
        plt.plot(t, Y[4], label=r"$\theta(t)$", color="purple")
        plt.axhline(0, color="grey", ls="--")
        plt.title("Angle θ(t)")
        plt.xlabel("temps $t$")
        plt.grid(True)
        plt.legend()

        # f(t)
        plt.subplot(2, 3, 6)
        plt.plot(t, f_control(t), label=r"$f(t)$", color="red")
        plt.axhline(M*g, color="grey", ls="--", label=r"$f=Mg$")
        plt.title("Force f(t)")
        plt.xlabel("temps $t$")
        plt.grid(True)
        plt.legend()

        plt.suptitle("Atterrissage Contrôlé", fontsize=14)
        plt.tight_layout()

        # Vérification numérique
        Y_final = sol(5.0)
        print(f"y(5)  = {Y_final[2]:.4f}  (cible : {l/2})")
        print(f"ẏ(5)  = {Y_final[3]:.4f}  (cible : 0)")
        print(f"x(5)  = {Y_final[0]:.4f}  (cible : 0)")
        print(f"ẋ(5)  = {Y_final[1]:.4f}  (cible : 0)")

        return plt.gcf()

    controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.function
def world(view_box, *objects):
    x_min, x_max, y_min, y_max = view_box

    w = x_max - x_min
    h = y_max - y_min
    scale = 50

    W = w * scale
    H = h * scale

    def wx(x): return (x - x_min) * scale
    def wy(y): return (y_max - y) * scale

    sky    = f'<rect x="0" y="0" width="{W}" height="{H}" fill="skyblue"/>'
    ground = f'<rect x="0" y="{wy(0)}" width="{W}" height="{H - wy(0)}" fill="#8B6914"/>'
    pad    = f'<rect x="{wx(-1)}" y="{wy(0)}" width="{2*scale}" height="{0.2*scale}" fill="lime"/>'

    objects_svg = "".join(str(obj) for obj in objects)
    flip = f'translate({wx(0)}, {wy(0)}) scale({scale}, {-scale})'
    objects_group = f'<g transform="{flip}">{objects_svg}</g>'

    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{sky}{ground}{pad}{objects_group}</svg>'


@app.cell
def _(mo):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            )

        ],
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, np):
    def booster(x, y, theta, f, phi):
        body_w = l / 5
        body_h = l
        flame_w = l / 5
        flame_len = (l / 2) * (f / (M * g)) if f > 0 else 0

        # Body centered at (x,y)
        body = f'<rect x="{-body_w/2}" y="{-body_h/2}" width="{body_w}" height="{body_h}" fill="black"/>'

        # Flame: starts at base (y = -l/2), extends downward by flame_len
        # Use positive height, position rect starting at y=-l/2 going to y=-(l/2+flame_len)
        flame = f'''<g transform="translate(0, {-(body_h/2 + flame_len)}) rotate({np.degrees(-phi)}, 0, {flame_len})">
            <rect x="{-flame_w/2}" y="0" width="{flame_w}" height="{flame_len}" fill="red"/>
        </g>''' if flame_len > 0 else ''

        angle_deg = np.degrees(-theta)

        return f'<g transform="translate({x}, {y}) rotate({angle_deg}, 0, 0)">{body}{flame}</g>'

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notre fonction controlled-landing ne prend pas de paramètres pour les conditions initiales, donc l'animation ci-dessous marche pour les conditions précédentes.
    """)
    return


@app.cell
def _(M, g, l, mo, np, plt, redstart_solve):
    import matplotlib.patches as patches
    import matplotlib.animation as animation
    from matplotlib.transforms import Affine2D

    T   = 5.0
    fps = 20

    y0_anim = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]

    c_coef = -2.0
    d_coef = 10.0
    A_coef = np.array([[125.0, 25.0], [75.0, 10.0]])
    b_coef = np.array([1.0 - 5*c_coef - d_coef, 0.0 - c_coef])
    a_coef, b_coef2 = np.linalg.solve(A_coef, b_coef)

    def f_phi_anim(t, s):
        yddot = 6*a_coef*t + 2*b_coef2
        return [max(0.0, M*(yddot + g)), 0.0]

    sol_anim  = redstart_solve([0.0, T], y0_anim, f_phi_anim)
    times_gif = np.linspace(0, T, int(T * fps) + 1)

    states_gif = []
    for t_i in times_gif:
        s_i      = sol_anim(t_i)
        fi, phii = f_phi_anim(t_i, s_i)
        states_gif.append({
            't': t_i,
            'x': float(s_i[0]),
            'y': float(s_i[2]),
            'theta': float(s_i[4]),
            'f': float(fi),
            'phi': float(phii),
        })

    fig_gif, ax_gif = plt.subplots(figsize=(4, 7))
    ax_gif.set_xlim(-2, 2)
    ax_gif.set_ylim(-0.5, 11)
    ax_gif.set_aspect('equal')
    ax_gif.axis('off')

    ax_gif.add_patch(patches.Rectangle((-2, -0.5), 4, 12,   color='skyblue', zorder=0))
    ax_gif.add_patch(patches.Rectangle((-2, -0.5), 4,  0.5, color='#8B6914', zorder=1))
    ax_gif.add_patch(patches.Rectangle((-1,  0.0), 2,  0.1, color='lime',    zorder=2))

    body_w_g  = l / 5
    body_h_g  = l
    flame_w_g = l / 5

    body_p = patches.Rectangle(
        (-body_w_g/2, -body_h_g/2), body_w_g, body_h_g,
        color='black', zorder=5
    )
    ax_gif.add_patch(body_p)

    flame_p = patches.Rectangle(
        (-flame_w_g/2, 0), flame_w_g, 0.001,
        color='red', zorder=4
    )
    ax_gif.add_patch(flame_p)

    info_txt = ax_gif.text(-1.8, 10.5, '', fontsize=8, color='black', zorder=6)

    def update_gif(frame):
        st          = states_gif[frame]
        x, y, theta = st['x'], st['y'], st['theta']
        f, phi      = st['f'], st['phi']

        # Hide flame when booster has landed
        landed = y <= l / 2 + 0.05

        tb = (Affine2D().rotate(-theta).translate(x, y) + ax_gif.transData)
        body_p.set_transform(tb)

        if landed:
            flame_p.set_visible(False)
        else:
            flame_len = (l/2) * (f / (M*g)) if f > 0 else 0.001
            flame_p.set_visible(True)
            flame_p.set_height(flame_len)
            flame_p.set_width(flame_w_g)
            flame_p.set_xy((-flame_w_g/2, -(body_h_g/2 + flame_len)))
            tf = (Affine2D()
                  .rotate_around(0, -body_h_g/2, -phi)
                  .rotate_around(0, 0, -theta)
                  .translate(x, y)
                  + ax_gif.transData)
            flame_p.set_transform(tf)

        info_txt.set_text(f't={st["t"]:.1f}s  y={y:.2f}m  {"LANDED" if landed else f"f={f:.2f}N"}')
        return body_p, flame_p, info_txt

    ani_gif = animation.FuncAnimation(
        fig_gif, update_gif,
        frames=len(states_gif),
        interval=1000/fps,
        blit=True,
        repeat=True,
    )

    ani_gif.save("/tmp/landing3.gif", writer="pillow", fps=fps)
    plt.close(fig_gif)

    mo.image(src="/tmp/landing3.gif")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Définition de nouvelles fonctions, cette fois paramétrées.
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    def controled_landing(x0, vx0, y0_init, vy0, theta0, omega0, phi_control):

        d = y0_init
        c = vy0

        A = np.array([[125, 25],
                      [75,  10]])

        b_vec = np.array([1 - 5*c - d, -c])
        a, b = np.linalg.solve(A, b_vec)

        def f_control(t):
            yddot = 6*a*t + 2*b
            return M * (yddot + g)

        t_span = [0.0, 5.0]

        y0 = [x0, vx0, y0_init, vy0, theta0, omega0]

        def f_phi(t, y):
            return np.array([f_control(t), phi_control])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(0, 5, 1000)
        Y = sol(t)

        plt.figure(figsize=(12,6))

        # x(t)
        plt.subplot(2, 3, 1)
        plt.plot(t, Y[0], label=r"$x(t)$")
        plt.axhline(0, color="grey", ls="--")
        plt.title("x(t)")
        plt.grid(True)
        plt.legend()

        # vx(t)
        plt.subplot(2, 3, 2)
        plt.plot(t, Y[1], label=r"$\dot{x}(t)$", color="orange")
        plt.axhline(0, color="grey", ls="--")
        plt.title("vx(t)")
        plt.grid(True)
        plt.legend()

        # y(t)
        plt.subplot(2, 3, 3)
        plt.plot(t, Y[2], label=r"$y(t)$", color="blue")
        plt.axhline(l/2, color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("y(t)")
        plt.grid(True)
        plt.legend()

        # vy(t)
        plt.subplot(2, 3, 4)
        plt.plot(t, Y[3], label=r"$\dot{y}(t)$", color="green")
        plt.axhline(0, color="grey", ls="--")
        plt.title("vy(t)")
        plt.grid(True)
        plt.legend()

        # theta(t)
        plt.subplot(2, 3, 5)
        plt.plot(t, Y[4], label=r"$\theta(t)$", color="purple")
        plt.axhline(0, color="grey", ls="--")
        plt.title("theta(t)")
        plt.grid(True)
        plt.legend()

        # force
        plt.subplot(2, 3, 6)
        plt.plot(t, f_control(t), label=r"$f(t)$", color="red")
        plt.axhline(M*g, color="grey", ls="--")
        plt.title("f(t)")
        plt.grid(True)
        plt.legend()

        plt.suptitle("Controlled Landing", fontsize=14)
        plt.tight_layout()

        # checks
        Y_final = sol(5.0)
        print("y(5) =", Y_final[2], "target:", l/2)
        print("vy(5) =", Y_final[3], "target:", 0)

        return plt.gcf() 
    
    controled_landing(0.0, 0.0, 10.0, -2.0, 0.0, 0.0, 0)
    return


if __name__ == "__main__":
    app.run()
