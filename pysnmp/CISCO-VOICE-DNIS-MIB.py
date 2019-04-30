#
# PySNMP MIB module CISCO-VOICE-DNIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-DNIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:03:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Integer32, Counter64, Gauge32, Unsigned32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Integer32", "Counter64", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "IpAddress")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
ciscoVoiceDnisMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 219))
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setLastUpdated('200205010000Z')
if mibBuilder.loadTexts: ciscoVoiceDnisMIB.setOrganization('Cisco Systems, Inc.')
class DnisMapname(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class CvE164String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

cvDnisMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1))
cvDnisMap = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1))
cvDnisMappingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1), )
if mibBuilder.loadTexts: cvDnisMappingTable.setStatus('current')
cvDnisMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1), ).setIndexNames((1, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"))
if mibBuilder.loadTexts: cvDnisMappingEntry.setStatus('current')
cvDnisMappingName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 1), DnisMapname().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: cvDnisMappingName.setStatus('current')
cvDnisMappingUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingUrl.setStatus('current')
cvDnisMappingRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("refresh", 2))).clone('idle')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingRefresh.setStatus('current')
cvDnisMappingUrlAccessError = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisMappingUrlAccessError.setStatus('current')
cvDnisMappingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisMappingStatus.setStatus('current')
cvDnisNodeTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2), )
if mibBuilder.loadTexts: cvDnisNodeTable.setStatus('current')
cvDnisNodeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-VOICE-DNIS-MIB", "cvDnisMappingName"), (1, "CISCO-VOICE-DNIS-MIB", "cvDnisNumber"))
if mibBuilder.loadTexts: cvDnisNodeEntry.setStatus('current')
cvDnisNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 1), CvE164String())
if mibBuilder.loadTexts: cvDnisNumber.setStatus('current')
cvDnisNodeUrl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeUrl.setStatus('current')
cvDnisNodeModifiable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvDnisNodeModifiable.setStatus('current')
cvDnisNodeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 219, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvDnisNodeStatus.setStatus('current')
cvDnisMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2))
cvDnisMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0))
cvDnisMappingUrlInaccessible = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 219, 2, 0, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"))
if mibBuilder.loadTexts: cvDnisMappingUrlInaccessible.setStatus('current')
cvDnisMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3))
cvDnisMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1))
cvDnisMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2))
cvDnisMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 1, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisGroup"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisMIBCompliance = cvDnisMIBCompliance.setStatus('current')
cvDnisGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 1)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingRefresh"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlAccessError"), ("CISCO-VOICE-DNIS-MIB", "cvDnisMappingStatus"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeUrl"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeModifiable"), ("CISCO-VOICE-DNIS-MIB", "cvDnisNodeStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisGroup = cvDnisGroup.setStatus('current')
cvDnisNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 219, 3, 2, 2)).setObjects(("CISCO-VOICE-DNIS-MIB", "cvDnisMappingUrlInaccessible"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvDnisNotificationGroup = cvDnisNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-DNIS-MIB", cvDnisNodeUrl=cvDnisNodeUrl, cvDnisMappingStatus=cvDnisMappingStatus, cvDnisMIBNotificationPrefix=cvDnisMIBNotificationPrefix, cvDnisNumber=cvDnisNumber, cvDnisMappingEntry=cvDnisMappingEntry, cvDnisMIBGroups=cvDnisMIBGroups, cvDnisNodeTable=cvDnisNodeTable, cvDnisGroup=cvDnisGroup, cvDnisMappingTable=cvDnisMappingTable, cvDnisMappingUrlInaccessible=cvDnisMappingUrlInaccessible, cvDnisMIBObjects=cvDnisMIBObjects, cvDnisMappingRefresh=cvDnisMappingRefresh, cvDnisMappingUrl=cvDnisMappingUrl, CvE164String=CvE164String, cvDnisMappingUrlAccessError=cvDnisMappingUrlAccessError, DnisMapname=DnisMapname, ciscoVoiceDnisMIB=ciscoVoiceDnisMIB, cvDnisMap=cvDnisMap, cvDnisMIBConformance=cvDnisMIBConformance, cvDnisMIBCompliances=cvDnisMIBCompliances, cvDnisMIBCompliance=cvDnisMIBCompliance, cvDnisNodeModifiable=cvDnisNodeModifiable, cvDnisNodeStatus=cvDnisNodeStatus, cvDnisMappingName=cvDnisMappingName, cvDnisNotificationGroup=cvDnisNotificationGroup, cvDnisMIBNotifications=cvDnisMIBNotifications, cvDnisNodeEntry=cvDnisNodeEntry, PYSNMP_MODULE_ID=ciscoVoiceDnisMIB)
