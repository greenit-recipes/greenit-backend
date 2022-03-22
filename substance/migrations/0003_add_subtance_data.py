from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('substance', '0002_rename_group_substance_group_subs'),
    ]

    operations = [
        
      migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";'),

      migrations.RunSQL("INSERT INTO substance_substance (id, name, group_subs, effect) VALUES "+ 
                        "(uuid_generate_v4(), 'Butylphenyl methylpropional', 'Agent parfumant', 'Allergènes reglementés en Europe, perturbateur endocrinien suspecté'), " +
                        "(uuid_generate_v4(), 'Hexyl cinnamal', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Geraniol', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Limonene', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Linalool', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Methylisothiazolinone', 'Conservateur synthétique', 'Allergènes puissants et interdits dans les produits non rincés depuis 2017'), " +
                        "(uuid_generate_v4(), 'Phenoxyethanol', 'Conservateur / Alcool', 'Toxicité pour les bébés suspectée, allergènes suspectés, impactant la reproduction suspectée'), " +
                        "(uuid_generate_v4(), 'Butane', 'Agent propulseur (COV)', 'Impact sur la couche d’ozone et l’effet de serre, interdit lorsqu’il contient plus de 0,1% de butadiène'), " +
                        "(uuid_generate_v4(), 'Distearyldimonium chloride', 'Ammonium quaternaire', 'Hautement irritant surtout en combinaison avec d’autres substances'), " +
                        "(uuid_generate_v4(), 'Cetrimonium chloride', 'Ammonium quaternaire, Conservateur', 'Hautement irritant surtout en combinaison avec d’autres substances'), " +
                        "(uuid_generate_v4(), 'Isobutane', 'Agent propulseur (COV)', 'Impact sur la couche d’ozone et l’effet de serre, interdit lorsqu’il contient plus de 0,1% de butadiène'), " +
                        "(uuid_generate_v4(), 'Propane', 'Agent propulseur (COV)', 'Provoque de lergers étourdissements'), " +
                        "(uuid_generate_v4(), 'Alcohol Denat', 'Alcool', 'Allergènes puissants et irritants surtout pour les peaux sensibles'), " +
                        "(uuid_generate_v4(), 'Benzyl Benzoate', 'Agent parfumant', 'Allergènes reglementés en Europe'), " +
                        "(uuid_generate_v4(), 'Benzyl Salicylate', 'Agent parfumant/Absorbant UV', 'Allergènes reglementés en Europe, perturbateur endocrinien suspecté'), " +
                        "(uuid_generate_v4(), 'Behentrimonium chloride', 'Ammonium quaternaire, Conservateur', 'Ammonium quaternaire, Conservateur'), " +
                        "(uuid_generate_v4(), 'Hydroxypropyltrimonium chloride', 'Ammonium quaternaire, Conservateur', 'Toxicité suspecté, règlementé en Europe'), " +
                        "(uuid_generate_v4(), 'Trideceth-6', 'Composé éthoxylé', 'Toxicité lors de la fabrication'), " +
                        "(uuid_generate_v4(), 'Amodimethicone', 'Silicone', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'Salicylic acid', 'Conservateur/Conditionner', 'Classé CMR catégorie 2 (Cancérigène, Mutagène et Réprotoxique)'), " +
                        "(uuid_generate_v4(), 'Paraffinum Liquidium', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie'), " +
                        "(uuid_generate_v4(), 'Cera Microcristallina', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie, très peu biodagradable'), " +
                        "(uuid_generate_v4(), 'Paraffin', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie'), " +
                        "(uuid_generate_v4(), 'Methyl Metacrylate Crosspolymer', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Cyclopentasiloxane', 'Silicone', 'Peu biodégradable, impact sur l’environnement non négligeable, perturbateur endocrinens suspecté'), " +
                        "(uuid_generate_v4(), 'Cyclohexasiloxane', 'Silicone', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'Dimethicone', 'Silicone', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'Sodium Polycrylate', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'C30-45 - ALKYL Cetearyl Dimethicone Crosspolymer', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Lauryl PEC/PPG', 'Silicone/PEG-PPG', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'Hydroxyethylpiperazine Ethane Sulfonic Acid', 'Composé éthoxylé', 'Toxicité lors de la fabrication'), " +
                        "(uuid_generate_v4(), 'Disodium EDTA', 'EDTA', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'PEG', 'Polymères de synthèse/Composé éthoxylé', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Chlorphenesin', 'Conservateur synthétique', 'Causes des irritations'), " +
                        "(uuid_generate_v4(), 'Proplyparaben', 'Paraben', 'Considéré comme un perturbateur endocrinien'), " +
                        "(uuid_generate_v4(), 'Benzyl Alcohol', 'Agent parfumant/Conservateur', 'Allergènes reglementés en Europe'), " +
                        "(uuid_generate_v4(), 'Citronellol', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Eugenol', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Citral', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Sodium Laureth Sulfate', 'Sulfate/Composé éthoxylé', 'Toxicité lors de la fabrication'), " +
                        "(uuid_generate_v4(), 'Glyceryl Cocoate', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Tetrasodium EDTA', 'EDTA', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'PEG-100 Stearate', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Ceteth-20', 'Composé éthoxylé', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Polysorbate', 'Composé éthoxylé', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Carbomer', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Stearamidopropyl Dimethylamine', 'Ammonium quaternaire', 'Hautement irritant surtout en combinaison avec d’autres substances'), " +
                        "(uuid_generate_v4(), 'Hydroxypropyl Guar', 'Ammonium quaternaire/Composé éthoxylé', 'Hautement irritant surtout en combinaison avec d’autres substances'), " +
                        "(uuid_generate_v4(), 'Poloxamer', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Myrtrimonium Bromide', 'Ammonium quaternaire', 'Hautement irritant surtout en combinaison avec d’autres substances, réglementé'), " +
                        "(uuid_generate_v4(), 'Capryloyl Salicylic Acid', 'Conservateur/Conditionner', 'Perturbateur endocrinien suspecté'), " +
                        "(uuid_generate_v4(), 'Polyquarternium-30', 'Ammonium quaternaire', 'Hautement irritant surtout en combinaison avec d’autres substances, réglementé'), " +
                        "(uuid_generate_v4(), 'Hydrogenated oil', 'Huiles hydrogénées', 'La Slow cosmétique évite ce genre d’huiles car elles sont fausses le consommateur en leur proposant un produit naturel qui n’en est pas.'), " +
                        "(uuid_generate_v4(), 'Aluminum chlorohydrate', 'Sel d’aluminium', 'Perturbateur endocrinien suspecté'), " +
                        "(uuid_generate_v4(), 'BHT', 'Conservateur/Agent masquant', 'Perturbateur endocrinien suspecté'), " +
                        "(uuid_generate_v4(), 'Butylphenyl Methylpropional', 'Agent parfumant', 'Allergènes et perturbateurs endocriniens interdit en Europe à partir du 1er mars 2022'), " +
                        "(uuid_generate_v4(), 'Disteardimonium hectorite', 'Ammonium quaternaire', 'Hautement irritant surtout en combinaison avec d’autres substances'), " +
                        "(uuid_generate_v4(), 'Dimethiconol', 'Silicone', 'Peu biodégradable, impact sur l’environnement non négligeable'), " +
                        "(uuid_generate_v4(), 'Bromo-2-Nitropopane', 'Conservateur', 'Libérateur de Formaldéhyde, réglementé'), " +
                        "(uuid_generate_v4(), 'Colorant blanc', 'Colorant minéral/Dioxyde de titane', 'Cancérogènes possibles , réglementé dans les produits d’hygiène buccale'), " +
                        "(uuid_generate_v4(), 'Ethylhexyl Methoxycinnamate', 'Filtre UV/Agent stabilisant', 'Perturbateur endocrinien suspecté, réglementé'), " +
                        "(uuid_generate_v4(), 'Triethanolamine', 'TEA', 'Toxicité lors de la fabrication'), " +
                        "(uuid_generate_v4(), 'Cocamide MEA', 'Emulsifiant', 'Toxicité lors de la fabrication'), " +
                        "(uuid_generate_v4(), 'DMDM Hydantoin', 'Conservateur', 'Libérateur de Formaldéhyde, réglementé'), " +
                        "(uuid_generate_v4(), 'Guar Lauroyl Isethionate', 'Composé éthoxylé', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Synthetic Wax', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie'), " +
                        "(uuid_generate_v4(), 'Polybutene', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie'), " +
                        "(uuid_generate_v4(), 'Hydrogenated Microcrystalline Wax', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie'), " +
                        "(uuid_generate_v4(), 'Diethylamino Hydroxybenzoyl Hexyl Benzoate', 'Filtre UV/Agent stabilisant', 'Filtre UV Chimique, reglémenté'), " +
                        "(uuid_generate_v4(), 'Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine', 'Filtre UV/Agent stabilisant', 'Filtre UV Chimique, reglémenté'), " +
                        "(uuid_generate_v4(), 'Ethylhexyl Triazone', 'Filtre UV/Agent stabilisant', 'Filtre UV Chimique, reglémenté'), " +
                        "(uuid_generate_v4(), 'Isohexadecane', 'Huiles minérales', 'Dérivé d’hydrocarbures, issues de la pétrochimie'), " +
                        "(uuid_generate_v4(), 'Acrylamide', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Styrene', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Polyurethane', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Glyceryl Stearate', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Ethylenediamine', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'Agent de conservation', 'Conservateur', 'Peu d’informations sur la conservation des produits'), " +
                        "(uuid_generate_v4(), 'Methylchloroisothiazolinone', 'Conservateur', 'Hautement toxique pour l’humain et pour l’environnement'), " +
                        "(uuid_generate_v4(), 'Azurants Optiques', 'Colorants', 'Non biodégradable'), " +
                        "(uuid_generate_v4(), 'Coumarin', 'Agent parfumant', 'Allergènes reglementés en Europe et présent naturellement dans les huiles essentielles'), " +
                        "(uuid_generate_v4(), 'Benzisothiazolinone', 'Conservateur', 'Causes des irritations'), " +
                        "(uuid_generate_v4(), 'Chloromethylisothiazolinone', 'Conservateur', 'Allergènes puissants et irritants surtout pour les peaux sensibles'), " +
                        "(uuid_generate_v4(), 'Homopolymer', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'CETEARETH-25', 'Composé éthoxylé', 'Toxicité lors de la fabrication'), " +
                        "(uuid_generate_v4(), 'POLYVINYL ALCOHOL', 'Polymères de synthèse', 'Issus de procédé chimique lourd notamment un gaz toxique pour l’homme et la planète'), " +
                        "(uuid_generate_v4(), 'TITANIUM DIOXIDE', 'Colorant minéral/Dioxyde de titane', 'Cancérogènes possibles , réglementé dans les produits d’hygiène buccale'), " +
                        "(uuid_generate_v4(), 'alcohol ethoxylate', 'Composé éthoxylé', 'Toxicité lors de la fabrication')")
    ]
