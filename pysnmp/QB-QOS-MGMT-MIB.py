#
# PySNMP MIB module QB-QOS-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QB-QOS-MGMT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:34:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
qbMibs, = mibBuilder.importSymbols("QUANTUMBRIDGE-REG", "qbMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, MibIdentifier, iso, ObjectIdentity, NotificationType, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter64, Unsigned32, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "iso", "ObjectIdentity", "NotificationType", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter64", "Unsigned32", "TimeTicks", "Integer32")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
qbQosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4323, 2, 14))
if mibBuilder.loadTexts: qbQosMIB.setLastUpdated('0101022155Z')
if mibBuilder.loadTexts: qbQosMIB.setOrganization('Quantum Bridge')
class QbMbitRate(TextualConvention, Integer32):
    status = 'current'

qbQosObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1))
qbQosNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 2))
qbQosConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3))
qbQosIfConfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1))
qbQosIfConfTableLastUpdate = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfConfTableLastUpdate.setStatus('current')
qbQosIfConfTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2), )
if mibBuilder.loadTexts: qbQosIfConfTable.setStatus('current')
qbQosIfConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qbQosIfConfEntry.setStatus('current')
qbQosIfConfPolicingAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbQosIfConfPolicingAdminStatus.setStatus('current')
qbQosIfStatTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2), )
if mibBuilder.loadTexts: qbQosIfStatTable.setStatus('current')
qbQosIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qbQosIfStatEntry.setStatus('current')
qbQosIfStatDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfStatDiscPkts.setStatus('current')
qbQosIfStatUpThreshDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfStatUpThreshDiscPkts.setStatus('current')
qbQosIfStatDownThreshDiscPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 14, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbQosIfStatDownThreshDiscPkts.setStatus('current')
qbQosNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 2, 0))
qbQosCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 1))
qbQosGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 2))
qbQosCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 1, 1)).setObjects(("QB-QOS-MGMT-MIB", "qbQosClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbQosCompliance = qbQosCompliance.setStatus('current')
qbQosGroupInfo = ObjectGroup((1, 3, 6, 1, 4, 1, 4323, 2, 14, 3, 2, 1)).setObjects(("QB-QOS-MGMT-MIB", "qbQosIfConfPolicingAdminStatus"), ("QB-QOS-MGMT-MIB", "qbQosIfStatDiscPkts"), ("QB-QOS-MGMT-MIB", "qbQosIfStatUpThreshDiscPkts"), ("QB-QOS-MGMT-MIB", "qbQosIfStatDownThreshDiscPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbQosGroupInfo = qbQosGroupInfo.setStatus('current')
mibBuilder.exportSymbols("QB-QOS-MGMT-MIB", qbQosIfStatUpThreshDiscPkts=qbQosIfStatUpThreshDiscPkts, qbQosIfConfTable=qbQosIfConfTable, qbQosGroups=qbQosGroups, qbQosNotificationPrefix=qbQosNotificationPrefix, qbQosIfStatDiscPkts=qbQosIfStatDiscPkts, qbQosCompliances=qbQosCompliances, qbQosCompliance=qbQosCompliance, qbQosIfStatEntry=qbQosIfStatEntry, qbQosGroupInfo=qbQosGroupInfo, qbQosIfConfPolicingAdminStatus=qbQosIfConfPolicingAdminStatus, qbQosNotifications=qbQosNotifications, qbQosIfConfGroup=qbQosIfConfGroup, qbQosIfStatTable=qbQosIfStatTable, QbMbitRate=QbMbitRate, qbQosIfConfEntry=qbQosIfConfEntry, qbQosIfConfTableLastUpdate=qbQosIfConfTableLastUpdate, PYSNMP_MODULE_ID=qbQosMIB, qbQosMIB=qbQosMIB, qbQosObjects=qbQosObjects, qbQosConformance=qbQosConformance, qbQosIfStatDownThreshDiscPkts=qbQosIfStatDownThreshDiscPkts)
