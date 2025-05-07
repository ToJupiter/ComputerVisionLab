import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return min(zs)

class LinearCombinationVisualizer:
    def __init__(self):
        self.v = np.array([2, 4])
        self.w = np.array([1, 3])
        self.c = 1
        self.d = 1
        
    def visualize(self, filename="linear_combination.png"):
        plt.figure(facecolor='white')
        ax = plt.gca()
        
        # Plot vectors v and w
        ax.quiver(0, 0, self.v[0], self.v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v = [2, 4]')
        ax.quiver(0, 0, self.w[0], self.w[1], angles='xy', scale_units='xy', scale=1, color='b', label='w = [1, 3]')
        
        # Plot linear combination c*v + d*w
        combo = self.c * self.v + self.d * self.w
        ax.quiver(0, 0, combo[0], combo[1], angles='xy', scale_units='xy', scale=1, color='g', label=f'{self.c}v + {self.d}w')
        
        # Plot span of v and w
        for c in np.linspace(-1, 1, 10):
            for d in np.linspace(-1, 1, 10):
                point = c * self.v + d * self.w
                plt.scatter(point[0], point[1], color='gray', alpha=0.2, s=10)
        
        # Set limits and grid
        ax.set_xlim([-5, 10])
        ax.set_ylim([-5, 10])
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        
        plt.title('Linear Combination of Vectors')
        plt.legend()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

class DotProductVisualizer:
    def __init__(self):
        self.v = np.array([3, 2])
        self.w = np.array([1, 4])
        
    def visualize(self, filename="dot_product.png"):
        plt.figure(facecolor='white')
        ax = plt.gca()
        
        # Plot vectors
        ax.quiver(0, 0, self.v[0], self.v[1], angles='xy', scale_units='xy', scale=1, color='r', label=f'v = {self.v}')
        ax.quiver(0, 0, self.w[0], self.w[1], angles='xy', scale_units='xy', scale=1, color='b', label=f'w = {self.w}')
        
        # Calculate angle
        cos_theta = np.dot(self.v, self.w) / (np.linalg.norm(self.v) * np.linalg.norm(self.w))
        theta = np.arccos(cos_theta)
        
        # Draw angle arc
        arc_radius = 0.5
        arc = np.linspace(0, theta, 30)
        x_arc = arc_radius * np.cos(arc)
        y_arc = arc_radius * np.sin(arc)
        plt.plot(x_arc, y_arc, color='purple')
        
        # Add angle label
        plt.text(arc_radius*np.cos(theta/2), arc_radius*np.sin(theta/2), 
                 f'θ = {np.degrees(theta):.1f}°', ha='center', va='bottom')
        
        # Add projection of w onto v
        proj = (np.dot(self.w, self.v) / np.dot(self.v, self.v)) * self.v
        plt.plot([proj[0], self.w[0]], [proj[1], self.w[1]], 'k--', alpha=0.5)
        plt.quiver(0, 0, proj[0], proj[1], angles='xy', scale_units='xy', scale=1, color='g', alpha=0.5, 
                  label=f'Projection (dot product = {np.dot(self.v, self.w)})')
        
        # Set limits and grid
        ax.set_xlim([0, 4])
        ax.set_ylim([0, 5])
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        
        plt.title('Dot Product and Angle Between Vectors')
        plt.legend()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

class MatrixMultiplicationVisualizer:
    def __init__(self):
        self.A = np.array([[2, 1], [4, 3]])
        self.B = np.array([[5, 6], [7, 8]])
        
    def visualize(self, filename="matrix_multiplication.png"):
        AB = self.A @ self.B
        
        plt.figure(facecolor='white', figsize=(10, 5))
        
        # Plot matrix A
        plt.subplot(1, 3, 1)
        plt.imshow(self.A, cmap='Blues', vmin=0, vmax=10)
        for i in range(2):
            for j in range(2):
                plt.text(j, i, f'{self.A[i,j]}', ha='center', va='center', color='black')
        plt.title('Matrix A')
        plt.xticks([])
        plt.yticks([])
        
        # Plot matrix B
        plt.subplot(1, 3, 2)
        plt.imshow(self.B, cmap='Oranges', vmin=0, vmax=10)
        for i in range(2):
            for j in range(2):
                plt.text(j, i, f'{self.B[i,j]}', ha='center', va='center', color='black')
        plt.title('Matrix B')
        plt.xticks([])
        plt.yticks([])
        
        # Plot product AB
        plt.subplot(1, 3, 3)
        plt.imshow(AB, cmap='Greens', vmin=0, vmax=60)
        for i in range(2):
            for j in range(2):
                plt.text(j, i, f'{AB[i,j]}', ha='center', va='center', color='black')
        plt.title('Product AB')
        plt.xticks([])
        plt.yticks([])
        
        plt.suptitle('Matrix Multiplication: AB')
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

class LinearSystemVisualizer:
    def __init__(self):
        self.A = np.array([[2, 1], [4, 3]])
        self.b = np.array([2, 0])
        
    def visualize(self, filename="linear_system.png"):
        # Solve the system
        x = np.linalg.solve(self.A, self.b)
        
        plt.figure(facecolor='white', figsize=(10, 5))
        
        # Plot the two equations
        x_vals = np.linspace(-1, 3, 100)
        y1 = (self.b[0] - self.A[0,0]*x_vals) / self.A[0,1]
        y2 = (self.b[1] - self.A[1,0]*x_vals) / self.A[1,1]
        
        plt.plot(x_vals, y1, label=f'{self.A[0,0]}x + {self.A[0,1]}y = {self.b[0]}')
        plt.plot(x_vals, y2, label=f'{self.A[1,0]}x + {self.A[1,1]}y = {self.b[1]}')
        
        # Plot the solution point
        plt.scatter(x[0], x[1], color='red', s=100, label=f'Solution (x={x[0]:.1f}, y={x[1]:.1f})')
        
        # Set limits and grid
        plt.xlim(-1, 3)
        plt.ylim(-5, 5)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        
        plt.title('System of Linear Equations')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

class LUDecompositionVisualizer:
    def __init__(self):
        self.A = np.array([[2, 1, 1], [4, 3, 2], [8, 7, 9]])
        
    def visualize(self, filename="lu_decomposition.png"):
        from scipy.linalg import lu
        P, L, U = lu(self.A)
        
        plt.figure(facecolor='white', figsize=(12, 4))
        
        # Plot original matrix A
        plt.subplot(1, 4, 1)
        plt.imshow(self.A, cmap='Blues', vmin=0, vmax=10)
        for i in range(3):
            for j in range(3):
                plt.text(j, i, f'{self.A[i,j]}', ha='center', va='center', color='black')
        plt.title('Original Matrix A')
        plt.xticks([])
        plt.yticks([])
        
        # Plot permutation matrix P
        plt.subplot(1, 4, 2)
        plt.imshow(P, cmap='Greys', vmin=0, vmax=1)
        for i in range(3):
            for j in range(3):
                plt.text(j, i, f'{P[i,j]:.0f}', ha='center', va='center', color='black')
        plt.title('Permutation Matrix P')
        plt.xticks([])
        plt.yticks([])
        
        # Plot lower triangular L
        plt.subplot(1, 4, 3)
        plt.imshow(L, cmap='Greens', vmin=0, vmax=1)
        for i in range(3):
            for j in range(3):
                plt.text(j, i, f'{L[i,j]:.1f}', ha='center', va='center', color='black')
        plt.title('Lower Triangular L')
        plt.xticks([])
        plt.yticks([])
        
        # Plot upper triangular U
        plt.subplot(1, 4, 4)
        plt.imshow(U, cmap='Reds', vmin=0, vmax=10)
        for i in range(3):
            for j in range(3):
                plt.text(j, i, f'{U[i,j]:.1f}', ha='center', va='center', color='black')
        plt.title('Upper Triangular U')
        plt.xticks([])
        plt.yticks([])
        
        plt.suptitle('LU Decomposition with Partial Pivoting: PA = LU')
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    import os

    print("Generating linear algebra visualizations...")
    
    # Specify the folder to save images
    output_folder = "output_images"
    os.makedirs(output_folder, exist_ok=True)
    
    # Create and run each visualizer
    lc = LinearCombinationVisualizer()
    lc.visualize(filename=os.path.join(output_folder, "linear_combination.png"))
    
    dp = DotProductVisualizer()
    dp.visualize(filename=os.path.join(output_folder, "dot_product.png"))
    
    mm = MatrixMultiplicationVisualizer()
    mm.visualize(filename=os.path.join(output_folder, "matrix_multiplication.png"))
    
    ls = LinearSystemVisualizer()
    ls.visualize(filename=os.path.join(output_folder, "linear_system.png"))
    
    lu = LUDecompositionVisualizer()
    lu.visualize(filename=os.path.join(output_folder, "lu_decomposition.png"))
    
    print(f"Visualizations saved in folder: {output_folder}")