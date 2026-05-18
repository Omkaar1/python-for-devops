# Linux Architecture Notes

## What is Linux?
Linux is a free and open-source operating system that manages communication between computer hardware and software.

---

# Why is Linux used in DevOps?

- Lightweight and stable
- Open-source and highly customizable
- Supports automation and scripting
- Most cloud platforms and production servers run on Linux
- Better performance for servers and applications

---

# How Does Linux Work?

Linux works using different layers that communicate with each other.

Basic flow:

User → Shell → Kernel → Hardware

Example:
```bash
echo Hello
```

Flow explanation:
1. User types a command
2. Shell reads and interprets the command
3. Shell sends the request to the kernel
4. Kernel communicates with hardware
5. Output is returned to the user

This architecture helps Linux efficiently manage system resources and processes.

---

# Linux Architecture

Linux architecture mainly contains the following components:

## 1. Hardware Layer
Physical components of the computer:
- CPU
- RAM
- Disk
- Network devices

---

## 2. Kernel (Heart of Linux)

The kernel is the core part of Linux.

Responsibilities:
- Process management
- Memory management
- Device management
- File system management
- CPU scheduling

The Linux kernel is mostly written in C language.

---

## 3. Shell

The shell acts as an interface between the user and the kernel.

It helps users interact with Linux using human-readable commands instead of low-level programming language.

Popular shells:
- Bash
- Zsh
- Sh

---

## 4. System Libraries

System libraries help applications communicate with the kernel.

They provide predefined functions and APIs to applications.

---

## 5. User Space / Applications

Applications and tools used by users:
- Vim
- Docker
- Nginx
- VS Code
- Htop

Applications cannot directly access hardware.  
They communicate through the kernel.

---

# What is systemd?

`systemd` is the first process that starts after Linux boots.

- Runs with PID 1
- Manages services and background processes
- Handles system startup and service management

Useful command:
```bash
systemctl status nginx
```

---

# Process Management in Linux

Everything in Linux is treated as a process.
Processes are managed by the kernel and systemd.

Useful commands:
```bash
ps aux
top
htop
kill
```

---

# Basic Linux Commands Practiced
```bash
which bash
cd /
ls
cd
pwd
cat
echo
df -h
free -h
touch
vim
htop
wc -l
&
cat /etc/os-release
```

---

# Why This Matters in DevOps

Understanding Linux helps in:
- Troubleshooting services
- Managing servers
- Monitoring CPU and memory
- Understanding logs
- Automating tasks
- Managing production environments

Linux fundamentals are important because most cloud and production systems run on Linux.

#90DaysOfDevOps 🚀