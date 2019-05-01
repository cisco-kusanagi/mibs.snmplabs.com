#
# PySNMP MIB module CT-HSIMPHYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-HSIMPHYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ctHSIMPhysMib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctHSIMPhysMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Unsigned32, Counter64, NotificationType, ModuleIdentity, Integer32, Bits, ObjectIdentity, Counter32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Unsigned32", "Counter64", "NotificationType", "ModuleIdentity", "Integer32", "Bits", "ObjectIdentity", "Counter32", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hsimInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1))
hsimBoardRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimBoardRev.setStatus('mandatory')
if mibBuilder.loadTexts: hsimBoardRev.setDescription('The value of this object is the printed circuit board revision level.')
hsimBoardId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimBoardId.setStatus('mandatory')
if mibBuilder.loadTexts: hsimBoardId.setDescription('The value of this object is the printed circuit board idenitifer.')
hsimEpldRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimEpldRev.setStatus('mandatory')
if mibBuilder.loadTexts: hsimEpldRev.setDescription('The value of this object is the programmable logic device revision level.')
hsimEpldId = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimEpldId.setStatus('mandatory')
if mibBuilder.loadTexts: hsimEpldId.setDescription('The value of this object is the programmable logic device identifier.')
hsimFsbRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimFsbRev.setStatus('mandatory')
if mibBuilder.loadTexts: hsimFsbRev.setDescription('The value of this object is the first stage boot revision level.')
hsimSsbRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimSsbRev.setStatus('mandatory')
if mibBuilder.loadTexts: hsimSsbRev.setDescription('The value of this object is the second stage boot revision level.')
hsimFwRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hsimFwRev.setStatus('mandatory')
if mibBuilder.loadTexts: hsimFwRev.setDescription('The value of this object is the HSIM firmware revision level.')
hsimPeripheralMBusInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8))
mBusNumberBoardsInstalled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusNumberBoardsInstalled.setStatus('mandatory')
if mibBuilder.loadTexts: mBusNumberBoardsInstalled.setDescription('The value of this object is number of MBus boards installed in this unit.')
mBusBoardTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2), )
if mibBuilder.loadTexts: mBusBoardTable.setStatus('mandatory')
if mibBuilder.loadTexts: mBusBoardTable.setDescription('A list of MBus boards present in this unit')
mBusBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1), ).setIndexNames((0, "CT-HSIMPHYS-MIB", "mBusBoardID"))
if mibBuilder.loadTexts: mBusBoardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mBusBoardEntry.setDescription('The value of this object is an MBus board that is present in this unit')
mBusBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusBoardID.setStatus('mandatory')
if mibBuilder.loadTexts: mBusBoardID.setDescription('The value of this object is an index that uniquely identifies the physical MBus board within the system.')
mBusBoardEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unknown", 1), ("cmm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusBoardEntryType.setStatus('mandatory')
if mibBuilder.loadTexts: mBusBoardEntryType.setDescription('The value of this object identifies the type of MBus board installed.')
mBusBoardOIDPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 8, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mBusBoardOIDPointer.setStatus('mandatory')
if mibBuilder.loadTexts: mBusBoardOIDPointer.setDescription('The value of this object defines the start of a MIB that can be used to determine more specific information about the given MBus board.')
hsimPeripheralWpimInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9))
wpimNumberBoardsInstalled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimNumberBoardsInstalled.setStatus('mandatory')
if mibBuilder.loadTexts: wpimNumberBoardsInstalled.setDescription('The value of this object is number of WPIM boards installed in this unit.')
wpimBoardTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2), )
if mibBuilder.loadTexts: wpimBoardTable.setStatus('mandatory')
if mibBuilder.loadTexts: wpimBoardTable.setDescription('A list of WPIM boards present in this unit')
wpimBoardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1), ).setIndexNames((0, "CT-HSIMPHYS-MIB", "wpimBoardID"))
if mibBuilder.loadTexts: wpimBoardEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wpimBoardEntry.setDescription('The value of this object is a WPIM board that is present in this unit')
wpimBoardID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimBoardID.setStatus('mandatory')
if mibBuilder.loadTexts: wpimBoardID.setDescription('The value of this object is an index that uniquely identifies this WPIM board.')
wpimBoardEntryType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimBoardEntryType.setStatus('mandatory')
if mibBuilder.loadTexts: wpimBoardEntryType.setDescription('The value of this object identifies the type of WPIM board installed. This is within the portWpim branch of the namingTree (1.3.6.1.4.1.52.3.8.1.2.5)')
wpimBoardOIDPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 9, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wpimBoardOIDPointer.setStatus('mandatory')
if mibBuilder.loadTexts: wpimBoardOIDPointer.setDescription('The value of this object defines the start of a MIB that can be used to determine more specific information about the given WPIM board.')
hsimLocalHwDevicesInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10))
localHwDevicesTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1), )
if mibBuilder.loadTexts: localHwDevicesTable.setStatus('mandatory')
if mibBuilder.loadTexts: localHwDevicesTable.setDescription('A list of specific hardware devices present in this unit')
localHwDevicesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1), ).setIndexNames((0, "CT-HSIMPHYS-MIB", "localHwDeviceID"))
if mibBuilder.loadTexts: localHwDevicesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: localHwDevicesEntry.setDescription('The value of this object is a WPIM module that is present in this unit')
localHwDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: localHwDeviceID.setStatus('mandatory')
if mibBuilder.loadTexts: localHwDeviceID.setDescription('The value of this object is an index that uniquely identifies the assoicated local hardware device.')
localHwDeviceType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("siemensMunich32", 2), ("mitelMT8985", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: localHwDeviceType.setStatus('mandatory')
if mibBuilder.loadTexts: localHwDeviceType.setDescription('The value of this object identifies the type of local hardware device. These local hardware devices are those specific ICs unique to this HSIM such as Siemens Munich32, or Mitel MT8985.')
localHwDeviceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: localHwDeviceOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: localHwDeviceOperStatus.setDescription('This object describes the current state of the device.')
localHwDeviceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17, 1, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: localHwDeviceAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: localHwDeviceAdminStatus.setDescription('This object is used by the Network Management System to request a change in the current state of the device.')
mibBuilder.exportSymbols("CT-HSIMPHYS-MIB", hsimEpldId=hsimEpldId, mBusBoardOIDPointer=mBusBoardOIDPointer, wpimBoardEntryType=wpimBoardEntryType, hsimBoardId=hsimBoardId, hsimPeripheralWpimInfo=hsimPeripheralWpimInfo, mBusBoardID=mBusBoardID, wpimBoardEntry=wpimBoardEntry, localHwDeviceType=localHwDeviceType, hsimInfo=hsimInfo, mBusBoardTable=mBusBoardTable, wpimNumberBoardsInstalled=wpimNumberBoardsInstalled, mBusBoardEntryType=mBusBoardEntryType, wpimBoardTable=wpimBoardTable, hsimFsbRev=hsimFsbRev, hsimSsbRev=hsimSsbRev, wpimBoardID=wpimBoardID, wpimBoardOIDPointer=wpimBoardOIDPointer, localHwDevicesTable=localHwDevicesTable, mBusNumberBoardsInstalled=mBusNumberBoardsInstalled, mBusBoardEntry=mBusBoardEntry, hsimLocalHwDevicesInfo=hsimLocalHwDevicesInfo, hsimFwRev=hsimFwRev, localHwDeviceAdminStatus=localHwDeviceAdminStatus, hsimPeripheralMBusInfo=hsimPeripheralMBusInfo, hsimEpldRev=hsimEpldRev, localHwDeviceID=localHwDeviceID, localHwDevicesEntry=localHwDevicesEntry, hsimBoardRev=hsimBoardRev, localHwDeviceOperStatus=localHwDeviceOperStatus)