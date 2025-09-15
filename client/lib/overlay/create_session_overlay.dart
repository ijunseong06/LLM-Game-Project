import 'package:flutter/material.dart';

class CreateSessionOverlay extends StatefulWidget {
  final VoidCallback onClose;

  const CreateSessionOverlay({super.key, required this.onClose});

  @override
  State<CreateSessionOverlay> createState() => _CreateSessionOverlayState();
}

class _CreateSessionOverlayState extends State<CreateSessionOverlay> {
  final TextEditingController _sessionNameController = TextEditingController();
  final TextEditingController _playerNameController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.black54,
      child: Center(
        child: Container(
          width: 400,
          padding: const EdgeInsets.all(24.0),
          decoration: BoxDecoration(
            color: const Color(0xFF2E2E2E),
            borderRadius: BorderRadius.circular(12.0),
            border: Border.all(color: Colors.grey[700]!),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Create New Session',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 20),
              _buildTextField(
                controller: _sessionNameController,
                labelText: 'Session Name',
              ),
              const SizedBox(height: 16),
              _buildTextField(
                controller: _playerNameController,
                labelText: 'Player Name',
              ),
              const SizedBox(height: 24),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  TextButton(
                    onPressed: widget.onClose,
                    child: const Text('Cancel', style: TextStyle(color: Colors.white70)),
                  ),
                  const SizedBox(width: 12),
                  ElevatedButton(
                    onPressed: () {
                      // TODO: Implement session creation logic
                      widget.onClose();
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.deepPurple,
                      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(8.0),
                      ),
                    ),
                    child: const Text('Create', style: TextStyle(fontSize: 16, color: Colors.white)),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String labelText,
  }) {
    return TextField(
      controller: controller,
      style: const TextStyle(color: Colors.white),
      decoration: InputDecoration(
        labelText: labelText,
        labelStyle: const TextStyle(color: Colors.white70),
        filled: true,
        fillColor: Colors.black26,
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8.0),
          borderSide: BorderSide(color: Colors.grey[600]!),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8.0),
          borderSide: const BorderSide(color: Colors.deepPurple),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _sessionNameController.dispose();
    _playerNameController.dispose();
    super.dispose();
  }
}

OverlayEntry? _overlayEntry;

void showCreateSessionOverlay(BuildContext context) {
  if (_overlayEntry != null) {
    return;
  }
  _overlayEntry = OverlayEntry(
    builder: (context) => CreateSessionOverlay(onClose: hideCreateSessionOverlay),
  );

  Overlay.of(context).insert(_overlayEntry!);
}

void hideCreateSessionOverlay() {
  _overlayEntry?.remove();
  _overlayEntry = null;
}
