package proj;

public class Ingredient {
	public String nom;
	public Type type; 
	public int calorie;
	public String emplacement;
	public String getNom() {
		return nom;
	}
	public void setNom(String nom) {
		this.nom = nom;
	}
	public Ingredient(String nom, Type type, int calorie, String emplacement) {
		super();
		this.nom = nom;
		this.type = type;
		this.calorie = calorie;
		this.emplacement = emplacement;
	}
	public Type getType() {
		return type;
	}
	public void setType(Type type) {
		this.type = type;
	}
	public int getCalorie() {
		return calorie;
	}
	public void setCalorie(int calorie) {
		this.calorie = calorie;
	}
	public String getEmplacement() {
		return emplacement;
	}
	public void setEmplacement(String emplacement) {
		this.emplacement = emplacement;
	}
}
