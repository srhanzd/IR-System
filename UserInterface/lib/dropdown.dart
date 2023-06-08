import 'package:flutter/material.dart';
import 'package:ir_project/search.dart';
import 'package:ir_project/search2.dart';

class DropDownButton extends StatefulWidget {
  const DropDownButton({Key? key}) : super(key: key);

  @override
  _DropDownButtonState createState() => _DropDownButtonState();
}

class _DropDownButtonState extends State<DropDownButton> {
  List<String> datasets = ["Mr-tydi", "Antique/train"];
  String _selectedDataset = "Mr-tydi";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton:Center(
        child: FloatingActionButton.extended(
          onPressed: () {
            if(_selectedDataset.isNotEmpty)
              {
                if(_selectedDataset=="Antique/train")
                  {
                    Navigator.push(context,  MaterialPageRoute(builder: (context) => Search()),);
                  }
                else if(_selectedDataset=="Mr-tydi")
                  {
                    Navigator.push(context,  MaterialPageRoute(builder: (context) => SearchTwo()),);
                  }
              }

            },
          icon: Icon(Icons.navigate_next_sharp),
          label: Text("Next"),
          backgroundColor: Colors.yellow.shade900,
        ),
      ),
      appBar: AppBar(
        title: const Center(
          child: Text(
            "Information Retrieval",
            style: TextStyle(color: Colors.white, fontSize: 20),
          ),
        ),
        backgroundColor: Colors.deepOrange,
      ),
      body: Center(
        child: Column(
          children: [
            const SizedBox(
              height: 60,
            ),
            const Text(
              "Choose Dataset",
              style: TextStyle(color: Colors.black45, fontSize: 20),
            ),
            const SizedBox(
              height: 30,
            ),
            DropdownButton(
              value: _selectedDataset,
              items: datasets.map((dataset) {
                return DropdownMenuItem(
                  child: Text(dataset),
                  value: dataset,
                );
              }).toList(),
              onChanged: (newValue) {
                setState(() {
                  _selectedDataset = newValue.toString();
                });
                print("You selected: $_selectedDataset");
              },
            ),

            SizedBox(height: 60,),


          ],
        ),
      ),
    );
  }
}