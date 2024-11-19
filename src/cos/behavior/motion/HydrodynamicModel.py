#!/usr/bin/python
# Filename: HydrodynamicModel.py
# Description: Implementation of the HydrodynamicModel class

import numpy as np


class PID_controller:
    def __init__(self, integrator_low, integrator_high, kp, kd, ki, sampling_time):
        """ Constructor
        Arguments
        	integrator_low -- #TODO
        	integrator_high -- #TODO
        	kp -- #TODO
        	kd -- #TODO
        	ki -- #TODO
        	sampling_time -- #TODO
        """
        self.prev_error = 0
        self.integrator_error = 0
        self.int_lo = integrator_low
        self.int_hi = integrator_high
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.dt = sampling_time

    def controller_law(self, measured_state, desired_state):
        """ #TODO: controller_law
        Arguments
        	measured_state -- #TODO
        	desired_state -- #TODO
        """
        error = desired_state - measured_state
        d_error = (error - self.prev_error) / self.dt
        error_i = self.integrator_error + error * self.dt
        # error_i = self.sat(error_i)
        self.prev_error = error
        self.integrator_error = error_i
        return error * self.kp + d_error * self.kd + error_i * self.ki

    def sat(self, val):
        """ #TODO: sat
        Arguments
        	val -- #TODO
        """
        ''' Saturate the input val such that it remains
        between "low" and "hi"
        '''
        return max(self.int_lo, min(val, self.int_hi))

class Ship:
    def __init__(self, mass, linear_damping_coeff, length, width, dt):
        """ Constructor
        Arguments
        	mass -- #TODO
        	linear_damping_coeff -- #TODO
        	length -- #TODO
        	width -- #TODO
        	dt -- #TODO
        """
        self.mass = mass
        self.moment_of_inertia_z = mass*width*length*length*length/12
        self.lin_damping = linear_damping_coeff
        self.heading_constant = 10

        self.heading_controller = PID_controller(
            integrator_low=-10,
            integrator_high=10,
            kp=1E10, kd=1E12, ki= 10, sampling_time=dt
        )  # controller gains should not be hardcoded
        self.speed_controller = PID_controller(
            integrator_low=-1e15,
            integrator_high=1E15,
            kp=4E9, kd=0, ki=1E8, sampling_time=dt
        )  # controller gains should not be hardcoded


    def dynamics(self, states, speed_ref, wind_speed, heading_ref, time_step):
        """ #TODO: dynamics
        Arguments
        	states -- #TODO
        	speed_ref -- #TODO
        	wind_speed -- #TODO
        	heading_ref -- #TODO
        	time_step -- #TODO
        """
        north_pos = states[0]
        east_pos = states[1]
        yaw_angle = states[2]
        speed = states[3]
        yaw_rate = states[4]

        # Measure states
        heading_measurement = yaw_angle #  perfect heading measurement
        speed_measurement = speed #  perfect speed measurement

        # Calculate control forces
        yaw_torque = self.heading_controller.controller_law(measured_state=heading_measurement, desired_state=heading_ref)
        propulsion_force = self.speed_controller.controller_law(measured_state=speed_measurement, desired_state=speed_ref)

        # Differential equations
        north_position_dot = speed * np.cos(yaw_angle)
        east_position_dot = speed * np.sin(yaw_angle)
        yaw_angle_dot = yaw_rate
        speed_dot = (propulsion_force - self.lin_damping * speed)/self.mass
        yaw_rate_dot = yaw_torque/ self.moment_of_inertia_z

        # Integrate using the Euler´s forward method
        north_pos = north_pos + time_step * north_position_dot
        east_pos = east_pos + time_step * east_position_dot
        yaw_angle = yaw_angle + time_step * yaw_angle_dot
        forward_speed = speed + time_step * speed_dot
        yaw_rate = yaw_rate + time_step * yaw_rate_dot

        return [north_pos, east_pos, yaw_angle, forward_speed, yaw_rate]


if __name__ == '__main__':
        # inititial states
        north = 1
        east = 2
        yaw = 0 * np.pi/180
        yaw_ref = 45 * np.pi/180
        speed = 5
        speed_ref = 7
        yaw_rate = 0
        states = [north, east, yaw, speed, yaw_rate]
        t = 0
        time = [t]
        dt = 0.01



        ship = Ship(mass= 5E10, linear_damping_coeff=500000000, length=20, width=3, dt=dt)

        stored_states = []
        speeds = [states[3]]
        norths = [states[0]]
        easts = [states[1]]
        stored_states.append(states)


        while t<5*60:
            states = ship.dynamics(states=states, wind_speed=2, speed_ref=speed_ref, heading_ref=yaw_ref, time_step=dt)
            stored_states.append(states)
            speeds.append(states[3])
            norths.append(states[0])
            easts.append(states[1])
            t = t + dt
            time.append(t)

        '''
        # Plot
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 8))  # Set the figure size
        plt.plot(easts, norths, linestyle='-')
        plt.title('Ship Position')
        plt.xlabel('East Position')
        plt.ylabel('North Position')
        plt.gca().set_aspect('equal', adjustable='box')  # Set equal aspect ratio
        plt.grid(True)

        plt.figure(2)
        plt.plot(time, speeds)
        plt.title('Forward Speed Over Time')
        plt.xlabel('Time')
        plt.ylabel('Forward Speed')
        plt.grid(True)

        plt.figure(2)
        plt.plot(time, speeds)
        plt.show()
        '''


