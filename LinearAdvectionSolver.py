class LinearWave:
    def __init__(self, xi, xf, nx, dx, c, dt, ti, tf, a0):
        """
        :param nx: Number of grid points in space.
        :param dx: Grid spacing.
        :param c: Wave speed (advection speed).
        :param dt: Time step.
        :param t_final: Maximum time for the simulation.
        :param u_initial: Initial condition function (optional). If None, it will use a default wave.
        """
        self.xi = xi
        self.xf = xf
        self.nx = nx
        self.dx = dx
        self.c = c
        self.dt = dt
        self.ti = ti
        self.tf = tf
        self.a = a0  # Wave field
        self.x = np.linspace(0, (nx-1)*dx, nx)  # Spatial grid

        # Initialize wave, either from a user function or a default initial condition
        if u_initial is not None:
            self.u = u_initial(self.x)
        else:
            # Default initial wave: a Gaussian pulse
            self.u = np.exp(-0.5 * ((self.x - 0.5*(nx-1)*dx) / (0.1*(nx-1)*dx))**2)
        
        self.nt = int(t_max / dt)  # Number of time steps
    
    def step(self):
        """
        Perform one time step of the advection equation using a first-order upwind scheme.
        """
        u_new = np.copy(self.u)
        for i in range(1, self.nx):
            u_new[i] = self.u[i] - self.c * self.dt / self.dx * (self.u[i] - self.u[i-1])
        
        self.u = u_new
    
    def run(self):
        """
        Run the simulation over time, performing the specified number of time steps.
        """
        for t in range(self.nt):
            self.step()
            if t % (self.nt // 10) == 0:  # Display some intermediate steps
                self.plot(t)

    def plot(self, t_step):
        """
        Plot the wave at a given time step.
        
        :param t_step: Time step number (for labeling).
        """
        plt.plot(self.x, self.u, label=f"t = {t_step * self.dt:.2f}")
    
    def show_results(self):
        """
        Display the final wave after simulation.
        """
        self.plot(self.nt)
        plt.xlabel("x")
        plt.ylabel("u(x, t)")
        plt.title("Wave Evolution (Advection Equation)")
        plt.legend()
        plt.show()