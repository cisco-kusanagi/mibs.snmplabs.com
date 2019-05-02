#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-AP-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, TimeTicks, MibIdentifier, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Counter32, iso, Counter64, Gauge32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Counter32", "iso", "Counter64", "Gauge32", "NotificationType", "ObjectIdentity")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
TrpzApSerialNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApSerialNum")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 16))
trpzApIfMib.setRevisions(('2008-11-20 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzApIfMib.setRevisionsDescriptions(('v1.0: Initial version, for 7.1 release',))
if mibBuilder.loadTexts: trpzApIfMib.setLastUpdated('200811200001Z')
if mibBuilder.loadTexts: trpzApIfMib.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzApIfMib.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzApIfMib.setDescription("AP network Interface objects for Trapeze Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent implementing this MIB. Copyright (c) 2008-2009 by Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzApInterfaceIndex(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each AP network interface.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

trpzApIfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1))
trpzApIfTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1), )
if mibBuilder.loadTexts: trpzApIfTable.setStatus('current')
if mibBuilder.loadTexts: trpzApIfTable.setDescription("A table describing the network interfaces on all the APs currently present and managed by this AC (APs in ''ALIVE'' state).")
trpzApIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfApSerialNum"), (0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfIndex"))
if mibBuilder.loadTexts: trpzApIfEntry.setStatus('current')
if mibBuilder.loadTexts: trpzApIfEntry.setDescription('Information about a particular network interface on an AP attached to the AC.')
trpzApIfApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 1), TrpzApSerialNum())
if mibBuilder.loadTexts: trpzApIfApSerialNum.setStatus('current')
if mibBuilder.loadTexts: trpzApIfApSerialNum.setDescription('The Serial Number of the AP containing this network interface.')
trpzApIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 2), TrpzApInterfaceIndex())
if mibBuilder.loadTexts: trpzApIfIndex.setStatus('current')
if mibBuilder.loadTexts: trpzApIfIndex.setDescription('A unique value, greater than zero, for each AP network interface.')
trpzApIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfName.setStatus('current')
if mibBuilder.loadTexts: trpzApIfName.setDescription('The textual name of the interface.')
trpzApIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfType.setStatus('current')
if mibBuilder.loadTexts: trpzApIfType.setDescription('The type of AP network interfaces.')
trpzApIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfMtu.setStatus('current')
if mibBuilder.loadTexts: trpzApIfMtu.setDescription('The size of the largest packet which can be sent/received on the interface, specified in octets.')
trpzApIfHighSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfHighSpeed.setStatus('current')
if mibBuilder.loadTexts: trpzApIfHighSpeed.setDescription('The nominal bandwidth of AP network interfaces in units of 1,000,000 bits per second.')
trpzApIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfMac.setStatus('current')
if mibBuilder.loadTexts: trpzApIfMac.setDescription('The MAC address of this network interface.')
trpzApIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2))
trpzApIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1))
trpzApIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2))
trpzApIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApIfCompliance = trpzApIfCompliance.setStatus('current')
if mibBuilder.loadTexts: trpzApIfCompliance.setDescription('The compliance statement for devices that implement AP If MIB. This compliance statement is for releases 7.1 and greater of AC (wireless switch) software.')
trpzApIfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfName"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfType"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMtu"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfHighSpeed"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApIfBasicGroup = trpzApIfBasicGroup.setStatus('current')
if mibBuilder.loadTexts: trpzApIfBasicGroup.setDescription('Group of columnar objects implemented to provide basic Interface info in releases 7.1 and greater.')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-IF-MIB", trpzApIfConformance=trpzApIfConformance, TrpzApInterfaceIndex=TrpzApInterfaceIndex, trpzApIfApSerialNum=trpzApIfApSerialNum, trpzApIfGroups=trpzApIfGroups, trpzApIfMtu=trpzApIfMtu, trpzApIfCompliances=trpzApIfCompliances, trpzApIfMib=trpzApIfMib, trpzApIfMibObjects=trpzApIfMibObjects, trpzApIfName=trpzApIfName, PYSNMP_MODULE_ID=trpzApIfMib, trpzApIfCompliance=trpzApIfCompliance, trpzApIfType=trpzApIfType, trpzApIfMac=trpzApIfMac, trpzApIfHighSpeed=trpzApIfHighSpeed, trpzApIfBasicGroup=trpzApIfBasicGroup, trpzApIfIndex=trpzApIfIndex, trpzApIfTable=trpzApIfTable, trpzApIfEntry=trpzApIfEntry)
