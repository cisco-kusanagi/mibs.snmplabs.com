#
# PySNMP MIB module CARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CARD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:46:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
coriolisMibs, card = mibBuilder.importSymbols("CORIOLIS-MIB", "coriolisMibs", "card")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, TimeTicks, iso, ModuleIdentity, ObjectIdentity, Bits, NotificationType, Unsigned32, Counter64, Counter32, Gauge32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "iso", "ModuleIdentity", "ObjectIdentity", "Bits", "NotificationType", "Unsigned32", "Counter64", "Counter32", "Gauge32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
cardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5812, 2, 1))
if mibBuilder.loadTexts: cardMIB.setLastUpdated('0007270000Z')
if mibBuilder.loadTexts: cardMIB.setOrganization('Coriolis Networks')
if mibBuilder.loadTexts: cardMIB.setContactInfo(' Shubhra Garg Postal: 330 Codman Hill Road, Boxboro MA, 01719. Tel: +1 978 264 1904 Fax: +1 978 264 1929 E-mail: shubhra@coriolisnet.com')
if mibBuilder.loadTexts: cardMIB.setDescription('The MIB module for cards in coriolis boxes')
cardCount = MibScalar((1, 3, 6, 1, 4, 1, 5812, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 26))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCount.setStatus('current')
if mibBuilder.loadTexts: cardCount.setDescription(' The number of active cards in the device')
cardEEPromTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 3), )
if mibBuilder.loadTexts: cardEEPromTable.setStatus('current')
if mibBuilder.loadTexts: cardEEPromTable.setDescription('The table containing various kinds of card information')
cardEEPromEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: cardEEPromEntry.setStatus('current')
if mibBuilder.loadTexts: cardEEPromEntry.setDescription('Entry containing information about a card in the system.')
slotNo = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 26)))
if mibBuilder.loadTexts: slotNo.setStatus('current')
if mibBuilder.loadTexts: slotNo.setDescription('This variable is used as an index in all card tables')
cardSIDFVer = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSIDFVer.setStatus('current')
if mibBuilder.loadTexts: cardSIDFVer.setDescription(' SID ROM Version of the SID-ROM format which represents the 1st 20 bytes with a 1 byte value. This variable is used only during the boot process when a sanity check is made. If the current version is 0xF0 (which indicates the initial version), then the next version would be 0xE1 and so on.')
cardHwType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28))).clone(namedValues=NamedValues(("mm", 1), ("smOSU", 2), ("rx1310", 4), ("tx1310", 5), ("rxDWDM", 6), ("txDWDM", 7), ("eth16", 8), ("atmOC3c", 9), ("atmOC12c", 10), ("tdmDS1", 11), ("tdmDS3", 12), ("tdmOC3c", 13), ("tdmOC12c", 14), ("gigio", 16), ("smOTU", 17), ("dwdmOSU", 18), ("thirteenTenOSU", 19), ("csOSU", 20), ("oauEth16Gig1FX", 21), ("fmOTU", 22), ("dwdmOSU14", 23), ("thirteenTenOSU14", 24), ("oauEth16DS1Fx", 25), ("oauGig4Fx", 26), ("posOC12c", 27), ("posOC48c", 28)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHwType.setStatus('current')
if mibBuilder.loadTexts: cardHwType.setDescription(' An object which uniquely identifies the card type.')
cardHwSubType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardHwSubType.setStatus('current')
if mibBuilder.loadTexts: cardHwSubType.setDescription("Identifies the functional revision of this card. Example: Suppose a card's hardware could be configured with internal or external timing modes and suppose firmware initialization differed depending on the type of timing mode configured on the card hardware, then the value of the hardware subtype object could be used by firmware to initialize to the appropriate timing mode.")
cardImageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 3), ValueRangeConstraint(4, 4), ValueRangeConstraint(5, 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardImageType.setStatus('current')
if mibBuilder.loadTexts: cardImageType.setDescription('An object which identifies the bootrom and system images to running on a card. This object only applies to card types with on-board processor. The values are: 0 - card without CPU or image. 3 - Management Module 4 - OptiFlow 3000/3500 Switch Module and OptiFlow 5000/5500 Switch Module 5 - OptiFlow 1010 (Pizza Box)')
cardMACaddressNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardMACaddressNum.setStatus('current')
if mibBuilder.loadTexts: cardMACaddressNum.setDescription(' Indicates the number of MAC Addresses allocated to this module. Current values range from 0 to 64. This value is 0 when not applicable.')
cardMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardMacAddress.setStatus('current')
if mibBuilder.loadTexts: cardMacAddress.setDescription(' Stores the starting MAC Address for this module. All 6 bytes are zero when not applicable. ')
cardAssemblyClass = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyClass.setStatus('current')
if mibBuilder.loadTexts: cardAssemblyClass.setDescription(" Identifies the hardware class. This field is a duplicate of the assembly class portion of the assembly number. It is stored and displayed in Binary Encoded Decimal (BCD) format. The following list provide some of the Assembly Class and its description: 04 Mechanical Assembly Drawing (Legacy Only) 10 Discrete Resistors 11 Resistor Networks 14 Capacitors 16 Crystals 17 Oscillators 18 Magnetic Modules (inductors, filters, ferrites, power chokes, transformers) 20 Active Components 21 Transistors, Diodes, FET's 22 Mechanical Hardware (Legacy Only) 23 Connectors 24 Electromechanical Components (switches, motors, fans) 26 Circuit Protection Devices (Fuses, PTC) 27 Power Components (power supplies, fuses, line filters) 30 LED's 31 Logic Components 32 Memory 34 Application Specific 36 Optical Component (Active, Passive) 38 Programmable Device (Raw device prior to programming) 40 Module Assemblies (Secondary Assy Required i.e., Optics) 42 Mechanical Fasteners (Screws, Washers, Nuts, Tywraps) 43 Labels 44 Wire & Cable 46 Packaging (Shipping Materials) 47 Manuals (HW, SW, Release Notes, Misc) 50 PCB Assemblies 51 Schematic 54 Printed Circuit Boards 60 Cable Assemblies 70 Mechanical / Electromechanical Assemblies (Chassis, Fan Tray) 72 Fabricated Components 74 Sub Assembly (Legacy Only) 75 Finished Assembly 80 PLD Files 82 FPGA Code 84 Operational Software 85 Programmed Device Assembly 86 PLD Daisy Chain Test File 99 Rework Instructions ")
cardAssemblyId = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyId.setStatus('current')
if mibBuilder.loadTexts: cardAssemblyId.setDescription('Identifies the module type. This field is a duplicate of the assembly identifier portion of the assembly number. It is stored and displayed in Binary Encoded Decimal (BCD) format. It has the following format: NN -1234 -NN RevNo | | | |____ Part Revision Number | | | | | |_________ Suffix = PartID (01-99) | | | |______________ Main Body = Sequential No. (0001 - 9999) | |___________________ Prefix = Part Class Number or Tab Number (01 - 99).')
cardAssemblyTabNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyTabNum.setStatus('current')
if mibBuilder.loadTexts: cardAssemblyTabNum.setDescription(" This field is a duplicate of the assembly tab number portion of the assembly number. It is stored and displayed in Binary Encoded Decimal (BCD) format. For Example, a Part Number like '60-3456-01' has the Tab Number -01. All new parts are released a tab number of -01. If a new member of a family of harwareType is introduced, then the tab number would be incremented. Its range is 01 - 99.")
cardAssemblyRev = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyRev.setStatus('current')
if mibBuilder.loadTexts: cardAssemblyRev.setDescription(" Identifies the assembly revision of the module. This field is a duplicate of the assembly revision field. It is stored and displayed in Binary Encoded Decimal (BCD) format. For example, a typical AssemblyID would be like '54-0001-01 Rev 2'.")
cardbrchecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardbrchecksum.setStatus('current')
if mibBuilder.loadTexts: cardbrchecksum.setDescription(' Contains a checksum calculated over the first 16 bytes of SID ROM data.')
cardSIDInfoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSIDInfoVersion.setStatus('current')
if mibBuilder.loadTexts: cardSIDInfoVersion.setDescription('Reflects the revision level of the information portion of the SID-ROM data.')
cardSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardSerialNum.setStatus('current')
if mibBuilder.loadTexts: cardSerialNum.setDescription(' Stores a 12 digit serial number associated with a module. (example: PLX1100-0100).')
cardAssemblyNumString = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyNumString.setStatus('current')
if mibBuilder.loadTexts: cardAssemblyNumString.setDescription(" Module's assembly number.")
cardAssemblyRevString = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 16), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardAssemblyRevString.setStatus('current')
if mibBuilder.loadTexts: cardAssemblyRevString.setDescription('Revision level of the card.')
cardCLEICode = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 17), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCLEICode.setStatus('current')
if mibBuilder.loadTexts: cardCLEICode.setDescription(' Stores an ASCII String duplicating CLEI (Common Language Equipment Identifier ) Code encoded into the bar code. 10 ASCII characters of CLEI code ')
cardCLEIECICode = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardCLEIECICode.setStatus('current')
if mibBuilder.loadTexts: cardCLEIECICode.setDescription(' Stores an ASCII String duplicating CLEI ECI (Equipment Catalog Item) Code encoded into the bar code. Bar Code in numeric form ')
cardChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 3, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cardChecksum.setStatus('current')
if mibBuilder.loadTexts: cardChecksum.setDescription(' Contains a checksum calculated over the previous 252 bytes of SID ROM data.')
slotTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 4), )
if mibBuilder.loadTexts: slotTable.setStatus('current')
if mibBuilder.loadTexts: slotTable.setDescription('The slot table')
slotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: slotEntry.setStatus('current')
if mibBuilder.loadTexts: slotEntry.setDescription('Entry containing information about a slot in the system.')
slotAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotAdminState.setStatus('current')
if mibBuilder.loadTexts: slotAdminState.setDescription(' The slot admin state ')
slotOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("removed", 0), ("syncWait", 1), ("synced", 2), ("syncFailed", 3), ("configStarted", 4), ("configFailed", 5), ("configed", 6), ("ready", 7), ("waitSM", 8), ("waitDeconfig", 9), ("designModeReady", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotOperState.setStatus('current')
if mibBuilder.loadTexts: slotOperState.setDescription(' The slot oper state. removed - card not in slot and not connected syncWait - card in slot waiting for syncPoint synced - card passed a syncPoint syncFailed - card failed a syncPoint configStarted - configuration started configFailed - configuration failed configed - configuration passed ready - card ready for normal operation waitSM - card waiting for SM reboot waitDeconfig - waiting for deconfiguration to complete designModeReady - card is configured but removed.')
slotType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("mmSlot", 1), ("optiFlow3xSMSlot", 2), ("optiFlow5xSMSlot", 3), ("regularIOSlot", 4), ("optiFlow3xSlotNumber1", 5), ("colorSeparator", 6), ("optiFlow3xOpticsSlot", 7), ("optiFlow5xOpticsSlotType1", 8), ("optiFlow5xOpticsSlotType2", 9), ("optiFlow5xFramerModuleSlot", 10), ("oauEth", 11), ("oauGig", 12), ("oauMM", 13), ("oauSM", 14), ("oauOptics", 15)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotType.setStatus('current')
if mibBuilder.loadTexts: slotType.setDescription(' The type of slot for this device. The following is a list of different kinds of slots: 1 - MMSlot (9,10 for optiFlow3X and 13,14 for optiFlow5x) 2 - optiFlow3xSMSlot (goes into slot 12) 3 - optiFlow5xSMSlot (goes into slots 7,9,18,20) 4 - regularIOSlot (goes into slots 3-6 in optiFlow3x, 1-6, 21-26 in optiFlow5x) The different types of cards that goes into this regular IO Slot are: A - 10/100 Ethernet B - Gigbit Ethernet C - DS1 TDM D - DS3 TDM E - OC12 ATM/POS F - OC12 TDM G - OC3 ATM H - OC48 POS I - Color Separator 5 - optiFlow3xSlotNumber1 The different types of cards that goes into this slot are: A - DS1 TDM B - DS3 TDM C - OC12 TDM 6 - optiFlow5x IO This type of slot takes: A - OC12 TDM (slots 5 and 21) 7 - optiFlow3x OpticsSlot (slots 11 and 12) This slot takes in: A - 1310TxRx B - 8 different cards with different lambdas (optiFlow3x OADM optics) C - 1550 TxRx 8 - optiFlow5x OpticsSlotType1 (slots 12 and 15 - Tx Only) This slot takes in: A - 1310 Tx / DWDM B - 8 different cards with different lambdas for DWDM Tx C - 1310 Tx D - 1550 Tx 9 - optiFlow5x OpticsSlotType2 (slots 11 and 16 - Rx only) This slot takes in: A - 1310 Rx / DWDM B - 8 different cards with different lambdas for DWDM Rx C - 1310 Rx 10 - optiFlow5x FM (goes into slots 8, 10, 17 and 19) 11 - colorSeparator (goes into slot 2 for OptiFlow3x) For an OAU, the slots are abstracted in the following manner: Slot 1 - IO (Eth16) Slot 2 - IO (GigIo) Slot 3 - MM Slot 4 - SM Slot 5 - OpRxTx')
slotCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))).clone(namedValues=NamedValues(("mm", 1), ("smOSU", 2), ("smISM", 3), ("rx1310", 4), ("tx1310", 5), ("rxDWDM", 6), ("txDWDM", 7), ("eth16", 8), ("atmOC3c", 9), ("atmOC12c", 10), ("tdmDS1", 11), ("tdmDS3", 12), ("tdmOC3c", 13), ("tdmOC12c", 14), ("islgmac", 15), ("gigio", 16), ("smOTU", 17), ("dwdmOSU", 18), ("thirteenTenOSU", 19), ("csOSU", 20), ("oauEth16Gig1Fx", 21), ("oauFmOTU", 22), ("osu14DWDM", 23), ("thirteenTenOSU14", 24), ("oauEth16Ds1Fx", 25), ("oauGig4Fx", 26), ("posOC12c", 27), ("posOC48c", 28), ("fifteenFiftyOSU14", 29), ("tx1550", 30), ("oau1550Eth16Gig1Fx", 31)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotCardType.setStatus('current')
if mibBuilder.loadTexts: slotCardType.setDescription(' The type of card in the slot ')
slotConnectionSize = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("auto", 0), ("sm8", 1), ("sm16", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotConnectionSize.setStatus('current')
if mibBuilder.loadTexts: slotConnectionSize.setDescription(' The connection size to SM ')
slotSMSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slotSMSlot.setStatus('current')
if mibBuilder.loadTexts: slotSMSlot.setDescription(' SM slot that this slot is connected to ')
slotInsertState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotInsertState.setStatus('current')
if mibBuilder.loadTexts: slotInsertState.setDescription(' Whether a card is present in the slot or not ')
slotFileState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("created", 1), ("ready", 2), ("locked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slotFileState.setStatus('current')
if mibBuilder.loadTexts: slotFileState.setDescription(' File locked or not ')
slotModuleChangeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("inserted", 1), ("removed", 2), ("failure", 3), ("failover", 4), ("configured", 5), ("syncpointFailure", 6), ("configFailure", 7), ("configDeleted", 8), ("configFailCardTypeMismatch", 9), ("configFailSMNotAvailable", 10), ("configFailOutOfSwitchPorts", 11), ("moduleConfigurationCorrupt", 12), ("warmBoot", 13)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotModuleChangeStatus.setStatus('current')
if mibBuilder.loadTexts: slotModuleChangeStatus.setDescription(" This variable is sent out in a module change event to communicate what happened to the module.The 'FAILURE' and 'FAILOVER' values are used by the mmr task to report failover events. The 'INSERTED' and 'REMOVED' values are used by AI to report module configuration and de-configuration events. The 'INSERTED' event will change to be reported whenever a card is inserted. The 'CONFIGURED' event will be reported when the card completes chassis configuration. The 'REMOVED' event will be reported whenever a card is removed. The events 'SYNCPOINT_FAILURE' and 'CONFIG_FAILURE' will be reported when a card fails syncPoints or chassis configuration respectively. The event 'CONFIG_DELETED' will be reported when a card configuration file is deleted (indicating the card configuration has been lost). ")
slotModuleTempStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("hot", 1), ("normal", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotModuleTempStatus.setStatus('current')
if mibBuilder.loadTexts: slotModuleTempStatus.setDescription('Indicates the temperature status of the module in the slot')
slotIoCardStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unresponsive", 1), ("responsive", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotIoCardStatus.setStatus('current')
if mibBuilder.loadTexts: slotIoCardStatus.setDescription('Indicates the responsiveness status of the module in the slot')
slotFlashThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 12), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotFlashThreshold.setStatus('current')
if mibBuilder.loadTexts: slotFlashThreshold.setDescription('Indicates the flash threshold, applicable for only the active and standby management modules')
slotFlashSectorsOverThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 4, 1, 13), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: slotFlashSectorsOverThreshold.setStatus('current')
if mibBuilder.loadTexts: slotFlashSectorsOverThreshold.setDescription('Indicates the number of sectors over threshold, applicable for only the active and standby MMs')
tdmIoCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 5), )
if mibBuilder.loadTexts: tdmIoCardTable.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardTable.setDescription('The table for TDM IO cards')
tdmIoCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: tdmIoCardEntry.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardEntry.setDescription('Entry containing information about an TDM IO module - DS1/DS3/E1/E3')
tdmIoCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("ds1", 1), ("ds3", 2), ("oc3", 3), ("oc12", 4), ("e1", 5), ("e3", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardType.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardType.setDescription('The type of the TDM IO module')
tdmIoCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmIoCardOperState.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardOperState.setDescription('The oper state of the TDM IO module')
tdmIoCardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unchannelized", 1), ("channelized", 2), ("sts1mode", 3), ("au3mode", 4), ("ds3ClearChannel", 5), ("ds3Channelized", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardMode.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardMode.setDescription('Whether this is an unchannelized or channelized module')
tdmIoCardConfiguredPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tdmIoCardConfiguredPorts.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardConfiguredPorts.setDescription("Bitmap of ports configured on the module. The bit positions of the 1 bits in the binary form of this number give the ports configured in this card. For example, if all the 3 ports of a DS3 card are configured, you'll get a value of 14 which in binary gives 1110. If 1st and 3rd are configured, you'll see 10 (1010). For a DS1 card, if all 16 ports are configured, you'll a value of 131070. The number of 1's in the binary representation of the value gives the number of configured ports.")
tdmIoCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardRowStatus.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardRowStatus.setDescription(' This variable is used to create or delete instances of TDM IO cards. This variable subsumes the admin state variable, and once the row is created, its value returns the admin state of the card')
tdmIoCardNumPMIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 5, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tdmIoCardNumPMIntervals.setStatus('current')
if mibBuilder.loadTexts: tdmIoCardNumPMIntervals.setDescription('This is the number of performance monitoring intervals for the ports on this card')
etherCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 6), )
if mibBuilder.loadTexts: etherCardTable.setStatus('current')
if mibBuilder.loadTexts: etherCardTable.setDescription('The table for ethernet cards')
etherCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: etherCardEntry.setStatus('current')
if mibBuilder.loadTexts: etherCardEntry.setDescription('Entry containing information about an ethernet module')
etherCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCardOperState.setStatus('current')
if mibBuilder.loadTexts: etherCardOperState.setDescription(' The oper state of the ethernet module ')
etherCardActivePortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherCardActivePortMask.setStatus('current')
if mibBuilder.loadTexts: etherCardActivePortMask.setDescription(' This returns a mask of active ports. An active port is one that has been created via a Port Create MO. A value of 1 in bit position N-1 indicates that port N has been created. For example, if port 1 has been created, then bit 0 is asserted. Since there are 16 ports, this can take the range of values from 0 to 65535.')
etherCardPhyResetState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inReset", 1), ("outOfReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherCardPhyResetState.setStatus('current')
if mibBuilder.loadTexts: etherCardPhyResetState.setDescription(' The phy reset state of the module ')
etherCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherCardRowStatus.setStatus('current')
if mibBuilder.loadTexts: etherCardRowStatus.setDescription(' This variable is used to create or delete instances of ethernet cards. This variable subsumes the admin state variable, and once the row is created, its value returns the admin state of the card')
atmCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 7), )
if mibBuilder.loadTexts: atmCardTable.setStatus('current')
if mibBuilder.loadTexts: atmCardTable.setDescription('The table for atm cards')
atmCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: atmCardEntry.setStatus('current')
if mibBuilder.loadTexts: atmCardEntry.setDescription('Entry containing information about an atm module')
atmCardOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardOperState.setStatus('current')
if mibBuilder.loadTexts: atmCardOperState.setDescription(' The oper state of the atm module ')
atmCardActivePortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmCardActivePortMask.setStatus('current')
if mibBuilder.loadTexts: atmCardActivePortMask.setDescription('This returns a mask of active ports. An active port is one that has been created via a Port Create MO. A value of 1 in bit position N-1 indicates that port N has been created. For example, if port 1 has been created, then bit 0 is asserted. Since there are 2 ports for an ATM card, this can take the range of values from 0 to 3.')
atmCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmCardRowStatus.setStatus('current')
if mibBuilder.loadTexts: atmCardRowStatus.setDescription(' This variable is used to create or delete instances of atm cards. This variable subsumes the admin state variable, and once the row is created, its value returns the admin state of the card')
opticalCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 8), )
if mibBuilder.loadTexts: opticalCardTable.setStatus('current')
if mibBuilder.loadTexts: opticalCardTable.setDescription('The table for optical cards')
opticalCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: opticalCardEntry.setStatus('current')
if mibBuilder.loadTexts: opticalCardEntry.setDescription('Entry containing information about an optical module')
opticalCardSlotType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rxOTU", 1), ("txOTU", 2), ("txRxOSU", 3), ("txRxOSU14", 4), ("oauEth16Gig1", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opticalCardSlotType.setStatus('current')
if mibBuilder.loadTexts: opticalCardSlotType.setDescription(' The type of module - transmitter or receiver ')
opticalCardOpticsType = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dwdm", 1), ("thirteenTen", 2), ("fifteenFifty", 3), ("thirteenTenFifteenFifty", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opticalCardOpticsType.setStatus('current')
if mibBuilder.loadTexts: opticalCardOpticsType.setDescription(' The type of optics on the module ')
opticalCardRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 6))).clone(namedValues=NamedValues(("createAndGo", 4), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: opticalCardRowStatus.setStatus('current')
if mibBuilder.loadTexts: opticalCardRowStatus.setDescription(' This variable is used to create or delete instances of optical cards')
posCardTable = MibTable((1, 3, 6, 1, 4, 1, 5812, 2, 9), )
if mibBuilder.loadTexts: posCardTable.setStatus('current')
if mibBuilder.loadTexts: posCardTable.setDescription('The table for pos cards')
posCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5812, 2, 9, 1), ).setIndexNames((0, "CARD-MIB", "slotNo"))
if mibBuilder.loadTexts: posCardEntry.setStatus('current')
if mibBuilder.loadTexts: posCardEntry.setDescription('Entry containing information about an pos module')
posCardActivePortMask = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: posCardActivePortMask.setStatus('current')
if mibBuilder.loadTexts: posCardActivePortMask.setDescription(' Bitmap describing the active ports on this pos module ')
posCardPhyResetState = MibTableColumn((1, 3, 6, 1, 4, 1, 5812, 2, 9, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inReset", 1), ("outOfReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: posCardPhyResetState.setStatus('current')
if mibBuilder.loadTexts: posCardPhyResetState.setDescription(' The phy reset state of the module ')
moduleStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,2)).setObjects(("CARD-MIB", "slotModuleChangeStatus"), ("CARD-MIB", "cardHwType"))
if mibBuilder.loadTexts: moduleStatusChange.setDescription(' Change in the operational state of a module. 1 means the module went down, 2 means it went up ')
moduleTempChange = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,44)).setObjects(("CARD-MIB", "slotModuleTempStatus"))
if mibBuilder.loadTexts: moduleTempChange.setDescription('Indicates temperature (hot/normal) in the chassis.')
ioCardStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,45)).setObjects(("CARD-MIB", "slotIoCardStatus"))
if mibBuilder.loadTexts: ioCardStatusChange.setDescription('Indicates the failure of IO card to respond.')
emFlashLife = NotificationType((1, 3, 6, 1, 4, 1, 5812) + (0,46)).setObjects(("CARD-MIB", "slotFlashThreshold"), ("CARD-MIB", "slotFlashSectorsOverThreshold"))
if mibBuilder.loadTexts: emFlashLife.setDescription('Flash End-of-life alarm.')
mibBuilder.exportSymbols("CARD-MIB", tdmIoCardRowStatus=tdmIoCardRowStatus, moduleTempChange=moduleTempChange, tdmIoCardOperState=tdmIoCardOperState, cardCLEICode=cardCLEICode, slotOperState=slotOperState, slotSMSlot=slotSMSlot, atmCardEntry=atmCardEntry, posCardTable=posCardTable, ioCardStatusChange=ioCardStatusChange, slotConnectionSize=slotConnectionSize, emFlashLife=emFlashLife, cardSIDInfoVersion=cardSIDInfoVersion, cardbrchecksum=cardbrchecksum, cardAssemblyTabNum=cardAssemblyTabNum, tdmIoCardNumPMIntervals=tdmIoCardNumPMIntervals, opticalCardRowStatus=opticalCardRowStatus, slotNo=slotNo, PYSNMP_MODULE_ID=cardMIB, slotModuleChangeStatus=slotModuleChangeStatus, slotType=slotType, slotFlashSectorsOverThreshold=slotFlashSectorsOverThreshold, atmCardActivePortMask=atmCardActivePortMask, slotEntry=slotEntry, opticalCardSlotType=opticalCardSlotType, tdmIoCardConfiguredPorts=tdmIoCardConfiguredPorts, slotAdminState=slotAdminState, slotFileState=slotFileState, cardMIB=cardMIB, posCardActivePortMask=posCardActivePortMask, posCardPhyResetState=posCardPhyResetState, slotFlashThreshold=slotFlashThreshold, cardSerialNum=cardSerialNum, cardCLEIECICode=cardCLEIECICode, tdmIoCardTable=tdmIoCardTable, cardMACaddressNum=cardMACaddressNum, slotInsertState=slotInsertState, cardAssemblyNumString=cardAssemblyNumString, etherCardEntry=etherCardEntry, atmCardTable=atmCardTable, cardChecksum=cardChecksum, slotIoCardStatus=slotIoCardStatus, cardCount=cardCount, etherCardOperState=etherCardOperState, opticalCardEntry=opticalCardEntry, moduleStatusChange=moduleStatusChange, atmCardRowStatus=atmCardRowStatus, tdmIoCardEntry=tdmIoCardEntry, cardMacAddress=cardMacAddress, cardEEPromEntry=cardEEPromEntry, opticalCardTable=opticalCardTable, cardEEPromTable=cardEEPromTable, cardHwType=cardHwType, slotTable=slotTable, etherCardPhyResetState=etherCardPhyResetState, etherCardActivePortMask=etherCardActivePortMask, slotCardType=slotCardType, posCardEntry=posCardEntry, cardHwSubType=cardHwSubType, slotModuleTempStatus=slotModuleTempStatus, etherCardTable=etherCardTable, tdmIoCardType=tdmIoCardType, etherCardRowStatus=etherCardRowStatus, opticalCardOpticsType=opticalCardOpticsType, cardAssemblyClass=cardAssemblyClass, cardAssemblyId=cardAssemblyId, cardAssemblyRev=cardAssemblyRev, cardAssemblyRevString=cardAssemblyRevString, tdmIoCardMode=tdmIoCardMode, atmCardOperState=atmCardOperState, cardSIDFVer=cardSIDFVer, cardImageType=cardImageType)
