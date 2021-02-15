%% clearing
clc;
clear all;
close all;

f1=input('Enter Carrier Frequency :');
f2=input('Enter Pulse frequency :');
a=1;
t=0:0.005:1;
x=a*sin(2*pi*f1*t);
u=square(2*pi*f2*t);
v=(x.*u)/a;
%% plotting
subplot(3,1,1);
plot(t,x);
grid on;
xlabel("Time ");
ylabel("Amplitude --->");
title("Carrier Wave");
subplot(3,1,2);
plot(t,u); 
grid on;
xlabel("Time ");
ylabel("Amplitude --->");
title("Square Wave");
subplot(3,1,3);
plot(t,v);
grid on;
xlabel("Time ");
ylabel("Amplitude --->");
title("PSK");