#
# PySNMP MIB module QOS-BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QOS-BRIDGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:35:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
dot1qVlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Unsigned32, NotificationType, Counter64, IpAddress, iso, ObjectIdentity, ModuleIdentity, mib_2, MibIdentifier, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Unsigned32", "NotificationType", "Counter64", "IpAddress", "iso", "ObjectIdentity", "ModuleIdentity", "mib-2", "MibIdentifier", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
dot1dQosMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 12346))
dot1dQosMib.setRevisions(('2000-06-07 00:00',))
if mibBuilder.loadTexts: dot1dQosMib.setLastUpdated('200006070000Z')
if mibBuilder.loadTexts: dot1dQosMib.setOrganization('Extreme Networks')
dot1dQosObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 1))
dot1dQosTables = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 2))
dot1dQosMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 3))
class Dot1dUserPri(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

dot1dQosUserPriTable = MibTable((1, 3, 6, 1, 2, 1, 12346, 2, 1), )
if mibBuilder.loadTexts: dot1dQosUserPriTable.setStatus('current')
dot1dQosUserPriEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12346, 2, 1, 1), ).setIndexNames((0, "QOS-BRIDGE-MIB", "dot1dQosUserPri"))
if mibBuilder.loadTexts: dot1dQosUserPriEntry.setStatus('current')
dot1dQosUserPri = MibTableColumn((1, 3, 6, 1, 2, 1, 12346, 2, 1, 1, 1), Dot1dUserPri()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dQosUserPri.setStatus('current')
dot1dQosVlanClfrTable = MibTable((1, 3, 6, 1, 2, 1, 12346, 2, 2), )
if mibBuilder.loadTexts: dot1dQosVlanClfrTable.setStatus('current')
dot1dQosVlanClfrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 12346, 2, 2, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: dot1dQosVlanClfrEntry.setStatus('current')
dot1dQosVlanStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 12346, 2, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dot1dQosVlanStatus.setStatus('current')
dot1dQosMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 3, 1))
dot1dQosMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 12346, 3, 2))
dot1dQosMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 12346, 3, 1, 1)).setObjects(("QOS-BRIDGE-MIB", "dot1dQosMIBUserPriGroup"), ("QOS-BRIDGE-MIB", "dot1dQosMIBVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1dQosMIBCompliance = dot1dQosMIBCompliance.setStatus('current')
dot1dQosMIBUserPriGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 12346, 3, 2, 1)).setObjects(("QOS-BRIDGE-MIB", "dot1dQosUserPri"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1dQosMIBUserPriGroup = dot1dQosMIBUserPriGroup.setStatus('current')
dot1dQosMIBVlanGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 12346, 3, 2, 2)).setObjects(("QOS-BRIDGE-MIB", "dot1dQosVlanStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot1dQosMIBVlanGroup = dot1dQosMIBVlanGroup.setStatus('current')
mibBuilder.exportSymbols("QOS-BRIDGE-MIB", Dot1dUserPri=Dot1dUserPri, dot1dQosUserPri=dot1dQosUserPri, dot1dQosMib=dot1dQosMib, dot1dQosObjects=dot1dQosObjects, dot1dQosVlanStatus=dot1dQosVlanStatus, dot1dQosVlanClfrEntry=dot1dQosVlanClfrEntry, dot1dQosMIBUserPriGroup=dot1dQosMIBUserPriGroup, dot1dQosMIBCompliance=dot1dQosMIBCompliance, dot1dQosMIBGroups=dot1dQosMIBGroups, dot1dQosTables=dot1dQosTables, dot1dQosVlanClfrTable=dot1dQosVlanClfrTable, dot1dQosUserPriTable=dot1dQosUserPriTable, dot1dQosMIBVlanGroup=dot1dQosMIBVlanGroup, dot1dQosMIBCompliances=dot1dQosMIBCompliances, PYSNMP_MODULE_ID=dot1dQosMib, dot1dQosMIBConformance=dot1dQosMIBConformance, dot1dQosUserPriEntry=dot1dQosUserPriEntry)
