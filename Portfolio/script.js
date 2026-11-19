document.addEventListener("DOMContentLoaded", () => {
  // 1. Dynamic Footer Year
  const yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // 2. Typing Effect in Hero Section
  const roles = [
    "full-stack web apps.",
    "intelligent AI agents.",
    "real-time chat systems.",
    "scalable CSE solutions."
  ];
  const typedTextEl = document.getElementById("typedText");
  let roleIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  function typeEffect() {
    if (!typedTextEl) return;
    const currentRole = roles[roleIndex];

    if (isDeleting) {
      typedTextEl.textContent = currentRole.substring(0, charIndex - 1);
      charIndex--;
    } else {
      typedTextEl.textContent = currentRole.substring(0, charIndex + 1);
      charIndex++;
    }

    let typeSpeed = isDeleting ? 45 : 90;

    if (!isDeleting && charIndex === currentRole.length) {
      typeSpeed = 1600; // Pause at end of phrase
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      typeSpeed = 400;
    }

    setTimeout(typeEffect, typeSpeed);
  }
  typeEffect();

  // 3. Dark / Light Theme Toggle with LocalStorage
  const themeToggleBtn = document.getElementById("themeToggle");
  const themeIcon = themeToggleBtn.querySelector("i");
  const savedTheme = localStorage.getItem("portfolio-theme");

  if (savedTheme === "light") {
    document.body.classList.add("light-theme");
    themeIcon.classList.replace("fa-sun", "fa-moon");
  }

  themeToggleBtn.addEventListener("click", () => {
    document.body.classList.toggle("light-theme");
    const isLight = document.body.classList.contains("light-theme");

    if (isLight) {
      themeIcon.classList.replace("fa-sun", "fa-moon");
      localStorage.setItem("portfolio-theme", "light");
    } else {
      themeIcon.classList.replace("fa-moon", "fa-sun");
      localStorage.setItem("portfolio-theme", "dark");
    }
  });

  // 4. Mobile Navigation Menu Toggle
  const menuToggleBtn = document.getElementById("menuToggle");
  const navLinks = document.getElementById("navLinks");

  menuToggleBtn.addEventListener("click", () => {
    navLinks.classList.toggle("open");
  });

  // Close mobile menu when a link is clicked
  navLinks.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navLinks.classList.remove("open");
    });
  });

  // 5. Project Category Filter
  const filterButtons = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");

  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      const filterValue = btn.getAttribute("data-filter");

      projectCards.forEach((card) => {
        const category = card.getAttribute("data-category");
        if (filterValue === "all" || category === filterValue) {
          card.classList.remove("hide");
        } else {
          card.classList.add("hide");
        }
      });
    });
  });

  // 6. One-Click Copy Email Button
  const copyEmailBtn = document.getElementById("copyEmailBtn");
  const copyBtnText = document.getElementById("copyBtnText");

  if (copyEmailBtn) {
    copyEmailBtn.addEventListener("click", () => {
      const email = copyEmailBtn.getAttribute("data-email");
      navigator.clipboard.writeText(email).then(() => {
        const originalText = copyBtnText.textContent;
        copyBtnText.textContent = "Email Copied!";
        setTimeout(() => {
          copyBtnText.textContent = originalText;
        }, 2000);
      });
    });
  }

  // 7. Active Nav Highlight on Scroll
  const sections = document.querySelectorAll("section[id]");
  window.addEventListener("scroll", () => {
    const scrollY = window.pageYOffset;

    sections.forEach((section) => {
      const sectionHeight = section.offsetHeight;
      const sectionTop = section.offsetTop - 120;
      const sectionId = section.getAttribute("id");
      const navItem = document.querySelector(`.nav-links a[href="#${sectionId}"]`);

      if (navItem) {
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
          navItem.classList.add("active");
        } else {
          navItem.classList.remove("active");
        }
      }
    });
  });
});