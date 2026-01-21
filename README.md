# uivision-agent

A vision-based GUI automation library for controlling black-box desktop software.

`uivision-agent` enables automated interaction with GUI-only applications
by combining computer vision (OpenCV) with OS-level mouse/keyboard control.
It is designed for scenarios where no official API is available
(e.g. simulation tools, legacy software, proprietary desktop applications).

---

## ✨ Features

- Vision-based UI element detection 
- OS-level mouse and keyboard control
- Robust input committing for unreliable GUI focus
- Visual state monitoring 
- Designed for **black-box software automation**
- Minimal, modular Python API

---

## 🎯 Typical Use Cases

- Automating simulation workflows (CFD / FEA / EM / etc.)
- Parameter sweeping for GUI-only software
- Batch execution and result export
- Research or engineering automation where APIs are unavailable

---

## 📦 Installation (Development)

This project is intended to be used in **editable (development) mode**.

```bash
pip install -e .
