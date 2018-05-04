package proj;

import java.sql.PreparedStatement;

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
		connect();
		insert(nomPlat);
	}
	public void AfficherPlat() {
		
	}
	private Connection connect() {
        // SQLite connection string
        String url = "jdbc:sqlite:STOCK.db";
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url);
            System.out.print("OK");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return conn;
    }
    public void insert(String name,String type) {
        String sql = "INSERT INTO plat(nom text,type text) VALUES(?,?)";
 
        try (Connection conn = this.connect();
                PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(name);
            pstmt.setString(type);
            pstmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    public static void main (Args[] String) {
    	
    }

}
