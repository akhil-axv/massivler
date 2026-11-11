import ast
import operator
import tkinter as tk
from tkinter import messagebox

_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def safe_calculate(expression: str):
    """Evaluate basic arithmetic without executing arbitrary Python code."""
    tree = ast.parse(expression, mode="eval")

    def visit(node):
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
            return _OPERATORS[type(node.op)](visit(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
            left = visit(node.left)
            right = visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent 10 dan úlken bolmawı kerek.")
            result = _OPERATORS[type(node.op)](left, right)
            if isinstance(result, (int, float)) and abs(result) > 10**100:
                raise ValueError("Nátiyje júdá úlken.")
            return result
        raise ValueError("Tek arifmetikalıq ámellerge ruqsat berilgen.")

    return visit(tree)


def calculate():
    expression = entry.get().strip()
    if not expression:
        messagebox.showinfo("Esaplagish", "Ańlatpanı kiritiń.")
        return

    try:
        result = safe_calculate(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
        messagebox.showerror("Qátelik", str(error))


def main():
    global entry

    root = tk.Tk()
    root.title("Qáwipsiz esaplagish")
    root.geometry("360x180")
    root.resizable(False, False)

    tk.Label(
        root,
        text="Matematikalıq ańlatpanı kiritiń",
        font=("Arial", 12),
    ).pack(pady=(18, 8))

    entry = tk.Entry(root, font=("Arial", 16), justify="right", width=28)
    entry.pack(padx=18, fill="x")
    entry.bind("<Return>", lambda _event: calculate())

    tk.Button(root, text="Esaplaw", command=calculate).pack(pady=14)
    root.mainloop()


if __name__ == "__main__":
    main()
