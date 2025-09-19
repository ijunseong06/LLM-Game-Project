import 'package:flutter/material.dart';
import 'package:client/services/overlay_manager.dart';

class CreateNewSessionWidget extends StatelessWidget{
  final CreateSessionOverlayDI manager;
  const CreateNewSessionWidget({super.key, required this.manager});

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder(
      valueListenable: manager.state,
      builder: (context, isVisible, child) {
        if (isVisible) {
          return  manager.overlay;
        }
        return SizedBox.shrink();
      },
    );
  }
}