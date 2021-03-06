#
# PySNMP MIB module PANDATEL-GMSF-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANDATEL-GMSF-MODEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:37:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
device_id, mdmSpecifics = mibBuilder.importSymbols("PANDATEL-MODEM-MIB", "device-id", "mdmSpecifics")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Integer32, Counter64, IpAddress, ObjectIdentity, ModuleIdentity, Counter32, MibIdentifier, Gauge32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Integer32", "Counter64", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gmsf_modem = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 10000, 2, 205)).setLabel("gmsf-modem")
gmsf = MibIdentifier((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205))
gmsfModemTable = MibTable((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1), )
if mibBuilder.loadTexts: gmsfModemTable.setStatus('mandatory')
if mibBuilder.loadTexts: gmsfModemTable.setDescription('This table contains information about all GM-F converters in all racks.')
gmsfTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1), ).setIndexNames((0, "PANDATEL-GMSF-MODEM-MIB", "mdmRack"), (0, "PANDATEL-GMSF-MODEM-MIB", "mdmModem"), (0, "PANDATEL-GMSF-MODEM-MIB", "mdmPosition"))
if mibBuilder.loadTexts: gmsfTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: gmsfTableEntry.setDescription('The index of the table.')
mdmRack = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmRack.setStatus('mandatory')
if mibBuilder.loadTexts: mdmRack.setDescription('The index of the rack where the converter is installed.')
mdmModem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModem.setStatus('mandatory')
if mibBuilder.loadTexts: mdmModem.setDescription('This entry displays the slot number where the corresponding converter is installed in the rack.')
mdmPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmPosition.setStatus('mandatory')
if mibBuilder.loadTexts: mdmPosition.setDescription("This entry displays the location of the corresponding converter: 'local' or 'remote'. The converter which is plugged into a managed rack is 'local', the counterpart is 'remote'.")
mdmModemName = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemName.setStatus('mandatory')
if mibBuilder.loadTexts: mdmModemName.setDescription('The verbal name of this converter.')
mdmInterfaceEmulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 99))).clone(namedValues=NamedValues(("other", 1), ("dte", 2), ("dce", 3), ("te", 4), ("nt", 5), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmInterfaceEmulationMode.setStatus('mandatory')
if mibBuilder.loadTexts: mdmInterfaceEmulationMode.setDescription("Interface mode of the unit: 'dte', 'dce', 'te' or 'nt'.")
mdmModemProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 99))).clone(namedValues=NamedValues(("other", 1), ("e1", 2), ("t1", 3), ("unknown", 99)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmModemProperty.setStatus('mandatory')
if mibBuilder.loadTexts: mdmModemProperty.setDescription("This entry displays the speed class of the GM-F: 'e1' or 't1'.")
mdmHDSLUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ntu", 2), ("ltu", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmHDSLUnit.setStatus('mandatory')
if mibBuilder.loadTexts: mdmHDSLUnit.setDescription('HDSL unit type: Line Termination Unit (LTU) or Network Termination Unit (LTU)')
mdmClockSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("dual", 2), ("single", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSystem.setStatus('mandatory')
if mibBuilder.loadTexts: mdmClockSystem.setDescription("The clock system of the link: 'dual' or 'single'.")
mdmClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("internal", 2), ("remote", 3), ("external", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmClockSource.setStatus('mandatory')
if mibBuilder.loadTexts: mdmClockSource.setDescription("The clock source of the link: 'internal', 'external', or 'remote'.")
mdmDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("other", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmDataRate.setStatus('mandatory')
if mibBuilder.loadTexts: mdmDataRate.setDescription("The data rate at the interface in bits per seconds. The data rate at the remote counterpart changes simultaneously. A data rate of 2.048 Mbps (E1) automatically disables CRC4, sets mdmStartTimeslot to 'unframed', enables time slot 16, and disables remote access. A data rate of 1.984 Mbps (E1) automatically sets mdmStartTimeslot to 'timeslot-1', enables time slot 16 and sets mdmRemoteAccessMode to 'via timeslot 0 sa4-bit'. A data rate of 1.544 Mbps (T1) automatically sets mdmStartTimeslot to 'unframed' and disables remote access.")
mdmStartTimeslot = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 98, 99, 100))).clone(namedValues=NamedValues(("timeslot-1", 1), ("timeslot-2", 2), ("timeslot-3", 3), ("timeslot-4", 4), ("timeslot-5", 5), ("timeslot-6", 6), ("timeslot-7", 7), ("timeslot-8", 8), ("timeslot-9", 9), ("timeslot-10", 10), ("timeslot-11", 11), ("timeslot-12", 12), ("timeslot-13", 13), ("timeslot-14", 14), ("timeslot-15", 15), ("timeslot-16", 16), ("timeslot-17", 17), ("timeslot-18", 18), ("timeslot-19", 19), ("timeslot-20", 20), ("timeslot-21", 21), ("timeslot-22", 22), ("timeslot-23", 23), ("timeslot-24", 24), ("timeslot-25", 25), ("timeslot-26", 26), ("timeslot-27", 27), ("timeslot-28", 28), ("timeslot-29", 29), ("timeslot-30", 30), ("timeslot-31", 31), ("unframed", 98), ("other", 99), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmStartTimeslot.setStatus('mandatory')
if mibBuilder.loadTexts: mdmStartTimeslot.setDescription("This entry determines the start time slot for framing. Start time slot and data rate must match. A start time slot which is too high will be ignored. The remote unit's configuration changes simultaneously.")
mdmTimeslotSize = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("nx64k", 2), ("nx56k", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmTimeslotSize.setStatus('mandatory')
if mibBuilder.loadTexts: mdmTimeslotSize.setDescription("This entry determines the size of the time slots: 'nx64k' or 'nx56k'. 'nx56k' is valid for T1 units only. The remote unit's configuration changes simultaneously.")
mdmTimeslot16 = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmTimeslot16.setStatus('mandatory')
if mibBuilder.loadTexts: mdmTimeslot16.setDescription('This entry enables or disables time slot 16. If it is disabled, it will not be used for data transmission but for framing. Valid for E1 units only.')
mdmCRC4Generation = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 41), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCRC4Generation.setStatus('mandatory')
if mibBuilder.loadTexts: mdmCRC4Generation.setDescription('This entry enables or disables the generation of a CRC4 check sum. Valid for E1 units only.')
mdmFramingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 100))).clone(namedValues=NamedValues(("other", 1), ("d4", 2), ("esf", 3), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmFramingMode.setStatus('mandatory')
if mibBuilder.loadTexts: mdmFramingMode.setDescription("The T1 framing mode: 'd4' or 'esf'. The remote unit's configuration changes simultaneously. Valid for T1 units only.")
mdmScrambler = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 63), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmScrambler.setStatus('mandatory')
if mibBuilder.loadTexts: mdmScrambler.setDescription('This entry enables or disables scrambling.')
mdmRemoteAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 64), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 7))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("via-next-free-timeslot", 3), ("via-timeslot-0-Sa4-bit", 4), ("via-hdsl-channel", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmRemoteAccessMode.setStatus('mandatory')
if mibBuilder.loadTexts: mdmRemoteAccessMode.setDescription("The remote access mode: 'disable', 'via-next-free-timeslot', 'via-timeslot-0-Sa4-bit', or 'via-hdsl-channel'. The value 'via-next-free-timeslot' means that one time slot higher than the last data time slot is used for remote access. The value 'via-timeslot-0-Sa4-bit' means that the sa4-bit in time slot 0 is used for remote access The remote unit's configuration changes simultaneously.")
mdmCRC6Test = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 100))).clone(namedValues=NamedValues(("other", 1), ("start", 3), ("stop", 4), ("not-available", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdmCRC6Test.setStatus('mandatory')
if mibBuilder.loadTexts: mdmCRC6Test.setDescription("This entry enables the execution of a CRC6 test. Write requests with values other than 'start' or 'stop' will be rejected. Valid for T1 units only.")
mdmCRC6Status = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 101), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 5, 6, 7, 100))).clone(namedValues=NamedValues(("other", 1), ("never-started", 2), ("running", 5), ("stopped", 6), ("start-failed", 7), ("not-available", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmCRC6Status.setStatus('mandatory')
if mibBuilder.loadTexts: mdmCRC6Status.setDescription('This entry indicates the status of the CRC6 test. Valid for T1 units only.')
mdmCRC6Error = MibTableColumn((1, 3, 6, 1, 4, 1, 760, 1, 1, 2, 1, 10, 205, 1, 1, 102), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdmCRC6Error.setStatus('mandatory')
if mibBuilder.loadTexts: mdmCRC6Error.setDescription('This entry indicates the number of errors detected during the last 60 seconds.')
mibBuilder.exportSymbols("PANDATEL-GMSF-MODEM-MIB", mdmModemName=mdmModemName, mdmClockSystem=mdmClockSystem, mdmClockSource=mdmClockSource, mdmStartTimeslot=mdmStartTimeslot, mdmTimeslot16=mdmTimeslot16, mdmTimeslotSize=mdmTimeslotSize, mdmCRC4Generation=mdmCRC4Generation, mdmHDSLUnit=mdmHDSLUnit, mdmScrambler=mdmScrambler, mdmModemProperty=mdmModemProperty, mdmPosition=mdmPosition, gmsfTableEntry=gmsfTableEntry, mdmRemoteAccessMode=mdmRemoteAccessMode, mdmCRC6Error=mdmCRC6Error, mdmCRC6Status=mdmCRC6Status, gmsf=gmsf, mdmCRC6Test=mdmCRC6Test, mdmDataRate=mdmDataRate, gmsf_modem=gmsf_modem, mdmRack=mdmRack, mdmModem=mdmModem, gmsfModemTable=gmsfModemTable, mdmFramingMode=mdmFramingMode, mdmInterfaceEmulationMode=mdmInterfaceEmulationMode)
