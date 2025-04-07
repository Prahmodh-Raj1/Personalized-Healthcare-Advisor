export function formatSymptomAnalysis(text: string): { heading: string; items: string[] }[] {
    const sections: { heading: string; items: string[] }[] = [];
    const parts = text.split("*").map(part => part.trim()).filter(Boolean);
  
    let currentSection: { heading: string; items: string[] } | null = null;
  
    parts.forEach(part => {
      if (/^[A-Z]/.test(part)) {
        // It's a new heading
        if (currentSection) sections.push(currentSection);
        currentSection = { heading: part.replace(/:$/, ""), items: [] };
      } else if (currentSection) {
        currentSection.items.push(part);
      }
    });
  
    if (currentSection) sections.push(currentSection);
    return sections;
  }
  