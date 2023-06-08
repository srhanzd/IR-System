import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService {


  static Future<List<dynamic>> search(String id, String query) async {
    print("post method search 1");
    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/SearchApi/$id+$query'),
    );
    print(response.statusCode);
    if (response.statusCode == 200) {
      final List<dynamic> body = jsonDecode(response.body);
      return body;
    } else {
      throw Exception('Failed to call search API');
    }
  }

}
