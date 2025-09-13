import 'package:flutter/material.dart';

class CreateSessionOverlay extends StatelessWidget{
  const CreateSessionOverlay({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        padding: const EdgeInsets.all(20),
        color: Colors.blueGrey,
        child: const Text("test"),
      ),
    );
  }
}

void showCreateSessionOverlay(BuildContext context) {
  OverlayEntry overlayEntry = OverlayEntry(
    builder: (context) => const CreateSessionOverlay(),
  );

  Overlay.of(context).insert(overlayEntry);
}