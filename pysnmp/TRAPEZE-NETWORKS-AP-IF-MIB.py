#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-AP-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Integer32, iso, Counter32, Counter64, Gauge32, ModuleIdentity, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Integer32", "iso", "Counter32", "Counter64", "Gauge32", "ModuleIdentity", "NotificationType", "TimeTicks")
TextualConvention, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress")
TrpzApSerialNum, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-AP-TC", "TrpzApSerialNum")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 16))
trpzApIfMib.setRevisions(('2008-11-20 00:01',))
if mibBuilder.loadTexts: trpzApIfMib.setLastUpdated('200811200001Z')
if mibBuilder.loadTexts: trpzApIfMib.setOrganization('Trapeze Networks')
class TrpzApInterfaceIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

trpzApIfMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1))
trpzApIfTable = MibTable((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1), )
if mibBuilder.loadTexts: trpzApIfTable.setStatus('current')
trpzApIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1), ).setIndexNames((0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfApSerialNum"), (0, "TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfIndex"))
if mibBuilder.loadTexts: trpzApIfEntry.setStatus('current')
trpzApIfApSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 1), TrpzApSerialNum())
if mibBuilder.loadTexts: trpzApIfApSerialNum.setStatus('current')
trpzApIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 2), TrpzApInterfaceIndex())
if mibBuilder.loadTexts: trpzApIfIndex.setStatus('current')
trpzApIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfName.setStatus('current')
trpzApIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 4), IANAifType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfType.setStatus('current')
trpzApIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfMtu.setStatus('current')
trpzApIfHighSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfHighSpeed.setStatus('current')
trpzApIfMac = MibTableColumn((1, 3, 6, 1, 4, 1, 14525, 4, 16, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trpzApIfMac.setStatus('current')
trpzApIfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2))
trpzApIfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1))
trpzApIfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2))
trpzApIfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 1, 1)).setObjects(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApIfCompliance = trpzApIfCompliance.setStatus('current')
trpzApIfBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 14525, 4, 16, 2, 2, 1)).setObjects(("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfName"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfType"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMtu"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfHighSpeed"), ("TRAPEZE-NETWORKS-AP-IF-MIB", "trpzApIfMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    trpzApIfBasicGroup = trpzApIfBasicGroup.setStatus('current')
mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-IF-MIB", trpzApIfIndex=trpzApIfIndex, trpzApIfMtu=trpzApIfMtu, trpzApIfMac=trpzApIfMac, trpzApIfMibObjects=trpzApIfMibObjects, PYSNMP_MODULE_ID=trpzApIfMib, trpzApIfConformance=trpzApIfConformance, trpzApIfMib=trpzApIfMib, trpzApIfHighSpeed=trpzApIfHighSpeed, trpzApIfGroups=trpzApIfGroups, trpzApIfTable=trpzApIfTable, trpzApIfBasicGroup=trpzApIfBasicGroup, trpzApIfApSerialNum=trpzApIfApSerialNum, trpzApIfEntry=trpzApIfEntry, trpzApIfType=trpzApIfType, trpzApIfName=trpzApIfName, TrpzApInterfaceIndex=TrpzApInterfaceIndex, trpzApIfCompliance=trpzApIfCompliance, trpzApIfCompliances=trpzApIfCompliances)
