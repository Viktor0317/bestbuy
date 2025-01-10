# Best Buy Store Management System

This is a project created as part of the Masterschool curriculum.

Welcome to the **Best Buy Store Management System**! This Python-based project allows you to manage a store's inventory, process orders, and provide a simple user interface for interactions.

---

## 📜 Features

- **Product Management**:
  - Add, remove, and manage product inventory.
  - Automatically deactivate products with zero inventory.
  
- **Store Management**:
  - View all active products.
  - Display total quantity of items in stock.
  - Process orders and update inventory.

- **User Interface**:
  - Command-line interface to interact with the store:
    - List products.
    - Show total inventory.
    - Place orders.
    - Exit the program.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.6 or higher installed on your system.

### Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Run the project using the `main.py` file:
   ```bash
   python main.py
   ```

---

## 🛠 Project Structure

```plaintext
Best Buy/
├── main.py          # Main user interface and entry point
├── products.py      # Product class for managing individual products
├── store.py         # Store class for managing store operations
├── README.md        # Project documentation
```

---

## 📝 Usage

1. **Run the program**:
   ```bash
   python main.py
   ```

2. Follow the on-screen menu:
   - **1**: List all products in the store.
   - **2**: Show total amount of inventory in the store.
   - **3**: Place an order by selecting products and their quantities.
   - **4**: Quit the program.

---

## 👨‍💻 Example

### Sample Menu:
```plaintext
-------- Store Menu --------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Please choose a number: 3
```

### Placing an Order:
```plaintext
Available Products:
1. MacBook Air M2, Price: $1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: $250, Quantity: 500
3. Google Pixel 7, Price: $500, Quantity: 250

Which product # do you want? 1
What amount do you want? 2
Product added to your list!

Order completed! Total cost: $2900.00
```

---

## 📂 Future Improvements

- Add support for saving and loading store data from a database or file.
- Expand user interface with a graphical UI.
- Implement user authentication for store managers.

---

## 🖋 Authors

- **Nikola Brajkovic** - Initial development

## 🙏 Acknowledgments

Special thanks to Masterschool for providing the guidance and resources for this project.

