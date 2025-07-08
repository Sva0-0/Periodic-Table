import tkinter as tk
from tkinter import messagebox

# Map element symbols to their types
ELEMENT_TYPES = {
    # Alkali metals
    'H': 'nonmetal', 'Li': 'alkali', 'Na': 'alkali', 'K': 'alkali', 'Rb': 'alkali', 'Cs': 'alkali', 'Fr': 'alkali',
    # Alkaline earth metals
    'Be': 'alkaline', 'Mg': 'alkaline', 'Ca': 'alkaline', 'Sr': 'alkaline', 'Ba': 'alkaline', 'Ra': 'alkaline',
    # Transition metals
    'Sc': 'transition', 'Ti': 'transition', 'V': 'transition', 'Cr': 'transition', 'Mn': 'transition', 'Fe': 'transition', 'Co': 'transition', 'Ni': 'transition', 'Cu': 'transition', 'Zn': 'transition',
    'Y': 'transition', 'Zr': 'transition', 'Nb': 'transition', 'Mo': 'transition', 'Tc': 'transition', 'Ru': 'transition', 'Rh': 'transition', 'Pd': 'transition', 'Ag': 'transition', 'Cd': 'transition',
    'Hf': 'transition', 'Ta': 'transition', 'W': 'transition', 'Re': 'transition', 'Os': 'transition', 'Ir': 'transition', 'Pt': 'transition', 'Au': 'transition', 'Hg': 'transition', 'Rf': 'transition', 'Db': 'transition', 'Sg': 'transition', 'Bh': 'transition', 'Hs': 'transition', 'Mt': 'transition', 'Ds': 'transition', 'Rg': 'transition', 'Cn': 'transition',
    # Post-transition metals
    'Al': 'post-transition', 'Ga': 'post-transition', 'In': 'post-transition', 'Sn': 'post-transition', 'Tl': 'post-transition', 'Pb': 'post-transition', 'Bi': 'post-transition', 'Nh': 'post-transition', 'Fl': 'post-transition', 'Mc': 'post-transition', 'Lv': 'post-transition',
    # Metalloids
    'B': 'metalloid', 'Si': 'metalloid', 'Ge': 'metalloid', 'As': 'metalloid', 'Sb': 'metalloid', 'Te': 'metalloid', 'Po': 'metalloid',
    # Nonmetals
    'C': 'nonmetal', 'N': 'nonmetal', 'O': 'nonmetal', 'P': 'nonmetal', 'S': 'nonmetal', 'Se': 'nonmetal',
    # Halogens
    'F': 'halogen', 'Cl': 'halogen', 'Br': 'halogen', 'I': 'halogen', 'At': 'halogen', 'Ts': 'halogen',
    # Noble gases
    'He': 'noble', 'Ne': 'noble', 'Ar': 'noble', 'Kr': 'noble', 'Xe': 'noble', 'Rn': 'noble', 'Og': 'noble',
    # Lanthanides
    'La': 'lanthanide', 'Ce': 'lanthanide', 'Pr': 'lanthanide', 'Nd': 'lanthanide', 'Pm': 'lanthanide', 'Sm': 'lanthanide', 'Eu': 'lanthanide', 'Gd': 'lanthanide', 'Tb': 'lanthanide', 'Dy': 'lanthanide', 'Ho': 'lanthanide', 'Er': 'lanthanide', 'Tm': 'lanthanide', 'Yb': 'lanthanide', 'Lu': 'lanthanide',
    # Actinides
    'Ac': 'actinide', 'Th': 'actinide', 'Pa': 'actinide', 'U': 'actinide', 'Np': 'actinide', 'Pu': 'actinide', 'Am': 'actinide', 'Cm': 'actinide', 'Bk': 'actinide', 'Cf': 'actinide', 'Es': 'actinide', 'Fm': 'actinide', 'Md': 'actinide', 'No': 'actinide', 'Lr': 'actinide',
}

# Map types to colors
TYPE_COLORS = {
    'alkali':      '#7c2f1c',
    'alkaline':    '#7a5c1e',
    'transition':  '#145c47',
    'post-transition': '#23272a',
    'metalloid':   '#14505c',
    'nonmetal':    '#1a2a40',
    'halogen':     '#2d1c4a',
    'noble':       '#444950',
    'lanthanide':  '#6c2a3a',
    'actinide':    '#2a2a6c',
    'unknown':     '#22242a',
}

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Periodic Table")
        self.root.configure(bg="#111217")
        self.root.geometry("1400x900")
        self.elements = [
            ("H", "Hydrogen", 1, "1.008", "Lightest element, essential for life. Used in stars and the universe's most abundant element. Discovered by Henry Cavendish in 1766. Used in rocket fuel, ammonia production, and hydrogen fuel cells.", 1, 1),
            ("He", "Helium", 2, "4.0026", "Second most abundant element. Used in balloons, cryogenics, and stars. Discovered in the Sun before Earth by Pierre Janssen in 1868. Named after Helios, Greek god of the Sun.", 1, 18),
            ("Li", "Lithium", 3, "6.94", "Soft, silvery metal. Used in batteries, mood-stabilizing drugs, and nuclear fusion. Discovered by Johan August Arfvedson in 1817. Lightest metal on Earth.", 2, 1),
            ("Be", "Beryllium", 4, "9.0122", "Rare, strong, lightweight metal. Used in aerospace, X-ray windows, and gemstones (emeralds). Discovered by Louis Nicolas Vauquelin in 1798. Named after beryl, the mineral containing it.", 2, 2),
            ("B", "Boron", 5, "10.81", "Metalloid. Used in glass, detergents, and as a neutron absorber in nuclear reactors. Discovered by Humphry Davy in 1808. Essential for plant growth and used in borax.", 2, 13),
            ("C", "Carbon", 6, "12.01", "Basis of all known life. Found in diamonds, graphite, and fuels. Forms more compounds than any other element. Known since ancient times. Used in steel, plastics, and organic chemistry.", 2, 14),
            ("N", "Nitrogen", 7, "14.01", "Makes up 78% of Earth's atmosphere. Used in fertilizers, explosives, and as a refrigerant. Discovered by Daniel Rutherford in 1772. Essential for proteins and DNA.", 2, 15),
            ("O", "Oxygen", 8, "16.00", "Essential for respiration. Most abundant element in Earth's crust. Used in water, breathing, and combustion. Discovered by Carl Wilhelm Scheele in 1774. Third most abundant element in universe.", 2, 16),
            ("F", "Fluorine", 9, "19.00", "Most reactive element. Used in toothpaste, Teflon, and uranium enrichment. Discovered by Henri Moissan in 1886. Named after Latin 'fluere' meaning to flow.", 2, 17),
            ("Ne", "Neon", 10, "20.18", "Inert gas. Used in neon signs and high-voltage indicators. Discovered by Sir William Ramsay in 1898. Named from Greek 'neos' meaning new.", 2, 18),
            ("Na", "Sodium", 11, "22.99", "Highly reactive metal. Used in table salt, street lights, and soap making. Discovered by Humphry Davy in 1807. Named after soda (sodium carbonate).", 3, 1),
            ("Mg", "Magnesium", 12, "24.31", "Lightweight metal. Used in fireworks, flares, and as a dietary supplement. Discovered by Joseph Black in 1755. Essential for photosynthesis in plants.", 3, 2),
            ("Al", "Aluminum", 13, "26.98", "Most abundant metal in Earth's crust. Used in cans, foil, airplanes, and construction. Discovered by Hans Christian Ørsted in 1825. Named after alum, the mineral containing it.", 3, 13),
            ("Si", "Silicon", 14, "28.09", "Second most abundant element in Earth's crust. Used in electronics, glass, and solar cells. Discovered by Jöns Jacob Berzelius in 1824. Named after Latin 'silex' meaning flint.", 3, 14),
            ("P", "Phosphorus", 15, "30.97", "Essential for DNA and energy transfer. Used in fertilizers, detergents, and matches. Discovered by Hennig Brand in 1669. Named from Greek 'phosphoros' meaning light-bearer.", 3, 15),
            ("S", "Sulfur", 16, "32.07", "Yellow solid. Used in vulcanized rubber, gunpowder, and as a fungicide. Known since ancient times. Named after Latin 'sulphur'. Essential for amino acids and proteins.", 3, 16),
            ("Cl", "Chlorine", 17, "35.45", "Greenish gas. Used in disinfectants, PVC, and water treatment. Discovered by Carl Wilhelm Scheele in 1774. Named from Greek 'chloros' meaning green-yellow.", 3, 17),
            ("Ar", "Argon", 18, "39.95", "Inert gas. Used in welding, light bulbs, and as a protective atmosphere. Discovered by Lord Rayleigh and William Ramsay in 1894. Named from Greek 'argos' meaning lazy.", 3, 18),
            ("K", "Potassium", 19, "39.10", "Soft, reactive metal. Essential for nerve function. Used in fertilizers and fireworks. Discovered by Humphry Davy in 1807. Named after potash (potassium carbonate).", 4, 1),
            ("Ca", "Calcium", 20, "40.08", "Essential for bones and teeth. Used in cement, plaster, and as a reducing agent. Discovered by Humphry Davy in 1808. Named after Latin 'calx' meaning lime.", 4, 2),
            ("Sc", "Scandium", 21, "44.96", "Transition metal, used in alloys. Discovered by Lars Fredrik Nilson in 1879. Named after Scandinavia. Used in high-intensity lamps and sports equipment.", 4, 3),
            ("Ti", "Titanium", 22, "47.87", "Strong, corrosion-resistant metal. Discovered by William Gregor in 1791. Named after Titans of Greek mythology. Used in aircraft, medical implants, and jewelry.", 4, 4),
            ("V", "Vanadium", 23, "50.94", "Transition metal with various uses. Discovered by Andrés Manuel del Río in 1801. Named after Vanadis, Norse goddess of beauty. Used in steel alloys and catalysts.", 4, 5),
            ("Cr", "Chromium", 24, "52.00", "Hard, corrosion-resistant metal. Discovered by Louis Nicolas Vauquelin in 1797. Named from Greek 'chroma' meaning color. Used in stainless steel and chrome plating.", 4, 6),
            ("Mn", "Manganese", 25, "54.94", "Important for biological systems. Discovered by Johan Gottlieb Gahn in 1774. Named after Latin 'magnes' meaning magnet. Used in steel production and batteries.", 4, 7),
            ("Fe", "Iron", 26, "55.85", "Most used metal. Essential for blood (hemoglobin). Used in construction, tools, and magnets. Known since ancient times. Named from Anglo-Saxon 'iren'. Core of Earth is mostly iron.", 4, 8),
            ("Co", "Cobalt", 27, "58.93", "Used in batteries and magnetic materials. Discovered by Georg Brandt in 1735. Named after German 'kobold' meaning goblin. Used in blue pigments and cancer treatment.", 4, 9),
            ("Ni", "Nickel", 28, "58.69", "Durable metal, used in alloys. Discovered by Axel Fredrik Cronstedt in 1751. Named after German 'kupfernickel' meaning devil's copper. Used in coins and stainless steel.", 4, 10),
            ("Cu", "Copper", 29, "63.55", "Excellent conductor. Used in wiring, coins, and bronze. Antimicrobial properties. Known since ancient times. Named after Cyprus where it was mined. Used in electrical wiring and plumbing.", 4, 11),
            ("Zn", "Zinc", 30, "65.38", "Used to galvanize steel, in batteries, and as a dietary supplement. Essential for immune function. Discovered by Andreas Sigismund Marggraf in 1746. Named after German 'zink'.", 4, 12),
            ("Ga", "Gallium", 31, "69.72", "Soft, silvery metal with a low melting point. Discovered by Paul-Émile Lecoq de Boisbaudran in 1875. Named after Gallia (Latin for France). Used in semiconductors and thermometers.", 4, 13),
            ("Ge", "Germanium", 32, "72.63", "Semi-metal used in semiconductors. Discovered by Clemens Winkler in 1886. Named after Germania (Latin for Germany). Used in fiber optics and infrared optics.", 4, 14),
            ("As", "Arsenic", 33, "74.92", "Toxic element with various uses. Known since ancient times. Named from Greek 'arsenikon' meaning yellow orpiment. Used in pesticides and semiconductors.", 4, 15),
            ("Se", "Selenium", 34, "78.97", "Trace element important for humans. Discovered by Jöns Jacob Berzelius in 1817. Named after Greek goddess Selene (Moon). Used in photocopiers and solar cells.", 4, 16),
            ("Br", "Bromine", 35, "79.90", "Red-brown liquid, used as a flame retardant. Discovered by Antoine-Jérôme Balard in 1826. Named from Greek 'bromos' meaning stench. Used in photography and medicine.", 4, 17),
            ("Kr", "Krypton", 36, "83.80", "Inert gas used in certain lighting. Discovered by Sir William Ramsay in 1898. Named from Greek 'kryptos' meaning hidden. Used in fluorescent lamps and lasers.", 4, 18),
            ("Rb", "Rubidium", 37, "85.47", "Soft alkali metal, reacts with water. Discovered by Robert Bunsen and Gustav Kirchhoff in 1861. Named from Latin 'rubidus' meaning deep red. Used in atomic clocks.", 5, 1),
            ("Sr", "Strontium", 38, "87.62", "Reacts with water and burns with a red flame. Discovered by Adair Crawford in 1790. Named after Strontian, Scotland. Used in fireworks and medical imaging.", 5, 2),
            ("Y", "Yttrium", 39, "88.91", "Used in alloys and electronics. Discovered by Johan Gadolin in 1794. Named after Ytterby, Sweden. Used in superconductors and phosphors.", 5, 3),
            ("Zr", "Zirconium", 40, "91.22", "Corrosion-resistant metal, used in nuclear reactors. Discovered by Martin Heinrich Klaproth in 1789. Named after zircon, the mineral containing it. Used in nuclear fuel rods.", 5, 4),
            ("Nb", "Niobium", 41, "92.91", "Used in superconductors and alloys. Discovered by Charles Hatchett in 1801. Named after Niobe, daughter of Tantalus. Used in superconducting magnets.", 5, 5),
            ("Mo", "Molybdenum", 42, "95.95", "Transition metal, high melting point. Discovered by Carl Wilhelm Scheele in 1778. Named from Greek 'molybdos' meaning lead. Used in steel alloys and catalysts.", 5, 6),
            ("Tc", "Technetium", 43, "98.00", "Radioactive element, used in medical imaging. Discovered by Carlo Perrier and Emilio Segrè in 1937. Named from Greek 'technetos' meaning artificial. First artificially produced element.", 5, 7),
            ("Ru", "Ruthenium", 44, "101.1", "Transition metal with various uses. Discovered by Karl Ernst Claus in 1844. Named after Ruthenia (Latin for Russia). Used in electronics and catalysts.", 5, 8),
            ("Rh", "Rhodium", 45, "102.9", "Rare, corrosion-resistant metal. Discovered by William Hyde Wollaston in 1803. Named from Greek 'rhodon' meaning rose. Used in catalytic converters and jewelry.", 5, 9),
            ("Pd", "Palladium", 46, "106.4", "Used in catalytic converters and electronics. Discovered by William Hyde Wollaston in 1803. Named after asteroid Pallas. Used in hydrogen storage and jewelry.", 5, 10),
            ("Ag", "Silver", 47, "107.9", "Best electrical conductor. Used in jewelry, photography, and medicine (antibacterial). Known since ancient times. Named from Anglo-Saxon 'seolfor'. Used in coins and mirrors.", 5, 11),
            ("Cd", "Cadmium", 48, "112.4", "Toxic metal, used in batteries. Discovered by Friedrich Stromeyer in 1817. Named after Latin 'cadmia' meaning calamine. Used in pigments and electroplating.", 5, 12),
            ("In", "Indium", 49, "114.8", "Soft, malleable metal. Discovered by Ferdinand Reich and Hieronymus Theodor Richter in 1863. Named after indigo color in its spectrum. Used in semiconductors and LCD screens.", 5, 13),
            ("Sn", "Tin", 50, "118.7", "Low melting point metal, used in alloys. Known since ancient times. Named from Anglo-Saxon 'tin'. Used in solder, bronze, and food packaging.", 5, 14),
            ("Sb", "Antimony", 51, "121.8", "Brittle metalloid, used in flame retardants. Known since ancient times. Named from Greek 'anti' + 'monos' meaning not alone. Used in alloys and semiconductors.", 5, 15),
            ("Te", "Tellurium", 52, "127.6", "Metalloid, used in alloys and electronics. Discovered by Franz-Joseph Müller von Reichenstein in 1782. Named after Latin 'tellus' meaning Earth. Used in solar cells.", 5, 16),
            ("I", "Iodine", 53, "126.9", "Essential for thyroid hormones. Discovered by Bernard Courtois in 1811. Named from Greek 'iodes' meaning violet. Used in medicine and photography.", 5, 17),
            ("Xe", "Xenon", 54, "131.3", "Inert gas, used in lighting and lasers. Discovered by Sir William Ramsay in 1898. Named from Greek 'xenos' meaning stranger. Used in flash lamps and anesthesia.", 5, 18),
            ("Cs", "Cesium", 55, "132.9", "Soft alkali metal, highly reactive. Discovered by Robert Bunsen and Gustav Kirchhoff in 1860. Named from Latin 'caesius' meaning sky blue. Used in atomic clocks.", 6, 1),
            ("Ba", "Barium", 56, "137.3", "Reacts with water, used in medical imaging. Discovered by Carl Wilhelm Scheele in 1772. Named from Greek 'barys' meaning heavy. Used in X-ray imaging and fireworks.", 6, 2),
            ("La", "Lanthanum", 57, "138.9", "Rare earth metal, used in alloys. Discovered by Carl Gustaf Mosander in 1839. Named from Greek 'lanthanein' meaning to lie hidden. Used in camera lenses and batteries.", 8, 3),
            ("Ce", "Cerium", 58, "140.1", "Used in catalytic converters and electronics. Discovered by Jöns Jacob Berzelius in 1803. Named after asteroid Ceres. Used in lighter flints and glass polishing.", 8, 4),
            ("Pr", "Praseodymium", 59, "140.9", "Rare earth metal, used in magnets. Discovered by Carl Auer von Welsbach in 1885. Named from Greek 'prasios' + 'didymos' meaning green twin. Used in aircraft engines.", 8, 5),
            ("Nd", "Neodymium", 60, "144.2", "Used in strong permanent magnets. Discovered by Carl Auer von Welsbach in 1885. Named from Greek 'neos' + 'didymos' meaning new twin. Used in headphones and wind turbines.", 8, 6),
            ("Pm", "Promethium", 61, "145.0", "Radioactive rare earth element. Discovered by Jacob A. Marinsky in 1945. Named after Prometheus, who stole fire from the gods. Used in nuclear batteries.", 8, 7),
            ("Sm", "Samarium", 62, "150.4", "Used in magnets and nuclear reactors. Discovered by Paul-Émile Lecoq de Boisbaudran in 1879. Named after samarskite, the mineral containing it. Used in cancer treatment.", 8, 8),
            ("Eu", "Europium", 63, "152.0", "Red phosphorescent in some TV screens. Discovered by Eugène-Anatole Demarçay in 1901. Named after Europe. Used in fluorescent lamps and security features.", 8, 9),
            ("Gd", "Gadolinium", 64, "157.3", "Used in medical imaging and neutron capture. Discovered by Jean Charles Galissard de Marignac in 1880. Named after Johan Gadolin. Used in MRI contrast agents.", 8, 10),
            ("Tb", "Terbium", 65, "158.9", "Used in fluorescent lights and lasers. Discovered by Carl Gustaf Mosander in 1843. Named after Ytterby, Sweden. Used in solid-state devices and green phosphors.", 8, 11),
            ("Dy", "Dysprosium", 66, "162.5", "Used in magnets and lasers. Discovered by Paul-Émile Lecoq de Boisbaudran in 1886. Named from Greek 'dysprositos' meaning hard to get. Used in nuclear control rods.", 8, 12),
            ("Ho", "Holmium", 67, "164.9", "Used in magnets and lasers. Discovered by Per Teodor Cleve in 1878. Named after Stockholm (Latin: Holmia). Used in optical fibers and nuclear reactors.", 8, 13),
            ("Er", "Erbium", 68, "167.3", "Used in lasers and nuclear control rods. Discovered by Carl Gustaf Mosander in 1843. Named after Ytterby, Sweden. Used in fiber optic communications.", 8, 14),
            ("Tm", "Thulium", 69, "168.9", "Used in medical imaging and lasers. Discovered by Per Teodor Cleve in 1879. Named after Thule, ancient name for Scandinavia. Used in portable X-ray machines.", 8, 15),
            ("Yb", "Ytterbium", 70, "173.0", "Used in lasers and certain alloys. Discovered by Jean Charles Galissard de Marignac in 1878. Named after Ytterby, Sweden. Used in atomic clocks and fiber optics.", 8, 16),
            ("Lu", "Lutetium", 71, "175.0", "Used in medical imaging and research. Discovered by Georges Urbain in 1907. Named after Lutetia (Latin for Paris). Used in cancer treatment and petroleum cracking.", 8, 17),
            ("Hf", "Hafnium", 72, "178.5", "Used in nuclear reactors and electronics. Discovered by Dirk Coster and Georg von Hevesy in 1923. Named after Hafnia (Latin for Copenhagen). Used in nuclear control rods.", 6, 4),
            ("Ta", "Tantalum", 73, "180.9", "Used in capacitors and surgical implants. Discovered by Anders Gustaf Ekeberg in 1802. Named after Tantalus of Greek mythology. Used in mobile phones and medical devices.", 6, 5),
            ("W", "Tungsten", 74, "183.8", "High melting point, used in filaments. Discovered by Carl Wilhelm Scheele in 1781. Named from Swedish 'tung sten' meaning heavy stone. Used in light bulbs and cutting tools.", 6, 6),
            ("Re", "Rhenium", 75, "186.2", "High melting point, used in jet engines. Discovered by Walter Noddack in 1925. Named after Rhine River. Used in high-temperature thermocouples.", 6, 7),
            ("Os", "Osmium", 76, "190.2", "Densest naturally occurring element. Discovered by Smithson Tennant in 1803. Named from Greek 'osme' meaning smell. Used in fountain pen tips and electrical contacts.", 6, 8),
            ("Ir", "Iridium", 77, "192.2", "Corrosion-resistant, used in spark plugs. Discovered by Smithson Tennant in 1803. Named after Iris, Greek goddess of rainbow. Used in compass bearings and jewelry.", 6, 9),
            ("Pt", "Platinum", 78, "195.1", "Precious metal, used in jewelry and catalytic converters. Discovered by Antonio de Ulloa in 1735. Named from Spanish 'platina' meaning little silver. Used in chemotherapy.", 6, 10),
            ("Au", "Gold", 79, "197.0", "Highly valued precious metal. Known since ancient times. Named from Anglo-Saxon 'geolu' meaning yellow. Used in jewelry, electronics, and dentistry. Symbol of wealth and power.", 6, 11),
            ("Hg", "Mercury", 80, "200.6", "Toxic liquid metal, used in thermometers. Known since ancient times. Named after Roman god Mercury. Used in dental amalgams and fluorescent lamps.", 6, 12),
            ("Tl", "Thallium", 81, "204.4", "Toxic metal, used in electronics. Discovered by Sir William Crookes in 1861. Named from Greek 'thallos' meaning green shoot. Used in infrared detectors.", 6, 13),
            ("Pb", "Lead", 82, "207.2", "Heavy metal, used in batteries and pipes. Known since ancient times. Named from Anglo-Saxon 'lead'. Used in radiation shielding and weights.", 6, 14),
            ("Bi", "Bismuth", 83, "208.9", "Brittle metal, used in cosmetics and medicine. Known since ancient times. Named from German 'wismuth'. Used in fire sprinklers and stomach remedies.", 6, 15),
            ("Po", "Polonium", 84, "209.0", "Radioactive element, highly toxic. Discovered by Marie Curie in 1898. Named after Poland, her homeland. Used in nuclear weapons and static eliminators.", 6, 16),
            ("At", "Astatine", 85, "210.0", "Radioactive halogen, very rare. Discovered by Dale R. Corson in 1940. Named from Greek 'astatos' meaning unstable. Used in cancer treatment research.", 6, 17),
            ("Rn", "Radon", 86, "222.0", "Radioactive noble gas, health hazard. Discovered by Friedrich Ernst Dorn in 1900. Named after radium. Used in cancer treatment and earthquake prediction.", 6, 18),
            ("Fr", "Francium", 87, "223.0", "Highly radioactive alkali metal. Discovered by Marguerite Perey in 1939. Named after France. Most unstable naturally occurring element.", 7, 1),
            ("Ra", "Radium", 88, "226.0", "Radioactive alkaline earth metal. Discovered by Marie Curie in 1898. Named from Latin 'radius' meaning ray. Used in cancer treatment and luminous paint.", 7, 2),
            ("Ac", "Actinium", 89, "227.0", "Radioactive rare earth metal. Discovered by André-Louis Debierne in 1899. Named from Greek 'aktis' meaning ray. Used in neutron sources and cancer treatment.", 9, 3),
            ("Th", "Thorium", 90, "232.0", "Radioactive element, potential nuclear fuel. Discovered by Jöns Jacob Berzelius in 1828. Named after Thor, Norse god of thunder. Used in nuclear reactors.", 9, 4),
            ("Pa", "Protactinium", 91, "231.0", "Radioactive element, used in research. Discovered by Kasimir Fajans in 1913. Named from Greek 'protos' + 'actinium' meaning parent of actinium. Used in nuclear research.", 9, 5),
            ("U", "Uranium", 92, "238.0", "Radioactive element, nuclear fuel. Discovered by Martin Heinrich Klaproth in 1789. Named after planet Uranus. Used in nuclear power plants and weapons.", 9, 6),
            ("Np", "Neptunium", 93, "237.0", "Radioactive element, used in research. Discovered by Edwin McMillan in 1940. Named after planet Neptune. Used in neutron detection.", 9, 7),
            ("Pu", "Plutonium", 94, "244.0", "Radioactive element, used in nuclear weapons. Discovered by Glenn T. Seaborg in 1940. Named after planet Pluto. Used in nuclear power and space probes.", 9, 8),
            ("Am", "Americium", 95, "243.0", "Radioactive element, used in smoke detectors. Discovered by Glenn T. Seaborg in 1944. Named after America. Used in smoke alarms and neutron sources.", 9, 9),
            ("Cm", "Curium", 96, "247.0", "Radioactive element, used in research. Discovered by Glenn T. Seaborg in 1944. Named after Marie and Pierre Curie. Used in space power sources.", 9, 10),
            ("Bk", "Berkelium", 97, "247.0", "Radioactive element, used in research. Discovered by Glenn T. Seaborg in 1949. Named after Berkeley, California. Used in nuclear research.", 9, 11),
            ("Cf", "Californium", 98, "251.0", "Radioactive element, used in research. Discovered by Glenn T. Seaborg in 1950. Named after California. Used in neutron sources and cancer treatment.", 9, 12),
            ("Es", "Einsteinium", 99, "252.0", "Radioactive element, used in research. Discovered by Albert Ghiorso in 1952. Named after Albert Einstein. Used in nuclear research.", 9, 13),
            ("Fm", "Fermium", 100, "257.0", "Radioactive element, used in research. Discovered by Albert Ghiorso in 1952. Named after Enrico Fermi. Used in nuclear research.", 9, 14),
            ("Md", "Mendelevium", 101, "258.0", "Radioactive element, used in research. Discovered by Albert Ghiorso in 1955. Named after Dmitri Mendeleev. Used in nuclear research.", 9, 15),
            ("No", "Nobelium", 102, "259.0", "Radioactive element, used in research. Discovered by Albert Ghiorso in 1958. Named after Alfred Nobel. Used in nuclear research.", 9, 16),
            ("Lr", "Lawrencium", 103, "262.0", "Radioactive element, used in research. Discovered by Albert Ghiorso in 1961. Named after Ernest Lawrence. Used in nuclear research.", 9, 17),
            ("Rf", "Rutherfordium", 104, "267.0", "Synthetic element, research interest. Discovered by Georgy Flerov in 1964. Named after Ernest Rutherford. Used in nuclear research.", 7, 4),
            ("Db", "Dubnium", 105, "270.0", "Synthetic element, research interest. Discovered by Georgy Flerov in 1967. Named after Dubna, Russia. Used in nuclear research.", 7, 5),
            ("Sg", "Seaborgium", 106, "271.0", "Synthetic element, research interest. Discovered by Albert Ghiorso in 1974. Named after Glenn T. Seaborg. Used in nuclear research.", 7, 6),
            ("Bh", "Bohrium", 107, "270.0", "Synthetic element, research interest. Discovered by Peter Armbruster in 1981. Named after Niels Bohr. Used in nuclear research.", 7, 7),
            ("Hs", "Hassium", 108, "277.0", "Synthetic element, research interest. Discovered by Peter Armbruster in 1984. Named after Hesse, Germany. Used in nuclear research.", 7, 8),
            ("Mt", "Meitnerium", 109, "276.0", "Synthetic element, research interest. Discovered by Peter Armbruster in 1982. Named after Lise Meitner. Used in nuclear research.", 7, 9),
            ("Ds", "Darmstadtium", 110, "281.0", "Synthetic element, research interest. Discovered by Peter Armbruster in 1994. Named after Darmstadt, Germany. Used in nuclear research.", 7, 10),
            ("Rg", "Roentgenium", 111, "280.0", "Synthetic element, research interest. Discovered by Peter Armbruster in 1994. Named after Wilhelm Röntgen. Used in nuclear research.", 7, 11),
            ("Cn", "Copernicium", 112, "285.0", "Synthetic element, research interest. Discovered by Peter Armbruster in 1996. Named after Nicolaus Copernicus. Used in nuclear research.", 7, 12),
            ("Nh", "Nihonium", 113, "284.0", "Synthetic element, research interest. Discovered by RIKEN in 2004. Named after Japan (Nihon). Used in nuclear research.", 7, 13),
            ("Fl", "Flerovium", 114, "289.0", "Synthetic element, research interest. Discovered by Joint Institute for Nuclear Research in 1999. Named after Georgy Flerov. Used in nuclear research.", 7, 14),
            ("Mc", "Moscovium", 115, "288.0", "Synthetic element, research interest. Discovered by Joint Institute for Nuclear Research in 2003. Named after Moscow Oblast. Used in nuclear research.", 7, 15),
            ("Lv", "Livermorium", 116, "293.0", "Synthetic element, research interest. Discovered by Joint Institute for Nuclear Research in 2000. Named after Livermore, California. Used in nuclear research.", 7, 16),
            ("Ts", "Tennessine", 117, "294.0", "Synthetic element, research interest. Discovered by Joint Institute for Nuclear Research in 2010. Named after Tennessee. Used in nuclear research.", 7, 17),
            ("Og", "Oganesson", 118, "294.0", "Synthetic element, research interest. Discovered by Joint Institute for Nuclear Research in 2002. Named after Yuri Oganessian. Used in nuclear research.", 7, 18)
        ]
        self.create_periodic_table()
        self.create_legend()

    def get_type_color(self, symbol):
        t = ELEMENT_TYPES.get(symbol, 'unknown')
        return TYPE_COLORS.get(t, TYPE_COLORS['unknown'])

    def on_enter(self, event, btn, symbol):
        btn.config(bg="#222a38", fg="#fff", relief="solid", bd=3)

    def on_leave(self, event, btn, symbol):
        btn.config(bg=self.get_type_color(symbol), fg="#ECF0F1", relief="raised", bd=2)

    def create_periodic_table(self):
        for element in self.elements:
            symbol, name, atomic_num, atomic_mass, description, row, col = element
            color = self.get_type_color(symbol)
            btn = tk.Button(
                self.root,
                text=f"{atomic_num}\n{symbol}\n{atomic_mass}",
                font=("Segoe UI", 14, "bold"),
                width=8,
                height=4,
                bg=color,
                fg="#ECF0F1",
                activebackground="#636e72",
                activeforeground="#fff",
                relief="raised",
                bd=2,
                highlightthickness=0,
                command=lambda s=symbol, n=name, a=atomic_num, m=atomic_mass, d=description: self.show_element_info(s, n, a, m, d)
            )
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn, s=symbol: self.on_enter(e, b, s))
            btn.bind("<Leave>", lambda e, b=btn, s=symbol: self.on_leave(e, b, s))

        for i in range(1, 10):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(1, 19):
            self.root.grid_columnconfigure(j, weight=1)

    def create_legend(self):
        legend_frame = tk.Frame(self.root, bg="#111217")
        legend_frame.grid(row=10, column=0, columnspan=19, sticky="ew", pady=10)
        
        legend_title = tk.Label(legend_frame, text="Element Types Legend", font=("Segoe UI", 16, "bold"), 
                               bg="#111217", fg="#ECF0F1")
        legend_title.pack(pady=(0, 10))
        
        legend_items = [
            ("Alkali Metals", "#7c2f1c"),
            ("Alkaline Earth Metals", "#7a5c1e"),
            ("Transition Metals", "#145c47"),
            ("Post-Transition Metals", "#23272a"),
            ("Metalloids", "#14505c"),
            ("Nonmetals", "#1a2a40"),
            ("Halogens", "#2d1c4a"),
            ("Noble Gases", "#444950"),
            ("Lanthanides", "#6c2a3a"),
            ("Actinides", "#2a2a6c")
        ]
        
        for i, (name, color) in enumerate(legend_items):
            legend_item = tk.Frame(legend_frame, bg="#111217")
            legend_item.pack(side="left", padx=10)
            
            color_box = tk.Frame(legend_item, bg=color, width=20, height=20, relief="solid", bd=1)
            color_box.pack(side="left", padx=(0, 5))
            
            label = tk.Label(legend_item, text=name, font=("Segoe UI", 10), bg="#111217", fg="#ECF0F1")
            label.pack(side="left")

    def show_element_info(self, symbol, name, atomic_num, atomic_mass, description):
                info = f"Symbol: {symbol}\nName: {name}\nAtomic Number: {atomic_num}\nAtomic Mass: {atomic_mass}\nDescription: {description}"
                messagebox.showinfo(f"Element Information - {name}", info)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()
