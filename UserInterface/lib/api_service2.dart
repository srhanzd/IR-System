import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService2 {



  static Future<List<dynamic>> searchSecond(String id, String query) async {
    print("post method search 2");
    print("$query");
    String baseUrl='http://127.0.0.1:8001/SecondSearchApi/$id+${query}';
    final response = await http.post(
      Uri.parse('$baseUrl'),
      headers: {
        'accept':'application/json',
      }
    );
    print("aya");
    print('$baseUrl');
    print(response.statusCode);
    if (response.statusCode == 200) {
      final List<dynamic> body = jsonDecode(response.body);
      return body;
    } else {
      throw Exception('Failed to call search API');
    }
  }
}