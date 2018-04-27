package proj;

public class Recette {
  
	public int dureeCuisson;
	public String Description;
	public String ListeQuantite  ; 
	public int DureePreparation;
	public String ListeIngredient;
	public int CalPArPersonne;
	public String Difficulte;
	
	public void CalculCalories() {
		
	}
	public void Disponibilite() {
		
	}
	public void VoirRecette() {
		
	}
	public Recette(int dureeCuisson, String description, String listeQuantite, int dureePreparation,
			String listeIngredient, int calPArPersonne, String difficulte) {
		super();
		this.dureeCuisson = dureeCuisson;
		Description = description;
		ListeQuantite = listeQuantite;
		DureePreparation = dureePreparation;
		ListeIngredient = listeIngredient;
		CalPArPersonne = calPArPersonne;
		Difficulte = difficulte;
	}
	public int getDureeCuisson() {
		return dureeCuisson;
	}
	public void setDureeCuisson(int dureeCuisson) {
		this.dureeCuisson = dureeCuisson;
	}
	public String getDescription() {
		return Description;
	}
	public void setDescription(String description) {
		Description = description;
	}
	public String getListeQuantite() {
		return ListeQuantite;
	}
	public void setListeQuantite(String listeQuantite) {
		ListeQuantite = listeQuantite;
	}
	public int getDureePreparation() {
		return DureePreparation;
	}
	public void setDureePreparation(int dureePreparation) {
		DureePreparation = dureePreparation;
	}
	public String getListeIngredient() {
		return ListeIngredient;
	}
	public void setListeIngredient(String listeIngredient) {
		ListeIngredient = listeIngredient;
	}
	public int getCalPArPersonne() {
		return CalPArPersonne;
	}
	public void setCalPArPersonne(int calPArPersonne) {
		CalPArPersonne = calPArPersonne;
	}
	public String getDifficulte() {
		return Difficulte;
	}
	public void setDifficulte(String difficulte) {
		Difficulte = difficulte;
	}
	 
}
