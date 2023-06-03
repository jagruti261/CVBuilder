from fpdf import FPDF


class CVBuilder:
    def __init__(self):
        self.cv_data = {}

    def get_personal_info(self):
        print("Personal Information")
        self.cv_data['name'] = input("Name: ")
        self.cv_data['email'] = input("Email: ")
        self.cv_data['phone'] = input("Phone: ")
        self.cv_data['address'] = input("Address: ")

    def get_education(self):
        print("Education")
        self.cv_data['education'] = []
        while True:
            degree = input("Degree: ")
            if not degree:
                break
            institution = input("Institution: ")
            year = input("Year: ")
            self.cv_data['education'].append({'degree': degree, 'institution': institution, 'year': year})

    def get_experience(self):
        print("Experience")
        self.cv_data['experience'] = []
        while True:
            title = input("Title: ")
            if not title:
                break
            company = input("Company: ")
            duration = input("Duration: ")
            self.cv_data['experience'].append({'title': title, 'company': company, 'duration': duration})

    def get_skills(self):
        print("Skills")
        self.cv_data['skills'] = input("Skills: ")

    def generate_cv(self):
        pdf = FPDF()
        pdf.add_page()

        # Header
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, self.cv_data['name'], 0, 1, 'C')
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, self.cv_data['email'], 0, 1, 'C')
        pdf.cell(0, 10, self.cv_data['phone'], 0, 1, 'C')
        pdf.cell(0, 10, self.cv_data['address'], 0, 1, 'C')

        # Education
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Education', 0, 1)
        pdf.set_font('Arial', '', 12)
        for edu in self.cv_data['education']:
            pdf.cell(0, 10, edu['degree'], 0, 1)
            pdf.cell(0, 10, edu['institution'] + ' (' + edu['year'] + ')', 0, 1)

        # Experience
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Experience', 0, 1)
        pdf.set_font('Arial', '', 12)
        for exp in self.cv_data['experience']:
            pdf.cell(0, 10, exp['title'], 0, 1)
            pdf.cell(0, 10, exp['company'] + ' (' + exp['duration'] + ')', 0, 1)

        # Skills
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, 'Skills', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, self.cv_data['skills'], 0, 1)

        pdf.output('cv.pdf')

    def build_cv(self):
        self.get_personal_info()
        self.get_education()
        self.get_experience()
        self.get_skills()
        self.generate_cv()


# Usage
cv_builder = CVBuilder()
cv_builder.build_cv()
