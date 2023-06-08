import 'package:flutter/material.dart';
import 'package:ir_project/api_service.dart';

class Search extends StatefulWidget {
  const Search({Key? key}) : super(key: key);

  @override
  State<Search> createState() => _SearchState();
}

class _SearchState extends State<Search> {
  TextEditingController id=TextEditingController();
  TextEditingController query=TextEditingController();
  List<dynamic> searchResults = [];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(
          child: Text(
            "Information Retrieval",
            style: TextStyle(color: Colors.white, fontSize: 20),
          ),
        ),
        backgroundColor: Colors.deepOrange,
      ),
      body: Column(
        children: [
          SizedBox(height: 100,),
          Padding(
            padding: const EdgeInsets.only(left: 300.0,right: 300),
            child: TextFormField(
              controller: id,


              onChanged: (val) {
                print(val);

              },
              cursorColor: Colors.deepOrange,
              decoration: InputDecoration(
                contentPadding:
                EdgeInsets.symmetric(vertical: 20),
                filled: true,
                fillColor: Colors.grey.shade50,
                hintText: 'Id',
                //hintStyle: searchStyle,
                prefixIcon: IconButton(
                  onPressed: () {
                   // controller.onSearchDoctors();
                    //    controller.search();
                  },
                  icon: Icon(Icons.numbers),
                  color: Colors.deepOrange,
                ),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15.0),
                  borderSide: BorderSide(color: Colors.grey),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey),
                  borderRadius: BorderRadius.circular(15.0),
                ),
              ),
            ),
          ),
          SizedBox(height: 50,),

          Padding(
            padding: const EdgeInsets.only(left: 300.0,right: 300),
            child: TextFormField(
              controller: query,

              onChanged: (val) {

                print(val);

              },
              cursorColor: Colors.deepOrange,
              decoration: InputDecoration(
                contentPadding:
                EdgeInsets.symmetric(vertical: 20),
                filled: true,
                fillColor: Colors.grey.shade50,
                hintText: 'Query',
                //hintStyle: searchStyle,
                prefixIcon: IconButton(
                  onPressed: () {
                    // controller.onSearchDoctors();
                    //    controller.search();
                  },
                  icon: Icon(Icons.text_fields),
                  color: Colors.deepOrange,
                ),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15.0),
                  borderSide: BorderSide(color: Colors.grey),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey),
                  borderRadius: BorderRadius.circular(15.0),
                ),
              ),
            ),
          ),

          SizedBox(height: 30,),
          ElevatedButton(
            onPressed: () async {

              final idText = id.text;
              final queryText = query.text;
              final results = await ApiService.search(idText, queryText);
              print(results);
              if (results != null && results.isNotEmpty) { // Check if results is not empty
                setState(() {
                  searchResults = results[1];
                });
              }

            },
            child: Text('Search'),
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all(Colors.orangeAccent),
            ),
          ),

          SizedBox(height: 50,),
          Expanded(
              child: ListView.builder(
                itemCount: searchResults.length,
                itemBuilder: (BuildContext context, int index) {
                  return  ListTile(
                      title: Text(searchResults[index][0]),
                      subtitle: Text(searchResults[index][1].toString()),
                    );
                },
              ),
            ),


        ],
      ),
    );
  }
}
