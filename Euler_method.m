function [ output_args ] = Euler_method(n,t_f,X_i)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
X = zeros(n);
t = zeros(n);
X(0) = X_i;
t(0) = 0;
step = t_f/n;
for i = 1:n-1
    X(i)=X(i-1) + (X(i-1)-X(i-1).^3)*step;
    t(i) = t(i-1) + step;
end
plot(t,X)
end

