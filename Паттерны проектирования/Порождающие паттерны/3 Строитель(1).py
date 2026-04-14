from abc import ABC, abstractmethod

# Класс Resume
class Resume:
    def __init__(
        self,
        name: str,
        email: str,
        phone: str = "",
        summary: str = "",
        experience: list[dict] = None,
        education: list[dict] = None,
        skills: list[str] = None,
        languages: list[str] = None,
        certifications: list[str] = None,
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.summary = summary
        self.experience = experience or []
        self.education = education or []
        self.skills = skills or []
        self.languages = languages or []
        self.certifications = certifications or []

    def __str__(self) -> str:
        return (
            f"=== {self.name} ===\n"
            f"Email: {self.email}\n"
            f"Навыки: {', '.join(self.skills)}\n"
            f"Опыт: {len(self.experience)} позиций"
        )

# Интерфейс строителя
class ResumeBuilder(ABC):
    @abstractmethod
    def set_name(self, name: str):
        pass

    @abstractmethod
    def set_contacts(self, email: str, phone: str = ""):
        pass

    @abstractmethod
    def add_experience(self, company: str, years: int):
        pass

    @abstractmethod
    def add_education(self, degree: str, school: str):
        pass

    @abstractmethod
    def add_skill(self, skill: str):
        pass

    @abstractmethod
    def build(self) -> Resume:
        pass

# Конкретный строитель
class ConcreteResumeBuilder(ResumeBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._name = ""
        self._email = ""
        self._phone = ""
        self._summary = ""
        self._experience = []
        self._education = []
        self._skills = []
        self._languages = []
        self._certifications = []

    def set_name(self, name: str):
        self._name = name
        return self

    def set_contacts(self, email: str, phone: str = ""):
        self._email = email
        self._phone = phone
        return self

    def add_experience(self, company: str, years: int):
        self._experience.append({"company": company, "years": years})
        return self

    def add_education(self, degree: str, school: str):
        self._education.append({"degree": degree, "school": school})
        return self

    def add_skill(self, skill: str):
        self._skills.append(skill)
        return self

    def add_language(self, language: str):
        self._languages.append(language)
        return self

    def add_certification(self, cert: str):
        self._certifications.append(cert)
        return self

    def build(self) -> Resume:
        resume = Resume(
            name=self._name,
            email=self._email,
            phone=self._phone,
            summary=self._summary,
            experience=self._experience,
            education=self._education,
            skills=self._skills,
            languages=self._languages,
            certifications=self._certifications,
        )
        self.reset()
        return resume

# Директор
class ResumeDirector:
    def __init__(self, builder: ResumeBuilder):
        self.builder = builder

    def build_standard_resume(self, name: str, email: str) -> Resume:
        return (
            self.builder
            .set_name(name)
            .set_contacts(email)
            .add_skill("Коммуникабельность")
            .add_skill("Работа в команде")
            .build()
        )

    def build_extended_resume(self, name: str, email: str, phone: str) -> Resume:
        return (
            self.builder
            .set_name(name)
            .set_contacts(email, phone)
            .add_experience("ООО Ромашка", 2)
            .add_education("Бакалавр", "МГУ")
            .add_skill("Python")
            .add_skill("SQL")
            .add_skill("Docker")
            .add_language("Английский (B2)")
            .add_certification("AWS Certified Developer")
            .build()
        )

# Использование
builder = ConcreteResumeBuilder()
director = ResumeDirector(builder)

standard = director.build_standard_resume("Анна Иванова", "anna@example.com")
print("=== Стандартное резюме ===")
print(standard)

extended = director.build_extended_resume("Анна Иванова", "anna@example.com", "+7-900-000-00-00")
print("\n=== Расширенное резюме ===")
print(extended)