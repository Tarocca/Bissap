package proj;

public class Plat {
	public String nomPlat;
	public Type type;
	
	
	public String getNomPlat() {
		return nomPlat;
	}
	public void setNomPlat(String nomPlat) {
		this.nomPlat = nomPlat;
	}
	public Type getType() {
		return type;
	}
	public void setType(Type type) {
		this.type = type;
	}
	public Plat(String nomPlat, Type type) {
		super();
		this.nomPlat = nomPlat;
		this.type = type;
	}
	public void AfficherPlat() {
		
	}

}
