class Molecule:
    "Implement Molecules and their vector positions"

    def __init__(self,atoms,positions,charge,mass):
        "Initialising the molecule"
        self.atoms=atoms
        "The atom will have the symbol given when the Molecules class is called"
        self.positions=positions
        "Positions of each atom"
        self.charge=charge
        self.mass=mass
         
    def bondlength(self, i, j):
        "calculating and returning the bond length betwwen two atoms"
        difference = self.positions[j]-self.positions[i]
        length = difference.norm()
        return length

    def bondangle(self,i,j,k):
        "Calculating the bond angle between central atom j and two other atoms i and k"
        #find the difference between positions i and j and i and k
        vec_1 = self.positions[j]-self.positions[i]
        vec_2 = self.positions[j]-self.positions[k]

        #call the dot product of the two differences
        dot_prod = vec_1.dot(vec_2)

        #call the bond length of the two differences
        norm_1 = vec_1.norm()
        norm_2 = vec_2.norm()
        
        #angle
        ang = arccos((dot_prod)/(norm_1*norm_2))
        return ang

    def dipolemoment(self):
        moment = Vector(0,0,0)
        for i in range(len(self.charge)):
            j = self.positions[i].scale(self.charge[i])
            moment += j
        return moment

    def c_of_mass(self):
        total = sum(self.mass)
        c_vec=Vector(0,0,0)
        for i in range(len(self.mass)):
            c_vec += self.positions[i].scale(self.mass[i])

        centre=c_vec/total
        return centre

    def moment_inertia(self):
        
    
    def __repr__(self):
        return (f"Atoms: {self.atoms},"
                f"Vector Positions: {self.positions},"
                f"charges: {self.charge},"
                f"masses: {self.mass})")

atoms = ['O', 'H', 'H']
positions = [Vector(0, 0, 0), Vector(0.96, 0, 0), Vector(-0.24, 0.93, 0)]
charges = [-0.84, 0.42, 0.42]
masses = [16.00, 1.00, 1.00]

h2o = Molecule(atoms, positions, charges, masses)

h2o