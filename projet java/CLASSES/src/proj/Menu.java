package proj;

public class Menu {
	public String nom;
	private String  Recette;

	public Menu(String nom, String recette) {
		super();
		this.nom = nom;
		Recette = recette;
	}

	public String getNomMenu() {
		return nom;
	}

	public void setNomMenu(String nom) {
		this.nom = nom;
	}

	public String getRecette() {
		return Recette;
	}

	public void setRecette(String recette) {
		Recette = recette;
	}
	
 
	
}
