#
# PySNMP MIB module NTWS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-AP-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
NtwsApSerialNum, = mibBuilder.importSymbols("NTWS-AP-TC", "NtwsApSerialNum")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, iso, Bits, Integer32, TimeTicks, Counter32, ObjectIdentity, ModuleIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "iso", "Bits", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
ntwsApIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16))
ntwsApIfMib.setRevisions(('2008-11-20 00:01',))
if mibBuilder.loadTexts: ntwsApIfMib.setLastUpdated('200811200001Z')
if mibBuilder.loadTexts: ntwsApIfMib.setOrganization('Nortel Networks')
class NtwsApInterfaceIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

ntwsApIfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1))
ntwsApIfTable = MibTable((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1), )
if mibBuilder.loadTexts: ntwsApIfTable.setStatus('current')
ntwsApIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1), ).setIndexNames((0, "NTWS-AP-IF-MIB", "ntwsApIfApSerialNum"), (0, "NTWS-AP-IF-MIB", "ntwsApIfIndex"))
if mibBuilder.loadTexts: ntwsApIfEntry.setStatus('current')
ntwsApIfApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 1), NtwsApSerialNum())
if mibBuilder.loadTexts: ntwsApIfApSerialNum.setStatus('current')
ntwsApIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 2), NtwsApInterfaceIndex())
if mibBuilder.loadTexts: ntwsApIfIndex.setStatus('current')
ntwsApIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfName.setStatus('current')
ntwsApIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfType.setStatus('current')
ntwsApIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfMtu.setStatus('current')
ntwsApIfHighSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfHighSpeed.setStatus('current')
ntwsApIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntwsApIfMac.setStatus('current')
ntwsApIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2))
ntwsApIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1))
ntwsApIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2))
ntwsApIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 1, 1)).setObjects(("NTWS-AP-IF-MIB", "ntwsApIfBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApIfCompliance = ntwsApIfCompliance.setStatus('current')
ntwsApIfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 16, 2, 2, 1)).setObjects(("NTWS-AP-IF-MIB", "ntwsApIfName"), ("NTWS-AP-IF-MIB", "ntwsApIfType"), ("NTWS-AP-IF-MIB", "ntwsApIfMtu"), ("NTWS-AP-IF-MIB", "ntwsApIfHighSpeed"), ("NTWS-AP-IF-MIB", "ntwsApIfMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntwsApIfBasicGroup = ntwsApIfBasicGroup.setStatus('current')
mibBuilder.exportSymbols("NTWS-AP-IF-MIB", ntwsApIfApSerialNum=ntwsApIfApSerialNum, ntwsApIfConformance=ntwsApIfConformance, ntwsApIfCompliance=ntwsApIfCompliance, PYSNMP_MODULE_ID=ntwsApIfMib, ntwsApIfName=ntwsApIfName, ntwsApIfMib=ntwsApIfMib, ntwsApIfHighSpeed=ntwsApIfHighSpeed, NtwsApInterfaceIndex=NtwsApInterfaceIndex, ntwsApIfBasicGroup=ntwsApIfBasicGroup, ntwsApIfEntry=ntwsApIfEntry, ntwsApIfMac=ntwsApIfMac, ntwsApIfIndex=ntwsApIfIndex, ntwsApIfMtu=ntwsApIfMtu, ntwsApIfType=ntwsApIfType, ntwsApIfTable=ntwsApIfTable, ntwsApIfCompliances=ntwsApIfCompliances, ntwsApIfMibObjects=ntwsApIfMibObjects, ntwsApIfGroups=ntwsApIfGroups)
