import tkinter as tk
from tkinter import ttk, messagebox
import psycopg2

# Database connection setup
def connect_to_database():
    try:

        conn = psycopg2.connect(
            dbname="librarydb",
            user="postgres",
            password="database123",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not connect to the database: {e}")
        return None

# Initialize the main window
root = tk.Tk()
root.title("Library Management System")
root.geometry("1200x650")
root.configure(bg="#E6F3F3")

# Sidebar Frames
sidebar_frame = tk.Frame(root, bg="#FFFFFF", width=250)
sidebar_frame.pack(side="left", fill="y")
sidebar_frame.pack_propagate(False)

# Top logo and title section
top_frame = tk.Frame(sidebar_frame, bg="#FFFFFF")
top_frame.pack(pady=(20, 10))
# tk.Image

# Selected indicator frame
selected_indicator_frame = tk.Frame(sidebar_frame, bg="#0056b3", width=5, height=40)
selected_indicator_frame.place(x=0, y=45)  # Start with the first button selected

# Helper function to update selected item indicator
def select_sidebar_item(y_position):
    selected_indicator_frame.place(y=y_position)

# Function to create sidebar buttons
def create_nav_button(text, command, y_position):
    label = tk.Label(
        sidebar_frame,
        text=text,
        font=("Poppins", 14),
        bg="#FFFFFF",
        fg="#2E3A59",
        cursor="hand2"
    )
    label.bind("<Button-1>", lambda e: [command(), select_sidebar_item(y_position)])
    label.bind("<Enter>", lambda e: label.config(fg="#0056b3"))  # Change color on hover
    label.bind("<Leave>", lambda e: label.config(fg="#2E3A59"))  # Revert color on leave
    label.pack(fill="x", padx=10, pady=20)

# Create sidebar buttons
create_nav_button("Add User", lambda: load_buttons(), 45)
create_nav_button("Add Book", lambda: load_form("Add Book"), 110)
create_nav_button("Record", lambda: record_buttons(), 180)
create_nav_button("Retrieve", lambda: retrieve_buttons(), 250)

button_width = 15  # Fixed width
button_height = 1

# Main Content Frame
content_frame = tk.Frame(root, bg="#C8E6E5", padx=20, pady=20)
content_frame.pack(side="right", fill="both", expand=True)

def record_buttons():
    for widget in content_frame.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(content_frame, width=700, height=500, bg="#C8E6E5", highlightthickness=0)
    canvas.pack(pady=20)

    # Create rounded rectangle background
    rect_x0, rect_y0, rect_x1, rect_y1 = 20, 10, 680, 490
    corner_radius = 40
    
    # Create rounded corners
    canvas.create_arc(rect_x0, rect_y0, rect_x0 + 2*corner_radius, rect_y0 + 2*corner_radius, start=90, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y0, rect_x1, rect_y0 + 2*corner_radius, start=0, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x0, rect_y1 - 2*corner_radius, rect_x0 + 2*corner_radius, rect_y1, start=180, extent=90, fill ="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y1 - 2*corner_radius, rect_x1, rect_y1, start=270, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    
    # Create rectangle fills
    canvas.create_rectangle(rect_x0 + corner_radius, rect_y0, rect_x1 - corner_radius, rect_y1, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_rectangle(rect_x0, rect_y0 + corner_radius, rect_x1, rect_y1 - corner_radius, fill="#E6F3F3", outline="#E6F3F3")

    # Add buttons
    add_lend_button = tk.Button(content_frame, text="Lend", font=("Arial", 24), bg="#C8E6E5", width=button_width , height=button_height , command=lambda: load_form("Lend"))
    add_return_button = tk.Button(content_frame, text="Return", font=("Arial", 24), bg="#C8E6E5", width=button_width , height=button_height , command=lambda: load_form("Return"))

    # Center the buttons in the canvas
    canvas.create_window(345, 200, window=add_lend_button)
    canvas.create_window(345, 300, window=add_return_button)

def retrieve_buttons():
    for widget in content_frame.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(content_frame, width=700, height=500, bg="#C8E6E5", highlightthickness=0)
    canvas.pack(pady=20)

    # Create rounded rectangle background
    rect_x0, rect_y0, rect_x1, rect_y1 = 20, 10, 680, 490
    corner_radius = 40
    
    # Create rounded corners
    canvas.create_arc(rect_x0, rect_y0, rect_x0 + 2*corner_radius, rect_y0 + 2*corner_radius, start=90, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y0, rect_x1, rect_y0 + 2*corner_radius, start=0, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x0, rect_y1 - 2*corner_radius, rect_x0 + 2*corner_radius, rect_y1, start=180, extent=90, fill ="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y1 - 2*corner_radius, rect_x1, rect_y1, start=270, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    
    # Create rectangle fills
    canvas.create_rectangle(rect_x0 + corner_radius, rect_y0, rect_x1 - corner_radius, rect_y1, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_rectangle(rect_x0, rect_y0 + corner_radius, rect_x1, rect_y1 - corner_radius, fill="#E6F3F3", outline="#E6F3F3")

    # Add buttons
    add_user_search_button = tk.Button(content_frame, text="User Info", font=("Arial", 24), bg="#C8E6E5",width=button_width , height=button_height , command=lambda: load_form("User Info"))
    add_book_search_button = tk.Button(content_frame, text="Book Info", font=("Arial", 24), bg="#C8E6E5",width=button_width , height=button_height , command=lambda: load_form("Book Info"))
    add_record_button = tk.Button(content_frame, text="Record Info", font=("Arial", 24), bg="#C8E6E5",width=button_width , height=button_height , command=lambda: load_form("Record Info"))

    # Center the buttons in the canvas
    canvas.create_window(345, 150, window=add_user_search_button)
    canvas.create_window(345, 250, window=add_book_search_button)
    canvas.create_window(345, 350, window=add_record_button)

def load_buttons():
    for widget in content_frame.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(content_frame, width=700, height=500, bg="#C8E6E5", highlightthickness=0)
    canvas.pack(pady=20)

    # Create rounded rectangle background
    rect_x0, rect_y0, rect_x1, rect_y1 = 20, 10, 680, 490
    corner_radius = 40
    
    # Create rounded corners
    canvas.create_arc(rect_x0, rect_y0, rect_x0 + 2*corner_radius, rect_y0 + 2*corner_radius, start=90, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y0, rect_x1, rect_y0 + 2*corner_radius, start=0, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x0, rect_y1 - 2*corner_radius, rect_x0 + 2*corner_radius, rect_y1, start=180, extent=90, fill ="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y1 - 2*corner_radius, rect_x1, rect_y1, start=270, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    
    # Create rectangle fills
    canvas.create_rectangle(rect_x0 + corner_radius, rect_y0, rect_x1 - corner_radius, rect_y1, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_rectangle(rect_x0, rect_y0 + corner_radius, rect_x1, rect_y1 - corner_radius, fill="#E6F3F3", outline="#E6F3F3")

    # Add buttons
    add_student_button = tk.Button(content_frame, text="Add Student", font=("Arial", 24), bg="#C8E6E5", width=button_width , height=button_height , command=lambda: load_form("Add Student"))
    add_teacher_button = tk.Button(content_frame, text="Add Faculty", font=("Arial", 24), bg="#C8E6E5",width=button_width , height=button_height , command=lambda: load_form("Add Faculty"))

    # Center the buttons in the canvas
    canvas.create_window(345, 200, window=add_student_button)
    canvas.create_window(345, 300, window=add_teacher_button)

# Create entries with consistent styling and layout
def create_entries(parent_frame, labels, bg_color="#E6F3F3"):
    entries = {}
    for label_text in labels:
        # Create a row frame for each entry
        row_frame = tk.Frame(parent_frame, bg=bg_color)
        row_frame.pack(fill="x", pady=5)

        # Label configuration
        label = tk.Label(
            row_frame, 
            text=label_text,
            font=("Poppins", 12), 
            bg=bg_color, 
            anchor="e",
            width=20  # Fixed width for consistent alignment
        )
        label.pack(side="left", padx=(0, 10))

        # Check if the label requires a combo box
        if label_text in ["Department:", "Year:", "Book Category:", "Lending Status:"]:
            # Define options for combo boxes
            options = {
                "Department:": ["Computer Science", "Electronics", "Electrical","Mechanical","Robotics","Civil","B.Arch"],
                "Year:": ["1", "2", "3", "4", "5"],
                "Book Category:": ["Novel", "Story", "Poem", "Biography", "Drama", "Philosophy", "Autobiography", "Children’s Literature", "Textbook", "Research", "Reference"],
                "Lending Status:": ["Available", "Not Available"]
            }
        
            entry = ttk.Combobox(row_frame, values=options[label_text], state="readonly")
            entry.set("")  # Default text

        elif label_text in ["Publish Date:", "Issue Date:"]:
            entry = tk.Entry(row_frame, width=30, font=("Arial", 10))
            entry.insert(0, "YYYY-MM-DD")  # Default text
            entry.config(fg="grey")  # Set text color to grey

            # Define event handlers for entry focus
            def on_entry_click(event):
                if entry.get() == "YYYY-MM-DD":
                    entry.delete(0, "end")  # Delete default text
                    entry.config(fg="black")  # Change text color to black

            def on_focusout(event):
                if entry.get() == "":
                    entry.insert(0, "YYYY-MM-DD")  # Reset to default text
                    entry.config(fg="grey")  # Change text color to grey

            entry.bind("<FocusIn>", on_entry_click)
            entry.bind("<FocusOut>", on_focusout)

        else:
            # Entry configuration with custom style
            entry = ttk.Entry(
                row_frame, 
                width=30, 
                style="Custom.TEntry"
            )

        entry.pack(side="left", fill="x", expand=True, padx=(0, 20))
        
        # Store entries with their corresponding labels
        entries[label_text] = entry

    return entries

# In your style configuration section
style = ttk.Style()
style.configure("Custom.TEntry", 
                font=("Poppins", 12),
                padding=5,
                relief="flat")


# Modify the form creation function to use the new create_entries method
def create_form(form_title, labels):
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Canvas for the rounded rectangle background
    canvas = tk.Canvas(content_frame, width=700, height=500, bg="#C8E6E5", highlightthickness=0)
    canvas.pack(pady=20)

    # Create rounded rectangle background
    rect_x0, rect_y0, rect_x1, rect_y1 = 20, 10, 680, 490
    corner_radius = 40
    
    # Create rounded corners
    canvas.create_arc(rect_x0, rect_y0, rect_x0 + 2*corner_radius, rect_y0 + 2*corner_radius, start=90, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y0, rect_x1, rect_y0 + 2*corner_radius, start=0, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x0, rect_y1 - 2*corner_radius, rect_x0 + 2*corner_radius, rect_y1, start=180, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_arc(rect_x1 - 2*corner_radius, rect_y1 - 2*corner_radius, rect_x1, rect_y1, start=270, extent=90, fill="#E6F3F3", outline="#E6F3F3")
    
    # Create rectangle fills
    canvas.create_rectangle(rect_x0 + corner_radius, rect_y0, rect_x1 - corner_radius, rect_y1, fill="#E6F3F3", outline="#E6F3F3")
    canvas.create_rectangle(rect_x0, rect_y0 + corner_radius, rect_x1, rect_y1 - corner_radius, fill="#E6F3F3", outline="#E6F3F3")

    # Inside form content
    form_content = tk.Frame(canvas, bg="#E6F3F3")
    form_content.place(relx=0.5, rely=0.5, anchor="center")

    # Add form title
    tk.Label(
        form_content, 
        text=form_title, 
        font=("Poppins", 16, "bold"), 
        bg="#E6F3F3"
    ).pack(pady=(0, 20))

    # Create entries using the new method
    entries = create_entries(form_content, labels, bg_color="#E6F3F3")

    # Submit button
    if form_title == "Record Info":
        submit_button = tk.Button(
            form_content, 
            text="Search", 
            bg="#2E3A59", 
            fg="white", 
            font=("Poppins", 12), 
            command=lambda: retrieve_data(entries)
        )
    elif form_title == "User Info":
        submit_button = tk.Button(
            form_content, 
            text="Search", 
            bg="#2E3A59", 
            fg="white", 
            font=("Poppins", 12), 
            command=lambda: user_retrieve_data(entries)
        )
    elif form_title == "Book Info":
        submit_button = tk.Button(
            form_content, 
            text="Search", 
            bg="#2E3A59", 
            fg="white", 
            font=("Poppins", 12), 
            command=lambda: book_retrieve_data(entries)
        )
    else:
        submit_button = tk.Button(
            form_content, 
            text="Submit", 
            bg="#2E3A59", 
            fg="white", 
            font=("Poppins", 12), 
            command=lambda: submit_form_data(form_title, entries)
        )
    submit_button.pack(pady=20)

    return entries

# Load form based on selected option
def load_form(form_type):
    # Define form labels based on type
    form_labels = {
        "Add Student": [
            "Name:","Admission No:","Year:","Roll no:",
            "Department:", "Email Id:", "Mobile Number:"
        ],
        "Add Faculty": [
            "Name:","Faculty Id:","Designation:",
            "Department:", "Email Id:", "Mobile Number:"
        ],
        "Add Book": [
            "Title:", "Author:", 
            "Book Category:", "Edition:","Publisher:","Publish Date:"
        ],
        "Lend": [
            "User Id:", "Book Id:","Book Damage:"
        ],
        "Return":[
             "User Id:", "Book Id:", "Issue Date:", "Return Damage:", "Fine Amount:",
        ],
        "Record Info": [
            "Search by User Id:", "Search by Book Id:", "Search by Date:"
        ],
        "User Info": [
            "Search by User Id:", "Search by User Name:"
        ],
        "Book Info": [
            "Search by Book Id:" , "Search by Title:"
        ]
    }
    
    # Create form with appropriate labels
    create_form(form_type, form_labels.get(form_type, []))

# Data submission function
def submit_form_data(form_type, entries):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()

            if form_type == "Add Faculty":
                name = entries["Name:"].get()
                department = entries["Department:"].get()
                email = entries["Email Id:"].get()
                mobile_number = entries["Mobile Number:"].get()
                faculty_id = entries["Faculty Id:"].get()
                design = entries["Designation:"].get()

                # Insert into library_user without user_id
                query = """
                INSERT INTO library_user (
                    user_name, department, email, mobile_number
                ) VALUES (%s, %s, %s, %s) RETURNING user_id;
                """
                data = (name, department, email, mobile_number)
                
                cursor.execute(query, data)
                user_id = cursor.fetchone()[0]  
                conn.commit() 

                # Insert into faculty using the generated user_id
                query_faculty = """
                INSERT INTO faculty (
                    user_id, faculty_id, designation
                ) VALUES (%s, %s, %s)
                """
                data_faculty = (user_id, faculty_id, design)

                cursor.execute(query_faculty, data_faculty)
                conn.commit() 

                # Show success message with assigned user ID
                messagebox.showinfo("Success", f"Faculty data added successfully.\nAssigned User ID: {user_id}")

            elif form_type == "Add Student":
                name = entries["Name:"].get()
                department = entries["Department:"].get()
                email = entries["Email Id:"].get()
                mobile_number = entries["Mobile Number:"].get()
                roll_no = entries["Roll no:"].get()
                admission_no = entries["Admission No:"].get()
                student_year = entries["Year:"].get()

                # Insert into library_user without user_id
                query = """
                INSERT INTO library_user (
                    user_name, department, email, mobile_number
                ) VALUES (%s, %s, %s, %s) RETURNING user_id;
                """
                data = (name, department, email, mobile_number)
                
                cursor.execute(query, data)
                user_id = cursor.fetchone()[0]  
                conn.commit() 

                # Insert into student using the generated user_id
                query_student = """
                INSERT INTO student (
                    user_id, roll_no, admission_no, student_year
                ) VALUES (%s, %s, %s, %s)
                """
                data_student = (user_id, roll_no, admission_no, student_year)

                cursor.execute(query_student, data_student)
                conn.commit() 

                # Show success message with assigned user ID
                messagebox.showinfo("Success", f"Student data added successfully.\nAssigned User ID: {user_id}")

            elif form_type == "Add Book":
                try:
                    query_book = """
                    INSERT INTO book (
                        title, author, category, edition
                    ) VALUES (%s, %s, %s, %s) RETURNING book_id;
                    """
                    data_book = (
                        entries["Title:"].get(),
                        entries["Author:"].get(),
                        entries["Book Category:"].get(),
                        entries["Edition:"].get()
                    )
                    
                    cursor.execute(query_book, data_book)
                    book_id = cursor.fetchone()[0] 
                    conn.commit() 

                    query_publish = """
                    INSERT INTO publish (
                        title, author, edition, publisher, publish_date
                    ) VALUES (%s, %s, %s, %s, %s);
                    """
                    data_publish = (
                        entries["Title:"].get(),
                        entries["Author:"].get(),
                        entries["Edition:"].get(),
                        entries["Publisher:"].get(),
                        entries["Publish Date:"].get()
                    )
                    cursor.execute(query_publish, data_publish)
                    conn.commit() 

                    messagebox.showinfo("Success", f"Book data added successfully,\nAssigned Book ID: {book_id}")

                except Exception as e:
                    messagebox.showerror("Error", f"Could not add data: {e}")


            elif form_type == "Lend":
                query_check_status = """
                    SELECT lending_status FROM book 
                    WHERE book_id = %s;
                """
                cursor.execute(query_check_status, (entries["Book Id:"].get(),))
                result = cursor.fetchone()

                if result and result[0] == 'Available':
                    query_borrow = """
                        INSERT INTO borrow (
                            user_id, book_id, book_damage
                        ) VALUES (%s, %s, %s)
                    """
                    data_borrow = (
                        entries["User Id:"].get(),
                        entries["Book Id:"].get(),
                        entries["Book Damage:"].get()
                    )
                    cursor.execute(query_borrow, data_borrow)
                    conn.commit()

                    # Update the book's lending status to 'Not Available'
                    query_book = """
                        UPDATE book 
                        SET lending_status = 'Not Available' 
                        WHERE book_id = %s;
                    """
                    cursor.execute(query_book, (entries["Book Id:"].get(),))
                    conn.commit()

                    messagebox.showinfo("Success", "Lend status added successfully")
                else:
                    # If the book is not available, show a warning message
                    messagebox.showwarning("Warning", "The book is currently not available for lending.")

            elif form_type == "Return":
                query = """
                    UPDATE borrow 
                    SET return_damage = %s, fine_amount = %s, return_date = CURRENT_DATE
                    WHERE user_id = %s AND book_id = %s AND issue_date = %s;
                """
                data = (
                    entries["Return Damage:"].get(),
                    entries["Fine Amount:"].get(),
                    entries["User Id:"].get(),
                    entries["Book Id:"].get(),
                    entries["Issue Date:"].get()
                )

                try:
                    cursor.execute(query, data)
                    conn.commit()  

                    query_book = """
                        UPDATE book 
                        SET lending_status = 'Available' WHERE book_id = %s;
                    """
                    data_book = (entries["Book Id:"].get(),)  # Create a single-element tuple

                    cursor.execute(query_book, data_book)
                    conn.commit()  # Commit the changes to the book table

                    messagebox.showinfo("Success", "Return status added successfully")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not update return status: {e}")

            else:
                messagebox.showinfo("Info", "Invalid form type")

            # Clear the form entries after successful submission
            for entry in entries.values():
                if isinstance(entry, tk.Entry):
                    entry.delete(0, tk.END)  # Clear the entry field
                if isinstance(entry, tk.ttk.Combobox):
                    entry.set("")  # Clear the combobox

        except Exception as e:
            messagebox.showerror("Error", f"Could not add data: {e}")
        finally:
            conn.close()

# Retrieve book retrieval function
def book_retrieve_data(search_criteria):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Prepare search conditions
            search_conditions = []
            search_values = []
            
            # Check each search criteria
            if search_criteria.get("Search by Book Id:").get():
                search_conditions.append("b.book_id = %s")
                search_values.append(search_criteria["Search by Book Id:"].get())
            
            if search_criteria.get("Search by Title:").get():
                search_conditions.append("b.title = %s")
                search_values.append(search_criteria["Search by Title:"].get())
        
            # If no search criteria provided
            if not search_conditions:
                messagebox.showwarning("Warning", "Please provide at least one search criteria")
                return
            
            # Construct the query with joins to get comprehensive information
            query = """
            SELECT 
                b.book_id,
                b.title,
                b.author,
                b.category,
                b.lending_status,
                b.edition,
                p.publisher,
                p.publish_date
            FROM book b 
            JOIN publish p ON b.title = p.title
            WHERE """ + " AND ".join(search_conditions)
            
            # Execute the query
            cursor.execute(query, tuple(search_values))
            results = cursor.fetchall()
            
            # Define column names for user results
            column_names = [
                "Book ID", "Title", "Author", 
                "Category", "Lending Status", "Edition", 
                "Publisher", "Publish Date"
            ]
            
            # Display results
            display_search_results(results, column_names)
        
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data: {e}")
        finally:
            conn.close()

# Retrieve user Data retrieval function
def user_retrieve_data(search_criteria):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Prepare search conditions
            search_conditions = []
            search_values = []
            
            # Check each search criteria
            if search_criteria.get("Search by User Id:").get():
                search_conditions.append("u.user_id = %s")
                search_values.append(search_criteria["Search by User Id:"].get())
            
            if search_criteria.get("Search by User Name:").get():
                search_conditions.append("u.user_name = %s")
                search_values.append(search_criteria["Search by User Name:"].get())
        
            # If no search criteria provided
            if not search_conditions:
                messagebox.showwarning("Warning", "Please provide at least one search criteria")
                return
            
            # Construct the query to check if the user is a student or faculty
            query = """
            SELECT 
                u.user_id, 
                u.user_name,
                u.department,
                u.email,
                u.mobile_number,
                s.admission_no,
                s.student_year,
                s.roll_no,
                f.faculty_id,
                f.designation,
                CASE 
                    WHEN s.user_id IS NOT NULL THEN 'Student'
                    WHEN f.user_id IS NOT NULL THEN 'Faculty'
                    ELSE 'Unknown'
                END AS user_type
            FROM library_user u 
            LEFT JOIN student s ON u.user_id = s.user_id 
            LEFT JOIN faculty f ON u.user_id = f.user_id 
            WHERE """ + " AND ".join(search_conditions)
            
            # Execute the query
            cursor.execute(query, tuple(search_values))
            results = cursor.fetchall()
            
            # Process results to show only relevant information
            processed_results = []
            column_names = []
            for row in results:
                user_type = row[-1]  # Get the user type from the last column
                if user_type == 'Student':
                    # Extract only student-related columns
                    processed_row = row[:8]  # Indices 0 to 7 (user_id to roll_no)
                    processed_results.append(processed_row)
                    column_names = ["User  ID", "User  Name", "Department", "Email", "Mobile Number", "Admission No", "Student Year", "Roll No"]
                elif user_type == 'Faculty':
                    # Extract only faculty-related columns
                    processed_row = row[0:5] + row[8:10]  # Indices 0 to 4 (user_id to mobile_number) + indices 8 to 9 (faculty_id, designation)
                    processed_results.append(processed_row)
                    column_names = ["User  ID", "User  Name", "Department", "Email", "Mobile Number", "Faculty ID", "Designation"]

            # Display results
            if processed_results:
                display_search_results(processed_results, column_names)
            else:
                messagebox.showinfo("Info", "No results found for the given criteria.")
        
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data: {e}")
        finally:
            conn.close()

# Retrieve Data retrieval function
def retrieve_data(search_criteria):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()
            
            # Prepare search conditions
            search_conditions = []
            search_values = []
            
            # Check each search criteria
            if search_criteria.get("Search by User Id:").get():
                search_conditions.append("b.user_id = %s")
                search_values.append(search_criteria["Search by User Id:"].get())
            
            if search_criteria.get("Search by Book Id:").get():
                search_conditions.append("b.book_id = %s")
                search_values.append(search_criteria["Search by Book Id:"].get())
            
            if search_criteria.get("Search by Date:").get():
                search_conditions.append("b.issue_date = %s")
                search_values.append(search_criteria["Search by Date:"].get())
            
            # If no search criteria provided
            if not search_conditions:
                messagebox.showwarning("Warning", "Please provide at least one search criteria")
                return
            
            # Construct the query with joins to get comprehensive information
            query = """
            SELECT 
                b.user_id, 
                lu.user_name,
                lu.department,
                b.book_id, 
                bk.title, 
                bk.author,
                b.issue_date, 
                b.due_date, 
                b.return_date, 
                b.book_damage,
                b.fine_amount
            FROM borrow b 
            LEFT JOIN library_user lu ON b.user_id = lu.user_id 
            LEFT JOIN book bk ON b.book_id = bk.book_id 
            WHERE """ + " AND ".join(search_conditions)
            
            # Execute the query
            cursor.execute(query, tuple(search_values))
            results = cursor.fetchall()
            
            # Define column names for book results
            column_names = [
                "User   ID", "User   Name", "Department", 
                "Book ID", "Title", "Author", 
                "Issue Date", "Due Date", "Return Date", 
                "Book Damage", "Fine Amount"
            ]
            
            # Display results
            display_search_results(results, column_names)
        
        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve data: {e}")
        finally:
            conn.close()

def display_search_results(results, column_names):
    # Create a new window to display results
    results_window = tk.Toplevel()
    results_window.title("Search Results")
    results_window.geometry("1200x500")
    
    # Create Treeview to display results
    tree = ttk.Treeview(results_window, columns=column_names, show="headings")
    
    # Define headings and configure columns
    for heading in column_names:
        tree.heading(heading, text=heading)
        tree.column(heading, width=100, anchor="center")
    
    # Insert results
    for result in results:
        tree.insert("", "end", values=result)
    
    # Add scrollbar
    scrollbar = ttk.Scrollbar(results_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    
    # Pack widgets
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # If no results found
    if not results:
        tk.Label(results_window, text="No results found", font=("Poppins", 14)).pack(pady=20)

# Run the Tkinter main loop
root.mainloop()