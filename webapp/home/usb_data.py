classes = {0: {'name': '(Defined at Interface level)', 'subclasses': {}},
 1: {'name': 'Audio',
     'subclasses': {1: {'name': 'Control Device', 'protocols': {}},
                    2: {'name': 'Streaming', 'protocols': {}},
                    3: {'name': 'MIDI Streaming', 'protocols': {}}}},
 2: {'name': 'Communications',
     'subclasses': {1: {'name': 'Direct Line', 'protocols': {}},
                    2: {'name': 'Abstract (modem)',
                        'protocols': {0: 'None',
                                      1: 'AT-commands (v.25ter)',
                                      2: 'AT-commands (PCCA101)',
                                      3: 'AT-commands (PCCA101 + wakeup)',
                                      4: 'AT-commands (GSM)',
                                      5: 'AT-commands (3G)',
                                      6: 'AT-commands (CDMA)',
                                      254: 'Defined by command set descriptor',
                                      255: 'Vendor Specific (MSFT RNDIS?)'}},
                    3: {'name': 'Telephone', 'protocols': {}},
                    4: {'name': 'Multi-Channel', 'protocols': {}},
                    5: {'name': 'CAPI Control', 'protocols': {}},
                    6: {'name': 'Ethernet Networking', 'protocols': {}},
                    7: {'name': 'ATM Networking', 'protocols': {}},
                    8: {'name': 'Wireless Handset Control', 'protocols': {}},
                    9: {'name': 'Device Management', 'protocols': {}},
                    10: {'name': 'Mobile Direct Line', 'protocols': {}},
                    11: {'name': 'OBEX', 'protocols': {}},
                    12: {'name': 'Ethernet Emulation',
                         'protocols': {7: 'Ethernet Emulation (EEM)'}}}},
 3: {'name': 'Human Interface Device',
     'subclasses': {0: {'name': 'No Subclass',
                        'protocols': {0: 'None', 1: 'Keyboard', 2: 'Mouse'}},
                    1: {'name': 'Boot Interface Subclass',
                        'protocols': {0: 'None', 1: 'Keyboard', 2: 'Mouse'}}}},
 5: {'name': 'Physical Interface Device', 'subclasses': {}},
 6: {'name': 'Imaging',
     'subclasses': {1: {'name': 'Still Image Capture',
                        'protocols': {1: 'Picture Transfer Protocol (PIMA 15470)'}}}},
 7: {'name': 'Printer',
     'subclasses': {1: {'name': 'Printer',
                        'protocols': {0: 'Reserved/Undefined',
                                      1: 'Unidirectional',
                                      2: 'Bidirectional',
                                      3: 'IEEE 1284.4 compatible bidirectional',
                                      255: 'Vendor Specific'}}}},
 8: {'name': 'Mass Storage',
     'subclasses': {1: {'name': 'RBC (typically Flash)',
                        'protocols': {0: 'Control/Bulk/Interrupt',
                                      1: 'Control/Bulk',
                                      80: 'Bulk-Only'}},
                    2: {'name': 'SFF-8020i, MMC-2 (ATAPI)', 'protocols': {}},
                    3: {'name': 'QIC-157', 'protocols': {}},
                    4: {'name': 'Floppy (UFI)',
                        'protocols': {0: 'Control/Bulk/Interrupt',
                                      1: 'Control/Bulk',
                                      80: 'Bulk-Only'}},
                    5: {'name': 'SFF-8070i', 'protocols': {}},
                    6: {'name': 'SCSI',
                        'protocols': {0: 'Control/Bulk/Interrupt',
                                      1: 'Control/Bulk',
                                      80: 'Bulk-Only'}}}},
 9: {'name': 'Hub',
     'subclasses': {0: {'name': 'Unused',
                        'protocols': {0: 'Full speed (or root) hub',
                                      1: 'Single TT',
                                      2: 'TT per port'}}}},
 10: {'name': 'CDC Data',
      'subclasses': {0: {'name': 'Unused',
                         'protocols': {48: 'I.430 ISDN BRI',
                                       49: 'HDLC',
                                       50: 'Transparent',
                                       80: 'Q.921M',
                                       81: 'Q.921',
                                       82: 'Q.921TM',
                                       144: 'V.42bis',
                                       145: 'Q.932 EuroISDN',
                                       146: 'V.120 V.24 rate ISDN',
                                       147: 'CAPI 2.0',
                                       253: 'Host Based Driver',
                                       254: 'CDC PUF',
                                       255: 'Vendor specific'}}}},
 11: {'name': 'Chip/SmartCard', 'subclasses': {}},
 13: {'name': 'Content Security', 'subclasses': {}},
 14: {'name': 'Video',
      'subclasses': {0: {'name': 'Undefined', 'protocols': {}},
                     1: {'name': 'Video Control', 'protocols': {}},
                     2: {'name': 'Video Streaming', 'protocols': {}},
                     3: {'name': 'Video Interface Collection',
                         'protocols': {}}}},
 88: {'name': 'Xbox',
      'subclasses': {66: {'name': 'Controller', 'protocols': {}}}},
 220: {'name': 'Diagnostic',
       'subclasses': {1: {'name': 'Reprogrammable Diagnostics',
                          'protocols': {1: 'USB2 Compliance'}}}},
 224: {'name': 'Wireless',
       'subclasses': {1: {'name': 'Radio Frequency',
                          'protocols': {1: 'Bluetooth',
                                        2: 'Ultra WideBand Radio Control',
                                        3: 'RNDIS'}},
                      2: {'name': 'Wireless USB Wire Adapter',
                          'protocols': {1: 'Host Wire Adapter Control/Data Streaming',
                                        2: 'Device Wire Adapter Control/Data Streaming',
                                        3: 'Device Wire Adapter Isochronous Streaming'}}}},
 239: {'name': 'Miscellaneous Device',
       'subclasses': {1: {'name': '?',
                          'protocols': {1: 'Microsoft ActiveSync',
                                        2: 'Palm Sync'}},
                      2: {'name': '?',
                          'protocols': {1: 'Interface Association',
                                        2: 'Wire Adapter Multifunction Peripheral'}},
                      3: {'name': '?',
                          'protocols': {1: 'Cable Based Association'}},
                      5: {'name': 'USB3 Vision', 'protocols': {}}}},
 254: {'name': 'Application Specific Interface',
       'subclasses': {1: {'name': 'Device Firmware Update', 'protocols': {}},
                      2: {'name': 'IRDA Bridge', 'protocols': {}},
                      3: {'name': 'Test and Measurement',
                          'protocols': {1: 'TMC', 2: 'USB488'}}}},
 255: {'name': 'Vendor Specific Class',
       'subclasses': {255: {'name': 'Vendor Specific Subclass',
                            'protocols': {255: 'Vendor Specific Protocol'}}}}}
