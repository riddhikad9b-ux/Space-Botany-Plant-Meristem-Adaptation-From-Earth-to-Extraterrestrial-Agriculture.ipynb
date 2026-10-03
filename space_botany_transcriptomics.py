import os
import shutil
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs('/workspace/scratch/space_botany', exist_ok=True)

# 1. Set seed for reproducible synthetic transcriptomic dataset grounded in sources
np.random.seed(42)

genes_data = [
    # Auxin Transport & Gravitropism
    ('PIN2', 'Auxin Transport', -2.15, 0.0001, 'Root Apical Meristem'),
    ('PIN3', 'Auxin Transport', -1.85, 0.0004, 'Root Apical Meristem'),
    ('PIN7', 'Auxin Transport', -1.92, 0.0002, 'Root Apical Meristem'),
    ('AUX1', 'Auxin Transport', -1.45, 0.0021, 'Root Apical Meristem'),
    ('LAZY1', 'Auxin Transport', -2.30, 0.00005, 'Root Apical Meristem'),
    ('ARF7', 'Auxin Signaling', 1.65, 0.0012, 'Elongation Zone'),
    ('ARF19', 'Auxin Signaling', 1.58, 0.0018, 'Elongation Zone'),
    ('PABA_Syn', 'Hormone Cross-Talk', 2.10, 0.0003, 'Root Apical Meristem'),
    ('EIN2', 'Ethylene Signaling', 1.75, 0.0008, 'Elongation Zone'),
    
    # Meristem Maintenance & Stem Cell Niche
    ('WUS', 'Meristem Maintenance', -1.72, 0.0006, 'Shoot Apical Meristem'),
    ('WOX4', 'Meristem Maintenance', -1.68, 0.0009, 'Shoot Apical Meristem'),
    ('CLV3', 'Meristem Maintenance', 1.25, 0.0150, 'Shoot Apical Meristem'),
    ('GRF1', 'Meristem Proliferation', -1.55, 0.0031, 'Shoot Apical Meristem'),
    ('GRF4', 'Meristem Proliferation', -1.48, 0.0045, 'Shoot Apical Meristem'),
    ('ATHB15', 'Meristem Maintenance', -1.80, 0.0005, 'Shoot Apical Meristem'),
    
    # Cell Wall Remodeling & Stress Response
    ('XTH1', 'Cell Wall Remodeling', 2.45, 0.00002, 'Elongation Zone'),
    ('EXPA1', 'Cell Wall Remodeling', 2.18, 0.0001, 'Elongation Zone'),
    ('Ivr2', 'Sugar Metabolism', 1.95, 0.0004, 'Elongation Zone'),
    ('GST1', 'Oxidative Stress', 2.60, 0.00001, 'Root Apical Meristem'),
    ('PRX5', 'Oxidative Stress', 2.35, 0.00004, 'Shoot Apical Meristem'),
    ('CesA1', 'Cellulose Synthesis', -1.95, 0.0003, 'Elongation Zone'),
    
    # Control / Unchanged Genes
    ('ACT2', 'Housekeeping', 0.12, 0.6500, 'All Tissues'),
    ('TUB4', 'Housekeeping', -0.08, 0.7800, 'All Tissues'),
    ('UBQ10', 'Housekeeping', 0.05, 0.8900, 'All Tissues'),
    ('GAPDH', 'Housekeeping', -0.15, 0.5200, 'All Tissues'),
    ('EF1A', 'Housekeeping', 0.02, 0.9400, 'All Tissues')
]

# Add background noise genes
for i in range(35):
    gname = f"GENE_BG_{i+1:02d}"
    pathway = np.random.choice(['Primary Metabolism', 'Lipid Biosynthesis', 'Protein Transport', 'Photosynthesis'])
    l2fc = np.random.normal(0, 0.4)
    pval = np.random.uniform(0.05, 0.95)
    tissue = np.random.choice(['Shoot Apical Meristem', 'Root Apical Meristem', 'Elongation Zone'])
    genes_data.append((gname, pathway, l2fc, pval, tissue))

df_deg = pd.DataFrame(genes_data, columns=['Gene', 'Pathway', 'Log2_Fold_Change', 'p_value', 'Tissue'])
df_deg['neg_log10_p'] = -np.log10(df_deg['p_value'])

# Label regulation status
def get_status(row):
    if row['p_value'] < 0.01 and row['Log2_Fold_Change'] >= 1.2:
        return 'Upregulated (Space Stress/Remodeling)'
    elif row['p_value'] < 0.01 and row['Log2_Fold_Change'] <= -1.2:
        return 'Downregulated (Disrupted Transport/Niche)'
    else:
        return 'Not Significant'

df_deg['Status'] = df_deg.apply(get_status, axis=1)

# Save processed dataframe
csv_path = '/workspace/scratch/space_botany/space_botany_deg_results.csv'
df_deg.to_csv(csv_path, index=False)

# 2. Build Visualization Dashboard
sns.set_theme(style='whitegrid', palette='colorblind', font='DejaVu Sans')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Title
fig.suptitle('Microgravity Transcriptomic Reprogramming in Plant Meristems & Auxin Pathways', 
             fontsize=16, fontweight='bold', y=0.98)

# --- Subplot 1: Volcano Plot ---
palette_dict = {
    'Upregulated (Space Stress/Remodeling)': '#e74c3c',
    'Downregulated (Disrupted Transport/Niche)': '#3498db',
    'Not Significant': '#95a5a6'
}

sns.scatterplot(
    data=df_deg,
    x='Log2_Fold_Change',
    y='neg_log10_p',
    hue='Status',
    palette=palette_dict,
    s=70,
    alpha=0.85,
    ax=ax1
)

# Threshold lines
ax1.axhline(-np.log10(0.01), color='black', linestyle='--', linewidth=1, alpha=0.7, label='p = 0.01 threshold')
ax1.axvline(1.2, color='gray', linestyle=':', linewidth=1, alpha=0.7)
ax1.axvline(-1.2, color='gray', linestyle=':', linewidth=1, alpha=0.7)

# Annotate key genes
key_annotations = ['PIN2', 'PIN3', 'LAZY1', 'WUS', 'WOX4', 'XTH1', 'GST1', 'EXPA1', 'PABA_Syn']
for _, row in df_deg[df_deg['Gene'].isin(key_annotations)].iterrows():
    ax1.annotate(
        row['Gene'],
        (row['Log2_Fold_Change'], row['neg_log10_p']),
        xytext=(5, 5),
        textcoords='offset points',
        fontsize=9,
        fontweight='bold',
        alpha=0.9
    )

ax1.set_title('Spaceflight DEGs: Auxin Transport Suppression vs Stress Elevation', fontsize=12, fontweight='bold', pad=10)
ax1.set_xlabel('Log2 Fold Change (Spaceflight vs Ground Control)', fontsize=10, fontweight='bold')
ax1.set_ylabel('-Log10 (p-value)', fontsize=10, fontweight='bold')
ax1.legend(loc='upper right', fontsize=8, frameon=True)

# --- Subplot 2: Heatmap of Target Functional Pathways across Tissues ---
heatmap_genes = ['PIN2', 'PIN3', 'LAZY1', 'WUS', 'WOX4', 'GRF1', 'ATHB15', 'XTH1', 'EXPA1', 'GST1', 'PRX5', 'CesA1']
df_hm = df_deg[df_deg['Gene'].isin(heatmap_genes)].copy()

# Generate tissue-specific Log2 Fold Change matrix
tissues = ['Shoot Apical Meristem', 'Root Apical Meristem', 'Elongation Zone']
hm_matrix = []

for g in heatmap_genes:
    base_l2fc = df_hm[df_hm['Gene'] == g]['Log2_Fold_Change'].values[0]
    primary_tissue = df_hm[df_hm['Gene'] == g]['Tissue'].values[0]
    
    row_vals = []
    for t in tissues:
        if t == primary_tissue:
            row_vals.append(base_l2fc)
        elif 'Meristem' in t and 'Meristem' in primary_tissue:
            row_vals.append(base_l2fc * 0.6)
        else:
            row_vals.append(base_l2fc * 0.2 + np.random.normal(0, 0.1))
    hm_matrix.append(row_vals)

hm_df = pd.DataFrame(hm_matrix, index=heatmap_genes, columns=tissues)

sns.heatmap(
    hm_df,
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    linewidths=0.8,
    cbar_kws={'label': 'Log2 Fold Change'},
    ax=ax2
)

ax2.set_title('Tissue-Specific Expression Shift (SAM vs RAM vs EZ)', fontsize=12, fontweight='bold', pad=10)
ax2.set_ylabel('Key Target Genes', fontsize=10, fontweight='bold')

sns.despine(fig=fig)
plt.tight_layout(pad=2.0)

fig_path = '/workspace/scratch/space_botany/space_botany_expression_dashboard.png'
fig.savefig(fig_path, dpi=150, bbox_inches='tight')
plt.close()

print('Script executed successfully. Output generated.')
