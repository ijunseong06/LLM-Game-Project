import 'package:flutter/material.dart';

class CreateSessionOverlay extends StatelessWidget{
  const CreateSessionOverlay({super.key});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Positioned(
          top: 10,
          bottom: 10,
          left: 10,
          right: 10,
          child: Container(),
        )
      ],
    );
  }
}