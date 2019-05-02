#
# PySNMP MIB module NTWS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-AP-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, TimeTicks, Counter64, MibIdentifier, Integer32, ModuleIdentity, Counter32, Gauge32, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
ntwsApIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16))
ntwsApIfMib.setRevisions(('2008-11-20 00:01',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsApIfMib.setRevisionsDescriptions(('v1.0: Initial version',))
if mibBuilder.loadTexts: ntwsApIfMib.setLastUpdated('200811200001Z')
if mibBuilder.loadTexts: ntwsApIfMib.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsApIfMib.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsApIfMib.setDescription("AP network Interface objects for Nortel Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent implementing this MIB. Copyright 2009 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsApInterfaceIndex(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each AP network interface.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

ntwsApIfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1))
ntwsApIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1), )
if mibBuilder.loadTexts: ntwsApIfTable.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfTable.setDescription("A table describing the network interfaces on all the APs currently present and managed by this AC (APs in ''ALIVE'' state).")
ntwsApIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1), ).setIndexNames((0, "NTWS-AP-IF-MIB", "ntwsApIfApSerialNum"), (0, "NTWS-AP-IF-MIB", "ntwsApIfIndex"))
if mibBuilder.loadTexts: ntwsApIfEntry.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfEntry.setDescription('Information about a particular network interface on an AP attached to the AC.')
ntwsApIfApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 1), NtwsApSerialNum())
if mibBuilder.loadTexts: ntwsApIfApSerialNum.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfApSerialNum.setDescription('The Serial Number of the AP containing this network interface.')
ntwsApIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 2), NtwsApInterfaceIndex())
if mibBuilder.loadTexts: ntwsApIfIndex.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfIndex.setDescription('A unique value, greater than zero, for each AP network interface.')
ntwsApIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfName.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfName.setDescription('The textual name of the interface.')
ntwsApIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfType.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfType.setDescription('The type of AP network interfaces.')
ntwsApIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfMtu.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfMtu.setDescription('The size of the largest packet which can be sent/received on the interface, specified in octets.')
ntwsApIfHighSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfHighSpeed.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfHighSpeed.setDescription('The nominal bandwidth of AP network interfaces in units of 1,000,000 bits per second.')
ntwsApIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfMac.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfMac.setDescription('The MAC address of this network interface.')
ntwsApIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2))
ntwsApIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1))
ntwsApIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2))
ntwsApIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1, 1)).setObjects(("NTWS-AP-IF-MIB", "ntwsApIfBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApIfCompliance = ntwsApIfCompliance.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfCompliance.setDescription('The compliance statement for devices that implement AP If MIB. This compliance statement is for releases 7.1 and greater of AC (wireless switch) software.')
ntwsApIfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2, 1)).setObjects(("NTWS-AP-IF-MIB", "ntwsApIfName"), ("NTWS-AP-IF-MIB", "ntwsApIfType"), ("NTWS-AP-IF-MIB", "ntwsApIfMtu"), ("NTWS-AP-IF-MIB", "ntwsApIfHighSpeed"), ("NTWS-AP-IF-MIB", "ntwsApIfMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApIfBasicGroup = ntwsApIfBasicGroup.setStatus('current')
if mibBuilder.loadTexts: ntwsApIfBasicGroup.setDescription('Group of columnar objects implemented to provide basic Interface info in releases 7.1 and greater.')
mibBuilder.exportSymbols("NTWS-AP-IF-MIB", ntwsApIfBasicGroup=ntwsApIfBasicGroup, ntwsApIfTable=ntwsApIfTable, ntwsApIfEntry=ntwsApIfEntry, ntwsApIfConformance=ntwsApIfConformance, ntwsApIfCompliances=ntwsApIfCompliances, ntwsApIfName=ntwsApIfName, ntwsApIfCompliance=ntwsApIfCompliance, ntwsApIfGroups=ntwsApIfGroups, ntwsApIfMibObjects=ntwsApIfMibObjects, ntwsApIfHighSpeed=ntwsApIfHighSpeed, ntwsApIfApSerialNum=ntwsApIfApSerialNum, ntwsApIfIndex=ntwsApIfIndex, ntwsApIfMtu=ntwsApIfMtu, ntwsApIfMac=ntwsApIfMac, ntwsApIfMib=ntwsApIfMib, ntwsApIfType=ntwsApIfType, PYSNMP_MODULE_ID=ntwsApIfMib, NtwsApInterfaceIndex=NtwsApInterfaceIndex)
