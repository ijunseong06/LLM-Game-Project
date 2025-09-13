import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:client/overlay/create_session_overlay.dart';

class CreateNewSessionButton extends StatelessWidget {
  const CreateNewSessionButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.end,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Padding(
          padding: const EdgeInsets.fromLTRB(0, 0, 3, 5),
          child: IconButton(
            icon: SvgPicture.asset('assets/icons/Add.svg', width: 30, height: 30,),
            hoverColor: Colors.blueAccent,
            onPressed: () => showCreateSessionOverlay(context),
          ),
        ),
      ],
    );
  }
}