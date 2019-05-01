#
# PySNMP MIB module CISCO-ADAPTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ADAPTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:49:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, Gauge32, IpAddress, ObjectIdentity, NotificationType, MibIdentifier, TimeTicks, Counter64, Bits, Unsigned32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "Gauge32", "IpAddress", "ObjectIdentity", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "Bits", "Unsigned32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = MibIdentifier((1, 3, 6, 1, 4, 1, 9))
workgroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 5))
adapterCard = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 5, 2))
adptrNumber = MibScalar((1, 3, 6, 1, 4, 1, 9, 5, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrNumber.setStatus('mandatory')
if mibBuilder.loadTexts: adptrNumber.setDescription('The number of Cisco network adapter cards in the machine.')
adptrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 5, 2, 2), )
if mibBuilder.loadTexts: adptrTable.setStatus('mandatory')
if mibBuilder.loadTexts: adptrTable.setDescription('A list of adapter table entries. The number of entries is given by adptrNumber.')
adptrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1), ).setIndexNames((0, "CISCO-ADAPTER-MIB", "adptrIndex"))
if mibBuilder.loadTexts: adptrEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adptrEntry.setDescription('An adapter table entry containing information about a Cisco network adapter card.')
adptrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrIndex.setStatus('mandatory')
if mibBuilder.loadTexts: adptrIndex.setDescription("A unique value for each Cisco adapter card in the machine. The value ranges between 1 and the value of adptrNumber. The value for each adapter card must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization.")
adptrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 10))).clone(namedValues=NamedValues(("other", 1), ("sBusCddi", 2), ("sBusFddiSt", 3), ("sBusFddi", 4), ("mcaCddi", 5), ("mcaFddiSt", 6), ("mcaFddi", 7), ("eisaCddi", 8), ("eisaFddi", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrType.setStatus('mandatory')
if mibBuilder.loadTexts: adptrType.setDescription('The type of adapter card.')
adptrSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrSerialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: adptrSerialNumber.setDescription('The serial number of the adapter card.')
adptrHwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrHwHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrHwHiVersion.setDescription('The high part of the hardware version of the adapter card. For example, if the hardware version is 3.1, the value of adptrHwHiVersion is 3.')
adptrHwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrHwLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrHwLoVersion.setDescription('The low part of the hardware version of the adapter card. For example, if the hardware version is 3.1, the value of adptrHwLoVersion is 1.')
adptrFwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrFwHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrFwHiVersion.setDescription('The high part of the firmware version of the adapter card. For example, if the firmware version is 3.1, the value of adptrFwHiVersion is 3.')
adptrFwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrFwLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrFwLoVersion.setDescription('The low part of the firmware version of the adapter card. For example, if the firmware version is 3.1, the value of adptrFwLoVersion is 1.')
adptrSwHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrSwHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrSwHiVersion.setDescription('The high part of the software version number. For example, if the software version is 3.1, the value of adptrSwHiVersion is 3.')
adptrSwLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrSwLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrSwLoVersion.setDescription('The low part of the software version number. For example, if the software version is 3.1, the value of adptrSwLoVersion is 1.')
adptrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("ok", 2), ("minorFault", 3), ("majorFault", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrStatus.setStatus('mandatory')
if mibBuilder.loadTexts: adptrStatus.setDescription("The operational status of the adapter card. If the status is not ok(2), the value of adptrSelfTestResult gives more detailed information about the adapter card's failure condition(s).")
adptrSelfTestResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrSelfTestResult.setStatus('mandatory')
if mibBuilder.loadTexts: adptrSelfTestResult.setDescription("The result of the adapter card's self test. A zero indicates that the adapter passed all tests. Bits set in the result indicate error conditions.")
adptrDriverHiVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrDriverHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrDriverHiVersion.setDescription('The high part of the driver version number. For example, if the driver version is 3.1, the value of adptrDriverHiVersion is 3.')
adptrDriverLoVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrDriverLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrDriverLoVersion.setDescription('The low part of the driver version number. For example, if the driver version is 3.1, the value of adptrDriverLoVersion is 1.')
adptrMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("cddi", 2), ("fiber", 3), ("tppmd", 4), ("mlt3", 5), ("sddi", 6), ("smf", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrMediaType.setStatus('mandatory')
if mibBuilder.loadTexts: adptrMediaType.setDescription('The type of physical layer medium dependent interface on the adapter port(s).')
adptrModel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrModel.setStatus('mandatory')
if mibBuilder.loadTexts: adptrModel.setDescription("The manufacturer's model number for the adapter.")
adptrTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 9, 5, 2, 3), )
if mibBuilder.loadTexts: adptrTrapReceiverTable.setStatus('mandatory')
if mibBuilder.loadTexts: adptrTrapReceiverTable.setDescription('The adapter trap receiver table (0 to 10 entries). This table lists the addresses of Network Management Stations that should receive trap messages from this adapter when an exception condition occurs.')
adptrTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1), ).setIndexNames((0, "CISCO-ADAPTER-MIB", "adptrTrapReceiverAddr"))
if mibBuilder.loadTexts: adptrTrapReceiverEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adptrTrapReceiverEntry.setDescription('A trap receiver table entry.')
adptrTrapReceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adptrTrapReceiverType.setStatus('mandatory')
if mibBuilder.loadTexts: adptrTrapReceiverType.setDescription('Setting this object to invalid(2) removes the corresponding entry from the adptrTrapReceiverTable. To add a new entry to the adptrTrapReceiverTable, set the adptrTrapReceiverAddr to an IpAddress which is not already in the table. The adptrTrapReceiverType for that entry is automatically set to other(1).')
adptrTrapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrTrapReceiverAddr.setStatus('mandatory')
if mibBuilder.loadTexts: adptrTrapReceiverAddr.setDescription('IP address for trap receiver.')
adptrTrapReceiverComm = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adptrTrapReceiverComm.setStatus('mandatory')
if mibBuilder.loadTexts: adptrTrapReceiverComm.setDescription('Community string used for trap messages to this trap receiver.')
adptrCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 9, 5, 2, 4), )
if mibBuilder.loadTexts: adptrCommunityTable.setStatus('mandatory')
if mibBuilder.loadTexts: adptrCommunityTable.setDescription('The adapter community table (4 entries). This table lists community strings and their access levels. When an SNMP message is received by this adapter, the community string in the message is compared with this table to determine access rights of the sender.')
adptrCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 5, 2, 4, 1), ).setIndexNames((0, "CISCO-ADAPTER-MIB", "adptrCommunityAccess"))
if mibBuilder.loadTexts: adptrCommunityEntry.setStatus('mandatory')
if mibBuilder.loadTexts: adptrCommunityEntry.setDescription('A community table entry.')
adptrCommunityAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("readOnly", 2), ("readWrite", 3), ("readWriteAll", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrCommunityAccess.setStatus('mandatory')
if mibBuilder.loadTexts: adptrCommunityAccess.setDescription('A value of readWriteAll(4) allows the community to read and write all objects in the MIB. A value of readWrite(3) allows the community to read and write all objects except the adptrCommunityTable, which it cannot access at all. A value of readOnly(2) allows the community to read all objects except the adptrCommunityTable. A value of other(1) allows the community no access.')
adptrCommunityString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 5, 2, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adptrCommunityString.setStatus('mandatory')
if mibBuilder.loadTexts: adptrCommunityString.setDescription('Configurable community string with access rights defined by the value of adptrCommunityAccess.')
adptrMgmtType = MibScalar((1, 3, 6, 1, 4, 1, 9, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("snmp", 2), ("smux", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrMgmtType.setStatus('mandatory')
if mibBuilder.loadTexts: adptrMgmtType.setDescription('The type of network management for the adapter.')
adptrMgmtHiVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 5, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrMgmtHiVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrMgmtHiVersion.setDescription('The high part of the network management version number. For example, if the network management version is 3.1, the value of adptrMgmtHiVersion is 3.')
adptrMgmtLoVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 5, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adptrMgmtLoVersion.setStatus('mandatory')
if mibBuilder.loadTexts: adptrMgmtLoVersion.setDescription('The low part of the network management version number. For example, if the network management version is 3.1, the value of adptrMgmtLoVersion is 1.')
mibBuilder.exportSymbols("CISCO-ADAPTER-MIB", adptrDriverHiVersion=adptrDriverHiVersion, adptrIndex=adptrIndex, adptrCommunityEntry=adptrCommunityEntry, adptrSerialNumber=adptrSerialNumber, adptrSwHiVersion=adptrSwHiVersion, adptrHwHiVersion=adptrHwHiVersion, adptrCommunityTable=adptrCommunityTable, adptrCommunityAccess=adptrCommunityAccess, workgroup=workgroup, adapterCard=adapterCard, adptrMediaType=adptrMediaType, adptrType=adptrType, adptrNumber=adptrNumber, adptrHwLoVersion=adptrHwLoVersion, adptrTrapReceiverTable=adptrTrapReceiverTable, cisco=cisco, adptrTrapReceiverType=adptrTrapReceiverType, adptrModel=adptrModel, adptrSelfTestResult=adptrSelfTestResult, adptrTrapReceiverEntry=adptrTrapReceiverEntry, adptrStatus=adptrStatus, adptrFwLoVersion=adptrFwLoVersion, adptrCommunityString=adptrCommunityString, adptrEntry=adptrEntry, adptrMgmtLoVersion=adptrMgmtLoVersion, adptrSwLoVersion=adptrSwLoVersion, adptrTrapReceiverComm=adptrTrapReceiverComm, adptrTable=adptrTable, adptrFwHiVersion=adptrFwHiVersion, adptrTrapReceiverAddr=adptrTrapReceiverAddr, adptrDriverLoVersion=adptrDriverLoVersion, adptrMgmtHiVersion=adptrMgmtHiVersion, adptrMgmtType=adptrMgmtType)