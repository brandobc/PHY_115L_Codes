%% Uncertainty in Refractive Index
syms n theta d s
n = (sin(theta)^2*(4*d^2*cos(theta)^2/s^2+1))^(1/2); % Rearranges Eqn 1.6 for n
dndt = diff(n,theta); % Derivative of n with respect to theta
dndd = diff(n,d); % Derivative of n with respect to block thickness
dnds = diff(n,s); % Derivative of n with respect to separation
delt = deg2rad(0.5); % Uncertainty in angle measurements
dels = 0.05; % Uncertainty in separation distance
deld = 0.05; % Uncertainty in block thickness distance
deln = ((dndt*delt)^2 + (dndd*deld)^2 + (dnds*dels)^2)^(1/2);
angle = 12345; % Put values here!!!!!
separation = 12345; % Put values here!!!!
double(subs(subs(subs(deln, theta, deg2rad(angle)), s, separation),d,3.78)) % 3.78 was my block thickness


%% Uncertainty in Critical Angle
% The naming of the angles here is consistent with Figure 6.8
% The uncertainty of theta 2 should be the same as theta 3 (i.e. the
% critical angle)
syms theta1 theta2 n
theta2 = asin(1/n*sin(theta1)); % Solves for theta 2 using Snell's Law
d2d1 = diff(theta2, theta1);  % Derivative of theta 2 with respect to theta 1
del1 = deg2rad(0.5); % Uncertainty in angle measurements
del2 = ((d2d1*del1)^2)^(1/2);
t1 = 12345; % Put the correct angle here!!!
index = 1.514; % Put the correct n here!!!
double(rad2deg(subs(subs(del2,theta1, deg2rad(t1)),n,index)))
