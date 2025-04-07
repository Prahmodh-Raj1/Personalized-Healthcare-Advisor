// utils/formatLifestyleText.ts
export interface Section {
    heading: string;
    items: string[];
  }
  
  export const formatText = (text: string): Section[] => {
    const lines = text
      .split("*")
      .map((line) => line.trim())
      .filter((line) => line.length > 0);
  
    const sections: Section[] = [];
    let currentSection: Section | null = null;
  
    lines.forEach((line) => {
      const headingMatch = line.match(/\*\*(.+?)\*\*/);
      if (headingMatch) {
        if (currentSection) sections.push(currentSection);
        currentSection = { heading: headingMatch[1], items: [] };
      } else if (currentSection) {
        currentSection.items.push(line.replace(/\*/g, "").trim());
      }
    });
  
    if (currentSection) sections.push(currentSection);
    return sections;
  };
  