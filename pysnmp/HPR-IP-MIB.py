#
# PySNMP MIB module HPR-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPR-IP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:30:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
SnaControlPointName, = mibBuilder.importSymbols("APPN-MIB", "SnaControlPointName")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hprObjects, hprCompliances, hprGroups = mibBuilder.importSymbols("HPR-MIB", "hprObjects", "hprCompliances", "hprGroups")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ModuleIdentity, Counter64, IpAddress, TimeTicks, Unsigned32, iso, Bits, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "IpAddress", "TimeTicks", "Unsigned32", "iso", "Bits", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter32", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hprIp = ModuleIdentity((1, 3, 6, 1, 2, 1, 34, 6, 1, 5))
hprIp.setRevisions(('1998-09-24 00:00',))
if mibBuilder.loadTexts: hprIp.setLastUpdated('9809240000Z')
if mibBuilder.loadTexts: hprIp.setOrganization('IETF SNA NAU MIB WG / AIW APPN MIBs SIG')
class AppnTrafficType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("low", 1), ("medium", 2), ("high", 3), ("network", 4), ("llcAndFnRoutedNlp", 5))

class AppnTOSPrecedence(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

hprIpActiveLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1), )
if mibBuilder.loadTexts: hprIpActiveLsTable.setStatus('current')
hprIpActiveLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1), ).setIndexNames((0, "HPR-IP-MIB", "hprIpActiveLsLsName"), (0, "HPR-IP-MIB", "hprIpActiveLsAppnTrafficType"))
if mibBuilder.loadTexts: hprIpActiveLsEntry.setStatus('current')
hprIpActiveLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hprIpActiveLsLsName.setStatus('current')
hprIpActiveLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 2), AppnTrafficType())
if mibBuilder.loadTexts: hprIpActiveLsAppnTrafficType.setStatus('current')
hprIpActiveLsUdpPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hprIpActiveLsUdpPackets.setStatus('current')
hprIpAppnPortTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2), )
if mibBuilder.loadTexts: hprIpAppnPortTable.setStatus('current')
hprIpAppnPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1), ).setIndexNames((0, "HPR-IP-MIB", "hprIpAppnPortName"), (0, "HPR-IP-MIB", "hprIpAppnPortAppnTrafficType"))
if mibBuilder.loadTexts: hprIpAppnPortEntry.setStatus('current')
hprIpAppnPortName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hprIpAppnPortName.setStatus('current')
hprIpAppnPortAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 2), AppnTrafficType())
if mibBuilder.loadTexts: hprIpAppnPortAppnTrafficType.setStatus('current')
hprIpAppnPortTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 2, 1, 3), AppnTOSPrecedence()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hprIpAppnPortTOSPrecedence.setStatus('current')
hprIpLsTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3), )
if mibBuilder.loadTexts: hprIpLsTable.setStatus('current')
hprIpLsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1), ).setIndexNames((0, "HPR-IP-MIB", "hprIpLsLsName"), (0, "HPR-IP-MIB", "hprIpLsAppnTrafficType"))
if mibBuilder.loadTexts: hprIpLsEntry.setStatus('current')
hprIpLsLsName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10)))
if mibBuilder.loadTexts: hprIpLsLsName.setStatus('current')
hprIpLsAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 2), AppnTrafficType())
if mibBuilder.loadTexts: hprIpLsAppnTrafficType.setStatus('current')
hprIpLsTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 3), AppnTOSPrecedence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpLsTOSPrecedence.setStatus('current')
hprIpLsRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpLsRowStatus.setStatus('current')
hprIpCnTable = MibTable((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4), )
if mibBuilder.loadTexts: hprIpCnTable.setStatus('current')
hprIpCnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1), ).setIndexNames((0, "HPR-IP-MIB", "hprIpCnVrnName"), (0, "HPR-IP-MIB", "hprIpCnAppnTrafficType"))
if mibBuilder.loadTexts: hprIpCnEntry.setStatus('current')
hprIpCnVrnName = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 1), SnaControlPointName())
if mibBuilder.loadTexts: hprIpCnVrnName.setStatus('current')
hprIpCnAppnTrafficType = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 2), AppnTrafficType())
if mibBuilder.loadTexts: hprIpCnAppnTrafficType.setStatus('current')
hprIpCnTOSPrecedence = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 3), AppnTOSPrecedence()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpCnTOSPrecedence.setStatus('current')
hprIpCnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 34, 6, 1, 5, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hprIpCnRowStatus.setStatus('current')
hprIpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 34, 6, 2, 1, 2)).setObjects(("HPR-IP-MIB", "hprIpMonitoringGroup"), ("HPR-IP-MIB", "hprIpConfigurationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hprIpCompliance = hprIpCompliance.setStatus('current')
hprIpMonitoringGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 5)).setObjects(("HPR-IP-MIB", "hprIpActiveLsUdpPackets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hprIpMonitoringGroup = hprIpMonitoringGroup.setStatus('current')
hprIpConfigurationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 34, 6, 2, 2, 6)).setObjects(("HPR-IP-MIB", "hprIpAppnPortTOSPrecedence"), ("HPR-IP-MIB", "hprIpLsTOSPrecedence"), ("HPR-IP-MIB", "hprIpLsRowStatus"), ("HPR-IP-MIB", "hprIpCnTOSPrecedence"), ("HPR-IP-MIB", "hprIpCnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hprIpConfigurationGroup = hprIpConfigurationGroup.setStatus('current')
mibBuilder.exportSymbols("HPR-IP-MIB", hprIpCompliance=hprIpCompliance, hprIpCnVrnName=hprIpCnVrnName, hprIpActiveLsEntry=hprIpActiveLsEntry, hprIpLsTOSPrecedence=hprIpLsTOSPrecedence, hprIpActiveLsAppnTrafficType=hprIpActiveLsAppnTrafficType, AppnTrafficType=AppnTrafficType, hprIpCnAppnTrafficType=hprIpCnAppnTrafficType, hprIpMonitoringGroup=hprIpMonitoringGroup, hprIpActiveLsUdpPackets=hprIpActiveLsUdpPackets, hprIpAppnPortEntry=hprIpAppnPortEntry, hprIpCnTable=hprIpCnTable, hprIpLsTable=hprIpLsTable, hprIpActiveLsTable=hprIpActiveLsTable, hprIpLsEntry=hprIpLsEntry, PYSNMP_MODULE_ID=hprIp, AppnTOSPrecedence=AppnTOSPrecedence, hprIpAppnPortName=hprIpAppnPortName, hprIpLsRowStatus=hprIpLsRowStatus, hprIpAppnPortAppnTrafficType=hprIpAppnPortAppnTrafficType, hprIpActiveLsLsName=hprIpActiveLsLsName, hprIpCnEntry=hprIpCnEntry, hprIpAppnPortTable=hprIpAppnPortTable, hprIpAppnPortTOSPrecedence=hprIpAppnPortTOSPrecedence, hprIp=hprIp, hprIpLsLsName=hprIpLsLsName, hprIpCnTOSPrecedence=hprIpCnTOSPrecedence, hprIpLsAppnTrafficType=hprIpLsAppnTrafficType, hprIpConfigurationGroup=hprIpConfigurationGroup, hprIpCnRowStatus=hprIpCnRowStatus)
