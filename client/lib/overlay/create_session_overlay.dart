import 'package:flutter/material.dart';
import 'package:client/l10n/app_localizations.dart';

class CreateSessionOverlay extends StatelessWidget {
  const CreateSessionOverlay({super.key});

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        Positioned(
          top: 100,
          bottom: 100,
          left: 24,
          right: 24,
          child: Material(
            elevation: 12.0,
            borderRadius: BorderRadius.circular(16.0),
            color: const Color(0xFF2D3748),
            child: Container(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    AppLocalizations.of(context)!.createSessionOverlay_header,
                    style: TextStyle(
                      fontSize: 22.0,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFFF7FAFC),
                    ),
                  ),
                  const SizedBox(height: 24.0),
                  TextField(
                    style: const TextStyle(color: Colors.white),
                    cursorColor: Colors.white70,
                    decoration: InputDecoration(
                      labelText: AppLocalizations.of(context)!.createSessionOverlay_inputField_sessionName,
                      hintText: '',
                      labelStyle: TextStyle(color: Colors.grey[400]),
                      hintStyle: TextStyle(color: Colors.grey[600]),
                      filled: true,
                      fillColor: const Color(0xFF4A5568),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12.0),
                        borderSide: BorderSide.none,
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12.0),
                        borderSide: BorderSide(color: Colors.blueGrey.shade300, width: 2.0),
                      ),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  TextField(
                    style: const TextStyle(color: Colors.white),
                    cursorColor: Colors.white70,
                    decoration: InputDecoration(
                      labelText: AppLocalizations.of(context)!.createSessionOverlay_inputField_sessionDesc,
                      hintText: '',
                      labelStyle: TextStyle(color: Colors.grey[400]),
                      hintStyle: TextStyle(color: Colors.grey[600]),
                      filled: true,
                      fillColor: const Color(0xFF4A5568),
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12.0),
                        borderSide: BorderSide.none,
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12.0),
                        borderSide: BorderSide(color: Colors.blueGrey.shade300, width: 2.0),
                      ),
                    ),
                  ),
                  const Spacer(),
                  ElevatedButton(
                    onPressed: () {},
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color.fromARGB(255, 171, 218, 241),
                      foregroundColor: const Color(0xFF1A202C),
                      shape: const CircleBorder(), // 버튼 모양을 원형으로 만듭니다.
                      padding: const EdgeInsets.all(16), // 원 안의 아이콘 여백을 설정합니다.
                      elevation: 4,
                    ),
                    child: const Icon(Icons.check_circle_outline),
                  )
                ],
              ),
            ),
          ),
        )
      ],
    );
  }
}